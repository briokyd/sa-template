# Kyd SaaS Starter Detailed Spec Completeness / Ambiguity Audit

> Task: `STS-020`  
> Audit Authority: `KSS-STS020-AUDIT-R1`  
> Candidate version: `DRAFT R1 - AUTHORED, NOT FROZEN`  
> Result: `FAIL — CORRECTION REQUIRED`

## 1. Executive Result

The candidate artifacts are structurally complete but are not ready to freeze. The audit independently confirmed 32 unique capabilities, 32 one-to-one acceptance records, and exactly 19 unique gaps with the required `P0=8`, `P1=8`, and `P2=3` distribution. The reported reuse-action distribution is also arithmetically correct, and all 24 `PATCH` classifications have repository evidence for a bounded delta.

Freeze is blocked by one `BLOCKER` and eight `MAJOR` findings. The payment contract refers to a state table that does not exist and leaves state authority, idempotency ownership, transaction sequencing, and entitlement grant/revocation behavior for implementation to decide. Other unresolved material areas are Magic Link lifecycle, session expectations, the concrete configuration inventory, named non-payment transaction invariants, release ownership, and the missing UI visual-reference/fresh-context Fidelity Audit contract. Two frozen requirements are omitted, and three Gap Matrix rows contain incorrect Capability IDs.

No application implementation was changed. `STS-030` must remain `NOT_READY`.

## 2. Inputs / Authority

Mandatory Authority:

- `docs/starter/KYD_SAAS_STARTER_STS020_AUDIT_AUTHORITY.md` (`KSS-STS020-AUDIT-R1`)
- `docs/starter/KYD_SAAS_STARTER_DETAILED_SPEC_AUTHORING_AUTHORITY.md` (`KSS-DS-AUTH-R1`)
- `docs/decisions/A-001_POSTGRES_PROVIDER_POLICY.md` (`DEC-A001-POLICY`)
- `docs/audit/SA_TEMPLATE_AUDIT_AUTHORITY.md` (`AUDIT-001`)

Candidate artifacts:

- `docs/starter/KYD_SAAS_STARTER_DETAILED_SPEC.md`
- `docs/starter/KYD_SAAS_STARTER_GAP_CLOSURE_MATRIX.md`
- `docs/starter/KYD_SAAS_STARTER_ACCEPTANCE_MATRIX.md`

Evidence reviewed:

- `docs/audit/00_AUDIT_SUMMARY.md` through `docs/audit/08_REFACTOR_JUSTIFICATION.md`
- `docs/audit/work/00_REPOSITORY_INVENTORY.md`
- `docs/audit/work/10_FRAMEWORK_CLOUDFLARE_ENV_CONFIG.md`
- `docs/audit/work/20_DATABASE_DRIZZLE_MIGRATIONS.md`
- `docs/audit/work/30_AUTH_EMAIL_SESSION_ACCOUNT.md`
- `docs/audit/work/40_PAYMENT_ORDERS_WEBHOOK_ENTITLEMENT.md`
- `docs/audit/work/50_OPTIONAL_PLATFORM_CAPABILITIES.md`
- `docs/audit/work/60_UI_FOUNDATION.md`
- `docs/audit/work/70_TEST_SECURITY_LOGGING_BUILD_DEPLOY.md`
- A-002 as frozen in `docs/audit/04_UI_FOUNDATION_AUDIT.md`, supported by `docs/audit/work/60_UI_FOUNDATION.md`

## 3. Artifact Integrity

| Check | Expected | Actual | Result |
|---|---:|---:|---|
| Master sections | 32 required non-empty sections | 32 | PASS |
| Material Capability IDs | 32 unique | 32 unique, `CAP-001` through `CAP-032` | PASS |
| Acceptance IDs | One per capability | 32 unique, `ACC-001` through `ACC-032` | PASS |
| Capability-to-acceptance mapping | One-to-one | One-to-one | PASS |
| Gap IDs | 19 unique | 19 unique, `GAP-001` through `GAP-019` | PASS |
| Gap priorities | P0=8, P1=8, P2=3 | P0=8, P1=8, P2=3 | PASS |
| Allowed action vocabulary | Seven frozen actions only | Seven frozen actions only | PASS |
| Product-specific leakage | None | None found | PASS |
| Candidate artifacts modified by STS-020 | No | No | PASS |

The candidate files are parseable and internally countable. Structural integrity does not resolve the semantic findings below.

## 4. Capability Coverage

