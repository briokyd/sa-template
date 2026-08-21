# Kyd SaaS Starter Detailed Spec

> Task: `STS-030`  
> Authority ID: `KSS-DS-SPEC-R1`  
> Version: `R1`  
> Status: `FROZEN`  
> Authoring Authority: `KSS-DS-AUTH-R1`  
> Correction Authority: `KSS-STS022-CORRECTION-R1`  
> Resolution Authority: `KSS-STS021A-RESOLUTION-R2`  
> Residual Correction Authority: `KSS-STS024-RESIDUAL-CORRECTION-R1`  
> Freeze Authority: `KSS-STS030-FREEZE-R1`  
> Freeze artifact: `KSS-DS-FREEZE-R1`  
> Independent freeze prerequisite: `KSS-STS025-REAUDIT-RESULT-R2` (`PASS`)  
> Repository baseline: verified `AUD-000` through `AUD-080`

## 1. Document Authority / Scope

This document specifies the reusable Kyd SaaS Starter extracted from the audited `sa-template` repository. `STS-030` freezes this exact R1 design baseline after the independent `STS-025` completeness and ambiguity re-audit returned `PASS`.

The controlling inputs are `docs/starter/KYD_SAAS_STARTER_DETAILED_SPEC_AUTHORING_AUTHORITY.md`, `docs/decisions/A-001_POSTGRES_PROVIDER_POLICY.md`, `docs/audit/SA_TEMPLATE_AUDIT_AUTHORITY.md`, and the registered final/work audit evidence in `docs/PROJECT_INDEX.md`. A-002 is the frozen keep list in `docs/audit/04_UI_FOUNDATION_AUDIT.md`, supported by `docs/audit/work/60_UI_FOUNDATION.md`.

No application implementation, dependency, build/deploy configuration, provider resource, or production/simulated-production validation is authorized by this specification.

## 2. Starter Goals

1. Preserve the audited Next.js, PostgreSQL/Drizzle, Auth.js, payment, optional-module, and UI foundations.
2. Close the 19 evidenced gaps with the smallest bounded changes sufficient for correctness, security, Cloudflare delivery, and reusable operation.
3. Supply a Core that can be configured for isolated `DEVELOPMENT`, `STAGING`, and `PRODUCTION` environments.
4. Make optional modules genuinely optional: OFF requires no unused secrets, no runtime calls, and no visible route/UI surface unless explicitly selected.
5. Define mechanically testable security, behavior, and release gates that future products inherit.

Evidence: `docs/audit/00_AUDIT_SUMMARY.md`, `docs/audit/02_REUSE_GAP_MATRIX.md`, `docs/audit/05_TEST_AND_RELEASE_AUDIT.md`.

## 3. Non-Goals

The Starter does not redesign `sa-template`, choose a permanent PostgreSQL vendor, add a D1 golden path, migrate wholesale to an Auth.js Adapter schema, rewrite orders/payments, implement request-level payment failover, replace Tailwind/shadcn/Radix, or establish product-specific visual design. It does not make i18n, AI, ads, analytics, storage/R2, Turnstile, credits, subscriptions, docs/blog, or alternate deployments mandatory.

Account deletion, new subscription scope, enterprise observability, an internal plugin platform, production resource provisioning, and provider bake-offs are out of scope. Evidence: `docs/audit/07_DELETION_REVIEW_CANDIDATES.md`, `docs/audit/08_REFACTOR_JUSTIFICATION.md`.

## 4. Repository Baseline

The source baseline is Next.js 15.2.3 App Router, React 19, strict TypeScript, pnpm, PostgreSQL with Drizzle and `postgres`, Auth.js v5 beta callbacks/JWT sessions, Stripe and Creem integrations, next-intl, AI SDK providers, S3-compatible storage, Tailwind v4, and shadcn/Radix primitives. The repository contains Vercel and Docker paths but no in-tree Cloudflare/OpenNext integration and no automated test/CI baseline.

The audit result is `YES — PATCH`; no `REFACTOR` is proven and no `DELETE` is justified. Evidence: `docs/audit/work/00_REPOSITORY_INVENTORY.md`, `docs/audit/01_CAPABILITY_MATRIX.md`.

## 5. Reuse Policy

Every capability has one primary action from `KEEP`, `KEEP + TEST`, `KEEP-DISABLED`, `WRAP`, `PATCH`, `REFACTOR`, or `DELETE`. Default reasoning order is `KEEP` -> `KEEP + TEST` -> `KEEP-DISABLED` -> `WRAP` -> `PATCH`; `REFACTOR` is unavailable without proof that all smaller actions fail, and `DELETE` requires Deletion Review plus explicit user approval.

This frozen baseline assigns 32 material capabilities: `KEEP=0`, `KEEP + TEST=4`, `KEEP-DISABLED=3`, `WRAP=1`, `PATCH=24`, `REFACTOR=0`, `DELETE=0`.

Starter upgrades use exactly `Snapshot + Controlled Patch`. There is `NO automatic merge into projects`. A generated project owns its snapshot; later Starter changes are reviewed and selectively applied as explicit, bounded patches rather than being merged automatically.

## 6. Architecture Boundaries

- Application framework boundary: retain App Router routes, layouts, route handlers, Server Actions, middleware, and component organization.
- Data boundary: model/service access remains PostgreSQL + Drizzle through generic `DATABASE_URL`; transaction patches are localized to approved invariants.
- Identity boundary: existing Auth.js callback/JWT/session and canonical `users.uuid` remain; trust/token/concurrency behavior is added around them.
- Payment boundary: existing orders, server pricing, Stripe/Creem clients, callbacks, and webhooks remain; replay-safe transitions and entitlement policy are localized.
- Optional capability boundary: explicit enable/config policy, not a general plugin framework.
- UI boundary: A-002 reusable structure remains; product data/content/assets are inputs, not Starter Authority.

Evidence: `docs/audit/work/20_DATABASE_DRIZZLE_MIGRATIONS.md`, `docs/audit/work/30_AUTH_EMAIL_SESSION_ACCOUNT.md`, `docs/audit/work/40_PAYMENT_ORDERS_WEBHOOK_ENTITLEMENT.md`, `docs/audit/04_UI_FOUNDATION_AUDIT.md`.

## 7. Environments

The only standard environments are `DEVELOPMENT`, `STAGING`, and `PRODUCTION`; local execution is a development method. Each environment owns an isolated URL, database, Auth configuration/callback, payment account/config/webhook secrets, email config, and enabled optional-module secrets. Disabled modules require none of their provider secrets.

STAGING runs on Cloudflare and is production-shaped. CI/verification determines whether a commit is eligible for PRODUCTION. Promotion then requires explicit operator approval and must use the exact immutable commit and build artifact verified in STAGING; no rebuild or code mutation is allowed between verification and promotion. Compile-time/client-inlined public values are artifact-bound and remain identical for that promotion. Public values that legitimately vary by environment are resolved from target server/runtime bindings through the bounded section 21 injection path and are not compiled into the promoted client artifact. Missing required enabled config fails before serving; secret values never appear in client bundles, committed examples, runtime-public payloads, or logs. Evidence: `AUD-FINAL-03`, `AUD-FINAL-05`, `KSS-STS021A-RESOLUTION-R2`; gaps `GAP-002`, `GAP-008`.

## 8. Deployment / Cloudflare

Cloudflare Workers + OpenNext is the golden path. The minimal implementation adds OpenNext adapter/config, Wrangler environments/bindings, compatibility settings, deploy commands, and CI integration without changing application architecture merely because integration is currently absent.

