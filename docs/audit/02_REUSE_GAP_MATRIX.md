# Reuse / Gap Matrix

> Task: `AUD-080`  
> Purpose: bounded Starter Detailed Spec backlog; this file does not create implementation Tasks.

## Final Action Summary

### KEEP

No major capability is assigned bare `KEEP`; verified test evidence is absent repository-wide.

### KEEP + TEST

Next.js/App Router, middleware/Server Actions, PostgreSQL/Drizzle/migrations, DB connection branch, JWT/session/logout, AdSense, analytics, shadcn/Radix primitives, forms/tables, dashboard/console/marketing shells, assets/icons, and retained build paths.

### KEEP-DISABLED

GitHub OAuth, Google One Tap, credits, Stripe subscriptions, API keys, blog/docs/charts/editor, Vercel, and Docker. Existing additional AI providers are intended to become cleanly disabled after `GAP-013` supplies the missing policy boundary.

### WRAP

Resend Auth email delivery and theme/application composition. Both preserve existing implementation behind a thin boundary.

### PATCH

Cloudflare/OpenNext, environment validation/separation, database transactions, Auth/Magic Link/trusted identity, account/profile, payment lifecycle/idempotency/entitlement, technical SEO, optional-module policy, storage/R2, UI state/accessibility gaps, testing/security/logging/CI/release.

### REFACTOR

None. No verified workstream proved `KEEP`, `KEEP + TEST`, `KEEP-DISABLED`, `WRAP`, and `PATCH` collectively insufficient.

### DELETE CANDIDATES

None. Retention or `KEEP-DISABLED` is lower risk for every non-Core capability found.

## Implementation Gap Backlog

