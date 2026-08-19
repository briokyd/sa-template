# Repository Inventory / Audit Bootstrap

> Task: `AUD-000`  
> Status: `VERIFIED`  
> Authority: `AUDIT-001`  
> Scope: factual repository inventory only; no product implementation audit or code change

## Audit boundary

This document establishes the repository map for `AUD-010` through `AUD-080`. It records repository-visible paths, configuration, dependencies, entry points, and explicit unknowns. It does not make final reuse, patch, refactor, or deletion decisions. Those decisions belong to the designated workstream tasks.

No application or product implementation files were modified for AUD-000.

## 1. Repository identity

| Field | Evidence |
|---|---|
| Repository | `sa-template`; root contains `package.json` and `.git/` |
| Audit branch | `audit/kyd-starter-v1` |
| Audited HEAD | `503ca9a0f46bc732fe974b6d336e1d1fcd2eb8a4` (`feat: preview img`) |
| Base branch/ref | Local `main` and `origin/main` point to the same HEAD before the audit branch was created |
| Remote | `origin git@github.com:briokyd/sa-template.git` for fetch and push |
| Upstream | `audit/kyd-starter-v1` tracks `origin/audit/kyd-starter-v1` |
| Baseline status | Before AUD-000 edits: `## audit/kyd-starter-v1...origin/audit/kyd-starter-v1` |
| Baseline untracked state | The Runtime bootstrap pack was already untracked before AUD-000 edits: `AGENTS.md`, `KYD_AUDIT_BOOTSTRAP_MANIFEST.json`, `KYD_AUDIT_BOOTSTRAP_README.md`, `docs/`, `sa_template_Kyd_Full_Repository_Audit_Bootstrap_R1.zip`, and `tools/` |

Evidence commands: `git status --short --branch`, `git rev-parse HEAD`, `git log -1 --oneline --decorate`, `git branch --all --no-color`, and `git remote -v`.

## 2. Top-level structure

| Path | Observed contents / purpose |
|---|---|
| `src/` | TypeScript application source; 251 files observed |
| `src/app/` | Next.js App Router pages, layouts, route handlers, global CSS; 51 files observed |
| `src/components/` | Shared UI, landing blocks, auth, dashboard, console, analytics, and provider surfaces; 97 files observed |
| `src/auth/` | Auth.js/NextAuth configuration, handler, exports, and session provider |
| `src/db/` | Drizzle schema, PostgreSQL client setup, migrations, and migration metadata |
| `src/models/` | Database model operations for users, orders, credits, posts, feedback, API keys, and affiliates |
| `src/services/` | User, order, Stripe, credit, affiliate, API key, page, and related business service functions |
| `src/integrations/` | Stripe and Creem client wrappers |
| `src/aisdk/` | AI SDK exports and a custom Kling image/video provider implementation |
| `src/i18n/` | `next-intl` routing, request configuration, locale definitions, messages, and page translations |
| `src/lib/` | Auth, storage, cache, hashing, IP, response, source, time, and utility helpers |
| `src/providers/` | Theme provider and AdSense provider |
| `src/hooks/`, `src/contexts/`, `src/types/` | React hooks, app context, and TypeScript declarations |
| `content/docs/` | Fumadocs MDX content and English/Chinese document metadata |
| `public/` | Static images, icons, logos, `robots.txt`, `sitemap.xml`, and favicon; 52 files observed |
| `debug/` | `apitest.http` request scratch file |
| `docs/` | Kyd Runtime, audit authority, workstream placeholders, task state, feature matrix, and trace; 25 files observed |
| `tools/` | `kyd_runtime_validate.py`, the Runtime validation tool |
| Root config | `package.json`, `pnpm-lock.yaml`, Next.js, TypeScript, PostCSS, Docker, Vercel, MDX, shadcn, env example, and README files |