Real implementation verification covers App Router, next-intl mode, Server Actions, DB, Auth cookies/callbacks, payment raw-body signatures, enabled AI streaming, and storage byte handling. Hyperdrive is optional and qualified only when selected. Vercel/Docker remain retained disabled alternates. The release requirements are target policy, not evidence that Cloudflare/OpenNext, CI, STAGING, or immutable promotion exists today. Evidence: `docs/audit/03_CLOUDFLARE_RUNTIME_AUDIT.md`; gaps `GAP-001`, `GAP-008`.

## 9. Database

A-001 freezes PostgreSQL, Drizzle, generic `DATABASE_URL`, and no provider-specific business/domain coupling. Vendor is `UNPINNED`; Provider Qualification PQ-01 through PQ-13 occurs only when a real environment selects a provider and before release reliance. Hyperdrive is not the stable data contract.

Keep the seven-table schema, migration history, model modules, and existing connection branches. Add tests for fresh/repeat migration, CRUD, constraints, selected-provider connectivity, transactions, and target runtime. Add bounded transactions/uniqueness/event invariants only for these evidenced multi-write requirements:

- With optional initial credits OFF, canonical user creation performs no credit write. With credits ON, canonical user creation and exactly one initial-credit grant commit together, or neither dependent outcome remains; concurrent trusted same-email creation still resolves one canonical user.
- With affiliate/referral OFF, its mutation route is unavailable. With it ON, `users.invited_by` and its corresponding affiliate relation commit together, or neither remains. Invalid, self, repeated, or wrong-owner attempts produce no state change.
- Payment atomicity is owned by section 11 and is not duplicated as a generic database rule.

Do not add a generic transaction framework or redesign naming, foreign keys, or provider-specific columns solely for aesthetics. Evidence: `DEC-A001-POLICY`, `AUD-WORK-020`, `KSS-STS021A-MAPPING-RESULT-R1`; gaps `GAP-007` and release qualification in `GAP-008`.

## 10. Auth / Account

Core Auth is Auth.js with Google OAuth and Email Magic Link. Only verified/trusted provider email can create or link identity. Google-first, Magic-Link-first, and concurrent first-login paths with the same trusted email resolve to one canonical `users.uuid`.

Magic Link has one active logical token/credential per normalized email. Initial validity is 15 minutes. An accepted re-request while it is active does not rotate or invalidate it and does not create a second active token: the current link is resent and `expires_at` becomes the latest accepted request time plus 15 minutes. Delayed delivery from that active-token lifecycle therefore remains valid. Successful use atomically consumes the token immediately; consumed and expired links cannot authenticate. The first accepted request after true expiry creates a new active token. Request throttling is a separate security control and must not use token rotation/invalidation as its mechanism. Token encoding and storage remain local implementation choices only where they preserve these observable rules.

Retain JWT/session callbacks, server `auth()` use, protected console/admin layouts, and logout. Starter V1 delegates lifetime, refresh/update, and cookie defaults to the pinned Auth.js version; it does not invent `maxAge`, `updateAge`, or other numeric session values for completeness. These pinned defaults are the Kyd Starter V1 baseline. Any custom product-specific session lifetime, update, or cookie override belongs to Product-Specific Design: it must be explicit, documented, and tested, cannot silently alter the Starter baseline, and cannot be inferred by an implementation model. Tests record and verify the resolved pinned defaults, secure runtime/cookie properties, canonical UUID payload, expiry/update behavior, protected access, and current-browser logout. A dependency update uses Snapshot + Controlled Patch and re-evaluates changed defaults. Add safe callback validation, explicit error states, account/profile read/update with owner authorization, and tests. Account deletion is OFF/out of scope. GitHub OAuth and Google One Tap remain disabled until their own trust/security gates pass. Evidence: `AUD-WORK-030`, `KSS-STS021A-MAPPING-RESULT-R1`; gaps `GAP-004`, `GAP-009`.

## 11. Payments / Orders / Entitlement

Core payment support is Stripe and Creem one-time checkout over server-derived product/price/currency. `PAY_PROVIDER` remains an operator-controlled selection that must reject invalid values; requests cannot select a provider or trigger automatic failover.

Keep orders, callbacks, raw-body signature verification, and provider services. Patch created/succeeded/failed/cancelled/refunded outcomes, durable event idempotency, atomic paid transition plus side effects, retry behavior, and a thin queryable one-time entitlement/revocation policy over existing records. Credits and subscriptions are retained OFF and inherit payment/atomicity gates when enabled. Evidence: `AUD-WORK-040`; gaps `GAP-007`, `GAP-010`.

The existing verified entry paths remain authoritative evidence sources: Stripe callback and webhook converge through `handleCheckoutSession -> updateOrder`; Creem callback and webhook converge on the same `updateOrder` mutation. A browser success/cancel redirect by itself is never payment authority. No replacement transition service or provider framework is required.

| Current state | Verified provider fact | Result | Entitlement result |
|---|---|---|---|
| `created` | successful one-time payment | `paid` | Core one-time ownership becomes queryable in the same transaction. |
| `created` | confirmed failure | `failed` | No ownership or optional grant. |
| `created` | confirmed cancellation | `cancelled` | No ownership or optional grant. |
| `paid` | confirmed refund/revocation | `refunded` | Core one-time ownership is revoked in the same transaction. |
| any state | verified exact duplicate or replay of an already-applied fact | Idempotent no-op with no durable mutation; return the provider-appropriate success acknowledgement. | No duplicate ownership, credit, or affiliate effect. |
| `paid`, `failed`, `cancelled`, or `refunded` | verified stale or incompatible fact with no legal transition | No durable mutation; record redacted reconciliation/anomaly evidence and return the provider-appropriate success acknowledgement. | Existing terminal result is not overwritten. |

`created` is non-terminal. `paid` is durable success and only an explicitly allowed `paid -> refunded` transition may follow. `failed` and `cancelled` are terminal attempt states; `refunded` is the terminal refunded state. An invalid or untrusted request is rejected under the existing provider/route security semantics before durable mutation. Provider routes retain their own acknowledgement/status mapping; this contract does not invent one numeric HTTP status for every provider.

The provider event ID is the durable idempotency identity when supplied by the provider. A verified callback without an event ID uses the provider checkout/session identity plus normalized outcome. The minimal durable representation is implementation-local, but claiming the idempotency identity, conditionally changing order state, changing Core entitlement, and applying every enabled credit/affiliate side effect occur in one database transaction. If a valid allowed transition suffers an internal failure before atomic commit, the transaction rolls back, the idempotency identity is not durably completed, the provider route reports its existing retryable failure outcome, and retry with the same evidence converges to one result. Optional credits/affiliate writes are included only when enabled. Refund/revocation cannot leave Core entitlement active. This bounded contract preserves existing routes, providers, `updateOrder`, schema ownership, and side-effect services; it does not require a new abstraction or schema rewrite.

## 12. Email

Resend is the production-ready Auth email path through a narrow server-only wrapper. The wrapper owns sender configuration, server-generated subject/body/link, provider invocation, redacted diagnostics, and deterministic provider failure. Auth owns token lifecycle; email delivery never treats provider acceptance as authentication success.

The generic demo send endpoint is not the production Auth boundary and must not accept caller-controlled authentication content. Disabled non-Auth email functionality requires no secret. Evidence: `AUD-WORK-030`; gap `GAP-005`.

## 13. AI

