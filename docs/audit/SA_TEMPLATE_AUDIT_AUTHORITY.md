# SA-TEMPLATE FULL REPOSITORY AUDIT AUTHORITY V1

> **Authority ID:** AUDIT-001  
> **Version:** v1  
> **Status:** FROZEN  
> **Purpose:** Define the scope, evidence standard, action taxonomy, and anti-refactor rules for the first Full Repository Audit of `sa-template` as the source base for Kyd SaaS Starter.

---

# 1. Audit objective

The audit objective is **not** to redesign `sa-template` and **not** to produce an idealized architecture.

The audit must determine, from repository facts:

```text
What already exists?
What already works?
What can be reused unchanged?
What only needs tests?
What can remain disabled?
What needs a wrapper?
What needs a minimal patch?
What truly requires refactor?
What, if anything, is a justified deletion candidate?
```

The governing principle is:

```text
Reuse First
+
Minimal Delta
+
Compatibility First
```

The purpose of the Starter is to shorten future project delivery and reduce rework. Template work must not become an indefinite architecture project.

---

# 2. Audit-only branch behavior

During AUD-000 through AUD-080:

```text
BUSINESS / PRODUCT IMPLEMENTATION CHANGES = FORBIDDEN
```

The audit may inspect any repository file required for factual evidence.

It may modify only:

- Runtime state/task/trace documents required by Kyd Project Runtime;
- `docs/audit/**` audit evidence and synthesis documents;
- no application/source implementation merely to make an audit finding disappear.

If a real defect is discovered, record it as a finding. Do not fix it during the audit unless a later separately planned implementation task explicitly authorizes that fix.

---

# 3. Mandatory action taxonomy

Every audited capability/item must receive exactly one primary Action:

```text
KEEP
KEEP + TEST
KEEP-DISABLED
WRAP
PATCH
REFACTOR
DELETE
```

No synonyms or fuzzy alternatives are allowed.

## KEEP

Existing implementation satisfies the planned Starter role. No implementation change required.

## KEEP + TEST

Implementation is reusable; only missing/insufficient verification must be added later.

## KEEP-DISABLED

Existing capability remains in the codebase but is not part of the default Starter path/UI/config.

Use this before deletion when the capability is mature or potentially reusable and cheap to retain.

## WRAP

Keep the mature internal implementation and add only a small facade/adapter/policy/config boundary later.

## PATCH

There is a concrete correctness/compatibility/reuse gap that can be fixed by the smallest localized change.

## REFACTOR

Allowed as a recommendation only if the audit explicitly proves why all of the following are insufficient:

```text
KEEP
KEEP + TEST
KEEP-DISABLED
WRAP
PATCH
```

A REFACTOR finding must state:

```text
why KEEP fails
why KEEP + TEST fails
why KEEP-DISABLED fails (if applicable)
why WRAP fails
why PATCH fails
minimum refactor scope
regression risk
tests required
```

## DELETE

Highest threshold. The audit may only identify a `DELETE CANDIDATE`.

No deletion is authorized by this audit.

Every candidate must include a Deletion Review:

```text
object
current purpose
deletion reason
retention cost
future reuse impact
why KEEP-DISABLED is insufficient
why WRAP/PATCH is insufficient
replacement
rollback
```

Actual deletion requires later user review/approval.

`Not in Starter V1 Core` is never sufficient deletion justification.

---

# 4. Mandatory audit item schema

Every meaningful capability finding must capture:

```text
Module / Capability
Existing implementation
Existing files
Current behavior
Starter planned role
Required behavior
Gap
Action
Default enabled?
Tests today
Tests required
Cloudflare compatibility
Risk
Reason
Evidence
```

Rules:

- `Existing implementation`, `Current behavior`, `Tests today`, and `Cloudflare compatibility` must be based on repository evidence, commands, or explicit inability to verify.
- Do not convert an assumption into a fact.
- When evidence is incomplete, state `UNKNOWN / NOT VERIFIED` and record what evidence is missing.
- Always cite concrete repository paths, symbols, config keys, scripts, or command output where applicable.
- Do not call something `REFACTOR` merely because naming, layering, directory structure, or schema aesthetics are imperfect.

---

# 5. Compatibility rules

Existing directories, routes, database schema, environment-variable names, services, and module boundaries should be preserved by default.

A structural/breaking change may only be recommended when factual evidence shows a material:

- correctness problem;
- security problem;
- Cloudflare Workers/OpenNext compatibility blocker;
- cross-project reuse blocker;
- unsupported/deprecated dependency problem;
- issue that cannot be solved by KEEP / KEEP+TEST / KEEP-DISABLED / WRAP / PATCH.

Prefer additive/compatible changes and wrappers over migrations/renames.

---

# 6. Frozen Starter targets relevant to the audit

The audit evaluates the existing repository against these already-frozen strategic targets without assuming implementation changes are required.

## Deployment

```text
Cloudflare First
Primary full-stack runtime: Cloudflare Workers + OpenNext
```

Cloudflare-first does not imply automatic use of D1/KV/Queues/Durable Objects/R2.

## Database

```text
PostgreSQL + Drizzle
vendor-neutral
Cloudflare/Workers/Hyperdrive compatible
```

Do not create a D1 second golden path in V1.