`Schema` means the mandatory capability fields are present. `Semantic audit` records whether those fields close implementation-affecting behavior.

| Capability | Role | Action | Schema | Acceptance | Semantic audit |
|---|---|---|---|---|---|
| CAP-001 Framework | CORE | KEEP + TEST | COMPLETE | ACC-001 | PASS |
| CAP-002 Cloudflare/OpenNext | CORE | PATCH | COMPLETE | ACC-002 | PASS |
| CAP-003 Environment/config | CORE | PATCH | COMPLETE | ACC-003 | MAJOR - F-004 |
| CAP-004 PostgreSQL/Drizzle | CORE | KEEP + TEST | COMPLETE | ACC-004 | PASS |
| CAP-005 Migrations | CORE | KEEP + TEST | COMPLETE | ACC-005 | PASS |
| CAP-006 DB atomicity | CORE | PATCH | COMPLETE | ACC-006 | MAJOR - F-008 |
| CAP-007 Auth core/session | CORE | PATCH | COMPLETE | ACC-007 | MAJOR - F-003 |
| CAP-008 Google OAuth | CORE | PATCH | COMPLETE | ACC-008 | PASS |
| CAP-009 Email Magic Link | CORE | PATCH | COMPLETE | ACC-009 | MAJOR - F-002 |
| CAP-010 Email/Resend | CORE | WRAP | COMPLETE | ACC-010 | PASS |
| CAP-011 Account/profile/logout | CORE | PATCH | COMPLETE | ACC-011 | PASS |
| CAP-012 Orders | CORE | PATCH | COMPLETE | ACC-012 | BLOCKER - F-001 |
| CAP-013 Stripe one-time | CORE | PATCH | COMPLETE | ACC-013 | BLOCKER - F-001 |
| CAP-014 Creem one-time | CORE | PATCH | COMPLETE | ACC-014 | BLOCKER - F-001 |
| CAP-015 Payment provider switch | CORE | PATCH | COMPLETE | ACC-015 | BLOCKER - F-001 |
| CAP-016 Webhooks/idempotency | CORE | PATCH | COMPLETE | ACC-016 | BLOCKER - F-001 |
| CAP-017 Entitlement | CORE | PATCH | COMPLETE | ACC-017 | BLOCKER - F-001 |
| CAP-018 AI providers | OPTIONAL | PATCH | COMPLETE | ACC-018 | PASS |
| CAP-019 i18n | OPTIONAL | PATCH | COMPLETE | ACC-019 | PASS |
| CAP-020 Ads/analytics | OPTIONAL | KEEP + TEST | COMPLETE | ACC-020 | PASS |
| CAP-021 Non-default Auth | KEEP-DISABLED | KEEP-DISABLED | COMPLETE | ACC-021 | PASS |
| CAP-022 Storage/R2 | OPTIONAL | PATCH | COMPLETE | ACC-022 | PASS |
| CAP-023 Turnstile | OPTIONAL | PATCH | COMPLETE | ACC-023 | PASS |
| CAP-024 UI Foundation | CORE | PATCH | COMPLETE | ACC-024 | MAJOR - F-006 |
| CAP-025 Technical SEO | CORE | PATCH | COMPLETE | ACC-025 | PASS |
| CAP-026 Optional content/UI | KEEP-DISABLED | KEEP-DISABLED | COMPLETE | ACC-026 | PASS |
| CAP-027 Security controls | CORE | PATCH | COMPLETE | ACC-027 | PASS |
| CAP-028 Logging/observability | CORE | PATCH | COMPLETE | ACC-028 | PASS |
| CAP-029 Testing/CI | CORE | PATCH | COMPLETE | ACC-029 | PASS |
| CAP-030 Build quality | CORE | PATCH | COMPLETE | ACC-030 | PASS |
| CAP-031 Release/promotion | CORE | PATCH | COMPLETE | ACC-031 | MAJOR - F-009 |
| CAP-032 Retained non-Core | KEEP-DISABLED | KEEP-DISABLED | COMPLETE | ACC-032 | PASS |

All 32 capabilities were audited. Presence of every table field is not treated as proof that its behavior is complete.

## 5. Gap Coverage

| Priority | Expected | Actual | Duplicate | Missing |
|---|---:|---:|---:|---:|
| P0 | 8 | 8 | 0 | 0 |
| P1 | 8 | 8 | 0 | 0 |
| P2 | 3 | 3 | 0 | 0 |
| Total | 19 | 19 | 0 | 0 |