AI is optional and OFF by default. OpenAI is the standard enabled path; existing other providers are retained but remain unavailable until explicitly operator-allowlisted. Enabled calls require authenticated/authorized callers, operator-selected provider/model policy, bounded input/usage, timeout/error handling, and redacted logs. Callers cannot submit an unrestricted provider/model choice. The retained Replicate image path is `PARTIAL`: `src/app/api/demo/gen-image/route.ts` imports the `@ai-sdk/replicate` singleton and calls `replicate.image(model)` without a repository-declared credential input or environment read. Replicate enablement therefore requires one logical server-only provider credential injected and validated at that existing provider-construction/selection boundary; the physical environment name is not frozen because repository evidence establishes none.

OFF mode has no API route reachability, secret requirement, initialization, or UI affordance. No general provider plugin framework is introduced. Evidence: `AUD-WORK-050`, `AUD-WORK-070`; gap `GAP-013`.

## 14. i18n

i18n is supported/tested but defaults OFF. Existing next-intl resources and locale routing remain for enabled mode. OFF mode removes forced locale routing/middleware complexity from the project experience without deleting the capability or duplicating the app tree.

Enabled mode verifies locale routing, fallback, messages, missing-key behavior, and canonical/SEO interaction. Both modes build and route deterministically. Evidence: `AUD-WORK-050`; gap `GAP-012`.

## 15. Ads / Analytics

AdSense and the existing GA/OpenPanel/Plausible components are independent optional browser integrations, OFF unless explicitly configured. OFF emits no script/request and requires no provider value. ON respects explicit provider config and the product's consent/loading policy; each provider initializes once and pageview behavior is tested.

No single analytics provider or general AdsService is mandated. Evidence: `AUD-WORK-050`; gap `GAP-018`.

## 16. Storage / R2

Storage is optional and OFF by default. Preserve the S3-compatible `aws4fetch` boundary. Enabled storage requires owner authorization, server-controlled object keys, type/size validation, explicit public/private policy, bounded signed URL behavior, and safe error/log output.

R2 is a selectable S3-compatible target, not mandatory. Worker byte/Buffer behavior and real R2 integration are qualified only when enabled in an implementation environment. Evidence: `AUD-WORK-050`; gap `GAP-014`.

## 17. Turnstile

Turnstile is optional, absent today, and OFF by default. It may be added to named abuse-prone routes only when Product/Security Authority selects it. Enabled mode requires a client widget plus server token validation and explicit invalid/expired/error handling.

Turnstile never replaces authentication, authorization, input validation, or targeted rate limiting; OFF mode has no secret, widget, or network cost. Evidence: `AUD-WORK-050`; gap `GAP-017`.

## 18. UI Foundation

A-002 freezes the reusable keep list:

| UI group | Starter role | Action | Bounded requirement |
|---|---|---|---|
| Tailwind v4 semantic tokens, global CSS, `cn` | CORE | PATCH | Correct localized token/tool drift; preserve semantic foundation. |
| 33 used shadcn/Radix primitives | CORE | KEEP + TEST | Render, keyboard, focus and overlay tests. |
| Generic forms/tables | CORE | KEEP + TEST | Validation, submit, empty and overflow tests. |
| Theme/application composition | CORE | WRAP | Separate small composition concerns and preserve theme persistence. |
| Dashboard/admin and console/member shells | CORE | KEEP + TEST | Responsive navigation, access, user menu and logout tests. |
| Marketing header/footer/sections | CORE | KEEP + TEST | Preserve structure; supply product content as data. |
| Pricing and Auth/account UI | CORE | PATCH | Fix semantics/states and add Magic Link/profile surfaces. |
| Asset/icon conventions | CORE | KEEP + TEST | Preserve conventions; replace product assets. |
| Loading/error/not-found and responsive/a11y baseline | CORE | PATCH | Add route states and browser-verified keyboard/mobile behavior. |
| Blog/Fumadocs, charts/carousel/editor/data cards | OPTIONAL | KEEP-DISABLED | Explicit opt-in and conditional tests. |
| ShipAny copy, claims, logos, imagery, links, pricing, menus, legal content | KEEP-DISABLED | KEEP-DISABLED | Never treat as Starter visual/product Authority. |

No UI framework replacement or repo-wide aesthetic redesign is allowed.

Visual Authority has two layers:

1. **Starter Visual Foundation Authority** owns product-neutral tokens/theme, shadcn/Radix primitives, generic forms/tables/shells/layouts, responsive/accessibility/loading/error behavior, generic asset conventions, and product-neutral reference states. Its minimum versioned reference manifest covers public navigation/marketing structure, sign-in, account, dashboard/admin, member console, pricing structure, loading, error, and not-found at named mobile and desktop viewports and in light/dark modes where applicable.
2. **Product Visual Authority** owns Approved Screens, Actual Assets, interaction/state references, responsive product references, brand, copy, imagery, pricing/content semantics, navigation, and legal/product presentation. ShipAny materials are repository evidence and replaceable inputs, never Starter visual Authority.

Each layer names its owner, version, routes, viewports, states, assets, and approved evidence. Every required manifest/reference item declares one or more comparison rules from this closed vocabulary: `EXACT_SEMANTIC`, `TOKEN`, `STRUCTURAL`, `RESPONSIVE_STATE`, `ASSET_IDENTITY`, `EXPLICIT_TOLERANCE`, and `APPROVED_DEVIATION`. `EXPLICIT_TOLERANCE` is valid only when its threshold and measurement are already recorded by the applicable Authority/reference/manifest; a reviewer cannot invent a tolerance during audit. An approved deviation records its deviation ID, affected item/reference, owner, reason, scope, and approval/evidence.

A fresh-context Fidelity Audit is performed by a reviewer who did not author the implementation under review. The reviewer compares only against the applicable approved layer and records screenshots plus interaction/responsive/accessibility evidence per required rule. Rendering noise may be ignored only when it does not alter a governed token, structure or geometry relationship, content, asset identity, interaction, overflow/clipping, or responsive state. An undeclared difference against a required rule creates a finding; a failed required rule without a recorded approved deviation fails/blocks the gate. The manifest and evidence must be sufficient for two fresh reviewers to reach the same gate result. Starter foundation verification cannot approve product fidelity, and product references cannot rewrite the frozen A-002 foundation by implication.

Evidence: `AUD-FINAL-04`, `AUD-WORK-060`, `KSS-STS021A-RESOLUTION-R2`; gap `GAP-015`.

## 19. Technical SEO

Core technical SEO owns configured site origin/metadata base, route title/description, canonical URLs, generated sitemap, robots/indexability policy, Open Graph/social metadata, icons, and structured data where the route has stable facts. STAGING is noindex; PRODUCTION indexability is explicit by route.

The Starter does not prescribe keywords, copy, content strategy, or product information architecture. Evidence: `AUD-WORK-050`; gap `GAP-011`.

## 20. Security

Minimum reusable gates are: trusted Auth identity and Google verified email; Magic Link expiry/single-use/replay/abuse; server-side protected API ownership; secret/public env separation; targeted rate limiting; server-derived payment pricing; Stripe/Creem signature rejection; webhook replay/concurrency/partial-failure safety; AI provider/model policy when enabled; storage authorization when enabled.

Errors must not expose credentials, tokens, provider payloads, or unnecessary PII. Turnstile is conditional. Every gate has a negative test, not only a success path. Evidence: `AUD-FINAL-05`, `AUD-WORK-070`; gaps `GAP-004`, `GAP-006`, `GAP-007`.

## 21. Configuration

Configuration remains environment variables and platform bindings with a narrow validation layer. Variables are classified as required Core, required-if-enabled, optional public, or server secret. Operator choices such as payment provider, optional module enablement, AI provider/model allowlist, site URL, and storage target are validated against explicit values.

