# Kyd SaaS Starter Detailed Spec Fresh-Context Re-Audit

> Task: `STS-023`  
> Audit Authority: `KSS-STS020-AUDIT-R1`  
> Resolution Authority: `KSS-STS021A-RESOLUTION-R2`  
> Candidate: `KSS-DS-SPEC-R1`, `KSS-DS-GAPS-R1`, `KSS-DS-ACCEPT-R1`  
> Result: `FAIL — CORRECTION REQUIRED`

## 1. Executive Result

The corrected artifacts retain structural integrity and capability-first reuse discipline, but they are not safe to freeze. The re-audit independently confirmed 32 unique capabilities, 32 unique acceptance records, and 19 unique gaps with `P0=8`, `P1=8`, and `P2=3`. No unproven abstraction, `REFACTOR`, `DELETE`, product-specific leakage, or Frozen Authority conflict was found.

Original findings `F-002`, `F-005`, `F-007`, `F-008`, and `F-009` are `CLOSED`. Findings `F-001`, `F-003`, `F-004`, and `F-006` remain `PARTIAL`. Payment terminal behavior still permits an implementation choice between ignore and reject; the session contract does not assign custom product overrides to Product-Specific Design; the configuration matrix omits a canonical credential/injection contract for the retained Replicate provider; and the Fidelity Audit uses an undefined “material mismatch” threshold.

The full ambiguity sweep also found one new `MAJOR` cross-capability inconsistency and one `MINOR` acceptance omission. Environment-specific public configuration and exact immutable no-rebuild promotion lack a defined runtime/artifact boundary (`R-001`). Technical SEO requires icons/structured data where applicable but its acceptance row does not verify them (`R-002`).

Under the deterministic result rule, unresolved original `MAJOR` findings and `R-001` require `FAIL — CORRECTION REQUIRED`. `STS-030` is not eligible.

## 2. Inputs / Authority

Mandatory Authority:

- `docs/starter/KYD_SAAS_STARTER_STS020_AUDIT_AUTHORITY.md` (`KSS-STS020-AUDIT-R1`)
- `docs/starter/KYD_SAAS_STARTER_STS021A_RESOLUTION_DECISIONS.md` (`KSS-STS021A-RESOLUTION-R2`)
- `docs/starter/KYD_SAAS_STARTER_DETAILED_SPEC_AUTHORING_AUTHORITY.md` (`KSS-DS-AUTH-R1`)
- `docs/decisions/KYD_CAPABILITY_FIRST_MULTI_TEMPLATE_REUSE_POLICY.md` (`KPS-CAP-REUSE-R1`)
- `docs/decisions/A-001_POSTGRES_PROVIDER_POLICY.md` (`DEC-A001-POLICY`)
- `docs/audit/SA_TEMPLATE_AUDIT_AUTHORITY.md` (`AUDIT-001`)

Correction chain and evidence:

- `docs/starter/KYD_SAAS_STARTER_DETAILED_SPEC_AUDIT.md`
- `docs/starter/KYD_SAAS_STARTER_STS020_FINDINGS_RESOLUTION_PACKET.md`
- `docs/starter/KYD_SAAS_STARTER_STS020_EXISTING_IMPLEMENTATION_MAPPING.md`
- `docs/starter/KYD_SAAS_STARTER_STS022_CORRECTION_AUTHORITY.md`
- `docs/audit/00_AUDIT_SUMMARY.md`
- `docs/audit/02_REUSE_GAP_MATRIX.md`
- `docs/audit/04_UI_FOUNDATION_AUDIT.md`
- `docs/audit/05_TEST_AND_RELEASE_AUDIT.md`
- finding-related work evidence registered as `AUD-WORK-010`, `AUD-WORK-020`, `AUD-WORK-030`, `AUD-WORK-040`, `AUD-WORK-050`, `AUD-WORK-060`, and `AUD-WORK-070`

Candidate start hashes:

| Artifact | SHA-256 |
|---|---|
| Detailed Spec | `fbcee94fa9a27449bd2b72fe21db00f1e091d01fa8c11ee874acd0a82e6adee7` |
| Gap Closure Matrix | `de356d12e1cab06f513e8bf52944dd870813c61d8503205d291ca8d72d54ab24` |
| Acceptance Matrix | `e2de48bf7ca0e81686e81cfd7d3d72cea085226b9a010a83def2d221fbe08d75` |