Every required gap field is present. `F-007` records semantic ID errors in three rows:

- `GAP-007` names `CAP-015 Webhooks` and `CAP-016 Entitlement`; the master defines Webhooks as `CAP-016` and Entitlement as `CAP-017`.
- `GAP-010` names `CAP-016 Entitlement`; Entitlement is `CAP-017`, while provider selection is `CAP-015`.
- `GAP-019` includes Core Entitlement `CAP-017` as retained non-Core and omits optional extra AI `CAP-018`.

No gap was added, removed, reprioritized, or renamed by this audit.

## 6. Reuse Action Audit

| Action | Reported | Validated | Unsupported |
|---|---:|---:|---:|
| KEEP | 0 | 0 | 0 |
| KEEP + TEST | 4 | 4 | 0 |
| KEEP-DISABLED | 3 | 3 | 0 |
| WRAP | 1 | 1 | 0 |
| PATCH | 24 | 24 | 0 |
| REFACTOR | 0 | 0 | 0 |
| DELETE | 0 | 0 | 0 |

The high PATCH count is supported by the final audit: each PATCH capability has a concrete absent or partial target behavior and a bounded delta. No capability was classified PATCH solely because tests are absent. No `UNJUSTIFIED-ACTION` finding is recorded.

## 7. Acceptance Audit

The matrix maps all 32 capabilities one-to-one and uses observable evidence types. Most requirements are testable, including optional OFF paths. Five acceptance records depend on behavior not actually specified:

- `ACC-006` refers to a “named user/payment/invite invariant”, but the candidate never names the user or invite invariants.
- `ACC-007` tests expired sessions without specifying retained/default expiry and refresh expectations.
- `ACC-009` tests Magic Link expiry and replay without fixing the lifecycle defaults that determine those results.
- `ACC-012` requires transitions to match “the specified state table”; no such state table exists.
- `ACC-024` requests screenshots and accessibility evidence but omits the required minimum visual reference and fresh-context Fidelity Audit contract.
- `ACC-031` proves revision equality but does not identify who owns gate evidence and who is authorized to promote.

`ACC-003` asks implementation evidence to supply the variable inventory rather than making that inventory part of the design contract. The affected acceptance rows are not sufficient to freeze until their referenced behavior is defined.

## 8. Frozen Decision Audit

| Frozen decision | Candidate result |
|---|---|
| Cloudflare-first; OpenNext target | REPRESENTED |
| DEVELOPMENT/STAGING/PRODUCTION; Local is not an environment | REPRESENTED |
| PostgreSQL + Drizzle + generic `DATABASE_URL`; vendor UNPINNED | REPRESENTED |
| Provider Qualification deferred to real use | REPRESENTED |
| Auth.js + Google + Magic Link + trusted same-email identity | REPRESENTED, lifecycle incomplete under F-002/F-003 |
| Creem + Stripe one-time; server pricing; operator selection; no failover | REPRESENTED, lifecycle incomplete under F-001 |
| AI optional; OpenAI standard when enabled | REPRESENTED |
| i18n default OFF | REPRESENTED |
| Snapshot + Controlled Patch; no automatic project merge | MISSING - F-005 |
| Resend production-ready Auth email path | REPRESENTED |
| AdSense production-ready ads path | REPRESENTED |
| Account/Profile/Logout Core; account deletion OFF | REPRESENTED |
| R2 and Turnstile optional | REPRESENTED |
| UI Visual Authority minimum reference | MISSING - F-006 |
| Fresh-context Fidelity Audit | MISSING - F-006 |
| Exact verified commit STAGING to PRODUCTION | REPRESENTED, ownership incomplete under F-009 |

No direct contradiction with Frozen Authority was found. The two omissions are `MISSING`, not competing decisions.

## 9. Optional Module Audit

| Module | Role/action | Explicit enablement | Secret-free/build-safe OFF | OFF test | Result |
|---|---|---|---|---|---|
| AI/OpenAI/other AI | OPTIONAL/PATCH | Yes | Yes | ACC-018 | PASS |
| i18n | OPTIONAL/PATCH | Yes | Yes | ACC-019 | PASS |
| Ads/analytics | OPTIONAL/KEEP + TEST | Yes | Yes | ACC-020 | PASS |
| Storage/R2 | OPTIONAL/PATCH | Yes | Yes | ACC-022 | PASS |
| Turnstile | OPTIONAL/PATCH | Yes | Yes | ACC-023 | PASS |
| GitHub/Google One Tap | KEEP-DISABLED | Yes | Yes | ACC-021 | PASS |
| Credits/subscriptions/API keys/affiliate | KEEP-DISABLED | Yes | Yes | ACC-032 | PASS |
| Blog/docs/charts/editor/carousel | KEEP-DISABLED | Yes | Yes | ACC-026 | PASS |

