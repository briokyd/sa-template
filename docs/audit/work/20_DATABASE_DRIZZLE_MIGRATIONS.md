# Database / Drizzle / Migration Audit

> Task: `AUD-020`  
> Status: VERIFIED  
> Authority: `AUDIT-001`

Scope: repository-grounded audit of the existing PostgreSQL, Drizzle, migration, access, and connection layers. No schema, migration, package, or application implementation was changed.

## Audit boundary

The frozen target is PostgreSQL plus Drizzle with a vendor-neutral product boundary and a Cloudflare-first deployment target. This workstream does not choose A-001, does not introduce a D1 path, and does not redesign existing tables. Payment, identity, and entitlement behavior is recorded only to the degree necessary to establish database ownership and transaction boundaries; deep behavior belongs to `AUD-030` and `AUD-040`.

The repository was inspected at `503ca9a0f46bc732fe974b6d336e1d1fcd2eb8a4` on `audit/kyd-starter-v1`. No committed application files had a diff. The untracked Runtime/bootstrap pack is pre-existing state.

## 1. Database provider and driver

- `package.json` declares `drizzle-orm` `^0.44.2`, `drizzle-kit` `^0.31.1`, and `postgres` `^3.4.7`; `pnpm-lock.yaml` resolves them to `0.44.2`, `0.31.1`, and `3.4.7` respectively.
- `src/db/index.ts` imports `drizzle-orm/postgres-js` and `postgres`, and obtains a generic `DATABASE_URL`. There is no provider SDK, provider-specific connection object, or provider-specific schema type in `src/db/`.
- `.env.example` labels the example connection as Supabase and exposes the `DATABASE_URL` variable name only. That comment is the only provider cue located in the database config; it does not establish a current provider or provider dependency.
- The existing driver path is PostgreSQL-specific and is compatible with the frozen ORM/database direction at the repository interface. Actual connectivity to any provider, SSL requirements, pooling limits, and staging credentials are `UNKNOWN / NOT VERIFIED` because no database environment or integration test is present in the repository.

## 2. Drizzle schema and ownership

- `src/db/schema.ts` defines seven `pgTable` tables: `users`, `orders`, `apikeys`, `credits`, `posts`, `affiliates`, and `feedbacks`. All use PostgreSQL identity integer primary keys; the public/business references are string fields such as `uuid`, `order_no`, and `user_uuid`.
- The schema has unique constraints for user UUID, order number, API key, credit transaction number, and post UUID, plus the `users(email, signin_provider)` unique index. Migration snapshot evidence reports no foreign keys or check constraints in the initial schema.
- The model layer is localized to `src/models/{user,order,credit,apikey,affiliate,post,feedback}.ts`. Each model imports `db` from `@/db` and its table from `@/db/schema`; the repository search found no other direct database client imports.
- Service composition is in `src/services/`. `saveUser` combines user creation and initial credit insertion. `updateOrder` and `updateSubOrder` compose order updates with credit and affiliate writes. `src/app/api/update-invite/route.ts` combines user and affiliate writes.
- The presence of denormalized string references and provider-named `orders.stripe_session_id` is a factual coupling observation for later auth/payment audits. It is not evidence that the schema needs refactoring. A foreign-key redesign is not recommended by this workstream.

## 3. Migration mechanism and database initialization

- `src/db/config.ts` uses `defineConfig` with `dialect: "postgresql"`, schema `./src/db/schema.ts`, and migration output `./src/db/migrations`. It reads `.env`, `.env.development`, and `.env.local` through `dotenv`, then supplies `process.env.DATABASE_URL!` to Drizzle Kit.
- `package.json` provides `db:generate`, `db:migrate`, `db:studio`, and `db:push`; all call Drizzle Kit with `src/db/config.ts`.
- The migration directory contains one generated SQL migration, `src/db/migrations/0000_wealthy_squirrel_girl.sql`, a matching `meta/0000_snapshot.json`, and `meta/_journal.json` with one `0000_wealthy_squirrel_girl` entry. The migration creates the same seven tables and declared unique constraints visible in `src/db/schema.ts`.
- No repository evidence shows that a migration has been applied against development, staging, or production. `node_modules/` is absent, so commands were not run and no database connection was attempted during this audit.
- Drizzle Kit configuration loads no `.env.staging` or `.env.production` file itself. External environment injection can still provide `DATABASE_URL`, but the intended per-environment migration invocation is `UNKNOWN / NOT VERIFIED`.