Examples contain names/placeholders only. Missing required config reports variable identity and capability, never its value. Optional OFF paths do not initialize providers or fail for absent secrets. Evidence: `AUD-WORK-010`; gap `GAP-002`.

The following redacted ownership matrix is normative. “Each env” means separate values/bindings owned by `DEVELOPMENT`, `STAGING`, and `PRODUCTION`; local execution consumes DEVELOPMENT values and is not a fourth environment. Empty/absent means OFF only where the table explicitly says so. A current `NEXT_PUBLIC_*` name records source provenance but does not by itself authorize compile-time injection when the target classification below is `ENVIRONMENT_RUNTIME_BOUND`.

| Capability owner | Canonical/current variable or binding | Kind / visibility | Required condition and default | Environment scope |
|---|---|---|---|---|
| Runtime/site | Platform environment identity; `NEXT_PUBLIC_WEB_URL`; `NEXT_PUBLIC_PROJECT_NAME`; `NODE_ENV` | Platform binding plus public values | Identity and absolute site URL required; project name is product input; no localhost default outside development. | Site origin is runtime-bound per env; project name is artifact-bound. |
| Database | `DATABASE_URL` | Server secret | Required for Core; generic PostgreSQL URL; no provider SDK contract. | Distinct per env. |
| Auth core | `AUTH_SECRET`; `AUTH_URL`; `AUTH_TRUST_HOST`; `NEXT_PUBLIC_AUTH_ENABLED` | Server secrets/settings plus runtime-public composition flag | Auth must be ON for a releasable Core; secret and canonical callback origin required; examples contain no fixed secret. | Secret/URL and public enablement are runtime-bound per env. |
| Google OAuth | `AUTH_GOOGLE_ID`; `AUTH_GOOGLE_SECRET`; `NEXT_PUBLIC_AUTH_GOOGLE_ID`; `NEXT_PUBLIC_AUTH_GOOGLE_ENABLED` | Server secret plus runtime-public client ID/flag | Required for Core Google ON; server/public IDs must identify the same environment client. | OAuth app/callback and runtime-public values are runtime-bound per env. |
| Google One Tap | `NEXT_PUBLIC_AUTH_GOOGLE_ONE_TAP_ENABLED` plus Google values above | Runtime-public flag; existing Google credentials | Default OFF; absent/false registers no One Tap UI/flow. | Runtime-bound per env. |
| GitHub OAuth | `AUTH_GITHUB_ID`; `AUTH_GITHUB_SECRET`; `NEXT_PUBLIC_AUTH_GITHUB_ENABLED` | Server secret plus runtime-public flag | Default OFF; credentials required only when explicitly enabled. | App/callback and enablement are runtime-bound per env when ON. |
| Magic Link/email | `RESEND_API_KEY`; `RESEND_SENDER_EMAIL`; `NEXT_PUBLIC_WEB_URL` | Server secret/sender plus runtime-public origin | Required for Core Magic Link delivery; 15-minute lifecycle is frozen behavior, not env configuration. | Provider secret/sender/origin are runtime-bound per env. |
| Admin authorization | `ADMIN_EMAILS` | Server configuration | Explicit normalized allowlist required when admin surfaces are enabled; empty means no email-authorized admin. | Explicit per env. |
| Payment selection | `PAY_PROVIDER` | Server configuration | Required when payments are enabled; only `stripe` or `creem`; no fallback for invalid/missing value. | Explicit per env. |
| Stripe | `STRIPE_PRIVATE_KEY`; `STRIPE_WEBHOOK_SECRET`; documented `STRIPE_PUBLIC_KEY` | Server secrets; public key only if a client path actually consumes it | Private/webhook values required when `PAY_PROVIDER=stripe`; unused public key is not required. | Distinct test/live account and webhook per env. |
| Creem | `CREEM_ENV`; `CREEM_API_KEY`; `CREEM_WEBHOOK_SECRET`; `CREEM_PRODUCTS` | Server configuration/secrets | Required when `PAY_PROVIDER=creem`; product mapping remains server-owned. | Distinct mode/account/webhook/product mapping per env. |
| Payment redirects | `NEXT_PUBLIC_PAY_SUCCESS_URL`; `NEXT_PUBLIC_PAY_FAIL_URL`; `NEXT_PUBLIC_PAY_CANCEL_URL` | Artifact-bound public same-origin paths | Required when payments ON; default target is a validated same-origin relative path and is never payment authority. An environment-varying approved external origin uses the runtime-public boundary instead. | Relative paths are identical for the promoted artifact. |
| i18n | `NEXT_PUBLIC_I18N_ENABLED`; `NEXT_PUBLIC_LOCALE_DETECTION` | Artifact-bound public composition flags | Both default OFF; locale detection cannot turn i18n ON by itself. Enabled locale/default/message config is build-owned product input. | Identical for the promoted artifact. |
| Theme/UI | `NEXT_PUBLIC_DEFAULT_THEME`; `NEXT_PUBLIC_SHOW_POWERED_BY` | Artifact-bound public presentation config | Theme defaults to `system`; powered-by is product input and has no security effect. | Identical for the promoted artifact. |
| AdSense | `NEXT_PUBLIC_GOOGLE_ADCODE` | Runtime-public provider ID | Empty/absent means OFF and emits no script/request. | Runtime-bound per env. |
| Analytics | `NEXT_PUBLIC_GOOGLE_ANALYTICS_ID`; `NEXT_PUBLIC_OPENPANEL_CLIENT_ID`; `NEXT_PUBLIC_PLAUSIBLE_DOMAIN`; `NEXT_PUBLIC_PLAUSIBLE_SCRIPT_URL` | Runtime-public provider config | Each provider independently OFF when its required value is absent; consent policy is product input. | Runtime-bound per env. |
| AI policy | `AI_ENABLED`; `AI_PROVIDER`; `AI_ALLOWED_MODELS`; `OPENAI_API_KEY`; `OPENROUTER_API_KEY`; `SILICONFLOW_API_KEY`; `SILICONFLOW_BASE_URL`; `KLING_ACCESS_KEY`; `KLING_SECRET_KEY`; logical Replicate provider credential | Server policy/config/secrets | `AI_ENABLED` defaults false; selected provider credential and operator allowlist are required only ON; OpenAI is standard. Replicate has no repository-declared physical credential name, so its logical server-only credential is injected/validated at the existing `replicate.image(model)` provider-construction/selection boundary. No AI provider initializes while OFF. | Explicit, isolated per env. |
| Storage | `STORAGE_ENABLED`; `STORAGE_ENDPOINT`; `STORAGE_REGION`; `STORAGE_ACCESS_KEY`; `STORAGE_SECRET_KEY`; `STORAGE_BUCKET`; `STORAGE_DOMAIN` | Server config/secrets | `STORAGE_ENABLED` defaults false; all target-required values are required only ON; public domain is optional only for an approved public policy. | Distinct bucket/credentials per env. |
| Turnstile | `TURNSTILE_ENABLED`; `NEXT_PUBLIC_TURNSTILE_SITE_KEY`; `TURNSTILE_SECRET_KEY` | Server flag/secret plus runtime-public site key | Defaults OFF; keys required only for named enabled routes. | Runtime-bound site/secret per env. |
| Retained non-Core | `CREDITS_ENABLED`; `AFFILIATE_ENABLED`; `SUBSCRIPTIONS_ENABLED` | Server composition flags | Each defaults false; OFF makes its route/job/side effect unavailable and requires no capability-only config. | Explicit per env. |
| Cloudflare/OpenNext | Wrangler environment bindings, compatibility flags, deployment revision, and any selected Hyperdrive binding | Platform bindings; secrets remain server-only | Required only for the target environment/integration; Hyperdrive only when selected. | Independently owned per Cloudflare env. |
| Release | immutable commit/artifact identity, artifact-public-config fingerprint, runtime-public binding map, STAGING gate bundle, migration/recovery record, operator approval | CI evidence/approval, not application env | All required before PRODUCTION promotion; no default approval and no rebuild. | STAGING evidence hands the identical artifact and its fingerprint to PRODUCTION; runtime-public bindings remain target-environment owned. |