There is no `pnpm-workspace.yaml`, `package-lock.json`, `yarn.lock`, `turbo.json`, `nx.json`, or other workspace/monorepo indicator in the observed repository tree.

## 3. Package manager, framework, and runtime

- Package manager evidence is `pnpm-lock.yaml`, the `pnpm` commands in `package.json`, and the README Quick Start instruction `pnpm install` / `pnpm dev`. The package is private and has no workspace members.
- Framework evidence is `next: 15.2.3`, `react: ^19.0.0`, `react-dom: ^19.0.0`, `typescript: ^5.7.2`, and the `src/app/` App Router tree.
- `next.config.mjs` enables `output: "standalone"`, MDX page extensions, `next-intl`, Fumadocs MDX, bundle analysis, and experimental `mdxRs`.
- UI/build libraries visible in `package.json` include Tailwind CSS/PostCSS, Radix UI, shadcn configuration, `lucide-react`, `react-icons`, React Hook Form, and Framer Motion.
- Data/runtime libraries visible in `package.json` include `drizzle-orm`, `drizzle-kit`, `postgres`, NextAuth/Auth.js beta, Stripe, Creem, Resend, AI SDK packages, `aws4fetch`, and `next-intl`.

Framework, runtime, compatibility, and environment behavior are routed to `AUD-010`; this section does not verify runtime behavior.

## 4. Build, test, deploy, and configuration entry points

### Package scripts

`package.json` declares:

- `dev`: `next dev --turbopack` through `cross-env`.
- `build`: `next build`.
- `start`: `next start`.
- `lint`: `next lint`.
- `analyze`: bundle analyzer wrapper around `pnpm build`.
- `docker:build`: Docker image build.
- `db:generate`, `db:migrate`, `db:studio`, and `db:push`: Drizzle Kit commands using `src/db/config.ts`.
- `postinstall`: `fumadocs-mdx` generation.

No test, typecheck, end-to-end, or coverage script is declared in `package.json`.

### Configuration and deployment files

| File | Observable role |
|---|---|
| `next.config.mjs` | Next.js standalone output, MDX, i18n plugin, bundle analyzer, image patterns |
| `tsconfig.json` | Strict TypeScript, bundler resolution, `@/*` alias to `src/*`, Next plugin |
| `postcss.config.mjs` | Tailwind v4 PostCSS plugin |
| `components.json` | shadcn component aliases and Tailwind CSS variable settings |
| `source.config.ts` | Fumadocs MDX source directory `content/docs` |
| `vercel.json` | Vercel function `maxDuration` for `app/api/**/*` |
| `Dockerfile` | Node 18 Alpine multi-stage standalone Next.js container |
| `.env.example` | Environment variable names and provider comments; actual local env files were not present in the observed file list |
| `README.md` | Vercel deployment, a claimed Cloudflare branch workflow, and `wrangler.toml.example` instructions |
| `.gitignore` | Ignores local env files, Next build output, coverage, build output, `.wrangler`, and `wrangler.toml` |

The current tree has no `wrangler.toml`, `wrangler.toml.example`, OpenNext package/config, Worker entrypoint, `.github/workflows`, or Cloudflare deployment script. The README references a Cloudflare branch and `npm run cf:deploy`, but the current `package.json` has no `cf:deploy` script. This is an AUD-010/AUD-070 observation, not a change request.

## 5. Application and route map

The application uses route groups under `src/app/[locale]/`:

- Default product surfaces: landing page, pricing, showcase, posts listing/detail, invite-code page, and legal pages.
- Auth surface: `src/app/[locale]/auth/signin/page.tsx`.
- Authenticated console: orders, credits, invites, API keys, and API-key creation under `src/app/[locale]/(default)/(console)/`.
- Admin surface: users, orders, posts, post creation/editing, and feedback under `src/app/[locale]/(admin)/`.
- Docs surface: Fumadocs catch-all route under `src/app/[locale]/(docs)/docs/[[...slug]]/`.

