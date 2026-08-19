# Framework / Cloudflare / Environment / Config Audit

> Task: `AUD-010`  
> Status: `VERIFIED`  
> Authority: `AUDIT-001`  
> Reference: `AUD-WORK-000`

## Audit boundary and evidence status

This audit covers framework/runtime, deployment entry points, Cloudflare/OpenNext readiness, and environment/configuration architecture only. No application, dependency, schema, route, or runtime configuration file was modified.

The repository is a single pnpm package on `audit/kyd-starter-v1` at audited HEAD `503ca9a0f46bc732fe974b6d336e1d1fcd2eb8a4`. Before AUD-010 edits, the worktree already contained untracked Runtime/bootstrap files plus `README_RUNTIME_R1_RESTORE.md` and `sa_template_Kyd_Runtime_V1_R1_Restore.zip`. They are not AUD-010 changes.

Evidence commands included `git status --short --branch`, `rg --files --hidden`, `rg -n` source/config searches, and targeted reads of `package.json`, `next.config.mjs`, `tsconfig.json`, `vercel.json`, `Dockerfile`, `.env.example`, `README.md`, `src/middleware.ts`, `src/db/config.ts`, `src/db/index.ts`, `src/lib/ip.ts`, `src/lib/storage.ts`, and `src/lib/source.ts`.

`node --version` returned `v20.19.5`, `pnpm --version` returned `10.28.2`, and `node_modules/` is absent. The existing build and Docker commands were therefore not executed: no dependency installation is authorized for this audit, and a build without installed dependencies would not establish application compatibility.

## 1. Framework and application structure

### Confirmed repository facts

| Area | Evidence | Current behavior |
|---|---|---|
| Package/workspace | `package.json`, `pnpm-lock.yaml`; no `pnpm-workspace.yaml`, `turbo.json`, `nx.json`, or additional package manifests | Single private pnpm package; no monorepo/workspace structure observed |
| Framework | `package.json`: `next` 15.2.3, `react`/`react-dom` ^19.0.0, TypeScript ^5.7.2 | Next.js application using the App Router under `src/app/`; no `pages/` router directory observed |
| TypeScript | `tsconfig.json` | Strict, no-emit, bundler module resolution, Next TypeScript plugin, `@/*` and generated `@/.source` aliases |
| Application boundary | `src/app/`, `src/app/api/`, `src/middleware.ts` | Locale route groups, server layouts/pages, 17 route handlers, and `next-intl` middleware |
| Server Actions | API-key creation and admin post create/edit pages contain `"use server"` actions | Server Actions are present; no per-route `runtime` or `preferredRegion` declarations were found |
| Build/start tooling | `package.json:scripts` | `next dev --turbopack`, `next build`, `next start`, analysis, Docker build, Drizzle commands, Fumadocs postinstall generation |
| Runtime pinning | `package.json` lacks `engines`, `packageManager`, or a tool-version file; `Dockerfile` starts from `node:18-alpine` | Local audit shell is Node 20 while the existing Docker path builds on Node 18; cross-version build behavior is not verified |

`next.config.mjs` composes `next-intl`, Fumadocs MDX, and optional bundle analysis. It uses standalone output, MDX page extensions, `experimental.mdxRs`, and wildcard HTTPS remote image patterns. These are existing configuration facts, not a request to redesign the configuration.

## 2. Cloudflare / OpenNext runtime compatibility

### Confirmed integration state

The repository contains no Wrangler configuration, OpenNext package/configuration, Cloudflare adapter, Worker entry point, Workers deployment script, compatibility date/flags, Cloudflare CI workflow, or Cloudflare binding module. `rg --files` found only `vercel.json` among provider deployment configuration files.

This is a **CONFIRMED GAP** in Cloudflare deployment integration. It is not proof that the application implementation is Cloudflare-incompatible.

`README.md` documents a Cloudflare branch workflow and references `wrangler.toml.example` plus `npm run cf:deploy`; neither the example/config file nor the `cf:deploy` script exists in the current tree. The README wording is therefore not executable evidence for the current branch.

### Runtime compatibility evidence