## 3. Original Finding Closure

| Finding ID | Original severity/type | Original problem | Required resolution | Corrected location | Closure | Evidence | New ambiguity introduced |
|---|---|---|---|---|---|---|---|
| F-001 | BLOCKER / UNDER-SPECIFIED | Payment authority, state transitions, idempotency, transaction sequence, and entitlement were not normative. | Preserve existing verified entry paths and shared mutation; define exact state/event, idempotency, atomicity, retry, and access semantics. | Detailed Spec section 11 and CAP-012..017; GAP-007/GAP-010; ACC-012..017 | PARTIAL | Architecture, state table, durable identity, transaction, retry, and entitlement are present, but terminal handling says “ignore or reject”. | YES |
| F-002 | MAJOR / AMBIGUOUS | Magic Link TTL, active-token replacement, consumption, replay, and throttling ownership were open. | Freeze one active credential, initial/sliding 15 minutes, single use, post-expiry creation, delayed-email behavior, and separate throttling. | Detailed Spec sections 10/22 and CAP-009; GAP-004; ACC-009 | CLOSED | All frozen lifecycle states and observable timing/replay cases are explicit and consistent. | NO |
| F-003 | MAJOR / AMBIGUOUS | Session lifetime/update/cookie behavior was neither frozen nor delegated. | Retain pinned Auth.js defaults, test resolved properties, invent no numeric policy, and keep product overrides Product-Specific. | Detailed Spec section 10 and CAP-007; ACC-007 | PARTIAL | Pinned defaults and resolved-property tests are explicit; ownership of a future custom product override is not. | NO |
| F-004 | MAJOR / UNDER-SPECIFIED | No canonical redacted variable/binding ownership matrix existed. | Map all logical/current config to owner, name/injection, visibility, required-if/default/OFF rule, and environment scope. | Detailed Spec section 21; GAP-002; ACC-003 | PARTIAL | The matrix is broad and preserves existing names, but the retained Replicate path has no named credential or injection contract. | NO |
| F-005 | MAJOR / MISSING | Snapshot + Controlled Patch and no-auto-merge were omitted. | Restore the exact policy and prohibit automatic project merges. | Detailed Spec sections 5 and 30 | CLOSED | Exact policy and prohibition are present. | NO |
| F-006 | MAJOR / MISSING | Visual reference ownership and fresh-context Fidelity Audit were absent. | Define two layers, minimum references, ownership/versioning/routes/viewports/states, tolerance/evidence, and independent pass/block behavior. | Detailed Spec section 18, release gates, CAP-024; GAP-015; ACC-024 | PARTIAL | Two layers, ownership, reference scope, evidence, reviewer independence, and block behavior exist; “material mismatch” has no deterministic tolerance or adjudication rule. | YES |
| F-007 | MAJOR / INCONSISTENT | GAP-007/GAP-010/GAP-019 used incorrect Capability IDs. | Repair exact mappings without changing IDs/counts. | GAP-007, GAP-010, GAP-019 | CLOSED | Mappings match CAP-006/CAP-012..018/CAP-021/CAP-026/CAP-032 exactly as frozen. | NO |
| F-008 | MAJOR / UNTESTABLE | User/onboarding and invite/affiliate transaction invariants were unnamed. | Name only evidenced writes, enable conditions, rollback/concurrency outcomes, and tests; reference payment separately. | Detailed Spec section 9 and CAP-006; ACC-006; GAP-007 dependency | CLOSED | Both exact non-payment invariants and OFF/ON/failure/concurrency acceptance are present; payment remains in section 11/ACC-016. | NO |
| F-009 | MAJOR / AMBIGUOUS | CI ownership, operator authority, immutable artifact handoff, and no-rebuild behavior were open. | CI eligibility, explicit operator approval, exact immutable commit/artifact, no rebuild/mutation, and target-vs-current distinction. | Detailed Spec sections 7/8/24/25 and CAP-031; GAP-008; ACC-031 | CLOSED | Policy, ownership, evidence handoff, identity verification, and current implementation absence are explicit. | NO |

## 4. F-001 Closure

### Closed portions