The common OFF contract explicitly prevents unused secrets, provider initialization, network calls, route/UI exposure, scheduled work, and build failure. No optional dependency is made silently mandatory by the candidate design.

## 10. Product-Specific Leakage Audit

Result: `NO PRODUCT-SPECIFIC LEAKAGE FOUND`.

ShipAny branding, copy, assets, pricing, navigation, and legal content appear only as excluded inputs that a project must replace. The candidate does not freeze a product workflow, prompt, SEO content plan, business state machine, or legal text as Starter Authority.

## 11. Environment / Release Audit

The candidate correctly freezes three environments, Cloudflare STAGING, isolated secrets/data/provider configuration, STAGING noindex, and exact-revision promotion. Provider qualification and target-runtime smoke are deferred to real implementation/environment use, as required.

The missing configuration ownership matrix (`F-004`) prevents deterministic validation of which capability owns each secret and when it becomes required. The release flow also omits the actor/automation ownership and evidence handoff between STAGING verification and PRODUCTION promotion (`F-009`). These are design omissions; no environment provisioning is required to correct them.

## 12. Cross-Capability Audit

| Boundary | Result |
|---|---|
| Auth <-> account/users | Canonical UUID and owner authorization are defined; session defaults remain ambiguous under F-003. |
| Magic Link <-> Resend | Token ownership and delivery ownership are separated; token lifecycle defaults remain ambiguous under F-002. |
| Payments <-> orders/entitlement/DB | NOT CLOSED; state authority, transition table, event invariant, atomic side effects, and revocation sequencing are blocked under F-001. |
| AI <-> Auth/rate limit/config | Defined by CAP-018/CAP-027 and ACC-018. |
| Storage <-> Auth/security/config | Defined by CAP-022/CAP-027 and ACC-022. |
| i18n <-> routing/SEO | OFF/ON modes and canonical interaction are defined. |
| SEO <-> route ownership | Route-owned metadata and environment indexability are defined. |
| Cloudflare <-> config/release | Target and exact-revision rule are defined; config and release ownership remain incomplete under F-004/F-009. |
| Optional modules <-> environment validation | Required-if-enabled and OFF contracts are defined. |
| UI <-> loading/error/a11y | Source behaviors are defined; Visual Authority and fresh-context Fidelity Audit are missing under F-006. |

## 13. Hidden Implementation Decision Audit

| Decision area | Closed? | Finding |
|---|---|---|
| Canonical account identity | YES | One `users.uuid`, trusted same-email convergence. |
| Trusted-email rule | YES | Verified Google identity or valid Magic Link only. |
| Magic Link lifecycle defaults | NO | F-002 |
| Session expectations | NO | F-003 |
| Payment order transitions/provider event authority | NO | F-001 |
| Entitlement grant/revocation point | NO | F-001 |
| Webhook replay/idempotency ownership | NO | F-001 |
| Payment transaction boundary | NO | F-001 |
| User/invite transaction invariants | NO | F-008 |
| Optional OFF behavior | YES | Common OFF contract plus conditional acceptance. |
| Required/optional config and secret ownership | NO | F-004 |
| Cloudflare release ownership | NO | F-009 |
| Provider-specific SDK policy | YES | Forbidden in reusable domain code; qualification deferred. |
| PRODUCTION promotion revision rule | YES | Exact STAGING-verified revision. |

Open implementation-affecting ambiguity findings: `F-001`, `F-002`, `F-003`, `F-004`, `F-006`, `F-008`, `F-009`.

## 14. Findings