The observed API route map is:

```text
src/app/api/add-feedback/route.ts
src/app/api/auth/[...nextauth]/route.ts
src/app/api/checkout/route.ts
src/app/api/demo/gen-image/route.ts
src/app/api/demo/gen-stream-text/route.ts
src/app/api/demo/gen-text/route.ts
src/app/api/demo/send-email/route.ts
src/app/api/docs/search/route.ts
src/app/api/get-user-credits/route.ts
src/app/api/get-user-info/route.ts
src/app/api/pay/callback/creem/route.ts
src/app/api/pay/callback/stripe/route.ts
src/app/api/pay/notify/creem/route.ts
src/app/api/pay/notify/stripe/route.ts
src/app/api/ping/route.ts
src/app/api/update-invite-code/route.ts
src/app/api/update-invite/route.ts
```

## 6. Capability inventory and later audit routing

This is an inventory map, not a preliminary capability decision. Initial notes identify what is visible and what must be verified later.

| Area / capability | Relevant directories and files | Visible framework / library / provider | Observable purpose from repository structure | Later audit task(s) | Initial notes and unknowns |
|---|---|---|---|---|---|
| Framework and App Router | `src/app/`, `src/middleware.ts`, `next.config.mjs`, `tsconfig.json` | Next.js 15.2.3, React 19, TypeScript | Locale-aware App Router pages and route handlers | `AUD-010` | Cloudflare/OpenNext runtime suitability is not established by inventory alone |
| Package/workspace | `package.json`, `pnpm-lock.yaml` | pnpm; single private package | Dependency and script entry point | `AUD-010` | No workspace/monorepo manifest observed |
| Environment/config | `.env.example`, `src/auth/config.ts`, `src/db/config.ts`, `src/i18n/locale.ts`, payment and AI routes | `process.env` configuration | Provider toggles, URLs, secrets, database, storage, analytics, and payment settings | `AUD-010`, plus `AUD-020`/`030`/`040`/`050` | Only example configuration was observed; runtime values and completeness require later verification |
| Cloudflare/OpenNext/deploy runtime | `README.md`, `next.config.mjs`, `vercel.json`, `Dockerfile`, `src/db/index.ts`, `src/lib/ip.ts` | Vercel config, standalone Node container; Cloudflare header/branch references | Vercel/Docker deployment and limited Cloudflare-aware code comments | `AUD-010`, `AUD-070` | No Wrangler/OpenNext config or Worker entrypoint observed; `src/db/index.ts` has a Cloudflare detection branch but that does not prove deployment compatibility |
| Database and migrations | `src/db/schema.ts`, `src/db/index.ts`, `src/db/config.ts`, `src/db/migrations/` | Drizzle ORM/Kit, `postgres`, PostgreSQL dialect | PostgreSQL schema/client and one SQL migration with snapshot/journal metadata | `AUD-020` | Tables visibly include users, orders, API keys, credits, posts, affiliates, and feedback; A-001 remains audit-dependent |
| Auth.js / OAuth / session | `src/auth/`, `src/lib/auth.ts`, `src/services/user.ts`, `src/components/sign/`, `src/hooks/useOneTapLogin.tsx`, auth API route | `next-auth` 5.0.0-beta.25; Google, GitHub, Google One Tap credentials flow | Provider-gated login, JWT/session callbacks, user persistence, client session provider, sign-in/sign-out UI | `AUD-030` | Google/GitHub and One Tap providers are visible; provider activation depends on env flags. Identity linking and account semantics require deep audit |
| Magic Link / email auth | `src/components/sign/form.tsx`, `src/components/sign/modal.tsx`, `src/auth/config.ts`, `src/app/api/demo/send-email/route.ts` | Resend dependency; no EmailProvider symbol located in the observed Auth config | Email form controls and a demo Resend send route are visible | `AUD-030` | Magic Link/Auth.js Email provider was not located by repository search; this is `UNKNOWN / NOT VERIFIED` until AUD-030 verifies the intended path. `RESEND_API_KEY` and `RESEND_SENDER_EMAIL` are used by the demo route but are not present in `.env.example` |
| Account/profile/logout | `src/services/user.ts`, `src/models/user.ts`, `src/components/sign/user.tsx`, `src/components/dashboard/sidebar/user.tsx`, console/admin layouts | NextAuth session and database user model | User lookup, session-derived profile display, sign-out, console/admin access checks | `AUD-030`, `AUD-060` | No dedicated account-deletion route/file was located in the inventory search; verify against requirements later |
| Orders and checkout | `src/models/order.ts`, `src/services/order.ts`, `src/app/api/checkout/route.ts`, pricing pages/components, `src/db/schema.ts` | Drizzle model operations; Stripe/Creem clients | Creates orders from pricing data, selects provider using `PAY_PROVIDER`, returns checkout result | `AUD-040` | One-time and subscription interval branches are visible; correctness, idempotency, and entitlement semantics are not verified |
| Stripe / Creem / callbacks / webhooks | `src/integrations/stripe/`, `src/integrations/creem/`, `src/services/stripe.ts`, `src/app/api/pay/callback/`, `src/app/api/pay/notify/` | `stripe` SDK, `@stripe/stripe-js`, `creem` SDK | Provider clients, browser callbacks, server notify routes, metadata and order updates | `AUD-040` | Both providers and a runtime provider switch are visible. The `orders` schema contains Stripe-named fields alongside Creem paths; provider-neutral behavior is deferred to deep audit |
| Credits / paid access / entitlement relationship | `src/db/schema.ts`, `src/models/credit.ts`, `src/services/credit.ts`, `src/app/api/get-user-credits/route.ts`, console credit/order pages | Drizzle-backed credit model and service | Credit transactions, credit display, and order-linked fields | `AUD-040` | Relationship between paid order status and credit grants requires evidence from the payment workstream |
| Email delivery | `src/app/api/demo/send-email/route.ts`, `package.json`, `src/i18n/messages/` | Resend 4.8.0 | Demo API sends email using `RESEND_API_KEY` and `RESEND_SENDER_EMAIL` | `AUD-030` | Production adapter role, templates, retries, and provider configuration are not verified |
| Ads and analytics | `src/providers/adsense.tsx`, `src/components/analytics/`, `src/providers/theme.tsx`, `.env.example` | AdSense, Google Analytics, OpenPanel, Plausible | Production-only, env-gated script/components mounted from theme provider | `AUD-050` | Default activation depends on environment values; consent, staging behavior, and provider isolation require later audit |
| SEO and metadata | `src/app/layout.tsx`, locale/default/docs/legal layouts, page `generateMetadata` functions, `public/robots.txt`, `public/sitemap.xml` | Next.js Metadata API and static robots/sitemap | Metadata, locale alternate links, canonical URLs on selected pages, static crawl files | `AUD-050` | Staging noindex, structured data, and canonical completeness are `UNKNOWN / NOT VERIFIED` |
| i18n | `src/i18n/`, `src/middleware.ts`, `src/app/[locale]/`, `src/i18n/messages/`, `src/i18n/pages/` | `next-intl` 4.1.0 | English/Chinese locale routing, messages, page content, optional locale detection | `AUD-050` | `en`/`zh`, default `en`, `as-needed` prefix; supported/tested behavior for all route classes requires later audit |
| AI text/image/video | `src/app/api/demo/gen-text/route.ts`, `gen-stream-text`, `gen-image`, `src/aisdk/` | Vercel AI SDK, OpenAI, DeepSeek, OpenRouter, SiliconFlow-compatible, Replicate, custom Kling | Provider-selected text/image generation and Kling image/video abstractions | `AUD-050` | Optional provider surface is visible; secrets, default path, rate limits, and Workers compatibility require later audit |
| Storage | `src/lib/storage.ts`, `src/app/api/demo/gen-image/route.ts`, `.env.example` | `aws4fetch`; S3-compatible endpoint configuration | Upload and download-then-upload helper with bucket/domain settings | `AUD-050` | No R2 binding/configuration is visible; R2 suitability and response/security behavior are deferred |
| Turnstile | Repository-wide filename and symbol search for `turnstile` / `TURNSTILE` | No provider/library/config found | No visible implementation entry point | `AUD-050` | `UNKNOWN / NOT VERIFIED` as a capability requirement; absence is recorded without recommending a change |
| Blog/posts/content/docs | `content/docs/`, `source.config.ts`, `src/lib/source.ts`, `src/app/[locale]/(docs)/`, `src/app/[locale]/(default)/posts/`, `src/models/post.ts`, admin post pages | Fumadocs MDX, `@mdx-js`, Next MDX, Drizzle posts model | MDX docs/search and database-backed post listing/detail/admin editing | `AUD-050`, `AUD-060` | Content and post surfaces are visible; publishing, search, and deployment behavior require later audit |
| API keys / affiliate / referral | `src/models/apikey.ts`, `src/services/apikey.ts`, API-key pages; affiliate model/service; invite routes/pages/components | Drizzle models and React console surfaces | API key creation/listing plus invite-code and affiliate reward flow | `AUD-050` | Security, key lifecycle, referral accounting, and default exposure are not verified |
| Dashboard / pricing / SaaS surfaces | `src/app/[locale]/(admin)/`, `src/app/[locale]/(default)/(console)/`, `src/components/dashboard/`, `src/components/console/`, pricing blocks/pages | React Server Components, Tailwind, shared sidebar/slot components | Admin and authenticated console workflows, pricing, orders, credits, invites, API keys | `AUD-050`, `AUD-060` | Capability existence is visible; UI foundation keep list and behavioral completeness are explicitly deferred |
| UI foundation and shared shells | `src/components/ui/`, `src/components/blocks/`, `src/components/sign/`, `src/components/console/`, `src/components/dashboard/`, `components.json`, `src/app/globals.css`, `src/app/theme.css` | shadcn-style components, Radix UI, Tailwind, Lucide/react-icons | Reusable primitives, landing blocks, auth shell, console/dashboard shell, theme | `AUD-060` | Shared components are inventoried only; A-002 remains audit-dependent |
| Tests, security, logging, errors | `package.json`, `.gitignore`, `debug/apitest.http`, `src/lib/resp.ts`, `src/lib/ip.ts`, `src/lib/hash.ts`, source `console.*` calls | Next lint script; no test framework/config found | Response helpers, IP/hash helpers, ad hoc console logging, HTTP scratch requests | `AUD-070` | No test candidates were found by filename search. Security, redaction, error handling, and real-provider staging support are not verified |
| Release tooling and documentation | `package.json`, `Dockerfile`, `vercel.json`, `README.md`, `content/docs/`, `tools/kyd_runtime_validate.py` | Next standalone/Docker, Vercel metadata, Fumadocs, Kyd Runtime validator | Local development/build, database commands, docs generation, deployment instructions, audit validation | `AUD-010`, `AUD-070` | README and package scripts contain deployment/documentation drift to verify later; Runtime validator itself is bootstrap tooling, not application behavior |

