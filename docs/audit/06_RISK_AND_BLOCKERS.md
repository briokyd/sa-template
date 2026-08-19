# Risk and Blockers

> Task: `AUD-080`  
> Scope: final repository-grounded risks and decisions requiring user/planner action.

| ID | Area | Risk / Blocker | Evidence | Severity | Suggested Action | Blocks Starter V1? |
|---|---|---|---|---|---|---|
| R-001 | A-001 PostgreSQL provider | Repository is vendor-neutral and cannot establish the best current default vendor without external facts. | AUD-020 generic `DATABASE_URL`, no provider SDK/binding/test | HIGH | KEEP + TEST | Blocks freezing A-001; does not block audit completion |
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

## A-001 Blocker

`BLOCKED — EXTERNAL FACT VERIFICATION REQUIRED`

The planner/user must approve a provider shortlist and verify these current external facts before freezing a default:

1. Standard PostgreSQL connection-string and `postgres`/Drizzle support from Cloudflare Workers/OpenNext.
2. Direct Worker connectivity and current Hyperdrive compatibility, including TLS/network restrictions.
3. Serverless connection, pooling, concurrency, idle timeout, and connection-limit behavior.
4. Current pricing for isolated DEVELOPMENT/STAGING/PRODUCTION databases, compute/storage, egress, backups, and recovery.
5. Regions and measured latency relative to intended Cloudflare deployments/users.
6. Current availability/GA status, operational limits, maintenance behavior, and support/SLA.
7. Migration, branching, PITR/backup/restore, observability, access control, and credential rotation capabilities.
8. A real Cloudflare Staging migration/read/write/concurrency/transaction smoke result for finalists.

No vendor is selected from model memory or the Supabase comment in `.env.example`.

## A-002 Status

`FROZEN — KEEP LIST`. No evidence blocker remains for structural classification. Browser/a11y tests are implementation/release gates, not a reason to discard or defer the repository-grounded keep list.

## Planner/User Actions

1. Resolve A-001 through the external fact checklist; freeze one provider only after Staging evidence.
2. Convert `GAP-001` through `GAP-019` into a Detailed Spec and deterministic implementation Task graph; do not execute directly from the audit matrix.
3. Define real provider accounts/credentials and isolated Cloudflare Staging resources for DB, Google, Resend, Stripe, Creem, and enabled optional modules.
4. Approve any future deletion separately; this audit has no deletion candidate.