| Finding ID | Severity | Type | Artifact | Capability/Gap | Evidence | Problem | Implementation Risk | Required Correction | User Decision Required |
|---|---|---|---|---|---|---|---|---|---|
| F-001 | BLOCKER | UNDER-SPECIFIED | Master Spec, Gap Matrix, Acceptance Matrix | CAP-012 through CAP-017; GAP-007/GAP-010; ACC-012/016/017 | Master Spec sections 11 and 31; Acceptance Matrix ACC-012 references a nonexistent “specified state table”; AUD-WORK-040 records partial lifecycle/idempotency/entitlement | No normative order transition table, provider-event/callback authority, terminal-state precedence, durable event identity owner, atomic side-effect sequence, or entitlement grant/refund/revocation point is specified. | Implementers can produce incompatible payment histories, double/omitted grants, or different refund access behavior while claiming conformance. | Add one provider-neutral state/event table and define callback/webhook authority, allowed/ignored/rejected transitions, idempotency key ownership, transaction boundary, side-effect ordering, retry convergence, and entitlement grant/revocation semantics. | YES |
| F-002 | MAJOR | AMBIGUOUS | Master Spec, Acceptance Matrix | CAP-009; GAP-004; ACC-009 | Master Spec section 10 and CAP-009; AUD-WORK-030 confirms Magic Link is absent | Expiry is required but no default TTL/config bounds, request-to-token replacement policy, consumption point, or behavior for multiple outstanding links is defined. | Security and user behavior differ materially depending on implementation choices; acceptance cannot assert expiry/replay deterministically. | Define the Magic Link lifecycle state/TTL defaults, issuance/replacement policy, atomic consumption point, replay behavior, and throttling ownership while leaving storage shape local. | YES |
| F-003 | MAJOR | AMBIGUOUS | Master Spec, Acceptance Matrix | CAP-007; ACC-007 | AUD-WORK-030 says exact JWT/session expiry, refresh, cookie, and persistence defaults are unknown; candidate only says retain callbacks and test expiry | The target session lifetime, refresh/update expectation, cookie/security expectation, and invalidation boundary are not frozen or explicitly delegated to retained Auth.js defaults. | Auth and logout behavior can vary materially and tests have no target values. | Either freeze explicit session expectations or explicitly freeze retained pinned Auth.js defaults plus the security/runtime properties that must be verified. | YES |
| F-004 | MAJOR | UNDER-SPECIFIED | Master Spec, Gap Matrix, Acceptance Matrix | CAP-003; GAP-002; ACC-003 | GAP-002 requires a complete variable inventory; Master Spec section 21 defines classes only; ACC-003 defers inventory to implementation evidence | No normative variable/flag/binding ownership matrix identifies canonical existing names, capability owner, public/server class, required condition, default, or environment scope. | Implementers must invent enable flags and secret ownership; optional OFF behavior and environment isolation can diverge. | Add a redacted configuration contract mapping each logical/current variable and binding to owner, visibility, required-if rule, default/OFF semantics, and DEVELOPMENT/STAGING/PRODUCTION scope. | NO |
| F-005 | MAJOR | MISSING | Master Spec | Cross-cutting reuse/upgrade policy | AUDIT-001 lines 276-281 freezes `Snapshot + Controlled Patch` and `NO automatic merge into projects`; candidate has no such rule | A frozen upgrade policy is absent from goals, reuse policy, release policy, and do-not-do rules. | Later implementation or maintenance may introduce an automatic merge/update workflow contrary to Frozen Authority. | Add the exact Snapshot + Controlled Patch policy and prohibit automatic merges into generated projects. | NO |
| F-006 | MAJOR | MISSING | Master Spec, Acceptance Matrix | CAP-024; GAP-015; ACC-024 | KSS-STS020-AUDIT-R1 requires a UI Visual Authority minimum reference and fresh-context Fidelity Audit; candidate provides only focused visual smoke | Neither the minimum visual-reference artifact contract nor an independent fresh-context Fidelity Audit procedure/gate is defined. | UI implementation can self-approve against screenshots without a stable reference or independent fidelity review. | Planner must define the minimum approved visual-reference set, ownership/versioning, routes/viewports/states, tolerance/evidence, and fresh-context Fidelity Audit pass/block rule; then trace it into CAP-024/ACC-024/release gates. | YES |
| F-007 | MAJOR | INCONSISTENT | Gap Closure Matrix | GAP-007, GAP-010, GAP-019 | Master capability table defines CAP-015 provider switch, CAP-016 webhooks, CAP-017 entitlement, CAP-018 AI; Gap rows attach different names/roles to those IDs | Three gap rows map to incorrect Capability IDs, including classifying Core Entitlement as retained non-Core. | Traceability and future task routing can target the wrong capability. | Correct mappings without renumbering gaps: GAP-007 to Webhooks CAP-016/Entitlement CAP-017 and relevant atomicity; GAP-010 to CAP-012 through CAP-017 as applicable; GAP-019 to actual retained non-Core IDs including CAP-018 and excluding Core CAP-017. | NO |
| F-008 | MAJOR | UNTESTABLE | Master Spec, Acceptance Matrix | CAP-006; ACC-006 | CAP-006 says “approved user/payment/invite invariants”; ACC-006 says “named” invariants, but no user/invite invariants are named | Payment atomicity is separately addressed, while user and invite transaction ownership, dependent writes, uniqueness result, and retry target remain unspecified. | Transaction patches and tests can target different operations or add unnecessary broad transactions. | Enumerate each evidenced user/invite multi-write invariant, its transaction/constraint owner, rollback result, concurrency result, and acceptance case; omit any invariant not supported by audit evidence. | NO |
| F-009 | MAJOR | AMBIGUOUS | Master Spec, Acceptance Matrix | CAP-031; GAP-008; ACC-031 | Candidate defines exact revision equality and CI workflow but no release evidence owner or promotion authority | It is unspecified which automation/role records gate evidence, who may approve/promote, and whether production deployment consumes the verified immutable artifact or merely rebuilds the same source revision. | A release can satisfy commit equality while bypassing gate ownership or changing build artifacts/configuration. | Define CI versus operator ownership, immutable revision/artifact identity, required approval/evidence handoff, failure stop, and configuration-only rollback authority without adding an enterprise release platform. | YES |

