# Test and Release Audit

> Task: `AUD-080`  
> Test baseline: `ABSENT`  
> Security baseline: `PATCH_REQUIRED`  
> Logging/observability: `PATCH`  
> Cloudflare/OpenNext release readiness: `ABSENT`  
> Environment promotion readiness: `ABSENT`

## Existing Test Tooling

- No Vitest, Jest, Playwright, Cypress, Testing Library, axe, visual-regression harness, test directory/file, fixture system, test script, or CI workflow was found.
- Strict TypeScript, `next build`, `next lint`, Docker build, and Runtime validator configuration exist. There is no explicit typecheck script.
- `node_modules` was absent throughout the audit. No dependency install, application typecheck, lint, build, provider call, database call, migration, browser run, or deploy was executed. Only Runtime validation results may be labeled PASS.

Final Actions: test/CI infrastructure `PATCH`; existing build scripts `KEEP + TEST`; explicit typecheck and reliable CI entry points `PATCH`.

## Shared Capability Coverage

### Final minimum Starter test matrix

| Test | Classification | Minimum evidence |
|---|---|---|
| Runtime validator | MANDATORY | Execution/closeout mode passes for governed work |
| Typecheck | MANDATORY | Explicit no-emit command passes in CI |
| Lint | MANDATORY | Configured lint command passes with pinned Next/tool versions |
| Production build | MANDATORY | Clean install and production build pass |
| Database/provider smoke | MANDATORY | Fresh/repeat migration plus isolated PostgreSQL read/write |
| Google Auth integration | MANDATORY | Verified/unverified identity, callback, session persistence |
| Magic Link lifecycle | MANDATORY | Request, expiry, one-time use, invalid/replay and abuse handling |
| Trusted-provider linking | MANDATORY | Google/Magic Link in both orders and concurrent first login produce one UUID |
| Session/logout/protected routes | MANDATORY | Session expiry/update, logout, console/admin/API denial |
| Stripe checkout/webhook | MANDATORY | One-time checkout, callback, signature, failure/retry in provider test mode |
| Creem checkout/webhook | MANDATORY | Product map, checkout, callback, signature, failure/retry in provider test mode |
| Webhook idempotency/double grant | MANDATORY | Sequential/concurrent replay and partial failure yield one consistent result |
| Core entitlement | MANDATORY | Durable one-time ownership and revocation/failure policy |
| Credits | CONDITIONAL_IF_ENABLED | Grant/consume/expiry/concurrency/no-double-grant |
| AdSense/analytics | CONDITIONAL_IF_ENABLED | Disabled loads nothing; enabled script/pageview/consent behavior |
| i18n | CONDITIONAL_IF_ENABLED | Default-off path plus locale routing/fallback/SEO when enabled |
| OpenAI | CONDITIONAL_IF_ENABLED | Operator model policy, auth, errors, stream, limits |
| Other AI providers | CONDITIONAL_IF_ENABLED | Explicit opt-in, secrets, allowed models and error paths |
| Storage/R2 | CONDITIONAL_IF_ENABLED | Authorization, size/type, upload/read, privacy and Worker bytes |
| Turnstile | CONDITIONAL_IF_ENABLED | Disabled bypass and valid/invalid/expired server verification |
| Blog/docs/charts/editor/API keys/affiliate/subscriptions | CONDITIONAL_IF_ENABLED | Focused domain/render/security tests for each selected surface |
| UI render/navigation | MANDATORY | Core public/auth/account/admin/member route smoke |
| Responsive browser smoke | MANDATORY | Shared mobile/desktop navigation, pricing, Auth and shells |
| Accessibility smoke | MANDATORY | Keyboard/focus, labels/errors, dialogs/drawers and navigation |
| Visual regression | OPTIONAL | Small baseline for highest-value shared shells/components |
| Cloudflare/OpenNext Staging smoke | MANDATORY | Production-shaped Worker deploy with DB/Auth/payment-enabled checks |

## Real Provider Staging Gaps

1. No PostgreSQL provider has been selected or exercised in Workers/Hyperdrive.
2. Google OAuth callback/cookie/session behavior has no Cloudflare Staging evidence.
3. Resend Magic Link does not exist and has no delivery/token lifecycle evidence.
4. Stripe and Creem have no real provider test-mode checkout/webhook replay evidence.
5. AI, storage/R2, analytics/ads, and Turnstile have no conditional Staging evidence.
6. No Staging deployment or exact-commit promotion mechanism exists.

