# Kyd SaaS Starter STS-020 Existing Implementation Mapping

> Task: `STS-021A`  
> Status: `EVIDENCE MAPPING`  
> Authorities: `KPS-CAP-REUSE-R1`, `KSS-STS021A-MAPPING-R1`  
> Scope: read-only mapping of `F-001` through `F-009` to the current `sa-template` implementation.

## 1. Executive Summary

All nine STS-020 findings were traced to source, configuration, frozen Authority, and completed audit evidence before considering a new design.

The mapping changes the earlier decision picture:

- `F-001` already has one shared one-time payment mutation function used by both providers and both verified callback/webhook paths. Its missing lifecycle, transaction, idempotency, and entitlement rules require a bounded `PATCH`; a new payment architecture or user choice between two architectures is not justified.
- `F-003` already delegates session behavior to pinned Auth.js `5.0.0-beta.25` while preserving canonical UUID data through JWT/session callbacks. The minimum action is `KEEP + TEST`, plus an explicit documentation delegation to the pinned defaults.
- `F-006` preserves a substantial A-002 UI implementation. Its unresolved item is a Planner-owned Visual Authority/Fidelity Audit process contract, not an application redesign or a product-level user decision.
- `F-009` has Vercel and Docker alternates but no Cloudflare/OpenNext/CI/promotion implementation. Exact-commit STAGING-to-PRODUCTION behavior is already frozen; only the bounded release ownership/approval rule remains Planner-owned.
- `F-002` is the only finding whose affected Core capability is wholly absent. The repository cannot determine the Magic Link TTL and outstanding-token policy, so one bounded user decision remains.

No finding proves that a new general abstraction, `REFACTOR`, or `DELETE` is necessary. Existing source can be preserved for every finding except the missing Magic Link capability; the missing Cloudflare release path is additive and does not invalidate retained Vercel/Docker alternates.

## 2. Governing Reuse Policy

`KPS-CAP-REUSE-R1` freezes the capability as the reuse unit and requires existing implementation mapping before redesign. The order applied here is:

```text
KEEP
KEEP + TEST
KEEP-DISABLED
WRAP
PATCH
REFACTOR
DELETE
```

The repository remains the source of truth for current behavior. Specification ambiguity is treated as a documentation/design gap only after source inspection. Product-specific ShipAny content is not Starter Authority, and future templates do not trigger repository rewrites.

## 3. Mapping Method

For each finding this task:

1. read the exact STS-020 finding and STS-021 resolution packet;
2. traced the named route, service, model, schema, configuration, dependency, or frozen policy;
3. separated current behavior from the frozen Starter target;
4. checked for current tests and executable evidence;
5. selected the first sufficient reuse action in the frozen order;
6. re-evaluated decision ownership without applying a correction.

No dependencies were installed. `node_modules` is absent, so dependency-runtime defaults were not executed. No provider, database, browser, Cloudflare, or deployment validation was performed.

## 4. F-001 Mapping

**Affected capability:** Orders, Stripe/Creem one-time payments, callbacks/webhooks, idempotency, entitlement, and payment-side transactions (`CAP-012` through `CAP-017`).

**Existing implementation:** `PARTIAL`.

**Exact repository paths and symbols:**

