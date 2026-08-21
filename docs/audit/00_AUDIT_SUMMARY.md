# Full sa-template Repository Audit Summary

> Task: `AUD-080`  
> Sources: verified `AUD-000` through `AUD-070`  
> Audited commit: `503ca9a0f46bc732fe974b6d336e1d1fcd2eb8a4` on `audit/kyd-starter-v1`  
> Result: final synthesis only; no application/product implementation was changed.

## Executive Summary

The current `sa-template` is a viable source base for Kyd SaaS Starter V1 through **REUSE FIRST + MINIMAL DELTA + COMPATIBILITY FIRST**.

Overall minimal-delta result: `YES — PATCH`.

- No `REFACTOR` is proven necessary.
- No `DELETE` is justified and no deletion is authorized.
- Existing Next.js, PostgreSQL/Drizzle, Auth.js boundary, dual one-time payment paths, optional platform modules, and UI foundation should be preserved.
- The largest missing work is production-readiness integration: Cloudflare/OpenNext, Auth Magic Link/trusted linking, payment idempotency/atomicity, clean optional-module policy, focused tests/security/logging, and three-environment release gates.
- The final backlog has 19 bounded gaps: P0=8, P1=8, P2=3.

## Repository Reuse Assessment

### Starter V1 capability model

| Classification | Capabilities |
|---|---|
| CORE | Next.js/React/TypeScript; PostgreSQL/Drizzle/migrations; Auth core, Google OAuth, Email Magic Link, account/profile/logout; Stripe and Creem one-time payments, operator provider switch, paid ownership; technical SEO; reusable UI foundation; Cloudflare/OpenNext; tests/security/logging/CI/release gates |
| OPTIONAL | AdSense, analytics, i18n, OpenAI, storage/R2, Turnstile |
| KEEP-DISABLED | GitHub OAuth, Google One Tap, credits, Stripe subscriptions, other AI providers after policy patch, API keys, affiliate/invite, blog/docs/charts/editor/carousel, Vercel, Docker |
| OUT_OF_SCOPE_FOR_V1 | Account deletion; new subscription work beyond retained code; request-level payment failover; D1 dual golden path; mandatory R2/Turnstile/i18n; product-specific visual design; enterprise observability/plugin architecture |

### Final reuse posture

| Action | Final scope |
|---|---|
| KEEP | No major capability is bare `KEEP` because automated verification is absent |
| KEEP + TEST | Framework, DB/ORM/migrations, session/logout, existing browser integrations, primitives/forms/tables/shells/assets and alternate build surfaces |
| KEEP-DISABLED | Mature non-default providers/features/content/deployment paths |
| WRAP | Resend Auth email delivery; theme/application composition |
| PATCH | Confirmed functional, security, compatibility, optionality, UI and release gaps |
| REFACTOR | None |
| DELETE | None |

## Highest-Value KEEP / KEEP + TEST Areas

1. Next.js 15 App Router, React 19 and strict TypeScript application structure.
2. PostgreSQL/Drizzle schema, migrations, model boundaries and generic `DATABASE_URL`.
3. Auth.js callback/JWT/session boundary, canonical `users.uuid`, server route/layout guards and logout controls.
4. Existing Stripe and Creem checkout/callback/webhook integrations plus server-derived pricing and `PAY_PROVIDER` switch.
5. Durable orders and optional credit ledger.
6. AdSense, GA/OpenPanel/Plausible environment-gated browser integrations.
7. Tailwind v4 tokens, `cn`, 33 shadcn/Radix primitives, generic forms/tables.
8. Dashboard, console, marketing, pricing and Auth structural UI.
9. Fumadocs/blog/charts/editor and alternate providers/deployments as retained disabled options.

## Material Gaps

P0: Cloudflare/OpenNext integration; validated three-environment configuration; tests/CI; Magic Link/trusted identity; Resend Auth delivery; high-risk API authorization/abuse controls; payment idempotency/transactions; Staging/same-commit/migration/rollback release path.

P1: Auth/account completion; payment lifecycle/entitlement; technical SEO; default-off i18n; AI policy; storage/R2 validation; bounded UI fixes/a11y/states; logging/diagnostics.