| Surface | Evidence | Cloudflare status | Assessment |
|---|---|---|---|
| Next App Router and route handlers | `src/app/`, `src/app/api/`; no explicit runtime declarations found | `LIKELY_COMPATIBLE_NEEDS_VERIFICATION` | No repository evidence proves an OpenNext Workers build or request smoke path |
| `next-intl` middleware | `src/middleware.ts` imports `next-intl/middleware` | `LIKELY_COMPATIBLE_NEEDS_VERIFICATION` | Edge-style middleware exists, but must be exercised in the target adapter |
| Server Actions | Three page-local `"use server"` actions found | `LIKELY_COMPATIBLE_NEEDS_VERIFICATION` | Need an OpenNext build and action request smoke test |
| PostgreSQL runtime branch | `src/db/index.ts` imports `postgres`, detects `globalThis.Cloudflare`, and creates a per-call client for that branch | `UNKNOWN` | Code intends a Workers path, but driver/connection/Hyperdrive compatibility belongs to AUD-020 and has not been tested |
| WebCrypto | `src/app/api/pay/notify/creem/route.ts`, `src/aisdk/kling/client.ts` use `crypto.subtle` | `COMPATIBLE` | WebCrypto API use is visible; end-to-end provider behavior remains outside AUD-010 |
| Buffer use | `src/lib/storage.ts`, `src/app/api/demo/gen-image/route.ts`, `src/aisdk/kling/client.ts` use `Buffer` | `LIKELY_COMPATIBLE_NEEDS_VERIFICATION` | No Workers compatibility flag/config is present; verify the OpenNext runtime provides the required Node compatibility surface |
| Browser storage helper | `src/lib/cache.ts` uses `localStorage`; no server import was found | `NOT_APPLICABLE` | Browser-only helper, not a Workers server-runtime requirement |
| Fumadocs generated source | `source.config.ts`, `src/lib/source.ts`, `package.json:postinstall` | `LIKELY_COMPATIBLE_NEEDS_VERIFICATION` | `.source` is generated at build/dev time; target build must prove generation and bundling work |
| Direct Node built-ins in source | Source search found no `node:` imports or direct fs/path/net/tls/child-process use | `LIKELY_COMPATIBLE_NEEDS_VERIFICATION` | This lowers source-level risk but does not prove transitive package compatibility |
| Node-oriented runtime dependencies | `postgres`, `stripe`, `resend`, `simple-flakeid`, and `dotenv` are imported by server/build code | `LIKELY_COMPATIBLE_NEEDS_VERIFICATION` | No package-level Workers compatibility test was run; `dotenv` is confined to Drizzle CLI config |

No **confirmed application-runtime incompatibility** was established from repository evidence. The confirmed gap is the missing Cloudflare/OpenNext deployment integration and target-runtime verification.

## 3. Existing build and deployment paths

| Deployment surface | Existing implementation | Current/default state | Cloudflare relationship | Action |
|---|---|---|---|---|
| Vercel | `vercel.json` sets `maxDuration: 60` for `app/api/**/*`; `vercel` is a dev dependency; README provides a Vercel deploy button | Existing documented deployment path | Does not conflict with Cloudflare-first when retained as a non-golden alternate | `KEEP-DISABLED` |
| Docker | `Dockerfile` builds a Node 18 Alpine standalone Next.js image; `docker:build` script exists | Manual alternate path; no compose file found | Node container path is not the Cloudflare golden path | `KEEP-DISABLED` |
| Cloudflare | README-only instructions reference a different branch/artifacts; no executable configuration in current tree | Not configured or runnable from this branch | Required golden deployment integration is absent | `PATCH` |
| Build execution | `build`, `dev`, `start`, `analyze`, and `postinstall` scripts exist | Not verified in this workspace because `node_modules/` is absent | Need target build and Worker smoke evidence before claiming compatibility | `KEEP + TEST` |

The Vercel and Docker files should remain. AUD-010 does not recommend deletion or modification of either alternate path.

## 4. Environment and configuration model

### Current architecture

`.env.example` documents web URL/project name, database, Auth.js, Google/GitHub, analytics, Stripe, Creem, locale/admin/theme, S3-compatible storage, and AdSense variable names. `src/db/config.ts` is the only centralized loader located: it invokes `dotenv` for `.env`, `.env.development`, and `.env.local` for Drizzle CLI configuration.

Application configuration is otherwise distributed. A source search found 96 direct `process.env.*` reads across route handlers, components/providers, integrations, database code, auth, i18n, storage, and AI code. No runtime environment schema, centralized validation module, or `process.env` Zod parse was found; the located Zod uses are form/error validation only.