- `src/app/api/checkout/route.ts:14-155` `POST`: validates a server-owned pricing item, creates a `created` order, and selects the provider from server environment `PAY_PROVIDER`.
- `src/app/api/checkout/route.ts:157-233` `stripeCheckout`: creates the provider session and records its ID/detail.
- `src/app/api/checkout/route.ts:236-287` `creemCheckout`: maps a server-side product ID, uses internal `order_no` as `requestId`, and records checkout ID/detail.
- `src/app/api/pay/callback/stripe/route.ts:5-37`: retrieves the Stripe session with server credentials and calls `handleCheckoutSession`.
- `src/app/api/pay/notify/stripe/route.ts:5-56`: verifies raw-body Stripe signatures and calls the same `handleCheckoutSession` for checkout completion.
- `src/services/stripe.ts:5-70` `handleCheckoutSession`: validates paid provider state and calls `updateOrder` for one-time payment.
- `src/app/api/pay/callback/creem/route.ts:5-55`: retrieves Creem checkout server-side, validates request ID/paid state, then calls `updateOrder`.
- `src/app/api/pay/notify/creem/route.ts:4-88`: verifies raw-body HMAC and calls `updateOrder` for paid `checkout.completed`.
- `src/services/order.ts:17-69` `updateOrder`: shared one-time mutation path; reads the order, ignores already-paid sequential repeats, permits only `created -> paid`, updates the order, then invokes credit and affiliate side effects.
- `src/services/credit.ts:135-154` and `src/services/affiliate.ts:10-34`: read-before-insert side-effect guards.
- `src/models/order.ts:6-10`, `src/db/schema.ts:41-68`: only `created`, `paid`, and `deleted` are represented; `order_no` is unique.

**Current behavior:** Stripe callback and webhook converge through `handleCheckoutSession -> updateOrder`; Creem callback and webhook call the same `updateOrder` directly. Therefore a reusable shared order/payment state path already exists. Both callbacks verify provider state through server-side provider retrieval; both webhooks independently verify signatures before mutation. Both kinds of verified provider evidence can currently grant durable `paid` state and trigger credits/affiliate side effects.

Sequential duplicate delivery normally stops at the `paid` guard. It is not durable event idempotency: no provider event ledger exists, no conditional database transition protects concurrent delivery, credits/affiliates lack unique order-level constraints, and no database transaction covers paid state plus side effects. If a side effect fails after the order is marked paid, retry returns early and can leave incomplete state. Durable paid orders and credits exist; general entitlement, failed/cancelled/refunded states, and revocation do not.

**Current config/defaults:** `PAY_PROVIDER` defaults to Stripe in code and `.env.example`; literal `creem` selects Creem and any other value currently falls through to Stripe. Provider credentials, product mapping, callback URLs, and webhook secrets are route/integration-local environment reads.

**Current tests/evidence:** No payment test files, test script, event-replay tests, concurrency tests, or provider staging evidence. Registered evidence: `AUD-WORK-040`, `AUD-WORK-020`, `AUD-FINAL-05`.

**Frozen target:** Stripe and Creem one-time payments, server-derived pricing, operator-controlled provider selection, no request-level failover, coherent durable order/access state, signature verification, replay/concurrency safety, and bounded atomic side effects.

**Actual delta:** Preserve the existing provider routes, verified callback/webhook evidence, `handleCheckoutSession`, `updateOrder`, order schema, and side-effect services. Later specify and implement a bounded state table, conditional transition/idempotency invariant, one transaction for required side effects, retry convergence, and thin order-backed entitlement/refund behavior. The existing shared path determines the minimum-delta direction; it does not prove a need for a new provider-neutral payment framework or a replacement shared-transition abstraction.

**Minimum justified reuse action:** `PATCH`.

**Decision still required:** `NO` user decision. The correction can mechanically preserve both existing verified entry types and the shared mutation path while defining the missing invariants. Planner may review the normative table, but no product-level architecture choice is required.

**New class:** `R1 - MECHANICAL CORRECTION`.

## 5. F-002 Mapping

**Affected capability:** Email Magic Link, token lifecycle, Resend Auth delivery, and trusted same-email identity (`CAP-009`, with `CAP-007`/`CAP-010`).

**Existing implementation:** `NO` for real Magic Link authentication.

**Exact repository paths and symbols:**

- `src/auth/config.ts:1-119`: providers are Google One Tap credentials, Google OAuth, and GitHub OAuth only.
- `src/db/schema.ts:13-39`: users table; no verification-token table or equivalent token columns.
- `src/app/api/demo/send-email/route.ts:1-22`: direct Resend demo accepts caller-supplied recipients/subject/content; it is not an Auth delivery path.
- `package.json:85,98`: pinned Auth.js and Resend packages exist.
- Repository scan found no Auth.js Email provider, `sendVerificationRequest`, Magic Link route/callback, token generation/hash/expiry/consumption logic, or verification-token schema.