Public configuration uses exactly one of these classifications:

| Classification | Current/equivalent public values | Target consumption rule |
|---|---|---|
| `ARTIFACT_BOUND` | `NEXT_PUBLIC_PROJECT_NAME`; relative `NEXT_PUBLIC_PAY_SUCCESS_URL`, `NEXT_PUBLIC_PAY_FAIL_URL`, `NEXT_PUBLIC_PAY_CANCEL_URL`; `NEXT_PUBLIC_I18N_ENABLED`; `NEXT_PUBLIC_LOCALE_DETECTION`; `NEXT_PUBLIC_DEFAULT_THEME`; `NEXT_PUBLIC_SHOW_POWERED_BY` | Compile-time/client-inlined values are fingerprinted and identical between STAGING and PRODUCTION for the promoted artifact. A value that needs to vary cannot remain in this class. |
| `ENVIRONMENT_RUNTIME_BOUND` | `NEXT_PUBLIC_WEB_URL`; `NEXT_PUBLIC_AUTH_ENABLED`; `NEXT_PUBLIC_AUTH_GOOGLE_ID`; `NEXT_PUBLIC_AUTH_GOOGLE_ENABLED`; `NEXT_PUBLIC_AUTH_GOOGLE_ONE_TAP_ENABLED`; `NEXT_PUBLIC_AUTH_GITHUB_ENABLED`; `NEXT_PUBLIC_GOOGLE_ADCODE`; `NEXT_PUBLIC_GOOGLE_ANALYTICS_ID`; `NEXT_PUBLIC_OPENPANEL_CLIENT_ID`; `NEXT_PUBLIC_PLAUSIBLE_DOMAIN`; `NEXT_PUBLIC_PLAUSIBLE_SCRIPT_URL`; `NEXT_PUBLIC_TURNSTILE_SITE_KEY`; any approved environment-varying external payment redirect origin | Resolve from the target server/runtime binding. Use the existing root layout/provider and Server Component-to-client prop composition to serialize only the named non-secret value to the exact consumer. Replace direct client compile-time reads only where needed. No arbitrary runtime-config endpoint or generic config framework is authorized. |

Current direct `NEXT_PUBLIC_*` reads are source provenance, not proof that their target class is correct. Implementing the runtime-bound class is a bounded `PATCH` under `GAP-002`/`GAP-008`. CI records the artifact-bound fingerprint; STAGING and PRODUCTION each validate their target runtime-public map, and a client artifact/runtime smoke proves no STAGING value or server secret leaks into PRODUCTION.

New explicit flags in this table are bounded configuration patches for capabilities whose existing code has no clean OFF switch. They do not create a plugin system. Existing names and localized consumers remain unless a later implementation proves a narrow compatibility correction necessary.

## 22. Testing

The mandatory baseline is Runtime validator, explicit no-emit typecheck, lint, production build, fresh/repeat migration and DB smoke, Google Auth, Magic Link lifecycle/linking, session/logout/protected APIs, Stripe and Creem checkout/webhooks, idempotency/entitlement, core UI navigation, responsive browser smoke, accessibility smoke, and Cloudflare STAGING smoke.

Magic Link coverage includes initial 15-minute validity, active re-request preserving the same logical credential, extension to latest accepted request plus 15 minutes, successful atomic single use, consumed-link rejection, expired-link rejection, creation of a new credential after true expiry, a delayed-email case from the same active lifecycle, throttling independent from token invalidation, and Google/Magic-Link same-email concurrency. Session tests record the pinned Auth.js defaults rather than asserting invented numeric values.

Conditional tests run only for enabled credits, ads/analytics, i18n, AI, storage/R2, Turnstile, retained content/tools, subscriptions, or alternate deployments. Visual regression is optional and focused. Evidence: `AUD-FINAL-05`; gap `GAP-003`.

## 23. Logging / Observability

Use a minimal server logging boundary with structured event name, severity, request/correlation ID, deployment revision, capability/provider identifier, and redacted error context. Never log secrets, raw tokens, unbounded provider responses, payment payloads, or unnecessary user records.

Provide a non-secret health/readiness target sufficient for deploy smoke and revision identification. A specific enterprise telemetry vendor is not required. Evidence: `AUD-WORK-070`; gap `GAP-016`.

## 24. Migration / Rollback

Each release records whether its database changes are backward-compatible with the currently running application, when migrations execute, expected failure behavior, and the application rollback point. Destructive or non-backward-compatible changes require separate planning and recovery evidence.

The minimal golden sequence is preflight -> compatible migration or migration readiness -> immutable build -> STAGING deploy/smoke -> CI eligibility record -> explicit operator approval -> promotion of the same immutable commit/artifact without rebuild or code mutation -> PRODUCTION revision check/smoke. Recovery may be a documented previous Worker revision/config rollback plus forward DB correction; automatic schema rollback is not assumed. Evidence: `AUD-FINAL-05`, `KSS-STS021A-RESOLUTION-R2`; gap `GAP-008`.

## 25. Release Gates

| Gate | Requirement |
|---|---|
| Runtime | Required execution/closeout validator passes. |
| Static/build | Clean install, typecheck, lint, production build pass. |
| Automated suite | Mandatory and enabled-capability tests pass. |
| Security/dependency | Secret scan and bounded dependency/security scan have no unaccepted high-risk result. |
| Database | Migration and isolated provider read/write/transaction smoke pass for selected environment. |
| Cloudflare STAGING | Production-shaped deployment plus core runtime smoke passes. |
| Domain smoke | Auth always; payment and optional capabilities when enabled. |
| UI | Responsive and accessibility smoke passes for shared Core routes. |
| Migration/recovery | Ordering, compatibility, and recovery evidence recorded. |
| Visual fidelity | Fresh-context reviewers apply the manifest's declared rule vocabulary; an undeclared difference creates a finding and a failed required rule without an approved deviation blocks eligibility. |
| Eligibility | CI records the immutable commit/artifact identity, artifact-bound public-config fingerprint, target runtime-public validation, and complete STAGING gate bundle; failed gates make it ineligible. |
| Approval/promotion | An explicit operator approval references that bundle; PRODUCTION promotes the identical immutable commit/artifact and artifact-bound fingerprint with no rebuild or code mutation, then resolves only the approved PRODUCTION runtime-public bindings. |
| Production verification | Deployed revision/artifact identity equals the approved STAGING identity and post-deploy smoke passes. |

No release gate is executed during design. Evidence: `AUD-FINAL-05`; gaps `GAP-003`, `GAP-008`.

## 26. Optional Module Rules

Every optional or retained-disabled capability must have an explicit enable flag or deterministic operator configuration. OFF means: no required secret, provider client initialization, network call, route/UI reachability, scheduled work, or build failure. ON means: validated config, named security boundary, failure behavior, conditional tests, and release smoke.

Retention is not default enablement. Disabling may be achieved by composition/configuration without deleting source. Evidence: `AUD-WORK-050`, `AUD-FINAL-07`; gaps `GAP-012` through `GAP-019`.

## 27. Capability-by-Capability Reuse Matrix