P2: optional Turnstile; Ads/analytics verification; retained non-Core enablement contracts/tests.

## Blocking Risks

- Starter implementation/release is blocked by P0 gaps, but the repository audit itself is complete.
- A-001 is frozen as a vendor-neutral PostgreSQL Provider Policy; the vendor remains unpinned and real provider qualification is deferred to implementation/environment validation.
- Cloudflare deployment integration is absent; this is not evidence of a general Worker incompatibility.
- No automated test/CI baseline exists, so no application build/provider/browser behavior was verified during audit.
- Auth Magic Link/trusted-linking and payment replay/atomicity are correctness/security gates, not optional polish.

## A-001 Evidence Summary

### Result

`FROZEN — PostgreSQL Provider Policy R1`

Repository evidence establishes the frozen portable boundary: PostgreSQL + Drizzle, existing schema/migrations, centralized database access, and generic `DATABASE_URL`, with provider-specific coupling forbidden by default in reusable business/domain code. The default vendor is `UNPINNED` during Starter design.

Provider Qualification is deferred until a real provider/environment is provisioned and before that environment is relied on for release. Hyperdrive is optional and is validated only when selected. The exact stable contract and PQ-01 through PQ-13 qualification gate are frozen in `docs/decisions/A-001_POSTGRES_PROVIDER_POLICY.md`; no vendor bake-off blocks Starter Detailed Spec.

## A-002 Evidence Summary

### Result

`FROZEN — KEEP LIST`

The frozen structural keep list is: Tailwind semantic token/global CSS/`cn` foundation; shadcn/Radix primitives; generic forms/tables; theme boundary; dashboard/admin and console/member shells; marketing Header/Footer/section structures; pricing and Auth/account structures; asset/icon conventions; shared loading/error/not-found and responsive/accessibility foundations after bounded patches.

Blog/Fumadocs and charts/carousel/editor/data-card groups remain optional `KEEP-DISABLED`. ShipAny copy, claims, logos, imagery, links, menus, pricing products and legal content are product-specific and are not Starter Visual Authority.

The detailed group/action/test boundary is frozen in `docs/audit/04_UI_FOUNDATION_AUDIT.md`.

## Minimum Production-Readiness Set

1. Implement GAP-001 through GAP-008 before Starter production release.
2. Run the mandatory test matrix for Runtime, build, DB, Auth, payment, UI, accessibility and Cloudflare Staging.
3. Enforce the minimum Security Gates for trusted identity, Magic Link, protected APIs, secrets/rate limits, server pricing and webhook idempotency.
4. Deploy isolated Cloudflare DEVELOPMENT/STAGING/PRODUCTION environments.
5. Promote only the exact Staging-verified commit and maintain a concise migration/rollback path.
6. Run conditional tests only for optional/non-Core capabilities selected by a product.

## Do Not Do

Starter implementation must not, without later evidence/authority:

- perform a repo-wide refactor or directory cleanup;
- migrate wholesale to a standard Auth.js Adapter schema;
- rewrite payment/order schema to remove provider-specific naming;
- add request-level automatic payment-provider failover;
- introduce PostgreSQL + D1 dual golden paths;
- make R2, Turnstile, or i18n mandatory;
- delete Vercel/Docker, existing AI providers, credits, subscriptions, or optional content/UI systems;
- replace Tailwind, shadcn/Radix, or the reusable UI foundation;
- freeze ShipAny branding/content as Starter product design;
- add account deletion or new subscription scope without Product Authority;
- add an enterprise observability platform or elaborate internal plugin framework;
- pin a default PostgreSQL vendor or require a vendor bake-off during Starter design without a concrete project/operational need.

## Next Step

The Full Repository Audit is complete. The next planning phase is Kyd SaaS Starter Detailed Spec: convert the 19-gap backlog into the Detailed Spec and deterministic implementation Task graph. Provider qualification and isolated provider/Cloudflare resources are deferred until a real implementation/environment needs them. No Starter implementation Task is created or started here.