**Current behavior:** OAuth/credentials sign-in calls `handleSignInUser -> saveUser`; no email authentication link can be requested or consumed. Resend proves an SDK dependency and demo send only.

**Current config/defaults:** `.env.example` contains Auth OAuth values but no Magic Link enable flag, token TTL, token policy, Auth email sender contract, or documented Resend Auth variables. The demo route reads `RESEND_API_KEY` and `RESEND_SENDER_EMAIL`, which are not present in the example.

**Current tests/evidence:** No Auth/Magic Link/email tests. Registered evidence: `AUD-WORK-030`, `AUD-FINAL-05`.

**Frozen target:** Core Email Magic Link with expiring, one-use, replay-safe token behavior; trusted same-email canonical UUID; generic non-enumerating request response; targeted throttling; thin server-only Resend delivery; no password Auth or mandatory Adapter migration.

**Actual delta:** This is a genuinely missing frozen capability. A bounded `PATCH` must add a minimal token lifecycle/persistence and Auth UI/callback path, and a thin Resend boundary. Existing implementation cannot determine whether a new request replaces earlier links or coexists with them, nor can it determine the exact default TTL.

**Minimum justified reuse action:** `PATCH`.

**Decision still required:** `YES`.

**Decision owner:** `USER`.

**Bounded question:** Select one active short-lived token per normalized email/purpose versus multiple individually valid outstanding tokens, including the default TTL. Minimum-delta recommendation remains one active token with the STS-021 proposed 15-minute default, subject to user approval.

**New class:** `R3 - USER DECISION`.

## 6. F-003 Mapping

**Affected capability:** Auth.js JWT/session behavior and logout/protected access (`CAP-007`).

**Existing implementation:** `YES`.

**Exact repository paths and symbols:**

- `package.json:84-86` and `pnpm-lock.yaml`: Next `15.2.3` and Auth.js/NextAuth `5.0.0-beta.25` are pinned.
- `src/auth/config.ts:118-175` `authOptions`: no adapter and no explicit `session`, `jwt`, `cookies`, `maxAge`, `updateAge`, or `trustHost` object; custom JWT callback persists canonical user data and session callback copies it to `session.user`.
- `src/auth/index.ts:1-4`: exports Auth.js handlers, `signIn`, `signOut`, and server `auth` from the pinned configuration.
- `src/services/user.ts:57-109`: server identity helpers read the Auth session UUID/email.
- `.env.example:20-22`: Auth secret/URL/trust-host inputs exist, although the reusable fixed sample secret is separately a confirmed config gap.

**Current behavior:** The repository intentionally relies on the pinned Auth.js callback/JWT/session path and implicit package defaults. Canonical `users.uuid` is copied into the JWT/session payload. No repository-owned numeric lifetime or refresh policy exists. With no installed dependencies, exact resolved default values were not executable in this task and must not be invented.

**Current config/defaults:** Package-level session/cookie defaults are delegated implicitly to pinned Auth.js. Application code adds only callbacks and custom user payload. Logout uses the exported Auth.js `signOut`; server routes/layouts use `auth()`/session helpers.

**Current tests/evidence:** No session, cookie, expiry, refresh, logout, or protected-route tests. Registered evidence: `AUD-WORK-030`, `AUD-FINAL-05`.

**Frozen target:** Retain Auth.js and the current callback/JWT/session architecture, canonical UUID payload, secure environment behavior, current-browser logout, and protected server access; no forced Adapter/database-session migration.

**Actual delta:** The candidate spec must explicitly delegate R1 lifetime/refresh/cookie behavior to the pinned Auth.js defaults and require those resolved properties to be recorded/tested during implementation. Dependency upgrades follow Snapshot + Controlled Patch and must re-evaluate changed defaults. No new numeric session policy or application architecture is evidenced.