The table is the normative material-capability contract. “Config/security” and “failure/tests/gate” cells satisfy the corresponding mandatory schema fields; evidence paths resolve through `PROJECT_INDEX`.

| Capability ID / Name | Role | Current sa-template state / Action | Frozen target behavior | Allowed delta / Forbidden delta | Configuration / Security requirements | Failure/retry behavior / Tests / Release gate | Audit evidence / Dependencies |
|---|---|---|---|---|---|---|---|
| CAP-001 Framework | CORE | Next 15 App Router, React 19, strict TS; **KEEP + TEST** | Preserve routes/layouts/actions/middleware under target adapter. | Add compatibility fixes only / no framework upgrade or route rewrite by default. | Existing app config; server/client boundary preserved. | Build/route/action/middleware smoke; fail build explicitly; static/build and STAGING gates. | `AUD-WORK-010`, `AUD-FINAL-03`; CAP-002. |
| CAP-002 Cloudflare/OpenNext | CORE | Integration absent; **PATCH** | Workers + OpenNext golden deployment. | Add adapter/Wrangler/bindings/scripts / no app rewrite or mandatory Hyperdrive. | Per-environment bindings and secrets. | Deploy failure is visible; DEVELOPMENT/STAGING smoke and release gates. | `AUD-FINAL-03`; GAP-001, CAP-003. |
| CAP-003 Environment/config | CORE | Distributed reads, incomplete validation; **PATCH** | Validated isolated three-environment contract with every public value classified artifact-bound or runtime-bound. | Narrow config/runtime-public prop boundary and safe examples / no giant subsystem, arbitrary config endpoint, or Local environment. | Required/conditional/public/secret classes; artifact fingerprint; target runtime-public map; no secret exposure. | Fail-fast enabled config; Replicate OFF/ON injection, artifact fingerprint, runtime target/no-leak, secret, and isolation tests; security/release gates. | `AUD-WORK-010`, `AUD-WORK-070`, `KSS-STS024-RESIDUAL-CORRECTION-R1`; GAP-002/008. |
| CAP-004 PostgreSQL/Drizzle | CORE | Generic URL, centralized models, seven tables; **KEEP + TEST** | Preserve vendor-neutral PostgreSQL/Drizzle boundary. | Provider qualification and focused compatibility fixes / no vendor SDK in domain code or D1 path. | `DATABASE_URL`; selected environment isolation. | Observable connection errors; CRUD/provider/transaction/runtime smoke before release. | `DEC-A001-POLICY`, `AUD-WORK-020`; CAP-002/003. |
| CAP-005 Migrations | CORE | Drizzle Kit and baseline migration; **KEEP + TEST** | Reproducible, environment-scoped migrations. | Add CI smoke/order docs / no generated rewrite without schema change. | Environment-injected DB URL. | Stop release on migration failure; fresh/repeat/drift tests and migration gate. | `AUD-WORK-020`; CAP-004/031. |
| CAP-006 DB atomicity | CORE | Multi-write paths lack transactions; **PATCH** | Enabled user+initial-credit and invite+affiliate pairs are atomic; payment uses CAP-016/section 11. | Bounded transactions/constraints on named paths / no generic transaction framework or repository rewrite. | Credits/affiliate flags determine whether dependent writes exist; no provider config. | Failure leaves neither dependent outcome; concurrency yields one canonical user/credit and one valid invite relation; focused failure/concurrency tests. | `AUD-WORK-020`, `KSS-STS021A-MAPPING-RESULT-R1`; GAP-007, CAP-016/032. |
| CAP-007 Auth core/session | CORE | Auth.js callbacks/JWT/session and server guards; **PATCH** overall, with the existing session sub-capability retained and tested | Trusted canonical identity and safe callbacks while retaining pinned Auth.js lifetime/update/cookie defaults and UUID payload. | Local trust/error/persistence patches plus resolved-default tests / no custom numeric session policy or forced Adapter migration. Any product override is owned by Product-Specific Design, explicit, documented, and tested. | Auth secret, site URL, enabled providers; Snapshot + Controlled Patch on Auth.js update. | Controlled callback/persistence errors; record resolved defaults and verify expiry/update/cookie/logout/protection behavior; reject silent/inferred override. | `AUD-WORK-030`, `KSS-STS021A-MAPPING-RESULT-R1`, `KSS-STS024-RESIDUAL-CORRECTION-R1`; GAP-004/009, CAP-004. |
| CAP-008 Google OAuth | CORE | Env-gated provider, no verified-email policy; **PATCH** | Verified trusted Google email maps to canonical UUID. | Add trust/profile checks / no alternate Google identity architecture. | Google ID/secret/callback per environment. | Reject unverified/invalid callback; provider integration and security gate. | `AUD-WORK-030`; GAP-004, CAP-007. |
| CAP-009 Email Magic Link | CORE | Absent; **PATCH** | One active logical token per normalized email, initial/sliding 15-minute expiry, atomic single use, trusted canonical UUID. | Add minimal token lifecycle/persistence/UI / no password auth, rotation-on-active-rerequest, provider framework, or schema migration for purity. | Core Auth, site URL, Resend boundary; lifecycle values are frozen rather than operator-selected. | Active re-request resends same credential and extends expiry; used/expired rejects; post-expiry request creates new token; delayed-email, linking, throttle-separation tests. | `AUD-WORK-030`, `KSS-STS021A-RESOLUTION-R2`; GAP-004, CAP-010. |
| CAP-010 Email/Resend | CORE | Generic direct demo only; **WRAP** | One server-only Auth delivery adapter. | Thin sender/template wrapper / no mail plugin platform or caller content. | Resend key/sender required only when Magic Link enabled. | Provider error observable, token/secret redacted; adapter/delivery tests. | `AUD-WORK-030`; GAP-005, CAP-009. |
| CAP-011 Account/profile/logout | CORE | Account shell/logout; profile edit absent; **PATCH** | Owner-authorized profile and reliable logout/account states. | Extend existing UI/service / no account deletion or Auth redesign. | Auth only; editable field allowlist. | Validation/auth errors rendered; browser/API/Auth gate. | `AUD-WORK-030`, `AUD-WORK-060`; GAP-009. |
| CAP-012 Orders | CORE | Durable created/paid records and shared mutation path, incomplete lifecycle; **PATCH** | Section 11 state table governs non-terminal `created`, durable `paid`, terminal `failed`/`cancelled`/`refunded`, and only the explicit refund transition after paid. | Extend existing order status/mapping only as required / no full schema or shared-service rewrite. | Server product catalog and selected provider. | Verified duplicate/stale incompatible facts are acknowledged no-mutation outcomes with reconciliation evidence where required; invalid facts reject; valid internal failure rolls back and remains retryable. | `AUD-WORK-040`, `KSS-STS021A-MAPPING-RESULT-R1`, `KSS-STS024-RESIDUAL-CORRECTION-R1`; GAP-010, CAP-013/014/016/017. |
| CAP-013 Stripe one-time | CORE | Checkout/callback/raw-body signature and shared `updateOrder` path exist; **PATCH** | Existing verified callback/webhook evidence feeds section 11 state/idempotency contract. | Complete outcome/idempotency/atomicity around existing paths / no new subscription or transition framework. | Stripe keys/webhook secret/product mapping per environment. | Invalid/untrusted evidence rejects with no mutation; verified duplicate/stale evidence receives provider-appropriate success acknowledgement; internal pre-commit failure remains retryable and converges once. | `AUD-WORK-040`; GAP-007/010. |
| CAP-014 Creem one-time | CORE | Checkout/callback/WebCrypto signature and shared `updateOrder` path exist; **PATCH** | Existing verified callback/webhook evidence feeds section 11 state/idempotency contract. | Complete mapping/outcome/idempotency/atomicity around existing paths / no provider or transition-framework rewrite. | Creem keys/webhook secret/product map/environment. | Invalid/untrusted evidence rejects with no mutation; verified duplicate/stale evidence receives provider-appropriate success acknowledgement; internal pre-commit failure remains retryable and converges once. | `AUD-WORK-040`; GAP-007/010. |
| CAP-015 Payment provider switch | CORE | `PAY_PROVIDER`, invalid falls to Stripe; **PATCH** | Explicit operator selection; no automatic failover. | Validate enum and enabled config / no request-selected provider. | `stripe` or `creem` only. | Invalid/missing required config fails before checkout; switch tests. | `AUD-WORK-040`; GAP-010. |
| CAP-016 Webhooks/idempotency | CORE | Signatures and one shared mutation path present; replay/atomicity partial; **PATCH** | Provider event ID, or callback session identity plus outcome, yields one atomic section 11 result. | Minimal durable claim/conditional order transaction around existing handlers/services / no distributed transaction or replacement transition service. | Provider endpoint secrets. | Duplicate/already-applied and stale/incompatible verified facts are success-acknowledged no-ops; invalid facts reject; pre-commit failure rolls back without completing idempotency and retry converges to one state and enabled side effect. | `AUD-WORK-040`, `AUD-WORK-070`, `KSS-STS021A-MAPPING-RESULT-R1`, `KSS-STS024-RESIDUAL-CORRECTION-R1`; GAP-007, CAP-006/012/017. |
| CAP-017 Entitlement | CORE | Paid order durable, generic policy partial; **PATCH** | Core one-time ownership activates atomically on `paid` and revokes atomically on `refunded`; all other states deny. | Thin query policy over existing orders in the payment transaction / no generalized entitlement framework. | Server product-to-entitlement mapping. | Unknown/unpaid/failed/cancelled/refunded denies; authorized query, transition, rollback, and replay tests. | `AUD-WORK-040`; GAP-007/010, CAP-012/016. |
| CAP-018 AI providers | OPTIONAL | Providers/routes present; Replicate singleton path has no declared credential input; **PATCH** | OFF by default; OpenAI standard; extras operator-allowlisted. | Add config/auth/limits/log safety and a logical server-only Replicate credential at its existing construction/selection call / no deletion, guessed physical env name, or plugin framework. | Enable flag, selected provider credential, provider/model allowlist; no provider initialization OFF. | Reject disabled/missing-credential/disallowed/unauthorized; Replicate OFF/ON injection and conditional provider smoke. | `AUD-WORK-050`, `src/app/api/demo/gen-image/route.ts`, `KSS-STS024-RESIDUAL-CORRECTION-R1`; GAP-002/013, CAP-003/027. |
| CAP-019 i18n | OPTIONAL | next-intl structurally active; **PATCH** | Supported/tested OFF default and enabled locale mode. | Bounded composition switch / no duplicate app tree or removal. | Enable flag, locale list/default only when ON. | Missing locale falls back or rejects per config; dual-mode build/route tests. | `AUD-WORK-050`; GAP-012, CAP-001/002. |
| CAP-020 Ads/analytics | OPTIONAL | Env-gated providers; **KEEP + TEST** | Independent OFF-default browser integrations. | Add tests/consent integration / no mandatory or unified provider. | Public IDs only when selected; no server secrets in client. | OFF loads nothing; ON loads once; conditional browser gate. | `AUD-WORK-050`; GAP-018. |
| CAP-021 Non-default Auth | KEEP-DISABLED | GitHub/One Tap present and off; **KEEP-DISABLED** | Retained, inaccessible until explicitly enabled and qualified. | Add conditional hardening/tests only if selected / no default enable or deletion. | Provider flag/credentials; One Tap claims policy. | Disabled path absent; enabled failures safe; conditional Auth tests. | `AUD-WORK-030`; GAP-019, CAP-007. |
| CAP-022 Storage/R2 | OPTIONAL | S3 helper, policy/runtime partial; **PATCH** | OFF by default; authorized S3/R2 path when enabled. | Add policy/validation/runtime smoke / no mandatory R2 or provider domain code. | Endpoint/bucket/credentials required only ON. | Deny invalid/unauthorized; conditional Worker/storage gate. | `AUD-WORK-050`; GAP-014, CAP-027. |
| CAP-023 Turnstile | OPTIONAL | Absent; **PATCH** | Optional named-route bot check, OFF default. | Add thin widget/verifier only when selected / no global mandate. | Site/secret key only ON. | Invalid/expired token denies; conditional security smoke. | `AUD-WORK-050`; GAP-017, CAP-027. |
| CAP-024 UI Foundation | CORE | A-002 reusable stack with bounded gaps; **PATCH** | Preserve keep list under two-layer Starter/Product Visual Authority and add missing semantics/states/tests. | Apply A-002 table deltas and rule-declared reference manifest / no framework redesign, ShipAny leakage, reviewer-invented tolerance, or product-layer override of Starter foundation. | Versioned owners/routes/viewports/states/assets/rules; predeclared tolerances; fully evidenced approved deviations. | Predictable loading/error plus responsive/a11y evidence; two fresh reviewers applying the same manifest reach the same PASS/BLOCK result. | `AUD-FINAL-04`, `AUD-WORK-060`, `KSS-STS021A-RESOLUTION-R2`, `KSS-STS024-RESIDUAL-CORRECTION-R1`; GAP-015. |
| CAP-025 Technical SEO | CORE | Partial metadata/canonical and stale static assets; **PATCH** | Reusable route/environment SEO baseline including required icons and route-applicable structured data. | Add bounded helpers/generated assets / no product keyword, content, or product-specific schema strategy. | Site origin, indexability, social defaults, route-owned stable facts. | Invalid base fails config; metadata/icon/crawl tests, syntactically valid fact-matched structured data where applicable, and STAGING noindex gate. | `AUD-WORK-050`, `KSS-STS024-RESIDUAL-CORRECTION-R1`; GAP-011, CAP-003. |
| CAP-026 Optional content/UI | KEEP-DISABLED | Blog/docs/charts/editor/carousel exist; **KEEP-DISABLED** | Retained opt-in surfaces outside Core. | Add explicit visibility/tests if selected / no deletion or default exposure. | Feature flag/content source when ON. | OFF routes/UI absent; conditional render/search/editor tests. | `AUD-WORK-060`; GAP-019. |
| CAP-027 Security controls | CORE | Material controls plus Authz/abuse gaps; **PATCH** | Minimum reusable Security Gates enforced server-side. | Targeted validation/Authz/rate limits / no global CAPTCHA or broad framework. | Per-route policy and limit config. | Deny safely with bounded retry hints; negative suite gates release. | `AUD-WORK-070`; GAP-006 and domain gaps. |
| CAP-028 Logging/observability | CORE | Direct console logs, no correlation/health; **PATCH** | Redacted structured diagnostics and revision health. | Small logger/health boundary / no enterprise stack mandate. | Log level and revision; no credentials. | Logging failure does not authorize work; redaction/health tests. | `AUD-WORK-070`; GAP-016. |
| CAP-029 Testing/CI | CORE | Absent test/CI baseline; **PATCH** | Focused automated matrix and deterministic CI gates. | Add suitable harness/scripts/workflows / no architecture rewrite for tooling. | Test-only config and conditional provider credentials. | Gate failure blocks promotion; full mandatory matrix. | `AUD-FINAL-05`; GAP-003. |
| CAP-030 Build quality | CORE | Build/lint scripts exist, explicit typecheck absent; **PATCH** | Reproducible clean typecheck/lint/build. | Add/pin commands and execute / no dependency upgrade merely for freshness. | Pinned package manager/runtime contract. | Nonzero failure blocks release; clean CI verification. | `AUD-WORK-010`, `AUD-WORK-070`; GAP-003. |
| CAP-031 Release/promotion | CORE | Cloudflare/CI/promotion path absent; Vercel/Docker retained; **PATCH** | CI eligibility plus explicit operator approval promotes the exact immutable STAGING commit/artifact and artifact-bound public-config fingerprint with no rebuild or code mutation. | Minimal workflow/evidence/order/recovery and bounded runtime-public injection later / no elaborate release/config platform or claim that the path exists now. | Isolated runtime bindings, immutable commit/artifact ID, artifact-bound fingerprint, validated target runtime-public map, STAGING bundle, migration/recovery record, operator approval. | Failed gate stops eligibility; approval cannot change artifact/fingerprint; production identity, correct runtime-public resolution, no STAGING-value/secret leak, smoke, and rollback evidence required. | `AUD-FINAL-05`, `KSS-STS021A-RESOLUTION-R2`, `KSS-STS024-RESIDUAL-CORRECTION-R1`; GAP-002/008, CAP-002/003/005. |
| CAP-032 Retained non-Core | KEEP-DISABLED | Credits, subscriptions, API keys, affiliate, Vercel/Docker retained; **KEEP-DISABLED** | OFF by default and conditionally verified if advertised. | Add explicit defaults/conditional tests / no deletion, new subscription work, or alternate golden path. | Capability-specific flags/config only ON. | OFF absent/secret-free; ON inherits domain gates. | `AUD-FINAL-02`, `AUD-FINAL-07`; GAP-019. |