## 7. Generated, vendor, and low-signal directories

The following paths are excluded from normal later inventory reads unless a workstream explicitly needs them:

- `node_modules/`, `.next/`, `out/`, `coverage/`, `build/`, `.wrangler/`, and local env files are ignored or identified in `.gitignore` as generated/local output.
- `src/db/migrations/meta/0000_snapshot.json` and `src/db/migrations/meta/_journal.json` are generated migration metadata and should be read with the migration SQL/schema, not treated as independent product modules.
- `.source` is referenced by the TypeScript alias and Fumadocs conventions but no generated `.source` file appeared in the observed repository file list.
- `pnpm-lock.yaml` is package-manager evidence and should be consulted for dependency provenance, not treated as application source.
- `sa_template_Kyd_Full_Repository_Audit_Bootstrap_R1.zip` and the untracked Runtime pack files are audit/bootstrap artifacts, not product capabilities.

## 8. Bootstrap blockers and explicit unknowns

### Bootstrap status

- Runtime execution validation passed before AUD-000 inspection: `KYD_RUNTIME_VALIDATE: PASS`, `MODE = execution`, `EXECUTION_ALLOWED = TRUE`.
- `AUD-000` has no execution blocker at inventory scope.
- No application/product implementation file was changed during inspection or inventory drafting.