| Gap ID | Capability | Description | Source audit | Action | Priority | Dependency | Required Gate | Evidence | Acceptance intent |
|---|---|---|---|---|---|---|---|---|---|
| GAP-001 | Cloudflare/OpenNext | Add the minimum Worker adapter, Wrangler/config, compatibility flags, bindings, and deploy scripts. | AUD-010, AUD-070 | PATCH | P0 | Frozen runtime target | Release Gate: Cloudflare Development/Staging deploy | No adapter/config/script exists; README references absent artifacts. | Current app builds and deploys to Cloudflare Development and Staging without structural rewrite. |
| GAP-002 | Environment/config/secrets | Add complete safe variable inventory, validation, and isolated DEVELOPMENT/STAGING/PRODUCTION bindings; remove reusable fixed secret sample. | AUD-010, AUD-070 | PATCH | P0 | GAP-001 | Security Gate: secret/public boundary; Release Gate: environment isolation | Distributed env reads, missing names, no Staging model, fixed Auth sample. | Disabled features need no secrets; enabled features fail clearly; environments use distinct URL/DB/Auth/payment/webhook config. |
| GAP-003 | Tests and CI | Add focused unit/integration/browser harness and CI gates for typecheck, lint, build, tests, scans, and Runtime validation. | AUD-070 | PATCH | P0 | None | Release Gate: automated verification | No test runner/files/scripts/CI; typecheck script absent. | Minimum matrix runs deterministically from pinned dependencies and records pass/fail. |
| GAP-004 | Magic Link and trusted identity | Add real Email Magic Link token lifecycle, Google verified-email policy, deterministic same-email canonical UUID behavior, and concurrency safety. | AUD-030 | PATCH | P0 | GAP-002, database invariant decision | Security Gate: Auth identity/Magic Link | Magic Link absent; email-first sequential reuse exists; trust/concurrency not guaranteed. | Google and Magic Link in either order resolve to one trusted user; tokens expire and are single-use. |
| GAP-005 | Resend Auth delivery | Preserve current Resend SDK use behind a narrow Auth email adapter/template/config boundary. | AUD-030 | WRAP | P0 | GAP-002, GAP-004 | Security Gate: Magic Link lifecycle | Resend exists only in generic demo route and is absent from Auth. | Auth sends redacted, configured Magic Links through one tested boundary. |
| GAP-006 | API authorization and abuse | Enforce caller ownership/authorization, request validation, provider/model policy, and targeted throttling for high-risk mutation/provider routes. | AUD-030, AUD-050, AUD-070 | PATCH | P0 | GAP-002, GAP-003 | Security Gate: protected APIs/rate limits | AI/email demo routes lack user checks; invite update trusts caller UUID; no rate limiter. | Negative tests prove unauthorized callers cannot mutate users or consume provider-backed services. |
| GAP-007 | Payment atomicity/idempotency | Make paid transition plus credit/affiliate/entitlement side effects replay-safe and atomic under retry/concurrency. | AUD-020, AUD-040, AUD-070 | PATCH | P0 | Database transaction scope, GAP-003 | Security Gate: webhook idempotency/double grant | Status/read-before-insert guards are partial; no transaction/event ledger/unique side-effect link. | Duplicate, concurrent, and partial-failure delivery produces one consistent paid result. |
| GAP-008 | Cloudflare release/promotion | Implement Staging smoke, same-commit Production promotion, migration ordering, and concise rollback/recovery process. | AUD-070 | PATCH | P0 | GAP-001, GAP-002, GAP-003 | Release Gate: exact verified commit | No Staging, promotion, migration-order, or rollback evidence. | Production commit equals Staging-verified commit and has documented recovery evidence. |
| GAP-009 | Auth/account completion | Harden callback/error handling and provide tested profile/account/logout UI without Adapter migration or account deletion. | AUD-030, AUD-060 | PATCH | P1 | GAP-004, GAP-003 | Security Gate: protected routes | Profile edit absent; callback/session/logout error paths untested. | Core account/profile/logout and safe callback behavior pass integration/browser tests. |
| GAP-010 | Payment lifecycle/entitlement | Validate provider selection and complete one-time failure/cancel/refund/revocation and paid-access policy around existing orders. | AUD-040 | PATCH | P1 | GAP-007, GAP-003 | Security/Release Gate: enabled payment smoke | Created orders can remain after checkout failure; general entitlement is partial. | Both providers expose coherent success/failure state and durable queryable one-time access. |
| GAP-011 | Technical SEO | Correct base URL/canonical coverage, replace static stale sitemap, add robots/noindex and social/structured metadata as bounded helpers. | AUD-050 | PATCH | P1 | GAP-002 | Release Gate: Staging noindex/SEO smoke | Static one-URL sitemap, no metadataBase/social/JSON-LD/Staging noindex. | Route metadata and crawl controls are correct per environment. |
| GAP-012 | i18n optionality | Keep next-intl but define a supported/tested default-off project path. | AUD-050 | PATCH | P1 | GAP-001, GAP-003 | Release Gate: optional-module disable behavior | Locale detection is off but routing/middleware/imports are structurally on. | Default Starter can run without forced localization complexity; enabled locales still work. |
| GAP-013 | AI provider policy | Make OpenAI the explicit optional standard and place other providers behind operator allowlist/config with auth, limits, and safe logging. | AUD-050, AUD-070 | PATCH | P1 | GAP-002, GAP-006 | Security Gate: AI provider/model policy | Public routes accept caller provider/model; no allowlist/auth/limits/accounting. | Disabled AI is unreachable and secret-free; enabled OpenAI/selected providers are bounded and tested. |
| GAP-014 | Storage/R2 | Retain S3-compatible helper; add config/authorization/object validation and verify R2/Worker byte behavior. | AUD-050 | PATCH | P1 | GAP-001, GAP-002, GAP-006 | Security Gate: storage authorization | No R2 proof, signed URL/privacy/size/type policy; Buffer path unverified. | Disabled storage is clean; enabled S3/R2 upload/read path passes authorization and Worker smoke. |
| GAP-015 | UI bounded fixes | Correct token/tool config, pricing grid/semantics, theme toggle/composition, Auth UI additions, route states, and accessibility issues. | AUD-060 | PATCH | P1 | GAP-003, GAP-004, GAP-010 | Release Gate: responsive/a11y smoke | Known localized UI gaps; reusable foundation otherwise evidenced. | Frozen A-002 foundation remains; core routes pass render, keyboard, mobile, loading/error tests. |
| GAP-016 | Logging/observability | Add minimal redacted structured server logging, request correlation, revision diagnostics, and health/readiness smoke target. | AUD-070 | PATCH | P1 | GAP-001, GAP-002 | Security Gate: secret/PII redaction | Direct console logs include provider/user result objects; no correlation/health/error telemetry. | High-risk failures are diagnosable without leaking secrets/PII; no enterprise stack required. |
| GAP-017 | Turnstile | Add only an opt-in widget/server verification boundary for selected abuse-prone routes if Product Spec enables it. | AUD-050 | PATCH | P2 | GAP-006 | Conditional Security Gate: Turnstile | No implementation exists; optional absence is non-blocking. | Disabled path has no config/runtime cost; enabled routes reject invalid/expired tokens. |
| GAP-018 | Ads/analytics verification | Retain clean env-gated browser integrations and add enabled/disabled/consent smoke. | AUD-050 | KEEP + TEST | P2 | GAP-003 | Conditional Release Gate: optional capability smoke | Existing providers return null when unset; no browser tests. | Unconfigured providers load nothing; configured provider behavior is verified. |
| GAP-019 | Retained non-Core surfaces | Define opt-in defaults and focused tests for API keys, affiliates, credits, subscriptions, blog/docs/charts/editor, alternate AI, Vercel, and Docker when selected. | AUD-040, AUD-050, AUD-060, AUD-070 | KEEP-DISABLED | P2 | Owning P0/P1 safety gaps | Mature surfaces exist but are not V1 Core/default and lack tests. | Starter default excludes the surfaces without deleting them; selected surfaces inherit required domain gates. |

## Counts

| Priority | Count |
|---|---:|
| P0 | 8 |
| P1 | 8 |
| P2 | 3 |
| Total | 19 |