- Existing Stripe/Creem checkout, server-verified callback, signed webhook, `handleCheckoutSession`, and shared `updateOrder` path are explicitly preserved.
- Browser redirects are not payment authority.
- The state table names `created -> paid/failed/cancelled` and `paid -> refunded` plus entitlement outcomes.
- Provider event ID, or callback session identity plus normalized outcome, owns durable idempotency identity.
- Idempotency claim, conditional order transition, Core entitlement, and enabled credit/affiliate effects share one transaction; failure rolls back and retry converges.
- No new transition service, provider framework, distributed transaction platform, or schema rewrite is frozen.
- ACC-012 through ACC-017 provide state, provider, replay, concurrency, rollback, side-effect, and authorization observations.

### Residual ambiguity

The terminal-state row says an incompatible or stale provider fact is “ignore or reject and record” while ACC-012 refers to a “specified no-op/reconciliation rule”. Ignore and reject produce different endpoint/retry behavior, and the spec does not define which states are terminal or the HTTP/retry outcome. The implementer must still choose a material replay/failure policy.

Result: `PARTIAL`.

## 5. F-002 Closure

The Detailed Spec, GAP-004, CAP-009, and ACC-009 consistently require:

- one active logical credential per normalized email;
- initial validity of 15 minutes;
- no rotation, invalidation, or second credential on an accepted active-window re-request;
- resend of the current link and `expires_at = latest accepted request + 15 minutes`;
- delayed earlier email validity in the same active lifecycle;
- immediate atomic single-use consumption and permanent replay rejection;
- permanent expiry rejection and a new credential on the first accepted post-expiry request;
- throttling independent of rotation/invalidation;
- controlled-time acceptance evidence for every lifecycle case.

No contradictory token policy was found. Encoding/storage remains implementation-neutral within fixed observable semantics.

Result: `CLOSED`.

## 6. F-003 Closure

The existing Auth.js callback/JWT/session architecture and pinned defaults are retained. No `maxAge`, `updateAge`, or other numeric policy is introduced. ACC-007 requires recording and testing resolved lifetime/update/cookie properties, UUID payload, protected access, expiry, and logout. The capability's overall primary action remains `PATCH` because trusted-identity work is still required, while the mapped session sub-capability is retained and tested.

The corrected design does not explicitly state that any later custom session lifetime/update override belongs to Product-Specific Design and must not silently alter the Starter default. That ownership boundary is a stated STS-023 criterion and remains implementation-affecting.

Result: `PARTIAL`.

## 7. F-004/F-005/F-007/F-008 Closure

### F-004

Section 21 supplies capability owner, canonical/current names, variable/binding kind, public/server classification, required condition/default/OFF behavior, and environment scope. It includes every direct `process.env` name recorded by AUD-WORK-010 and bounded new enable/policy settings.

AUD-WORK-050 and CAP-018 retain Replicate as an additional AI provider. The matrix lists OpenAI, OpenRouter, SiliconFlow, and Kling settings but does not name a Replicate credential or define an explicit provider-construction injection for it. “Selected provider key required” does not tell the implementer which canonical setting or injection boundary to validate. Therefore the “every logical setting” requirement is not complete.

Result: `PARTIAL`.

### F-005

Sections 5 and 30 state `Snapshot + Controlled Patch`, `NO automatic merge into projects`, project snapshot ownership, reviewed bounded updates, and an explicit prohibition on automatic merge.

Result: `CLOSED`.

### F-007

- GAP-007 maps CAP-006, CAP-016, CAP-017, and enabled CAP-032 side effects.
- GAP-010 maps CAP-012 through CAP-017 with correct names.
- GAP-019 maps CAP-018 additional AI, CAP-021, CAP-026, and CAP-032 and explicitly excludes Core CAP-017.

No ID, priority, action, or count changed.

Result: `CLOSED`.

### F-008

Section 9 and ACC-006 define the exact user-plus-initial-credit and invited-by-plus-affiliate invariants, OFF behavior, atomic rollback, concurrent uniqueness/result, and invalid invite cases. Payment atomicity is referenced through section 11/ACC-016 rather than duplicated. No generic transaction framework is authorized.

Result: `CLOSED`.

## 8. F-006 Closure

The corrected design explicitly separates:

- Layer 1, Starter Visual Foundation Authority: product-neutral tokens, primitives, shells, forms/tables, responsive/a11y/loading/error behavior, asset conventions, and neutral references.
- Layer 2, Product Visual Authority: Approved Screens, Actual Assets, interactions/states, responsive product references, branding, content, pricing, navigation, legal and visual semantics.

ShipAny content remains replaceable evidence and is excluded from Starter Authority. A fresh-context reviewer must be independent, compare only the applicable layer, record screenshots/interactions/responsive/a11y evidence, and block unexplained mismatch. No UI implementation rewrite is implied.

The original finding also required a tolerance/pass rule. “Unexplained material mismatch” is not mechanically defined: the manifest has no required tolerance category, waiver owner, or adjudication/evidence rule for deciding materiality. Two reviewers can reach different release outcomes while both claim conformance.

Result: `PARTIAL`.

## 9. F-009 Closure

The corrected contract makes CI responsible for eligibility evidence, requires explicit operator approval, binds that approval to the STAGING evidence bundle, promotes the exact immutable commit/artifact, forbids rebuild/code mutation, verifies production identity, and records migration/recovery readiness. It explicitly says Cloudflare/OpenNext, CI, STAGING, and promotion are currently absent and future bounded `PATCH` work. Vercel/Docker remain disabled alternates.

Result: `CLOSED`.

## 10. Capability-First Reuse Audit

Result: `PASS`.

| Check | Result | Evidence |
|---|---|---|
| Existing implementation mapped before redesign | PASS | STS-021A mapping paths and all current-state cells |
| Compatible implementation preserved | PASS | Existing framework, DB, Auth.js session, payment routes/services/shared mutation, UI foundation, optional modules, Vercel/Docker retained |
| Every PATCH has demonstrated bounded delta | PASS | GAP-001 through GAP-017 plus corresponding Audit work evidence |
| KEEP/KEEP + TEST/KEEP-DISABLED/WRAP used before larger action | PASS | Distribution remains `0/4/3/1/24/0/0`; no unsupported action found |
| New abstraction from ambiguity | PASS | None introduced; payment and optional-provider framework replacements are prohibited |
| REFACTOR proof | PASS | No REFACTOR |
| DELETE review | PASS | No DELETE |

## 11. Capability / Gap Integrity

### Capability coverage

| Capability range | Schema/count | Semantic result |
|---|---|---|
| CAP-001..005 | 5 unique, complete fields | CAP-003 PARTIAL under F-004/R-001; others PASS |
| CAP-006..011 | 6 unique, complete fields | CAP-007 PARTIAL under F-003; CAP-009 CLOSED; others PASS |
| CAP-012..017 | 6 unique, complete fields | PARTIAL under F-001 terminal policy; architecture/actions remain supported |
| CAP-018..023 | 6 unique, complete fields | CAP-018 config PARTIAL under F-004; OFF contracts PASS |
| CAP-024..026 | 3 unique, complete fields | CAP-024 PARTIAL under F-006; CAP-025 MINOR acceptance omission R-002 |
| CAP-027..032 | 6 unique, complete fields | CAP-031 affected by R-001; others PASS |
| Total | 32 expected / 32 actual / 32 unique | No unsupported action, REFACTOR, or DELETE |

### Gap coverage

| Priority | Expected | Actual | Missing | Duplicate |
|---|---:|---:|---:|---:|
| P0 | 8 | 8 | 0 | 0 |
| P1 | 8 | 8 | 0 | 0 |
| P2 | 3 | 3 | 0 | 0 |
| Total | 19 | 19 | 0 | 0 |

All 19 rows contain source, capability, evidence, target, action, allowed/forbidden delta, touch area, dependencies, acceptance, verification, and design status.

## 12. Acceptance Integrity

The 32 Acceptance IDs map one-to-one to CAP-001 through CAP-032. Most requirements are concrete and observable, including optional OFF/ON behavior, controlled-time Magic Link cases, DB failure/concurrency cases, payment signature/idempotency/transaction counts, UI reviewer evidence, and immutable release identity.

Material exceptions:

- ACC-012 cannot assert one result for stale/incompatible terminal facts while section 11 allows ignore or reject (`F-001`).
- ACC-003 cannot validate the retained Replicate path against a canonical credential/injection row (`F-004`).
- ACC-024 has no deterministic materiality/tolerance rule for a Fidelity Audit (`F-006`).
- ACC-003 and ACC-031 do not resolve how environment-specific public values coexist with one no-rebuild artifact (`R-001`).
- ACC-025 does not verify icons or route-applicable structured data required by section 19 (`R-002`).

## 13. Frozen Decision Integrity

| Frozen decision | Result |
|---|---|
| Cloudflare-first / OpenNext target | REPRESENTED |
| DEVELOPMENT/STAGING/PRODUCTION; Local is not an environment | REPRESENTED |
| PostgreSQL + Drizzle + generic DATABASE_URL; vendor UNPINNED; deferred real-use qualification | REPRESENTED |
| Auth.js + Google + Magic Link + trusted same-email canonical UUID | REPRESENTED |
| Stripe + Creem one-time; server pricing; operator switch; no request failover | REPRESENTED |
| AI optional; OpenAI standard when ON | REPRESENTED |
| i18n OFF | REPRESENTED |
| Snapshot + Controlled Patch; no automatic merge | REPRESENTED |
| Resend Auth path / AdSense ads path | REPRESENTED |
| Account/Profile/Logout Core; deletion OFF | REPRESENTED |
| R2/Turnstile optional | REPRESENTED |
| A-002 keep list and two Visual Authority layers | REPRESENTED |
| Fresh-context Fidelity Audit | REPRESENTED but tolerance remains under F-006 |
| Exact immutable STAGING-to-PRODUCTION promotion | REPRESENTED but public-config boundary remains under R-001 |

Frozen Authority conflicts: `0`.

## 14. Optional Module Integrity

| Module | Default/action | OFF contract | ON/config/test contract | Result |
|---|---|---|---|---|
| AI/OpenAI/additional AI | OFF / PATCH | No route, key, initialization, UI, or call | Auth, allowlist, limits, redaction, conditional smoke | PARTIAL only for Replicate ON config under F-004 |
| i18n | OFF / PATCH | No forced locale routing or unused config | Locale/fallback/canonical dual-mode tests | PASS |
| Ads/analytics | OFF / KEEP + TEST | Empty config emits no script/request | Independent provider/consent/pageview smoke | PASS |
| Storage/R2 | OFF / PATCH | No secret or reachable route | Auth/key/type/size/privacy and Worker smoke | PASS |
| Turnstile | OFF / PATCH | No secret/widget/request | Named-route client/server verification | PASS |
| GitHub/One Tap | OFF / KEEP-DISABLED | No provider registration/UI | Conditional trust/session tests | PASS |
| Credits/subscriptions/affiliate/API keys | OFF / KEEP-DISABLED | No route/job/side effect/config | Inherit owning domain gates | PASS |
| Blog/docs/charts/editor | OFF / KEEP-DISABLED | No route/menu requirement | Conditional render/navigation/security | PASS |

## 15. Product-Specific Leakage

Result: `NO`.

The Starter excludes ShipAny branding, copy, imagery, pricing, navigation, links, legal text, and product semantics. It does not freeze product workflow, AI prompts, SEO keyword/content strategy, visual identity, pricing data, or business state machine. Product Visual Authority owns those inputs separately.

## 16. New Ambiguity Sweep

The sweep rechecked canonical identity, Magic Link, Auth session, payment states, entitlement, idempotency, transactions, optional OFF behavior, configuration ownership, provider coupling, Visual Authority, release promotion, security, testing, and all 32 capability rows.

Closed or bounded areas include canonical UUID/trusted-email behavior, the Magic Link lifecycle, non-payment transaction invariants, payment transaction membership, optional OFF behavior, provider SDK prohibition, operator payment selection, release approval/identity, and minimum test/security gates.

Open implementation-affecting items:

1. `F-001`: ignore versus reject and terminal/retry behavior.
2. `F-003`: ownership of custom product session overrides.
3. `F-004`: canonical credential/injection for retained Replicate.
4. `F-006`: Fidelity Audit materiality/tolerance adjudication.
5. `R-001`: public per-environment configuration versus immutable no-rebuild artifact promotion.

## 17. New Findings