Provider smoke is mandatory only for Core and enabled optional capabilities. Disabled optional modules must be proven cleanly disabled without requiring secrets.

## Security / Logging

### Minimum Security Gates

| Gate | Classification | Pass condition |
|---|---|---|
| Auth canonical identity/linking | MANDATORY | Trusted Google/Magic Link same-email paths resolve to one UUID under concurrency |
| Google verified email | MANDATORY | Unverified/untrusted claims cannot create/link a canonical user |
| Magic Link token lifecycle | MANDATORY | Expiring, one-time, replay-safe token with bounded request abuse |
| Protected API authorization | MANDATORY | Every retained high-risk mutation/provider route proves caller/ownership server-side |
| Secret/public env boundary | MANDATORY | No fixed reusable secret, client-secret exposure, or secret/PII logging |
| Targeted rate limiting | MANDATORY | Auth and provider-backed abuse-prone routes enforce tested limits |
| Payment server pricing | MANDATORY | Client cannot select arbitrary product amount/currency behavior |
| Webhook signature | MANDATORY | Invalid Stripe/Creem signatures fail before mutation |
| Webhook idempotency/double grant | MANDATORY | Replay/concurrency/partial failure cannot duplicate or omit required side effects |
| AI provider/model policy | CONDITIONAL_IF_ENABLED | Operator allowlist/default, caller auth and bounded usage |
| Storage authorization | CONDITIONAL_IF_ENABLED | Object access/key/type/size/privacy rules are enforced |
| Turnstile | OPTIONAL | Apply only when selected route risk warrants it |

Logging final Action is `PATCH`: introduce minimal redacted structured server logs, request/correlation IDs, deployment revision, error context, and a non-secret health/readiness smoke target. A full Sentry/OpenTelemetry/enterprise observability platform is not required.

## Build / Deploy / Release

### Minimum Release Gates

| Gate | Classification | Pass condition |
|---|---|---|
| Runtime validator | MANDATORY | Required execution/closeout mode PASS |
| Typecheck | MANDATORY | Explicit CI command PASS |
| Lint | MANDATORY | Pinned lint command PASS |
| Production build | MANDATORY | Clean reproducible build PASS |
| Focused automated suite | MANDATORY | All mandatory and enabled-capability tests PASS |
| Dependency/secret scan | MANDATORY | Bounded scan has no unaccepted high-risk result |
| DB/provider smoke | MANDATORY | Migration/read/write/connection checks PASS in isolated environment |
| Cloudflare DEVELOPMENT deploy | MANDATORY | When used for active development, deployment and core smoke PASS |
| Cloudflare STAGING deploy | MANDATORY | Production-shaped Worker deployment PASS |
| Staging core smoke | MANDATORY | DB/Auth/UI/runtime checks PASS on Cloudflare |
| Payment smoke | CONDITIONAL_IF_ENABLED | Selected provider checkout/webhook test-mode flow PASS |
| Optional capability smoke | CONDITIONAL_IF_ENABLED | Each enabled module passes config/runtime smoke |
| Responsive/a11y smoke | MANDATORY | Shared desktop/mobile and keyboard/focus checks PASS |
| Migration/rollback readiness | MANDATORY | Compatible ordering and concise recovery procedure verified |
| Exact verified commit promotion | MANDATORY | Production commit equals the Staging-verified commit |

Vercel and Docker remain `KEEP-DISABLED`; their smoke tests are `CONDITIONAL_IF_ENABLED` when advertised as supported alternates.

## Actions

| Capability | Final Action | Minimum implementation scope |
|---|---|---|
| Test harness/scripts | PATCH | Focused framework and commands, no oversized test pyramid |
| Existing build scripts | KEEP + TEST | Execute in clean CI and Cloudflare target path |
| Security controls | PATCH | Close only evidenced high-risk gaps and add gates |
| Logging/diagnostics | PATCH | Redaction, context, health/revision; no enterprise platform |
| CI | PATCH | Run minimum test/security/release gates |
| Cloudflare release | PATCH | Development/Staging/Production, same commit promotion |
| Vercel/Docker | KEEP-DISABLED | Retain optional paths without golden-path status |

Cross-cutting production-readiness conclusion: `YES — PATCH`. No `REFACTOR` or `DELETE` is justified.