**Minimum justified reuse action:** `KEEP + TEST`.

**Decision still required:** `NO`.

**New class:** `R1 - MECHANICAL CORRECTION`.

## 7. F-004 Mapping

**Affected capability:** Environment/config ownership and optional-module OFF behavior (`CAP-003`).

**Existing implementation:** `PARTIAL`.

**Exact repository paths and symbols:**

- `.env.example:1-100`: documents site, DB, Auth, OAuth, analytics, payment, locale, admin, theme, storage, and AdSense variables, with local URLs and incomplete optional-provider coverage.
- Repository scan finds 96 direct `process.env` reads across `src/`.
- `src/db/index.ts:12`, `src/db/config.ts:14`: generic `DATABASE_URL` reads.
- `src/auth/config.ts:13-105`, `src/lib/auth.ts:1-28`: current Auth provider flags/credentials.
- `src/app/api/checkout/route.ts`, provider integrations, analytics/ads providers, AI demo routes, and `src/lib/storage.ts`: localized capability configuration.
- Repository scan found no centralized environment schema/startup validation; Zod is used for UI/data parsing, not an environment contract.

**Current behavior:** Several optional browser providers return nothing when configuration is absent, and Auth providers are conditionally registered. Other provider/server paths fail only at invocation. Names, visibility, required conditions, defaults, and environment ownership are distributed and incomplete.

**Current config/defaults:** Existing names should be preserved where feasible. `PAY_PROVIDER=stripe`, locale detection false, provider enable flags false, default theme system, and empty provider values are visible in the example. The fixed non-empty Auth secret sample is unsafe reusable guidance. There is no STAGING binding model.

**Current tests/evidence:** No config validation, OFF-mode, secret-boundary, or environment-isolation tests. Registered evidence: `AUD-WORK-010`, `AUD-WORK-050`, `AUD-WORK-070`.

**Frozen target:** Redacted canonical variable/binding ownership, public/server-secret classification, required-if-enabled rules, safe defaults, clean OFF behavior, and isolated DEVELOPMENT/STAGING/PRODUCTION values.

**Actual delta:** Preserve existing variable names and localized consumers. Later add the deterministic documentation matrix and a narrow validation/binding boundary; remove unsafe sample-secret guidance. No giant config subsystem or wholesale renaming is justified.

**Minimum justified reuse action:** `PATCH`.

**Decision still required:** `NO`; the matrix can be derived mechanically from current consumers and frozen enablement rules.

**New class:** `R1 - MECHANICAL CORRECTION`.

## 8. F-005 Mapping

**Affected capability:** Starter extraction/upgrade policy.

**Existing implementation:** `YES` as frozen Repository Authority; the candidate spec omitted it.

**Exact repository paths and symbols:** `docs/audit/SA_TEMPLATE_AUDIT_AUTHORITY.md:276-281` freezes `Snapshot + Controlled Patch` and `NO automatic merge into projects`.

**Current behavior:** The rule exists in controlling audit Authority. No source mechanism or automatic merge workflow is part of this finding.

**Current config/defaults:** Not applicable.

**Current tests/evidence:** Authority text is deterministic evidence; no runtime implementation test applies at design stage.

**Frozen target:** Preserve the exact rule in Starter goals, reuse/upgrade policy, release policy, and do-not-do boundaries.

**Actual delta:** Documentation correction only. No application or architecture change.

**Minimum justified reuse action:** `KEEP`.

**Decision still required:** `NO`.

**New class:** `R1 - MECHANICAL CORRECTION`.

## 9. F-006 Mapping

**Affected capability:** A-002 UI Foundation plus Starter/Product Visual Authority and fresh-context Fidelity Audit (`CAP-024`).

**Existing implementation:** `PARTIAL` for the complete finding: reusable UI implementation is present; the required visual-reference/Fidelity Audit process is absent.

**Exact repository paths and evidence:**