Direct client/component references found in `src/components/`, `src/contexts/`, `src/hooks/`, and `src/providers/` use `NEXT_PUBLIC_*` names or `NODE_ENV`. No non-public secret variable was found in that client-oriented search. This is a positive naming boundary, but it is not a substitute for build/runtime exposure testing.

### Configuration coverage and validation findings

| Finding | Evidence | Classification |
|---|---|---|
| Runtime variables absent from `.env.example` | Direct source reads include `KLING_ACCESS_KEY`, `KLING_SECRET_KEY`, `OPENROUTER_API_KEY`, `RESEND_API_KEY`, `RESEND_SENDER_EMAIL`, `SILICONFLOW_API_KEY`, `SILICONFLOW_BASE_URL`, and `NEXT_PUBLIC_SHOW_POWERED_BY`; none is documented in `.env.example` | **CONFIRMED GAP**: configuration documentation/coverage is incomplete |
| Environment validation is absent | No centralized env schema/validation file; missing database and integration secrets fail only when their paths execute (`src/db/index.ts`, `src/integrations/stripe/index.ts`, `src/integrations/creem/index.ts`) | **CONFIRMED GAP**: startup/feature validation is not centralized |
| Localhost sample URLs | `.env.example` sets sample `NEXT_PUBLIC_WEB_URL` and `AUTH_URL` to localhost; checkout, canonical, callback, invite, and metadata paths consume the web URL | **CONFIRMED GAP** in ready-to-use environment separation, not a hard-coded application URL defect |
| Static Auth secret sample | `.env.example` contains a non-empty fixed `AUTH_SECRET` sample value | **CONFIRMED GAP**: copied configuration could reuse a known value; no secret value is recorded here |
| Staging environment | README covers `.env.development` and `.env.production`; no staging template, mapping, deployment manifest, or CI workflow exists | **CONFIRMED GAP**: DEVELOPMENT/STAGING/PRODUCTION isolation is not evidenced |
| Provider selection | `PAY_PROVIDER` selects Stripe/Creem in `src/app/api/checkout/route.ts`; `CREEM_ENV` is read by `src/integrations/creem/index.ts` | Existing explicit provider/environment controls; payment correctness is deferred to AUD-040 |

### Environment support assessment

| Standard environment | Repository evidence | Status |
|---|---|---|
| DEVELOPMENT | README directs copying `.env.example` to `.env.development`; Drizzle CLI loads `.env.development`; `dev` script runs local Next Turbopack | `LIKELY_COMPATIBLE_NEEDS_VERIFICATION` for current local Next workflow; direct Cloudflare development is not configured |
| STAGING | No dedicated sample, deployment manifest, script, CI workflow, or URL/config map found | `GAP` |
| PRODUCTION | README describes `.env.production`, Vercel, Docker, and a missing Cloudflare workflow; production-only analytics/ad components are env-gated | `LIKELY_COMPATIBLE_NEEDS_VERIFICATION` for Vercel/Docker; Cloudflare production deployment is a `GAP` |

## 5. Cloudflare-specific blockers and minimal-delta direction

### Confirmed gaps

1. No OpenNext/Wrangler/Worker deployment integration or Cloudflare release workflow exists in this branch.
2. No evidence establishes Cloudflare-backed DEVELOPMENT, STAGING, and PRODUCTION configuration/binding separation.
3. Environment validation and `.env.example` coverage are incomplete for variables directly consumed by existing routes and providers.
4. The README references an absent Cloudflare branch artifact and `cf:deploy` script, so its Cloudflare instructions cannot be followed from this checkout.

### Not yet verified

1. OpenNext Workers build and request execution for App Router, `next-intl` middleware, Server Actions, Fumadocs generation/search, and route handlers.
2. Workers compatibility of transitive/runtime dependency surfaces: `postgres`, Stripe, Creem, Resend, Fumadocs, `simple-flakeid`, and Buffer-based code paths.
3. PostgreSQL network/Hyperdrive behavior, which is explicitly routed to AUD-020.
4. Build and Docker results, because this workspace has no installed dependencies and AUD-010 did not install them.
5. Environment-specific provider keys, callback URLs, webhook secrets, and isolated databases, because no actual credentials or deployment bindings were inspected.

### Minimal-delta direction

The evidence supports additive `PATCH` work later: add the missing Cloudflare/OpenNext deployment integration and an environment validation/binding layer while preserving current App Router structure, variable names where possible, Vercel, and Docker as optional disabled alternates. No evidence supports `REFACTOR` or `DELETE` in AUD-010.