## 4. Connection lifecycle, pooling, and runtime assumptions

- `db()` throws `DATABASE_URL is not set` before creating a client. This is the only runtime database-variable validation found in the access path; Drizzle Kit uses a non-null assertion rather than explicit validation.
- `src/db/index.ts` evaluates `isCloudflareWorker` at module initialization from `globalThis.Cloudflare`.
- In the non-Cloudflare branch, the module retains one Drizzle instance backed by `postgres(databaseUrl, { prepare: false, max: 10, idle_timeout: 30, connect_timeout: 10 })`.
- In the Cloudflare branch, every `db()` call creates a new `postgres` client with `prepare: false`, `max: 1`, `idle_timeout: 10`, and `connect_timeout: 5`, then returns `drizzle(client)`. The code has no explicit close/dispose call or binding-based configuration.
- The explicit Worker branch shows intent to constrain per-invocation connections. It does not prove that the `postgres` driver, direct TCP path, or the chosen deployment adapter works in the target Worker runtime.

## 5. Transactions and consistency boundaries

- Repository search for `transaction` in `src/` found no Drizzle transaction call.
- `src/services/user.ts` inserts a user and then calls `increaseCredits`; a failure after the first write can leave a user without initial credits.
- `src/services/order.ts` changes an order to paid before invoking `updateCreditForOrder` and `updateAffiliateForOrder`; subscription renewal inserts an order before credit creation. `src/app/api/update-invite/route.ts` updates `users.invited_by` before inserting an affiliate record.
- The existing service-level read-before-insert checks (`findCreditByOrderNo`, `findAffiliateByOrderNo`) help normal-path idempotency but are not a demonstrated atomic concurrency guarantee. Payment webhook idempotency and entitlement correctness remain for `AUD-040`; auth/new-user semantics remain for `AUD-030`.
- The concrete minimal future delta is to introduce bounded transaction handling only around the approved multi-write flows, after those downstream audits specify their invariants. This is a `PATCH` candidate, not a schema or directory refactor.

## 6. Workers and Hyperdrive suitability

- Cloudflare/OpenNext deployment integration is absent from the current tree, as recorded by `AUD-010`. The database-specific implementation contains only the `globalThis.Cloudflare` branch described above.
- No Hyperdrive binding name, Wrangler configuration, Cloudflare `env` binding, Hyperdrive connection string, or Worker smoke test was found. Hyperdrive compatibility is therefore `UNKNOWN` rather than a confirmed gap or incompatibility.
- The repository has no direct code evidence that identifies a database provider. The generic `DATABASE_URL` interface leaves A-001 open and permits a later provider decision without changing the product-level database contract.
- Required verification before a Cloudflare-first path can be declared compatible: build/deploy through the chosen OpenNext adapter; connect using the selected provider and, if selected, Hyperdrive; run migration and read/write smoke tests; and exercise the transaction-relevant flows under real concurrency. These are verification requirements, not changes made by AUD-020.

## 7. Evidence for A-001: Default PostgreSQL Provider