- `src/app/theme.css`, `src/app/globals.css`, `src/lib/utils.ts`, `components.json`: Tailwind v4 semantic tokens, global styles, and `cn`.
- `src/components/ui/*`: 33 shadcn-style primitives with concrete usage; Radix, Vaul, Sonner, React Hook Form, and Zod dependencies are present.
- `src/components/dashboard/*`, `src/components/console/*`: reusable admin/member shells and generic table/form slots.
- `src/components/blocks/*`, localized page-data composition: responsive marketing/pricing/Auth structures.
- `public/*`, `src/components/icon/*`: reusable asset/icon conventions with multiple retained libraries.
- `docs/audit/04_UI_FOUNDATION_AUDIT.md:15-35`: A-002 frozen keep list.
- `docs/audit/work/60_UI_FOUNDATION.md:39-82`: route/shell/responsive/a11y source evidence and absence of browser/a11y/visual tests.
- `src/i18n/pages/*`, current public assets, legal pages, admin/docs labels: evidenced ShipAny product copy, pricing, images, links, and legal content excluded from Starter Authority.

**Current behavior:** The structural foundation is already reusable and A-002 is frozen. Source has responsive and accessibility indicators but no browser, a11y, visual-regression, or independent fidelity process. Product-specific content is separable from data-driven structures.

**Current config/defaults:** Theme defaults to `system`; content/navigation/assets are supplied by current localized/project data. These product defaults do not become Starter Visual Authority.

**Current tests/evidence:** No evidenced UI, browser, a11y, responsive, or visual baseline tests.

**Frozen target:** Preserve the A-002 structural keep list; exclude product identity; define minimum approved references and a fresh-context Fidelity Audit gate without replacing Tailwind/shadcn/Radix or redesigning pages.

**Actual delta:** No new UI implementation architecture is required by F-006. The application foundation remains. The unresolved work is a design/delivery Authority decision defining how a neutral Starter structural reference and project-specific references are organized, versioned, and independently reviewed.

**Minimum justified reuse action:** `PATCH` for the missing process/Authority contract while preserving the implementation.

**Decision still required:** `YES`.

**Decision owner:** `PLANNER`, not user. Minimum-delta recommendation is the two-layer model from STS-021: neutral Starter structural references plus project-owned product references, with a fresh-context reviewer and explicit route/view/state evidence.

**New class:** `R2 - PLANNER DECISION`.

## 10. F-007 Mapping

**Affected capability:** Gap-to-capability traceability for payment, AI, optional Auth/UI, and retained non-Core surfaces.

**Existing implementation:** `YES`; canonical capability IDs exist, while three candidate gap rows reference them incorrectly.

**Exact repository paths and evidence:**

- `docs/starter/KYD_SAAS_STARTER_DETAILED_SPEC.md:206-237`: canonical `CAP-001` through `CAP-032`; specifically `CAP-015` provider switch, `CAP-016` webhooks/idempotency, `CAP-017` Core entitlement, and `CAP-018` AI providers.
- `docs/starter/KYD_SAAS_STARTER_GAP_CLOSURE_MATRIX.md:18,21,30`: `GAP-007`, `GAP-010`, and `GAP-019` use mismatched capability IDs/names.
- `docs/starter/KYD_SAAS_STARTER_DETAILED_SPEC_AUDIT.md:241`: exact inconsistency.

**Current behavior:** This is documentation routing only; no source runtime behavior is implicated.

**Current config/defaults:** Not applicable.

**Current tests/evidence:** IDs and rows can be mechanically parsed; current counts remain 19 gaps and 32 capabilities.

**Frozen target:** One-to-one names/IDs and correct Core/retained-non-Core ownership without renumbering gaps.

**Actual delta:** Correct only affected capability cells/dependency text in a later correction. Preserve every Gap ID, priority, action, and count.

**Minimum justified reuse action:** `KEEP`.

**Decision still required:** `NO`.

**New class:** `R1 - MECHANICAL CORRECTION`.

## 11. F-008 Mapping