Finding totals: `BLOCKER=1`, `MAJOR=8`, `MINOR=0`, `NOTE=0`.

## 15. Required Corrections

Corrections must be made in a new bounded design-authoring/correction task or by explicit Planner authority. They are not application work and require no production/simulated-production validation.

1. Resolve `F-001` before any other payment acceptance can be treated as normative.
2. Freeze Magic Link and session lifecycle expectations for `F-002` and `F-003` without forcing an Auth.js Adapter migration.
3. Add the concrete redacted configuration ownership matrix required by `F-004`.
4. Restore the exact frozen Snapshot + Controlled Patch rule for `F-005`.
5. Supply Planner Authority for the UI reference/Fidelity Audit contract in `F-006`.
6. Mechanically repair the three capability mappings in `F-007` after design corrections are approved.
7. Name only repository-evidenced user/invite transaction invariants for `F-008`.
8. Define the minimal release ownership/artifact contract for `F-009`.
9. Update affected acceptance and traceability rows after the normative master/gap corrections, then rerun STS-020 in a fresh context.

User/Planner decisions are required for `F-001`, `F-002`, `F-003`, `F-006`, and `F-009`. Mechanical or evidence-derived correction is sufficient for `F-004`, `F-005`, `F-007`, and `F-008`.

## 16. Freeze Recommendation

`NOT READY FOR STS-030`.

Audit result: `FAIL — CORRECTION REQUIRED` under the deterministic rule because one `BLOCKER` and eight unresolved `MAJOR` findings remain. `STS-020` must be `BLOCKED`; `STS-030` must remain `NOT_READY`. The candidate must not be frozen until all findings are corrected and independently re-audited.

## 17. Traceability

| Audit conclusion | Candidate evidence | Repository Authority/evidence | Finding |
|---|---|---|---|
| Structural capability/acceptance coverage passes | Master section 27; Acceptance Matrix | `KSS-DS-AUTH-R1` | None |
| Gap count/priority coverage passes | Gap Matrix rows and Count Check | `AUD-FINAL-02` | F-007 affects mapping, not count |
| Reuse actions are supported | Master section 27 | `AUD-FINAL-01`, `AUD-FINAL-08`, work audits | None |
| Payment behavior is not freeze-ready | Master sections 11/31; ACC-012/016/017 | `AUD-WORK-040`, GAP-007/GAP-010 | F-001 |
| Auth lifecycle is not freeze-ready | Master section 10; ACC-007/009 | `AUD-WORK-030`, GAP-004 | F-002, F-003 |
| Configuration contract is incomplete | Master section 21; ACC-003 | `AUD-WORK-010`, GAP-002 | F-004 |
| Frozen upgrade policy omitted | No candidate occurrence | `AUDIT-001` section 6 | F-005 |
| UI review contract omitted | Master section 18; ACC-024 | `KSS-STS020-AUDIT-R1`, `AUD-FINAL-04` | F-006 |
| DB non-payment atomicity is unnamed | CAP-006; ACC-006 | `AUD-WORK-020` | F-008 |
| Release ownership is incomplete | Master sections 24/25; ACC-031 | `AUD-FINAL-05`, GAP-008 | F-009 |
| No product leakage | Master sections 18/30 | `AUD-FINAL-04`, `AUD-FINAL-07` | None |