Default PostgreSQL provider remains audit-dependent decision `A-001`.

## Auth

Target:

```text
Auth.js
Google OAuth
Email Magic Link
trusted-provider linking for verified same-email identity
```

Existing Auth must be audited before recommending structural migration.

## Payment

Target:

```text
Creem one-time production-ready
Stripe one-time production-ready
operator-controlled active provider
NO request-level automatic failover
```

Existing orders/payment structures are reuse candidates. Provider-specific field names alone are not refactor justification.

## i18n

```text
Default OFF
Supported + Tested when enabled
```

Existing i18n should not be deleted merely because default is off.

## AI

Optional. OpenAI is the default standard path. Existing additional providers should normally be considered KEEP-DISABLED / WRAP / PATCH rather than deleted.

## Email

Resend is the sole V1 production-ready email adapter target, with reuse of existing implementation preferred.

## Ads

AdSense is the sole V1 production-ready ad adapter target, with reuse of existing implementation preferred.

## Account

Profile/Account/Logout are Core. Account deletion is not a generic mandatory V1 behavior.

## Upgrade strategy

```text
Snapshot + Controlled Patch
NO automatic merge into projects
```

---

# 7. Full Repository Audit coverage

The audit must cover at least:

```text
Framework / Next.js / React
Cloudflare runtime / OpenNext suitability
Build and deployment configuration
Environment / config handling
PostgreSQL / Drizzle / migrations / database access
Auth.js / NextAuth
Google OAuth
Email Magic Link / email / Resend
Session
Account / Profile / Logout
Orders
Creem
Stripe
Checkout
Payment callbacks / webhooks
Entitlement / paid access / credits relationship
Ads / AdSense
Analytics / GA / Plausible / OpenPanel
SEO infrastructure
robots / sitemap / canonical / metadata / structured data helpers
staging noindex behavior
i18n / next-intl
AI providers / client abstractions
Storage / R2 suitability
Turnstile
Blog / posts / Fumadocs / MDX
API keys
Affiliate / referral
Dashboard / pricing / common SaaS surfaces
UI primitives / shared components / auth/payment shells
Error handling
Logging / redaction
Security baseline
Tests
Real-provider staging support
Release tooling
```

If a listed capability is absent, report it as absent; do not invent an implementation.

---

# 8. Prior observations are hypotheses, not audit conclusions

Prior planning indicated that `sa-template` may contain capabilities such as Next.js/React, Auth.js, Google/GitHub auth, Google One Tap, PostgreSQL/Drizzle, Stripe, Creem, Resend, analytics providers, AdSense, i18n, Fumadocs/MDX, storage, orders, credits, affiliate, API keys, blog/posts, pricing/dashboard, and related SaaS components.

These are **starting hypotheses to verify**.

The audit must not mark them present merely because this Authority lists them.

Likewise, earlier concerns about Auth identity schema, provider-neutral payment schema, or testing quality are **Audit Hypotheses**, not pre-approved refactors.

---

# 9. Required workstream outputs

Each workstream writes only its designated file under:

```text
docs/audit/work/
```

Each finding follows the mandatory audit item schema.

Workstream files:

```text
00_REPOSITORY_INVENTORY.md
10_FRAMEWORK_CLOUDFLARE_ENV_CONFIG.md
20_DATABASE_DRIZZLE_MIGRATIONS.md
30_AUTH_EMAIL_SESSION_ACCOUNT.md
40_PAYMENT_ORDERS_WEBHOOK_ENTITLEMENT.md
50_OPTIONAL_PLATFORM_CAPABILITIES.md
60_UI_FOUNDATION.md
70_TEST_SECURITY_LOGGING_BUILD_DEPLOY.md
```

---

# 10. Final synthesis outputs

AUD-080 must synthesize the verified workstreams into:

```text
docs/audit/00_AUDIT_SUMMARY.md
docs/audit/01_CAPABILITY_MATRIX.md
docs/audit/02_REUSE_GAP_MATRIX.md
docs/audit/03_CLOUDFLARE_RUNTIME_AUDIT.md
docs/audit/04_UI_FOUNDATION_AUDIT.md
docs/audit/05_TEST_AND_RELEASE_AUDIT.md
docs/audit/06_RISK_AND_BLOCKERS.md
docs/audit/07_DELETION_REVIEW_CANDIDATES.md
docs/audit/08_REFACTOR_JUSTIFICATION.md
```

The synthesis must not weaken or silently reinterpret workstream evidence.

---

# 11. Audit-dependent decisions that must emerge from evidence

The final audit must provide enough evidence to decide later:

```text
A-001 — Default PostgreSQL Provider
A-002 — sa-template UI Foundation final keep list
```

AUD-080 may summarize evidence and candidate recommendation, but these decisions are not silently frozen by Codex.

---

# 12. Audit completion condition

The Full Repository Audit is complete only when:

- AUD-000 through AUD-080 are VERIFIED;
- all required audit outputs exist;
- every covered capability has evidence or an explicit `UNKNOWN / NOT VERIFIED` finding;
- every recommendation uses the fixed Action taxonomy;
- every REFACTOR recommendation has full justification;
- every DELETE candidate has a Deletion Review;
- no audit Task modified business/application implementation;
- Runtime closeout validation passes;
- A-001 / A-002 evidence sections are ready for user decision.