**Affected capability:** Evidence-backed database atomicity invariants for user/onboarding and invite/affiliate flows (`CAP-006`, with retained credits/affiliate behavior).

**Existing implementation:** `PARTIAL`.

**Exact repository paths and symbols:**

- `src/services/user.ts:14-55` `saveUser`: reads by email, inserts a canonical user, then separately grants initial credits through `increaseCredits`.
- `src/services/credit.ts:105-133` `increaseCredits`: separate credit insert.
- `src/app/api/update-invite/route.ts:16-63`: validates invite/user state, updates `users.invited_by`, then separately inserts an affiliate row.
- `src/models/user.ts:66-77` `updateUserInvitedBy`; `src/models/affiliate.ts:6-12` `insertAffiliate`.
- `src/services/order.ts:17-69`: payment multi-write path mapped by F-001.
- Repository scan found no `.transaction`, `BEGIN`, `COMMIT`, or `ROLLBACK` call in `src/`.
- `src/db/schema.ts`: users have UUID uniqueness and `(email, signin_provider)` uniqueness; credits have only unique `trans_no`; affiliates have no unique user/order relation.

**Current behavior:** User creation can persist while initial-credit grant fails. Invite ownership can persist while affiliate insert fails. Concurrent requests can race read-before-write checks. Payment atomicity is the separate F-001 path and should not be duplicated in the DB contract.

**Current config/defaults:** Initial credits are currently unconditional in `saveUser`; affiliate/referral routes are present rather than governed by a clean Starter OFF flag. Frozen Starter policy keeps credits/affiliate disabled by default.

**Current tests/evidence:** No DB transaction, failure-injection, concurrency, onboarding, or invite tests. Registered evidence: `AUD-WORK-020`, `AUD-WORK-040`, `AUD-WORK-070`.

**Frozen target:** Name only proven dependent writes; when optional side effects are OFF, no dependent write occurs; when enabled, user-plus-initial-credit and invited-by-plus-affiliate outcomes commit together or leave no partial dependent state; invalid/self/repeated/wrong-owner invite attempts have no state effect.

**Actual delta:** Preserve current models/services and add bounded transactions/constraints/guards only around these exact paths when enabled. Add server ownership validation to invite handling under the security gap. Do not build a generic transaction framework.

**Minimum justified reuse action:** `PATCH`.

**Decision still required:** `NO`; the writes and rollback invariants are source-evidenced.

**New class:** `R1 - MECHANICAL CORRECTION`.

## 12. F-009 Mapping

**Affected capability:** Cloudflare/OpenNext release, environment promotion, evidence ownership, and immutable production promotion (`CAP-031`).

**Existing implementation:** `PARTIAL` overall; alternate deployment paths exist, while the frozen primary release path is absent.

**Exact repository paths and evidence:**

- `vercel.json:1-8`: Vercel function-duration configuration.
- `Dockerfile:1-45`, `package.json:13`: standalone Docker build/run path.
- `README.md:43-78`: Vercel instructions and Cloudflare branch instructions that reference absent `wrangler.toml.example` and absent `cf:deploy` script.
- `package.json:7-18`: no OpenNext/Cloudflare deploy or CI scripts.
- Repository scan found no `.github` workflow, Wrangler/OpenNext config, Worker entry, Cloudflare binding manifest, STAGING promotion workflow, release-evidence bundle, or rollback process.
- `docs/audit/05_TEST_AND_RELEASE_AUDIT.md:90-116` and `docs/audit/work/70_TEST_SECURITY_LOGGING_BUILD_DEPLOY.md:115-164`: frozen minimum release gates and confirmed absence.
- Candidate `GAP-008`/`ACC-031` already require exact STAGING-verified revision equality and gate/migration/recovery evidence.

**Current behavior:** Vercel and Docker can remain `KEEP-DISABLED` alternate paths, though neither was executed. The checked-out tree cannot deploy the Cloudflare-first target. No actor or automation currently owns STAGING evidence or PRODUCTION promotion.