| Evidence question | Repository-grounded result |
|---|---|
| Current provider | `UNKNOWN / NOT VERIFIED`. `.env.example` contains a Supabase-oriented comment, but no provider package/configuration is imported by `src/db/`; no local environment was read. |
| Driver and ORM portability | `postgres` plus `drizzle-orm/postgres-js`, connected only through `DATABASE_URL`. The schema and migrations use PostgreSQL dialect constructs. |
| Provider-specific schema coupling | No provider SDK/table/binding is present in the audited database files. The schema is PostgreSQL-specific by frozen direction, not visibly provider-specific. |
| Cloudflare evidence | A Worker branch exists in `src/db/index.ts`; no actual Workers/OpenNext/Hyperdrive integration or test exists. |
| Pooling/connectivity evidence | Node singleton uses a pool limit of 10. The Worker branch creates a fresh `max: 1` client per `db()` call. Provider connection limits and lifecycle behavior are not verified. |
| Decision | A-001 remains undecided. AUD-020 supplies evidence only; provider selection awaits the remaining audit evidence and the required real-environment tests. |

## Findings Table

| Module / Capability | Existing implementation | Existing files | Current behavior | Starter planned role | Required behavior | Gap | Action | Default enabled? | Tests today | Tests required | Cloudflare compatibility | Risk | Reason | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PostgreSQL connectivity and driver | Drizzle `postgres-js` adapter over generic `DATABASE_URL` | `package.json`, `pnpm-lock.yaml`, `src/db/index.ts`, `.env.example` | Uses `postgres` 3.4.7 with PostgreSQL Drizzle adapter; no provider SDK located | One vendor-neutral PostgreSQL golden path | Connect with selected provider credentials without product-level provider coupling | Real-provider connection, SSL, and pooling limits unverified | `KEEP + TEST` | Yes | No database test files or test scripts found | Development, staging, production provider-connectivity smoke tests; SSL and connection-limit checks | `LIKELY_COMPATIBLE_NEEDS_VERIFICATION` | Medium | Existing generic connection surface already matches PostgreSQL + Drizzle; evidence is insufficient to assert runtime success | Package and lockfile declarations; `src/db/index.ts` imports and `DATABASE_URL` read; `.env.example` provider comment only |
| Drizzle schema and shared tables | Seven `pgTable` definitions; model modules per table | `src/db/schema.ts`, `src/models/*.ts` | Users, orders, credits, API keys, affiliates, posts, and feedback are defined and used through models | Reuse existing shared platform tables pending domain audits | Preserve operational schema while validating behavior in auth/payment workstreams | No schema tests; cross-table string references lack DB constraints, but no correctness case was proven that warrants redesign | `KEEP + TEST` | Yes | No schema/database integration test found | Schema-to-migration verification and table-level CRUD/constraint tests | `NOT_APPLICABLE` | Medium | PostgreSQL/Drizzle schema is present and migration-backed; naming and relationship style alone do not justify refactor | `src/db/schema.ts`; migration snapshot table/constraint counts; model imports |
| Migration generation and application | Drizzle Kit config, one SQL migration, journal, snapshot | `src/db/config.ts`, `src/db/migrations/0000_wealthy_squirrel_girl.sql`, `src/db/migrations/meta/*`, `package.json` | Generates/applies PostgreSQL migrations from the defined schema path | Controlled PostgreSQL migration golden path | Run reproducibly against isolated environments before release | No evidence of applied migration or environment-specific invocation; only one baseline history in repository | `KEEP + TEST` | Yes | No migration test or CI invocation found | Fresh-database migrate, repeat-migrate, and schema drift checks in development/staging | `NOT_APPLICABLE` | Medium | Existing Drizzle migration mechanism should be preserved; missing proof is a test/release concern | `db:generate`, `db:migrate`, `db:studio`, `db:push` scripts; journal and snapshot |
| Database configuration and environment separation | Dotenv config loads three local files; runtime checks `DATABASE_URL` | `src/db/config.ts`, `src/db/index.ts`, `.env.example` | CLI loads `.env`, `.env.development`, `.env.local`; runtime throws if DB URL missing | Isolated development/staging/production database config | Provide selected environment URL without secret exposure and fail clearly when absent | Staging/production CLI conventions and DB-specific config validation are not verified | `KEEP + TEST` | Yes | No config test found | Verify migrate/connect behavior with isolated env injection for all standard environments | `NOT_APPLICABLE` | Medium | The existing generic variable supports separation; no evidence requires a variable rename or config refactor | `src/db/config.ts` `config(...)` calls and non-null assertion; `src/db/index.ts` error path |
| Node and Worker connection lifecycle | Node singleton; Cloudflare conditional creates one-client Drizzle instance per `db()` call | `src/db/index.ts` | Node pool `max: 10`; Worker path `max: 1`, `prepare: false`, shorter timeouts | Cloudflare-first PostgreSQL access path | Demonstrate connection lifecycle and request behavior on selected Worker path | No Worker deployment or smoke evidence; no Hyperdrive binding/configuration | `KEEP + TEST` | Yes | No Worker/database integration test found | OpenNext Worker read/write test, concurrency/connection test, and selected-provider/Hyperdrive smoke test | `LIKELY_COMPATIBLE_NEEDS_VERIFICATION` | High | Existing branch is a reuse candidate; absence of deployment evidence is not a confirmed incompatibility | `src/db/index.ts` Worker detection and client options; absence of Wrangler/OpenNext/Hyperdrive files recorded by AUD-010 |
| Multi-write consistency | Sequential model writes from user, order, credit, affiliate, and invite workflows | `src/services/user.ts`, `src/services/order.ts`, `src/services/credit.ts`, `src/services/affiliate.ts`, `src/app/api/update-invite/route.ts` | Writes are composed without `db().transaction(...)` | Atomic approved onboarding, payment/entitlement, and invite updates | Prevent partial state where a dependent write fails | Concrete absence of transactions across evidenced multi-write sequences | `PATCH` | Yes | No transactional or concurrency tests found | Failure-injection and concurrent/idempotency tests after AUD-030/AUD-040 invariants are fixed | `LIKELY_COMPATIBLE_NEEDS_VERIFICATION` | High | A bounded transaction wrapper is smaller and safer than schema refactor; exact scope must follow downstream behavior audits | `rg -n 'transaction' src` returned no database transaction calls; cited service/route sequences |
| A-001 provider decision evidence | Generic PostgreSQL URL/driver and Postgres-only schema/migrations | `src/db/index.ts`, `src/db/config.ts`, `src/db/schema.ts`, `.env.example` | Provider not identified by runtime code; Supabase is only an example comment | Select one PostgreSQL provider after audit evidence | Decide based on Cloudflare connectivity, pooling, migration, and staging verification | Required provider comparison and real-environment evidence are not in repository | `KEEP + TEST` | Yes | No provider-specific integration test found | Selected-provider migration/connectivity/Cloudflare smoke suite | `UNKNOWN` | High | No provider decision can be made from an example comment; preserve the neutral `DATABASE_URL` surface while gathering evidence | Generic `DATABASE_URL`; no provider imports or bindings; no Worker/Hyperdrive deployment config |

## Verification notes

- `rg --files --hidden -g '!.git/**' -g '!node_modules/**' | rg '(^|/)(__tests__|tests?)(/|$)|\\.(test|spec)\\.[cm]?[jt]sx?$|playwright|vitest|jest|cypress'` returned no test candidates.
- `rg -n 'transaction' src --glob '!src/db/migrations/**'` found no database transaction use; the only returned match was unrelated legal-page prose.
- The audit did not run Drizzle commands, connect to a database, expose credential values, or modify source/migration/package files.
- No `REFACTOR` or `DELETE` action is recommended. The sole `PATCH` is bounded to transaction handling after the related domain audits define required invariants.
- Closeout verification passed: `python3 tools/kyd_runtime_validate.py --root . --mode closeout` returned `KYD_RUNTIME_VALIDATE: PASS` and `RUNTIME_STATE_VALID = TRUE`.
