# Cloudflare Runtime Audit

> Task: `AUD-080`  
> Final status: deployment integration `GAP`; general application incompatibility `NOT ESTABLISHED`.

## Current Runtime / Deployment

- The source is Next.js 15.2.3 App Router with React 19, TypeScript, route handlers, `next-intl` middleware, Server Actions, Fumadocs generation, and standalone output.
- Vercel (`vercel.json`) and Node/Docker (`Dockerfile`) paths exist. Final Action: `KEEP-DISABLED` as alternate, non-golden deployment paths.
- The current branch has no Wrangler file/example, OpenNext package/config, Worker entry, compatibility date/flags, Cloudflare bindings, deploy script, or Cloudflare CI workflow.
- README Cloudflare instructions reference a different branch and absent `wrangler.toml.example` / `cf:deploy`; they are not executable evidence for this checkout.

Final Action for the primary path: `PATCH`.

## OpenNext / Workers Compatibility

### Deployment integration gap versus runtime incompatibility

| Question | Final finding | Evidence |
|---|---|---|
| Is Cloudflare/OpenNext integrated? | No: `GAP` | AUD-010 and AUD-070 root/config scans |
| Is the application proven incompatible with Workers? | No | No direct `node:`/fs/path/net/tls/native-binary use was established in source; no target build was run |
| Is the application proven compatible? | No: `LIKELY_COMPATIBLE_NEEDS_VERIFICATION` | Adapter/build/deploy/provider smoke evidence is absent |
| Is a repo-wide runtime rewrite required? | No | All audited surfaces have `KEEP + TEST`, `WRAP`, or bounded `PATCH` paths |

Target-runtime verification must cover:

1. App Router pages, route handlers, `next-intl` middleware, Server Actions, image handling, and Fumadocs source generation/search.
2. `postgres`/Drizzle connection lifecycle and the existing `globalThis.Cloudflare` branch.
3. Auth.js callbacks, JWT cookies, Google OAuth, Resend Magic Link delivery, and canonical user persistence.
4. Stripe/Creem SDK calls, raw webhook bodies, Stripe signature verification, and Creem WebCrypto HMAC.
5. AI SDK streaming, provider clients, storage `Buffer`/byte conversion, and S3/R2 signing.

## Environment / Secrets / Config

Required minimum configuration model:

| Environment | Required Cloudflare state | Release requirement |
|---|---|---|
| DEVELOPMENT | Dedicated Worker deployment/bindings; isolated URL, database, Auth/provider and optional-module secrets | May run directly on Cloudflare; local is only a development method |
| STAGING | Dedicated Worker deployment and production-shaped bindings with provider test/staging accounts | Mandatory target for full release smoke |
| PRODUCTION | Dedicated bindings and secrets, isolated from Staging | Deploy only the exact commit verified in Staging |

Preserve existing environment names where feasible. Add a narrow validation/binding layer that distinguishes server secrets from `NEXT_PUBLIC_*`, documents every consumed variable, removes the reusable fixed Auth secret sample, and permits optional modules to remain secret-free while disabled. Final Action: `PATCH`.

## Database Connectivity / Hyperdrive Considerations

- PostgreSQL/Drizzle uses a generic `DATABASE_URL`; no provider SDK or product-layer vendor coupling was found.
- The Node path has a singleton pool; the detected Cloudflare path creates a `max: 1`, `prepare: false` client per `db()` call.
- No Hyperdrive binding/config or real Worker connection test exists. Hyperdrive is an optional implementation integration and is qualified only when selected.
- A-001 is `FROZEN — PostgreSQL Provider Policy R1`; the application contract is PostgreSQL + Drizzle + generic `DATABASE_URL`, while the vendor remains `UNPINNED` during Starter design.

When a real provider/environment is selected, Provider Qualification must cover migration, read/write, concurrency, TLS/network behavior, transactions, environment isolation, failure behavior, and optional Hyperdrive routing when applicable. This qualification does not block Starter Detailed Spec or Design Freeze.

## Blockers

1. `CF-01` P0: missing OpenNext/Wrangler deployment integration.
2. `CF-02` P0: no isolated Cloudflare Staging environment or real-provider smoke evidence.
3. `CF-03` P0: no exact-commit Staging-to-Production promotion path.
4. `CF-04` P1: real provider/runtime qualification is deferred until a concrete implementation environment is selected; it is not a Starter design blocker.
5. `CF-05` P1: Worker-sensitive DB/Auth/payment/AI/storage paths remain unverified, not confirmed incompatible.

## Actions

| Scope | Action | Minimum delta |
|---|---|---|
| Next.js application structure | KEEP + TEST | Preserve routes/layouts/actions; verify through target adapter |
| Cloudflare/OpenNext integration | PATCH | Add adapter/config/scripts/bindings only |
| Worker-sensitive dependencies/APIs | KEEP + TEST | Build and run focused Staging smoke before replacement |
| Environment validation/separation | PATCH | Add complete validated three-environment bindings |
| PostgreSQL/Drizzle boundary | KEEP + TEST | Keep `DATABASE_URL`; verify selected provider/Hyperdrive path |
| Vercel and Docker | KEEP-DISABLED | Retain as optional alternates |
| Release process | PATCH | Staging gate, exact commit promotion, migration and recovery procedure |

No confirmed application-runtime incompatibility and no `REFACTOR` or `DELETE` recommendation exists.