| Finding ID | Severity | Type | Artifact | Capability/Gap | Evidence | Problem | Implementation Risk | Required Correction | User Decision Required |
|---|---|---|---|---|---|---|---|---|---|
| R-001 | MAJOR | INCONSISTENT | Detailed Spec, Gap Matrix, Acceptance Matrix | CAP-003/CAP-031; GAP-002/GAP-008; ACC-003/ACC-031 | Section 21 classifies multiple `NEXT_PUBLIC_*` values as distinct per environment; sections 7/24/25 require the identical immutable build artifact and prohibit rebuild; AUD-WORK-010 records direct client/component reads | The spec does not state which public values are artifact-stable versus runtime-injected, or define the runtime public-config boundary. Separate STAGING/PRODUCTION values and identical no-rebuild artifact promotion can therefore drive incompatible implementation choices. | One implementation rebuilds per environment and violates F-009; another shares STAGING public values with PRODUCTION; another invents an unapproved runtime config subsystem. | Define a bounded public-config contract: classify artifact-stable values, define server/runtime injection for environment-specific public values, and add identity/config acceptance without weakening no-rebuild promotion. | NO |
| R-002 | MINOR | UNTESTABLE | Detailed Spec, Acceptance Matrix | CAP-025; ACC-025 | Section 19 requires icons and structured data where routes have stable facts; ACC-025 verifies base/canonical/sitemap/robots/social metadata only | Part of the technical SEO target has no observable acceptance. | Implementations can omit required icons/structured data while passing ACC-025. | Add route-applicable icon and structured-data assertions to ACC-025 and expected evidence; do not add product keyword/content strategy. | NO |

New finding totals: `BLOCKER=0`, `MAJOR=1`, `MINOR=1`, `NOTE=0`.

No new abstraction is introduced by the corrected Spec. New abstraction count: `0`.

## 18. Freeze Recommendation

`NOT READY FOR STS-030`.

Result: `FAIL — CORRECTION REQUIRED` because `F-001`, `F-003`, `F-004`, and `F-006` are not fully closed and `R-001` is an unresolved `MAJOR`. `R-002` is a bounded mechanical acceptance correction but cannot offset the unresolved major issues.

STS-023 must not become `VERIFIED`. STS-030 must remain `NOT_READY` and must not execute.

## 19. Traceability

| Re-audit conclusion | Candidate locations | Authority/evidence | Finding |
|---|---|---|---|
| Payment architecture preserved; terminal policy still ambiguous | Sections 11/27; GAP-007/010; ACC-012/016/017 | `KSS-STS021A-RESOLUTION-R2`, `AUD-WORK-040` | F-001 |
| Magic Link lifecycle fully closed | Sections 10/22; CAP-009; GAP-004; ACC-009 | `KSS-STS021A-RESOLUTION-R2`, `AUD-WORK-030` | F-002 CLOSED |
| Pinned Auth.js default delegation present; product override ownership absent | Section 10; CAP-007; ACC-007 | `KSS-STS021A-RESOLUTION-R2`, `AUD-WORK-030` | F-003 |
| Config matrix broad but retained Replicate ON contract incomplete | Section 21; GAP-002; ACC-003 | `KSS-STS021A-MAPPING-RESULT-R1`, `AUD-WORK-010/050` | F-004 |
| Upgrade policy restored | Sections 5/30 | `AUDIT-001` | F-005 CLOSED |
| Two visual layers present; deterministic tolerance absent | Section 18/25; CAP-024; GAP-015; ACC-024 | `KSS-STS021A-RESOLUTION-R2`, `AUD-FINAL-04` | F-006 |
| Gap capability mappings repaired | GAP-007/010/019 | Master CAP registry | F-007 CLOSED |
| Exact user/invite invariants named | Sections 9/27; ACC-006 | `AUD-WORK-020`, mapping result | F-008 CLOSED |
| Operator-approved immutable promotion closed | Sections 7/8/24/25; CAP-031; GAP-008; ACC-031 | `KSS-STS021A-RESOLUTION-R2`, `AUD-FINAL-05` | F-009 CLOSED |
| Public config/artifact boundary unresolved | Sections 7/21/24/25; GAP-002/008; ACC-003/031 | `AUD-WORK-010`, `AUD-FINAL-05` | R-001 |
| SEO acceptance omits two target elements | Section 19; CAP-025; ACC-025 | `AUD-WORK-050` | R-002 |