**Current config/defaults:** README describes development and generic production env files only. No isolated DEVELOPMENT/STAGING/PRODUCTION bindings or immutable artifact identity exists.

**Current tests/evidence:** No CI, deployment, staging, promotion, rollback, or Cloudflare smoke evidence.

**Frozen target:** Cloudflare Workers + OpenNext, isolated three environments, failed-gate stop, exact verified commit from STAGING to PRODUCTION, migration compatibility, concise recovery, and no enterprise release platform.

**Actual delta:** Add the missing generic Cloudflare/OpenNext and CI/release path later. Preserve Vercel/Docker as disabled alternates. The exact-commit rule is already decided, so it is not a user policy question. Planner must still select and document the bounded promotion owner: operator-approved immutable promotion or automatic immutable promotion. This is a release-governance decision, not evidence that application code requires redesign.

**Minimum justified reuse action:** `PATCH`.

**Decision still required:** `YES`.

**Decision owner:** `PLANNER`.

**New class:** `R2 - PLANNER DECISION`.

## 13. Finding Reclassification

| Finding ID | Previous class | Existing implementation | Minimum reuse action | Decision still required | New class | Reason |
|---|---|---|---|---|---|---|
| F-001 | R3 | PARTIAL | PATCH | NO | R1 | All four verified provider entry paths already converge on shared one-time `updateOrder`; preserve it and mechanically define missing state/idempotency/transaction/entitlement invariants. |
| F-002 | R3 | NO | PATCH | YES - USER | R3 | No Magic Link lifecycle exists, so TTL and outstanding-token policy cannot be derived. |
| F-003 | R3 | YES | KEEP + TEST | NO | R1 | Pinned Auth.js plus current JWT/session callbacks already establish the reusable behavior; delegate and test resolved defaults. |
| F-004 | R1 | PARTIAL | PATCH | NO | R1 | Existing names/consumers and frozen OFF/environment rules mechanically determine the ownership matrix. |
| F-005 | R1 | YES | KEEP | NO | R1 | Frozen policy exists in `AUDIT-001`; candidate omission is documentation-only. |
| F-006 | R3 | PARTIAL | PATCH | YES - PLANNER | R2 | UI implementation/A-002 are established; only the reusable reference/fresh-context review process needs Planner Authority. |
| F-007 | R1 | YES | KEEP | NO | R1 | Canonical IDs already exist; three rows need deterministic mapping repair. |
| F-008 | R1 | PARTIAL | PATCH | NO | R1 | Exact multi-write sequences and rollback targets are source-evidenced. |
| F-009 | R3 | PARTIAL | PATCH | YES - PLANNER | Exact-commit promotion is frozen and primary implementation is absent; only bounded promotion ownership remains a Planner rule. |

Reclassified former user decisions: `F-001`, `F-003`, `F-006`, and `F-009`. `F-006` and `F-009` remain decisions, but their owner is Planner rather than user. `F-001` and `F-003` become mechanical reuse-first corrections.

No `R4 - AUTHORITY CONFLICT` or `R5 - EVIDENCE GAP` finding remains. Lack of real provider/runtime/browser evidence belongs to future implementation/environment verification and does not require provisioning during design.

## 14. Remaining True User Decisions

### F-002 - Magic Link lifecycle defaults

**Why existing implementation cannot resolve it:** No Email provider, token model, issuance/consumption path, expiry value, or multi-link behavior exists.

**Exact bounded decision question:** Should each normalized email/purpose have one active token that a new request replaces, or multiple individually expiring one-use tokens, and what default TTL should apply?

**Options:**

- one active token, proposed default 15 minutes;
- multiple outstanding one-use tokens, proposed default 30 minutes.

**Minimum-delta recommendation:** One active token with atomic replacement/consumption and a 15-minute default, because it minimizes state and replay window. This recommendation is not selected by STS-021A.

No other true user decision remains.

## 15. Minimum Correction Plan