## 28. Gap Closure Summary

The implementation design backlog is exactly 19 gaps: P0=8, P1=8, P2=3. The authoritative row-level closure contract is `docs/starter/KYD_SAAS_STARTER_GAP_CLOSURE_MATRIX.md`. P0 establishes deploy/config/test/Auth/email/API/payment/release safety; P1 completes account/payment/SEO/i18n/AI/storage/UI/logging; P2 covers conditional Turnstile, ads/analytics verification, and retained non-Core enablement.

No gap authorizes implementation directly. No gap requires `REFACTOR` or `DELETE`.

## 29. Acceptance Summary

`docs/starter/KYD_SAAS_STARTER_ACCEPTANCE_MATRIX.md` maps every capability to observable evidence. Static design acceptance can run in repository/CI; provider and Cloudflare checks run only during real implementation/environment validation. Mandatory Core release evidence includes configuration negatives, DB migration/transaction smoke, Auth lifecycle/linking, payment signatures/replay, authorization negatives, core UI responsive/a11y checks, and exact-revision STAGING promotion.

Optional capability acceptance is `CONDITIONAL_IF_ENABLED`; OFF-path acceptance is always required for optional/retained-disabled capabilities.

## 30. Explicit Non-Goals / Do-Not-Do

Do not:

- rewrite or reorganize the repository for cleanliness;
- pin Neon, PlanetScale, Supabase, or another PostgreSQL vendor in Starter design;
- add provider SDK coupling to reusable business/domain code;
- introduce PostgreSQL + D1 dual golden paths or mandatory Hyperdrive;
- migrate wholesale to standard Auth.js Adapter tables;
- add account deletion or password Auth;
- rewrite order/payment schema or add request-level automatic failover;
- add new subscription scope or default-enable credits;
- make AI, i18n, ads, analytics, R2, Turnstile, content/tools, Vercel, or Docker mandatory;
- delete retained providers/features without Deletion Review and user approval;
- replace Tailwind, shadcn/Radix, forms/tables, or reusable shells;
- freeze ShipAny brand/copy/assets/pricing/navigation/legal content;
- add a general plugin framework or enterprise observability platform;
- automatically merge later Starter changes into generated projects instead of using `Snapshot + Controlled Patch`;
- require production/simulated-production provisioning to complete design.

