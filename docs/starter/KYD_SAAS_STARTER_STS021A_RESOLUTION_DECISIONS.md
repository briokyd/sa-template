# Kyd SaaS Starter - STS-021A Resolution Decisions R2

Authority ID: `KSS-STS021A-RESOLUTION-R2`  
Version: `R2`  
Status: `FROZEN`

## Purpose

This Authority freezes the resolution decisions required to correct the nine `STS-020` findings after the `STS-021A` existing-implementation mapping. It supersedes the unresolved-option state in the STS-021 packet for correction purposes but does not rewrite the historical STS-020 or STS-021 results.

The correction remains design-only. It preserves mapped `sa-template` implementation, introduces no application work, and does not authorize `STS-030`.

## Final Finding Resolution

```text
F-001 -> R1 / PATCH
F-002 -> R3 / RESOLVED / PATCH
F-003 -> R1 / KEEP + TEST
F-004 -> R1
F-005 -> R1 / KEEP
F-006 -> R2 / RESOLVED
F-007 -> R1 / KEEP
F-008 -> R1
F-009 -> R2 / RESOLVED
```

No new abstraction is proven necessary.

Existing implementation is preserved for `F-001`, `F-003`, `F-004`, `F-005`, `F-006`, `F-007`, `F-008`, and `F-009`.

True missing capabilities are:

- `F-002`: Email Magic Link;
- `F-009`: Cloudflare/OpenNext release implementation path. Its policy is frozen here; implementation remains future bounded `PATCH` work.

## F-001 Payment Resolution

Preserve the current payment architecture:

- server-derived pricing;
- operator-controlled `PAY_PROVIDER`;
- existing Stripe and Creem checkout paths;
- existing server-verified callbacks;
- existing signed raw-body webhooks;
- existing shared `updateOrder` one-time mutation path;
- existing orders, credits, and affiliate modules.

The corrected design specifies only bounded deltas for provider-event/order idempotency, conditional transition and transaction atomicity, durable paid/order/entitlement semantics, and failure/replay convergence. It must not require an unproven shared transition framework, provider plugin framework, or payment schema rewrite.

## F-002 Magic Link Resolution

Magic Link is a missing Core capability. Freeze exactly:

```text
one active Magic Link token per normalized email
initial validity = 15 minutes
single-use
```

### Re-request while active

When an accepted request occurs before the active token expires:

```text
DO NOT rotate the active token
DO NOT invalidate the current active link
DO NOT create a second active token

keep the same logical active token/credential
resend the current active Magic Link
expires_at = latest accepted request time + 15 minutes
```

A delayed email from the same active-token lifecycle must remain valid merely because the user requested another link while that token was active.

### Consumption and expiry

- Successful use immediately and atomically consumes the token.
- A consumed token cannot authenticate again.
- An expired token cannot authenticate.
- The first accepted request after true expiry creates a new active token.

Request throttling is a separate Auth security control. Token rotation or invalidation must not be used as the rate-limit mechanism.

The design remains implementation-neutral about token encoding and storage beyond the observable lifecycle. No provider/plugin framework or mandatory Auth.js Adapter migration is authorized.

Required acceptance covers initial 15-minute validity, active re-request preservation, expiry extension to latest accepted request plus 15 minutes, single use, consumed/expired rejection, new token after true expiry, and delayed-email behavior.

## F-003 Session Resolution

Starter V1 retains the existing pinned Auth.js session strategy and default behavior. It does not invent custom `maxAge`, `updateAge`, or other numeric session lifetime values merely for specification completeness.

Required tests record and verify the resolved pinned behavior, canonical UUID session payload, secure cookie/runtime properties, expiry, refresh/update behavior, protected access, and current-browser logout. Snapshot + Controlled Patch review is required when the pinned dependency changes.

## F-004 Configuration Resolution

Preserve current variable names and consumers where feasible. Correct the design with a redacted ownership matrix that records capability owner, canonical/current name, environment variable versus platform binding, public/server-secret class, required condition, default/OFF behavior, and DEVELOPMENT/STAGING/PRODUCTION ownership.

Use a narrow validation/binding boundary. Do not create a giant configuration subsystem or rename the repository wholesale.

## F-005 Upgrade Resolution

Freeze the existing Authority verbatim in the candidate spec:

```text
Snapshot + Controlled Patch
NO automatic merge into projects
```

## F-006 Visual Authority Resolution

Use a two-layer model:

```text
Layer 1 - Starter Visual Foundation Authority
Layer 2 - Product Visual Authority
```

Layer 1 may contain product-neutral tokens/theme, shadcn/Radix primitives, generic shells/layouts, responsive/accessibility/loading/error baseline, generic asset conventions, and product-neutral references.

Layer 2 contains Approved Screens, Actual Assets, interaction/state references, responsive product references, and product-specific brand/content/visual semantics.

ShipAny-specific brand, copy, imagery, pricing, navigation, legal content, and product semantics must not become Starter Authority. Existing A-002 implementation is preserved. Fresh-context Fidelity Audit compares each layer only to its approved reference scope.

## F-007 Traceability Resolution

Correct the three capability mappings without renumbering gaps or capabilities:

- `GAP-007`: `CAP-006` DB atomicity, `CAP-016` Webhooks/idempotency, `CAP-017` Entitlement, and `CAP-032` only for enabled credit/affiliate side effects.
- `GAP-010`: `CAP-012` Orders, `CAP-013` Stripe, `CAP-014` Creem, `CAP-015` provider switch, `CAP-016` Webhooks/idempotency, and `CAP-017` Entitlement.
- `GAP-019`: `CAP-018` additional AI providers, `CAP-021` non-default Auth, `CAP-026` optional content/UI, and `CAP-032` retained non-Core; Core `CAP-017` is excluded.

## F-008 Atomicity Resolution

Name only repository-evidenced invariants:

- When optional initial credits are OFF, canonical user creation performs no credit write. When enabled, canonical user creation and exactly one initial-credit grant commit together or leave neither dependent outcome.
- When affiliate/referral is OFF, its mutation route is unavailable. When enabled, `users.invited_by` and the corresponding affiliate relation commit together or neither commits. Invalid, self, repeated, or wrong-owner attempts create no partial state.
- Payment atomicity is owned by the F-001 payment contract and is referenced rather than duplicated.

No generic transaction framework is authorized.

## F-009 Release Resolution

Freeze the target policy:

```text
CI/verification determines whether a commit is eligible for Production.

Production promotion requires explicit operator approval.

Production promotes the exact immutable commit verified in Staging.

No rebuild or code mutation is allowed between verified Staging and Production promotion.
```

The evidence bundle records commit identity, Staging gates, migration/recovery readiness, and operator approval. Production deployment and post-deploy smoke verify that the promoted revision equals the approved Staging revision.

This is target release policy. It is not evidence that the current Cloudflare/OpenNext, CI, Staging, or promotion path exists. That implementation remains a future bounded `PATCH`; Vercel and Docker remain retained disabled alternates.

## Correction and Re-audit Boundary

The candidate master spec, gap matrix, and acceptance matrix must be corrected together without changing 32 capability IDs, 19 gap IDs, the `P0=8/P1=8/P2=3` priority counts, or the evidence-backed primary actions except where this Authority explicitly resolves finding wording.

After correction, a fresh-context completeness/ambiguity re-audit is mandatory before `STS-030`. Correction alone does not authorize freeze.