| Finding | Smallest later correction | Dependency/order |
|---|---|---|
| F-005 | Documentation only: copy exact Snapshot + Controlled Patch/no-auto-merge policy. | Independent; first. |
| F-007 | Documentation only: repair three capability mappings without renumbering. | Independent ID repair; final consistency check after payment wording. |
| F-003 | `KEEP + TEST` clarification: delegate session behavior to pinned Auth.js defaults and name verification properties. | Independent. |
| F-002 | New missing-capability specification after user selects token policy/TTL. | User decision first. |
| F-001 | Bounded `PATCH` specification preserving callbacks/webhooks/shared `updateOrder`; add state, idempotency, transaction, and entitlement rules. | Independent of F-002; complete before payment acceptance updates. |
| F-008 | Bounded `PATCH` specification naming user/onboarding and invite/affiliate invariants; reference F-001 for payment. | After F-001 wording to avoid duplicate payment rules. |
| F-006 | Process/Authority clarification for two-layer visual references and fresh-context Fidelity Audit. | Planner decision first; no UI code work. |
| F-009 | Bounded release-process specification preserving exact-commit rule and selecting promotion ownership. | Planner decision first. |
| F-004 | Redacted configuration matrix plus narrow validation contract using current names. | Last domain correction, after F-002/F-006/F-009 define any conditional ownership. |

After correction, update affected master/gap/acceptance traceability together, preserve 32 capabilities, 32 acceptances, and 19 gaps, then execute a fresh-context STS-020 re-audit. This plan does not authorize correction.

## 16. Capability Provenance / Repository Paths

| Finding | Capability provenance | Primary repository paths |
|---|---|---|
| F-001 | Existing shared payment/order/side-effect implementation | `src/app/api/checkout/route.ts`; `src/app/api/pay/callback/{stripe,creem}/route.ts`; `src/app/api/pay/notify/{stripe,creem}/route.ts`; `src/services/{stripe,order,credit,affiliate}.ts`; `src/models/order.ts`; `src/db/schema.ts` |
| F-002 | Missing Auth capability; reusable OAuth identity and Resend SDK evidence only | `src/auth/config.ts`; `src/auth/handler.ts`; `src/services/user.ts`; `src/app/api/demo/send-email/route.ts`; `src/db/schema.ts` |
| F-003 | Existing pinned Auth.js JWT/session callbacks | `package.json`; `pnpm-lock.yaml`; `src/auth/{config,index}.ts`; `src/services/user.ts`; `.env.example` |
| F-004 | Distributed existing environment contract | `.env.example`; `src/db/*`; `src/auth/config.ts`; `src/lib/auth.ts`; `src/integrations/*`; `src/providers/*`; `src/app/api/*` |
| F-005 | Existing frozen upgrade policy | `docs/audit/SA_TEMPLATE_AUDIT_AUTHORITY.md` |
| F-006 | Existing A-002 foundation plus missing visual process | `src/app/{globals,theme}.css`; `src/lib/utils.ts`; `src/components/{ui,dashboard,console,blocks}/*`; `public/*`; `docs/audit/04_UI_FOUNDATION_AUDIT.md`; `docs/audit/work/60_UI_FOUNDATION.md` |
| F-007 | Existing canonical capability registry and mismapped gap rows | `docs/starter/KYD_SAAS_STARTER_DETAILED_SPEC.md`; `docs/starter/KYD_SAAS_STARTER_GAP_CLOSURE_MATRIX.md` |
| F-008 | Existing non-atomic user/credit and invite/affiliate flows | `src/services/user.ts`; `src/services/credit.ts`; `src/app/api/update-invite/route.ts`; `src/models/{user,affiliate}.ts`; `src/db/schema.ts` |
| F-009 | Existing alternate deploy paths; missing target release path | `vercel.json`; `Dockerfile`; `README.md`; `package.json`; `docs/audit/05_TEST_AND_RELEASE_AUDIT.md`; `docs/audit/work/70_TEST_SECURITY_LOGGING_BUILD_DEPLOY.md` |

No candidate Detailed Spec artifact or application implementation file was modified by this mapping.