Evidence: `docs/audit/00_AUDIT_SUMMARY.md`, `docs/audit/07_DELETION_REVIEW_CANDIDATES.md`, `docs/audit/08_REFACTOR_JUSTIFICATION.md`, `docs/starter/KYD_SAAS_STARTER_DETAILED_SPEC_AUTHORING_AUTHORITY.md`.

## 31. Open Decisions / Ambiguities

`NONE`. Independent `STS-025` re-audit verified zero open implementation-affecting ambiguities.

Implementation may select local mechanisms only within the explicit allowed deltas, for example the exact test runner, the minimal storage shape for the fixed webhook idempotency identity, or the Magic Link token encoding/storage shape. Those choices are not open product/architecture decisions because lifecycle, acceptance, security, reuse, and forbidden boundaries are frozen. Historical `STS-023` findings were closed through `STS-024` and independently verified by `STS-025`; later substantive change requires controlled amendment under `KSS-STS030-FREEZE-R1`.

Evidence: `docs/audit/02_REUSE_GAP_MATRIX.md`, `docs/audit/06_RISK_AND_BLOCKERS.md`, `docs/starter/KYD_SAAS_STARTER_DETAILED_SPEC_AUTHORING_AUTHORITY.md`, `KSS-STS021A-RESOLUTION-R2`, `KSS-STS024-RESIDUAL-CORRECTION-R1`.

## 32. Traceability to Audit Evidence

| Starter capability group | Audit evidence | Frozen decision | Gap IDs | Acceptance IDs |
|---|---|---|---|---|
| Framework, Cloudflare, config, build/release | `AUD-WORK-010`, `AUD-FINAL-03`, `AUD-FINAL-05` | Cloudflare first; three environments | GAP-001, GAP-002, GAP-003, GAP-008 | ACC-001 through ACC-003, ACC-029 through ACC-031 |
| Database/Drizzle/migrations/atomicity | `AUD-WORK-020` | `DEC-A001-POLICY` | GAP-007, GAP-008 | ACC-004 through ACC-006 |
| Auth, Google, Magic Link, email, account | `AUD-WORK-030` | Google + Magic Link trusted identity | GAP-004, GAP-005, GAP-009 | ACC-007 through ACC-011, ACC-021 |
| Orders, Stripe, Creem, webhooks, entitlement | `AUD-WORK-040` | One-time dual provider, operator switch | GAP-007, GAP-010 | ACC-012 through ACC-017, ACC-032 |
| AI, i18n, ads/analytics, storage, Turnstile | `AUD-WORK-050` | Optional, explicit, clean OFF | GAP-012, GAP-013, GAP-014, GAP-017, GAP-018 | ACC-018 through ACC-023 |
| UI and technical SEO | `AUD-FINAL-04`, `AUD-WORK-060`, `AUD-WORK-050` | A-002 frozen keep list | GAP-011, GAP-015, GAP-019 | ACC-024 through ACC-026 |
| Security, logging, tests, release | `AUD-WORK-070`, `AUD-FINAL-05` | Minimum reusable gates | GAP-003, GAP-006, GAP-008, GAP-016 | ACC-027 through ACC-031 |
| Retained non-Core surfaces | `AUD-FINAL-02`, `AUD-FINAL-07` | Retain disabled; no deletion | GAP-019 | ACC-021, ACC-026, ACC-032 |

The acceptance IDs above resolve in `docs/starter/KYD_SAAS_STARTER_ACCEPTANCE_MATRIX.md`; the gap rows resolve in `docs/starter/KYD_SAAS_STARTER_GAP_CLOSURE_MATRIX.md`.