### Deferred unknowns

- Cloudflare Workers/OpenNext compatibility and actual deployment path are not proven by the current repository tree; route to `AUD-010`.
- Actual environment values, provider credentials, database connectivity, and real-provider staging behavior are not present/verified; route to the relevant workstreams and `AUD-070`.
- Auth.js Email/Magic Link behavior was not located in the visible provider configuration; route to `AUD-030` as `UNKNOWN / NOT VERIFIED`.
- Test coverage, security baseline, logging/redaction, and release smoke support are not established; route to `AUD-070`.
- Turnstile has no visible repository entry point; route to `AUD-050` as `UNKNOWN / NOT VERIFIED`.
- A-001 (default PostgreSQL provider) and A-002 (final UI foundation keep list) remain audit-dependent and are not decided here.

## 9. Action taxonomy boundary

AUD-000 is inventory-only and does not issue capability recommendations or preliminary module classifications. The Findings Table from the bootstrap template is intentionally not populated with capability rows. Later workstream recommendations must use exactly one of: `KEEP`, `KEEP + TEST`, `KEEP-DISABLED`, `WRAP`, `PATCH`, `REFACTOR`, or `DELETE`. No deletion or refactor decision is made by this inventory.

## Closeout verification

- `docs/audit/work/00_REPOSITORY_INVENTORY.md` is populated with repository-grounded evidence and explicit routing/unknowns for the declared audit areas.
- `AUD-000` is `VERIFIED` in `docs/tasks/TASK_INDEX.md`; `AUD-F000` is `VERIFIED` in `docs/product/FEATURE_MATRIX.md`.
- `AUDIT_BOOTSTRAP` is `PASS` in `docs/CURRENT_STATE.md`, with the audited HEAD recorded as `503ca9a0f46bc732fe974b6d336e1d1fcd2eb8a4`.
- `python3 tools/kyd_runtime_validate.py --root . --mode execution` returned `KYD_RUNTIME_VALIDATE: PASS`.
- `python3 tools/kyd_runtime_validate.py --root . --mode closeout` returned `KYD_RUNTIME_VALIDATE: PASS` and `RUNTIME_STATE_VALID = TRUE`.
- The final status review showed only the pre-existing untracked Runtime/bootstrap pack plus the permitted audit and Runtime documentation files; no application/product implementation file was modified.

## Evidence commands

The inventory was assembled from these read-only repository commands, in addition to targeted file reads cited above:

```text
git status --short --branch
git rev-parse HEAD
git log --all --oneline --decorate -20
git branch --all --no-color
git remote -v
rg --files --hidden -g '!.git/**' -g '!node_modules/**'
rg --files src/app
rg --files src/components
rg --files docs
rg --files --hidden -g '!.git/**' -g '!node_modules/**' | rg '(^|/)(__tests__|tests?)(/|$)|\.(test|spec)\.'
rg -n -i 'cloudflare|open.?next|wrangler|turnstile|resend|EmailProvider|robots|sitemap|canonical|storage|stripe|creem|analytics|adsense' src package.json .env.example README.md
```
