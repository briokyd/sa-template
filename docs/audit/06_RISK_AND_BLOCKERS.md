# Risk and Blockers

> Task: `AUD-080`  
> Scope: final repository-grounded risks and decisions requiring user/planner action.

| ID | Area | Risk / Blocker | Evidence | Severity | Suggested Action | Blocks Starter V1? |
|---|---|---|---|---|---|---|
| R-001 | A-001 PostgreSQL provider qualification | Vendor is intentionally unpinned; real provider/runtime behavior remains unverified until a concrete environment exists. | AUD-020 generic `DATABASE_URL`, no provider SDK/binding/test; DEC-A001-POLICY | MEDIUM | KEEP + TEST | No for Starter design; qualification gates the selected environment before release |
| R-002 | Cloudflare release | No OpenNext/Wrangler/Worker/CI integration or Cloudflare Staging exists. | AUD-010, AUD-070 | CRITICAL | PATCH | Yes |
| R-003 | Environment promotion | No isolated three-environment model, same-commit promotion, migration order, or rollback process. | AUD-010, AUD-070 | HIGH | PATCH | Yes |
| R-004 | Test/CI baseline | No automated tests, test framework, typecheck script, CI, or executed app build evidence. | AUD-070 | CRITICAL | PATCH | Yes |
| R-005 | Auth identity | Magic Link absent; Google verified-email and concurrent same-email canonical linking not guaranteed. | AUD-030 | CRITICAL | PATCH | Yes |
| R-006 | Auth email delivery | Resend exists only as an unauthenticated generic demo route, not an Auth boundary. | AUD-030, AUD-070 | HIGH | WRAP | Yes |
| R-007 | Public mutation/provider routes | AI/email demo routes lack caller checks/rate controls; invite update trusts caller UUID. | AUD-050, AUD-070 | CRITICAL | PATCH | Yes for retained routes |
| R-008 | Payment consistency | Webhook signatures exist, but replay/concurrency/partial failure can duplicate or omit dependent side effects. | AUD-020, AUD-040, AUD-070 | CRITICAL | PATCH | Yes when payments enabled |
| R-009 | Payment lifecycle/access | Checkout failure/cancel/refund/revocation and general entitlement policy are incomplete. | AUD-040 | HIGH | PATCH | Yes for production one-time payment |
| R-010 | Secrets/config | Fixed reusable Auth sample, missing env names, distributed unvalidated reads. | AUD-010, AUD-070 | HIGH | PATCH | Yes |
| R-011 | Logging | Provider/user result objects are logged directly without redaction/correlation/health diagnostics. | AUD-040, AUD-050, AUD-070 | HIGH | PATCH | Yes for production readiness |
| R-012 | Technical SEO | Stale sitemap, incomplete canonical/social/structured metadata, no Staging noindex. | AUD-050 | MEDIUM | PATCH | Yes for Starter SEO baseline |
| R-013 | Optional-module cleanliness | i18n structurally on; AI/storage providers reachable or fail late; R2/Buffer unverified. | AUD-050 | HIGH | PATCH | Yes for promised clean optionality |
| R-014 | UI verification/semantics | No browser/a11y/visual tests; localized pricing/theme controls and route states need fixes. | AUD-060, AUD-070 | HIGH | PATCH | Yes for reusable UI release gate |
| R-015 | Non-Core retained surfaces | Credits/subscriptions/API keys/affiliate/docs/charts/editor lack complete tests and may remain visible in current template. | AUD-040, AUD-050, AUD-060 | MEDIUM | KEEP-DISABLED | No when disabled |

## A-001 Policy

`FROZEN — PostgreSQL Provider Policy R1`

The Starter freezes PostgreSQL + Drizzle + generic `DATABASE_URL`, not a permanent vendor. Provider-specific coupling in reusable business/domain code is forbidden by default, and the vendor remains `UNPINNED` during Starter design.

The PQ-01 through PQ-13 gate in `DEC-A001-POLICY` becomes mandatory only when a real provider/environment is provisioned and before that environment is relied on for release. Hyperdrive is optional and qualifies only when selected. No Neon/PlanetScale/Supabase bake-off is required for Starter Detailed Spec, Delivery Protocol Detailed Spec, design audit, or Design Freeze.

## A-002 Status

`FROZEN — KEEP LIST`. No evidence blocker remains for structural classification. Browser/a11y tests are implementation/release gates, not a reason to discard or defer the repository-grounded keep list.

## Planner/User Actions

1. Convert `GAP-001` through `GAP-019` into a Detailed Spec and deterministic implementation Task graph; do not execute directly from the audit matrix.
2. Apply A-001 Provider Qualification only when a concrete provider/environment is selected.
3. Define real provider accounts/credentials and isolated Cloudflare Staging resources before the relevant environment is relied on for release, not as a Starter design prerequisite.
4. Approve any future deletion separately; this audit has no deletion candidate.