## 6. Findings table

| Module / Capability | Existing implementation | Existing files | Current behavior | Starter planned role | Required behavior | Gap | Action | Default enabled? | Tests today | Tests required | Cloudflare compatibility | Risk | Reason | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Next.js App Router framework | Next 15.2.3, React 19, strict TS, App Router; no Pages Router | `package.json`, `tsconfig.json`, `src/app/` | Locale route groups, layouts, pages, and route handlers | Preserve current framework under Cloudflare-first deployment | Build and serve through OpenNext Workers without structural rewrite | Target build not executed; no adapter integration | `KEEP + TEST` | Yes | No project test/build result; dependencies absent | Install-independent CI build plus Workers route smoke | `LIKELY_COMPATIBLE_NEEDS_VERIFICATION` | Medium | Existing framework matches the target application model; evidence does not justify redesign | Package versions, App Router tree, absent `pages/` directory |
| Middleware and Server Actions | `next-intl` middleware and three `"use server"` page actions | `src/middleware.ts`; API-key and admin post pages | Locale routing plus server-side mutations | Keep current routing/action surfaces | Prove adapter supports middleware and actions | No target-runtime verification | `KEEP + TEST` | Yes | No tests found | OpenNext middleware/action request smoke | `LIKELY_COMPATIBLE_NEEDS_VERIFICATION` | Medium | No source-level incompatibility was established | Runtime declaration search found no edge/node overrides |
| Cloudflare/OpenNext integration | No executable integration found | Repository root, `package.json`, deployment file search | README-only Cloudflare instructions reference absent artifacts | Cloudflare Workers + OpenNext golden path | Wrangler/OpenNext config, scripts, bindings, and release workflow | **CONFIRMED GAP**: deployment integration missing | `PATCH` | No | None | Workers build, local/dev, staging, and production deployment smoke | `GAP` | High | Additive deployment work is the smallest path; no application redesign required | No Wrangler/OpenNext/Worker/CI files; no `cf:deploy` script |
| Worker-sensitive dependency/API surface | `postgres`, Stripe, Creem, Resend, Fumadocs, `simple-flakeid`, Buffer and WebCrypto paths | `src/db/index.ts`, `src/lib/storage.ts`, `src/aisdk/kling/client.ts`, server integrations/routes | Server/build paths use these packages and APIs; database has a Cloudflare-specific branch | Reuse where Worker runtime supports them | Verify built output and targeted provider/database paths | Runtime/transitive compatibility unproven | `KEEP + TEST` | Yes | No target-runtime tests | OpenNext build; Worker smoke; database validation deferred to AUD-020 | `LIKELY_COMPATIBLE_NEEDS_VERIFICATION` | High | Lack of config is not proof of incompatibility; no Node built-in source imports found | Source imports and Buffer/WebCrypto search |
| Vercel deployment path | Vercel function duration config and documented deploy path | `vercel.json`, `package.json`, `README.md` | Existing alternate hosting support | Retain without making it the golden path | Remain available as optional fallback/legacy path | No Cloudflare conflict | `KEEP-DISABLED` | Yes in current docs | Not run | Optional Vercel smoke only if retained | `NOT_APPLICABLE` | Low | Frozen direction changes default priority, not retention value | `vercel.json` has API `maxDuration: 60` |
| Docker deployment path | Node 18 Alpine multi-stage standalone image | `Dockerfile`, `package.json` | Manual `docker:build` path; no compose file | Retain as optional alternate | Keep container build independently testable | No Cloudflare conflict; Node-version build outcome unverified | `KEEP-DISABLED` | No | Not run; dependencies absent | Docker build/smoke if alternate is retained | `NOT_APPLICABLE` | Low | Working alternate support should not be deleted for Cloudflare-first | Docker standalone build and `docker:build` script |
| Build and runtime version controls | Dev/build/start/analyze scripts; no engine/package-manager version declaration | `package.json`, `Dockerfile` | Local shell is Node 20; Docker uses Node 18 | Reproducible builds across supported environments | Verify compatible Node/pnpm build matrix before pinning/changes | No build evidence; version alignment not declared | `KEEP + TEST` | Yes | Not run; `node_modules/` absent | Clean pnpm install plus build in supported CI/target environment | `LIKELY_COMPATIBLE_NEEDS_VERIFICATION` | Medium | Version mismatch is not a confirmed failure without a build result | `node --version`, `pnpm --version`, Docker base image, package manifest |
| Environment variable naming and public boundary | `.env.example` groups variables; client-oriented reads use `NEXT_PUBLIC_*`/`NODE_ENV` | `.env.example`, components/hooks/providers, `src/app/` | 96 distributed env reads; public naming is mostly explicit | Preserve names where feasible and prevent secret exposure | Verify client bundle contains no non-public variables | No centralized config contract; exposure test absent | `KEEP + TEST` | Yes | No config tests | Client bundle/env exposure smoke and per-environment config test | `LIKELY_COMPATIBLE_NEEDS_VERIFICATION` | Medium | Existing public-prefix usage is reusable; validation can be additive | Component/hook/provider `process.env` search |
| Env validation and example coverage | Direct reads with localized throw paths; incomplete example | `.env.example`, `src/db/config.ts`, DB/integration/AI/email routes | Missing values can fail at execution; several consumed names are undocumented | Validated DEVELOPMENT/STAGING/PRODUCTION config | Central validation and complete safe variable inventory | **CONFIRMED GAP**: no centralized validation; direct consumed variables omitted | `PATCH` | Partial | No env validation tests | Unit validation plus environment startup/feature checks | `LIKELY_COMPATIBLE_NEEDS_VERIFICATION` | High | Add a narrow validation/binding layer without renaming all variables | 96 reads; missing-name comparison; localized throws |
| Environment separation and URLs | Localhost sample URLs; DEV and PROD docs only | `.env.example`, `README.md`, checkout/canonical/auth usage | URLs feed auth, checkout callbacks, metadata, invites, and redirects | Isolated DEVELOPMENT/STAGING/PRODUCTION URLs, secrets, DBs, and webhooks | Explicit staging config/binding map and safe per-environment values | **CONFIRMED GAP**: staging support is not evidenced; fixed sample auth secret is unsafe to copy | `PATCH` | Development sample only | No environment tests | Per-environment configuration and callback/webhook smoke | `GAP` | High | Configuration/documentation change is sufficient; no route rewrite is indicated | README env instructions, `.env.example`, URL consumers |
| Fumadocs/MDX build source | Generated `.source` alias and Fumadocs postinstall | `source.config.ts`, `src/lib/source.ts`, `package.json` | Docs tree generated during dev/postinstall and used by docs route/search | Retain docs subsystem | Prove target build generates/bundles source | No target build result | `KEEP + TEST` | Yes | Not run | OpenNext build plus docs/search route smoke | `LIKELY_COMPATIBLE_NEEDS_VERIFICATION` | Medium | Existing subsystem has no confirmed runtime blocker | Generated-source comment and postinstall script |
| Provider selection config | `PAY_PROVIDER`, `CREEM_ENV`, provider-specific environment variables | `.env.example`, checkout route, Creem/Stripe integration files | Operator-configured payment selection is present | Preserve explicit operator-controlled selection | Verify per-environment provider/webhook settings in AUD-040 | Configuration execution not audited here | `KEEP + TEST` | Stripe default in example | No tests | Defer payment/provider staging smoke to AUD-040/AUD-070 | `NOT_APPLICABLE` | Medium | Existing explicit selection matches frozen direction; payment behavior is outside this task | Checkout route provider branch and Creem integration |

## 7. Verification record

- Runtime bootstrap: `python3 tools/kyd_runtime_validate.py --root . --mode execution` returned `KYD_RUNTIME_VALIDATE: PASS` and `EXECUTION_ALLOWED = TRUE` before inspection.
- Task contract: `CURRENT_TASK.contract` matched the AUD-010 TASK_INDEX contract; AUD-000 dependency is VERIFIED and `RUNTIME_V1_FREEZE`/`AUDIT_BOOTSTRAP` are PASS.
- Framework evidence: package/config/source searches recorded App Router, middleware, Server Actions, direct runtime APIs, and deployment/config files.
- Cloudflare classification: confirmed missing deployment integration is separated from unverified application/dependency runtime compatibility.
- Environment evidence: only variable names and configuration architecture are recorded; no actual credential values are reproduced.
- Build limitation: `node_modules/` is absent; build/Docker commands were deliberately not run or repaired in this audit.
- Scope: no application/product implementation file was modified.
- Closeout: `python3 tools/kyd_runtime_validate.py --root . --mode closeout` returned `KYD_RUNTIME_VALIDATE: PASS` and `RUNTIME_STATE_VALID = TRUE`.
