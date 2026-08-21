# Kyd SaaS Starter STS-020 Findings Resolution Packet

> Task: `STS-021`  
> Authority: `KSS-STS021-RESOLUTION-R1`  
> Source audit: `KSS-STS020-AUDIT-RESULT-R1`  
> Status: `DECISION PACKET COMPLETE - NO CANDIDATE CORRECTIONS APPLIED`

## 1. Executive Summary

This packet converts all nine `STS-020` findings into deterministic later-resolution paths without editing the candidate Detailed Spec, Gap Closure Matrix, or Acceptance Matrix.

Classification result:

- `R1 — MECHANICAL CORRECTION`: `F-004`, `F-005`, `F-007`, `F-008`
- `R2 — PLANNER DECISION`: none
- `R3 — USER DECISION`: `F-001`, `F-002`, `F-003`, `F-006`, `F-009`
- `R4 — AUTHORITY CONFLICT`: none
- `R5 — EVIDENCE GAP`: none

No provider, Cloudflare, Hyperdrive, database, payment, email, or other external provisioning is needed to resolve these design findings. `STS-030` remains `NOT_READY` until the user decisions are recorded, a separately authorized correction task updates the three candidate artifacts, and a fresh-context `STS-020` re-audit passes.

## 2. STS-020 Result

| Item | Result |
|---|---|
| Audit result | `FAIL — CORRECTION REQUIRED` |
| Runtime status | `BLOCKED` |
| Findings | `BLOCKER=1`, `MAJOR=8`, `MINOR=0`, `NOTE=0` |
| Capability coverage | 32 expected / 32 actual / 32 audited |
| Gap coverage | P0=8 / P1=8 / P2=3 / total=19 / duplicate=0 / missing=0 |
| Unsupported reuse actions | 0 |
| Product-specific leakage | No |
| Frozen Authority conflicts | 0 |
| Freeze recommendation | `NOT READY FOR STS-030` |

The authoritative finding text remains in `docs/starter/KYD_SAAS_STARTER_DETAILED_SPEC_AUDIT.md`.

## 3. Finding Inventory

| Finding ID | Severity | Finding Type | Affected Artifact | Capability / Gap / Acceptance | Short Problem | Resolution Class | User Decision Required | Correction Dependency |
|---|---|---|---|---|---|---|---|---|
| F-001 | BLOCKER | UNDER-SPECIFIED | Master, Gap, Acceptance | CAP-012..017; GAP-007/010; ACC-012/016/017 | Payment state authority, idempotency, atomic side effects, and entitlement grant/revocation are not normative. | R3 | YES | First-order decision; F-007/F-008 consistency work and payment corrections consume it. |
| F-002 | MAJOR | AMBIGUOUS | Master, Acceptance | CAP-009; GAP-004; ACC-009 | Magic Link TTL, outstanding-token policy, consumption point, and throttling ownership are open. | R3 | YES | Independent; F-004 config inventory consumes the selected defaults. |
| F-003 | MAJOR | AMBIGUOUS | Master, Acceptance | CAP-007; ACC-007 | Session lifetime, refresh, cookie expectations, and invalidation boundary are open. | R3 | YES | Independent; F-004 config inventory consumes any explicit settings. |
| F-004 | MAJOR | UNDER-SPECIFIED | Master, Gap, Acceptance | CAP-003; GAP-002; ACC-003 | The redacted variable/binding ownership matrix is absent. | R1 | NO | Apply after F-002/F-003/F-009 so their selected settings/ownership are represented. |
| F-005 | MAJOR | MISSING | Master | Reuse/upgrade policy | Frozen Snapshot + Controlled Patch and no-auto-merge policy is omitted. | R1 | NO | Independent. |
| F-006 | MAJOR | MISSING | Master, Acceptance | CAP-024; GAP-015; ACC-024 | Minimum UI Visual Authority and fresh-context Fidelity Audit contract are absent. | R3 | YES | Independent; selected model drives UI/acceptance/release corrections. |
| F-007 | MAJOR | INCONSISTENT | Gap Matrix | GAP-007/010/019 | Three rows attach incorrect names/roles to Capability IDs. | R1 | NO | ID mapping is independent; final payment wording follows F-001. |
| F-008 | MAJOR | UNTESTABLE | Master, Acceptance | CAP-006; ACC-006 | User/invite multi-write invariants are unnamed. | R1 | NO | Evidence-derived; integrate after F-001 so payment atomicity is not duplicated. |
| F-009 | MAJOR | AMBIGUOUS | Master, Acceptance | CAP-031; GAP-008; ACC-031 | Release evidence owner, promotion authority, and immutable artifact rule are open. | R3 | YES | Independent; F-004 records resulting release bindings/ownership. |

## 4. Resolution Classification

| Finding | Class | Classification basis |
|---|---|---|
| F-001 | R3 — USER DECISION | Repository evidence proves the gap but does not choose callback/webhook mutation authority or terminal-state policy. |
| F-002 | R3 — USER DECISION | No current Magic Link exists; repository evidence cannot choose TTL or outstanding-token policy. |
| F-003 | R3 — USER DECISION | Current Auth.js options are implicit; retaining defaults versus freezing explicit Starter values changes behavior. |
| F-004 | R1 — MECHANICAL CORRECTION | Source/env audit already supplies names and ownership evidence; the missing work is a redacted deterministic inventory. |
| F-005 | R1 — MECHANICAL CORRECTION | `AUDIT-001` freezes exact wording; no choice remains. |
| F-006 | R3 — USER DECISION | A-002 excludes product visual design, so the scope of Starter versus project visual references needs explicit authority. |
| F-007 | R1 — MECHANICAL CORRECTION | The master table already defines the canonical Capability IDs. |
| F-008 | R1 — MECHANICAL CORRECTION | `AUD-WORK-020` names the exact user and invite write sequences; no new invariant should be invented. |
| F-009 | R3 — USER DECISION | Frozen Authority requires exact revision promotion but does not choose manual/automatic approval or artifact-promotion mechanics. |

No classification changes the severity or finding text recorded by STS-020.

## 5. Mechanical Corrections

### F-004 — Configuration ownership matrix

**Violated requirement:** CAP-003/GAP-002 require a complete, mechanically classified environment/config contract before implementation.

**Evidence:** `AUD-WORK-010` records 96 distributed reads, the existing `.env.example` coverage, omitted email/AI/public names, public-prefix usage, missing Staging mapping, and localized failure behavior.

**Deterministic correction:**

1. Add a redacted logical/configuration matrix; never include values.
2. Preserve current variable names where feasible and identify any new enable setting by logical name before implementation naming.
3. For every entry record: capability owner, current/canonical name, binding versus environment variable, public/server-secret class, required/required-if-enabled/optional status, default or OFF behavior, and DEVELOPMENT/STAGING/PRODUCTION ownership.
4. Include Core URL/database/Auth/payment/email settings, operator provider switches, and each optional module's enable/config condition.
5. State that missing required enabled configuration fails before serving and that disabled modules require no unused secret.

**Target files:** Detailed Spec, Gap Closure Matrix, Acceptance Matrix.

**Target IDs:** sections 7 and 21; CAP-003; GAP-002; ACC-003; dependent config references in CAP-007/009/010/018/019/020/022/023/025/027/031/032.

**Expected post-correction state:** An implementer can enumerate validation inputs and ownership without inventing a feature flag, secret class, or environment scope.

**Re-audit check:** Every logical setting used by a material capability resolves to exactly one matrix row; OFF paths have no required provider secret; no value is recorded.

### F-005 — Snapshot + Controlled Patch policy

**Violated requirement:** Frozen `AUDIT-001` upgrade strategy is absent.

**Evidence:** `docs/audit/SA_TEMPLATE_AUDIT_AUTHORITY.md` section 6 freezes `Snapshot + Controlled Patch` and `NO automatic merge into projects`.

**Deterministic correction:** Insert those exact rules into Reuse Policy and Explicit Non-Goals/Do-Not-Do. Clarify that Starter/project updates are reviewed bounded patches against a known snapshot; generated projects do not automatically merge upstream changes.

**Target files:** Detailed Spec only, followed by traceability consistency review in the other candidate artifacts without adding a new gap.

**Target IDs:** sections 5 and 30; CAP-001/CAP-030 maintenance boundary; existing acceptance may reference the policy but no new CAP/GAP/ACC ID is created.

**Expected post-correction state:** The frozen upgrade policy is explicit and cannot be mistaken for automated template synchronization.

**Re-audit check:** Exact policy language is present, no automatic merge path is authorized, and no new architecture/action is introduced.

### F-007 — Capability ID mapping repair

**Violated requirement:** Every gap must trace to canonical Capability IDs without renumbering.

**Evidence:** The master table defines CAP-006 DB atomicity, CAP-015 provider switch, CAP-016 webhooks/idempotency, CAP-017 entitlement, and CAP-018 AI providers.

**Deterministic correction:** Update only the affected-capability cells and related dependency text:

- `GAP-007`: `CAP-006 DB atomicity; CAP-016 Webhooks/idempotency; CAP-017 Entitlement; CAP-032 Retained non-Core` (CAP-032 only for enabled credit/affiliate side effects).
- `GAP-010`: `CAP-012 Orders; CAP-013 Stripe; CAP-014 Creem; CAP-015 Payment provider switch; CAP-016 Webhooks/idempotency; CAP-017 Entitlement`.
- `GAP-019`: `CAP-018 AI providers` (additional providers only), `CAP-021 Non-default Auth`, `CAP-026 Optional content/UI`, and `CAP-032 Retained non-Core`; remove Core `CAP-017`.

Do not change any Gap ID, priority, count, reuse action, or audited source.

**Target files:** Gap Closure Matrix; then verify master traceability and acceptance references remain aligned.

**Target IDs:** GAP-007, GAP-010, GAP-019.

**Expected post-correction state:** Every affected row names the same capability that its ID denotes; Core Entitlement is not classified retained non-Core.

**Re-audit check:** All CAP names resolve one-to-one to the master table and gap counts remain P0=8/P1=8/P2=3/total=19.

### F-008 — Named user/invite atomicity invariants

**Violated requirement:** CAP-006/ACC-006 promise named invariants but leave user/invite scope untestable.

**Evidence:** `AUD-WORK-020` identifies only these non-payment multi-write sequences: user insert followed by initial credit, and invite-user update followed by affiliate insert. Payment writes remain governed by F-001.

**Deterministic correction:** Specify only these evidence-backed invariants:

- **User/onboarding:** when optional initial credits are OFF, canonical user creation is a single identity write and no credit write occurs. When initial credits are enabled, canonical user creation plus exactly one initial-credit grant either commit together or leave neither dependent outcome; concurrent trusted same-email creation still resolves through the Auth identity invariant.
- **Invite/affiliate:** when affiliate/referral is OFF, its mutation route is unavailable. When enabled, setting `users.invited_by` plus creating the corresponding affiliate relation commit together or neither commits; invalid, self, repeated, or wrong-owner attempts create no partial state.
- **Payment:** reference the F-001-selected payment transaction contract rather than duplicating it in CAP-006.

**Target files:** Detailed Spec and Acceptance Matrix; Gap Matrix only where dependency wording needs alignment.

**Target IDs:** section 9; CAP-006/CAP-032; ACC-006/ACC-032; GAP-006/GAP-007 dependency text.

**Expected post-correction state:** Every CAP-006 non-payment invariant names its writes, enabled condition, rollback result, concurrency result, and acceptance evidence.

**Re-audit check:** ACC-006 can construct failure/concurrency cases without inventing a flow; no unevidenced transaction or broad repository wrapper is added.

## 6. Planner Decisions

None.

All non-mechanical findings change user-visible security, lifecycle, visual-authority, or release-governance behavior and remain `R3`. No finding is silently frozen as a planner-only preference.

## 7. User Decisions

### F-001 — Payment lifecycle, idempotency, and entitlement authority

**Decision question:** Should durable payment mutation be owned by one shared idempotent transition service used by verified callbacks and webhooks, or by signed webhooks only?

**Why it matters:** The choice fixes the order state graph, concurrent replay behavior, partial-failure recovery, and when paid access is granted or revoked.

**Frozen constraints:** Stripe + Creem one-time; server-derived pricing; operator-selected provider; no request failover; retain existing orders/callbacks/webhooks/signature checks; credits/subscriptions OFF; bounded PATCH only; no payment schema rewrite.

**Option A — Shared verified transition service:**

- Server-retrieved provider callbacks and signature-verified webhooks both submit provider facts to one transition service.
- State graph: `CREATED -> PAID | FAILED | CANCELLED`; `PAID -> REFUNDED`. Repeated same outcomes are no-ops; incompatible terminal transitions are rejected/logged for reconciliation. A browser cancel URL alone is not provider proof.
- Webhooks use unique `(provider, provider_event_id)` identity. Callback fallback uses a unique provider checkout/session identity plus outcome when no event ID exists.
- One database transaction records idempotency, performs the conditional state transition, updates Core entitlement, and writes enabled credit/affiliate side effects with unique order linkage.
- Entitlement is active only for `PAID` qualifying orders and revoked for `REFUNDED`.

**Impact:** Preserves both current callback and webhook paths and centralizes correctness with the smallest behavioral patch. It must handle two trusted entry points and conflict reporting.

**Option B — Webhook-only durable authority:**

- Signed provider webhooks are the only path that mutates durable order/entitlement state.
- Browser callbacks retrieve/display provider status but remain read-only until webhook convergence.
- The same state graph, event uniqueness, transaction, side-effect, and entitlement rules apply inside the webhook-owned service.

**Impact:** Creates a single durable writer and simpler replay ownership, but changes current callback mutation behavior and makes user-visible completion depend on webhook delivery/reconciliation.

**Evidence:** `AUD-WORK-040` sections 1, 3-6 and findings for order lifecycle, provider callbacks/webhooks, idempotency, and entitlement; STS-020 F-001.

**Recommended option:** `Option A — Shared verified transition service`.

**Recommendation confidence:** `HIGH`. It retains the existing callback and webhook investments while forcing both through one invariant; no broader architecture is required.

**Unchanged regardless of option:** Provider signatures/server retrieval remain mandatory; client callback values never authorize payment; pricing remains server-derived; provider switch remains operator-only; credits/subscriptions remain OFF; invalid/replayed events cannot double grant; no automatic failover or schema rewrite.

**Exact later correction targets:** Detailed Spec sections 9/11/20/21/22/24/25/31/32; CAP-006 and CAP-012..017; GAP-007/GAP-010; ACC-012..017; payment/config/security/release traceability rows.

### F-002 — Magic Link lifecycle defaults

**Decision question:** Should the Starter permit only one short-lived active Magic Link per normalized email/purpose, or allow multiple outstanding links until individual expiry/use?

**Why it matters:** TTL and replacement behavior determine replay window, multi-device behavior, storage/query semantics, throttling, and deterministic acceptance.

**Frozen constraints:** Email Magic Link is Core; trusted same-email identity maps to one canonical UUID; tokens expire, are one-use and replay-safe; generic request responses prevent enumeration; Resend is a thin server-only delivery boundary; no password Auth or mandatory Auth.js Adapter migration.

**Option A — One active short-lived token:**

- Default TTL 15 minutes, configurable only within a documented bounded range.
- Normalize email before issuance; store only a token hash and purpose.
- Issuing a new token atomically invalidates any prior unconsumed token for the same email/purpose.
- Successful callback atomically consumes the token before establishing/linking identity; expired/used/invalid tokens fail identically.
- Request throttling is owned by Auth and keyed by normalized email plus client/IP signal; the response remains generic.

**Impact:** Smallest active-token state and shortest replay window; requesting a new link invalidates an earlier email, which may surprise users opening older messages.

**Option B — Multiple individually valid tokens:**

- Default TTL 30 minutes; each issued token remains valid until its own first use or expiry.
- Tokens are hashed and atomically consumed individually; successful use does not automatically invalidate other outstanding tokens unless the session/security policy does so.
- The same generic response and Auth-owned throttling apply.

**Impact:** Better multi-device/email latency tolerance but a wider replay surface, more outstanding state, and more complex test/revocation semantics.

**Evidence:** `AUD-WORK-030` sections 3 and 5 establishes complete absence of a current lifecycle and confirms only the trusted-identity target; STS-020 F-002.

**Recommended option:** `Option A — One active short-lived token`.

**Recommendation confidence:** `MEDIUM`. Minimal-delta/security principles favor one bounded token, but repository evidence does not determine the exact TTL; the user must approve it.

**Unchanged regardless of option:** Token values are never stored/logged in plaintext evidence; consumption is atomic; expiry/use/replay/throttle tests are mandatory; Resend delivery does not authenticate; canonical identity and no-enumeration rules remain.

**Exact later correction targets:** Detailed Spec sections 10/12/20/21/22/31/32; CAP-007/CAP-009/CAP-010/CAP-027; GAP-004/GAP-005/GAP-006; ACC-007/009/010/027.

### F-003 — Session policy

**Decision question:** Should Starter R1 retain the pinned Auth.js JWT/session defaults as the normative session policy, or add explicit Starter max-age/refresh values?

**Why it matters:** Tests, cookie lifetime, refresh behavior, logout scope, and upgrade behavior need a stable target.

**Frozen constraints:** Retain Auth.js v5 callback/JWT/session path and canonical UUID payload; no database-session/Adapter migration is required; protected APIs/layouts verify server-side identity; logout must remove subsequent access in the current browser; Snapshot + Controlled Patch governs upgrades.

**Option A — Retain pinned Auth.js defaults:**

- The exact resolved JWT/session/cookie defaults of the pinned lockfile version become the R1 baseline and are recorded by name/value in the corrected spec before re-audit.
- Tests verify expiry, refresh/update, secure cookie attributes in each environment, canonical UUID payload, server/client access, and browser logout.
- Account-wide/session-revocation infrastructure is not added; logout invalidates the current browser session boundary.

**Impact:** Best matches `KEEP + TEST` and existing architecture. A controlled dependency upgrade must explicitly review any changed defaults.

**Option B — Explicit Starter session values:**

- Freeze a Starter-owned absolute/rolling lifetime, refresh cadence, and cookie policy independent of future Auth.js defaults.
- Retain JWT sessions but configure the values directly and test them; current-browser logout remains the minimum invalidation boundary unless separately authorized.

**Impact:** More stable across dependency changes and easier to explain, but adds configuration/policy not evidenced by current `sa-template` behavior and needs the user to select concrete durations.

**Evidence:** `AUD-WORK-030` section 4 and JWT/session finding classify the current path `KEEP + TEST` and identify defaults as unknown/not verified; STS-020 F-003.

**Recommended option:** `Option A — Retain pinned Auth.js defaults`.

**Recommendation confidence:** `HIGH`. It follows reuse-first and avoids an unevidenced session redesign while still making the resolved pinned behavior explicit and testable.

**Unchanged regardless of option:** JWT/session callbacks and canonical UUID remain; cookies/secrets are server-controlled; unauthenticated/expired access is denied; logout/protected-route/session tests are mandatory; no Adapter migration.

**Exact later correction targets:** Detailed Spec sections 4/5/10/20/21/22/30/31/32; CAP-001/CAP-007/CAP-030; ACC-007/030; Auth/config/release traceability.

### F-006 — UI Visual Authority and Fidelity Audit model

**Decision question:** Should visual fidelity be governed by a Starter-neutral reference, project-specific references, or a two-layer combination?

**Why it matters:** A stable reference prevents self-approval, while A-002 forbids treating ShipAny product content/identity as Starter visual Authority.

**Frozen constraints:** Preserve A-002 Tailwind/shadcn/Radix/forms/tables/shells foundation; no UI replacement/repo-wide redesign; ShipAny branding/copy/assets/pricing/navigation/legal text are excluded; responsive/a11y/browser evidence is required; fidelity review must use fresh context.

**Option A — Starter-neutral reference only:**

- Freeze neutral-fixture references for shared primitives, Auth/account, dashboard/admin/member shells, marketing structure, pricing structure, and loading/error/not-found states.
- Cover light/dark and defined mobile/desktop viewports.
- All projects use this structural baseline; product-specific visual choices are outside the audit.

**Impact:** Simple reusable baseline, but can overconstrain future product visual composition or be mistaken for product design.

**Option B — Project reference only:**

- Starter freezes only the reference-manifest schema and test procedure.
- Each project must supply approved route/view/state references before UI implementation/freeze.

**Impact:** Maximizes product freedom and prevents ShipAny leakage, but leaves the shared Starter foundation without a stable visual baseline of its own.

**Option C — Two-layer reference model:**

- Layer 1 freezes a Starter-neutral structural reference set for shared primitives/shells/states using neutral fixtures.
- Layer 2 requires project-approved references for brand/product-specific routes, content, imagery, pricing, and navigation.
- Minimum shared set covers sign-in modal/drawer, account, admin/member shells, marketing header/footer, pricing structure, loading/error/not-found, light/dark, and mobile/desktop viewports.
- A fresh-context reviewer receives the frozen reference manifest, reviewed build/revision, and acceptance contract but no authoring rationale. The reviewer records route/view/state evidence and blocks missing states, overlap/clipping, broken navigation, semantic-token drift, or unexplained structural deviation. Pixel diff is supporting evidence, not a product-content authority.

**Impact:** Preserves reusable structural fidelity while keeping product identity under project Authority; it requires maintaining two explicit reference scopes.

**Evidence:** `AUD-FINAL-04` freezes structural keep groups and excludes product identity; `AUD-WORK-060` records no browser/a11y/visual baseline; `KSS-STS020-AUDIT-R1` requires minimum references and fresh-context audit; STS-020 F-006.

**Recommended option:** `Option C — Two-layer reference model`.

**Recommendation confidence:** `HIGH`. It is the only option that directly satisfies both reusable Starter verification and the frozen no-product-leakage boundary.

**Unchanged regardless of option:** A-002 keep list, no framework replacement, responsive/a11y requirements, product-content exclusion, fresh-context reviewer independence, and no claim of fidelity before evidence.

**Exact later correction targets:** Detailed Spec sections 18/22/25/29/30/31/32; CAP-024/CAP-029/CAP-031; GAP-015; ACC-024/029/031; UI/release traceability.

### F-009 — Release evidence and promotion ownership

**Decision question:** Should Production promotion require an authorized operator approval of the same immutable STAGING-tested artifact, or occur automatically after gates pass?

**Why it matters:** Commit equality alone does not prove artifact equality or identify who owns gate evidence and promotion authority.

**Frozen constraints:** Cloudflare-first/OpenNext; DEVELOPMENT/STAGING/PRODUCTION isolation; STAGING runs production-shaped gates; PRODUCTION receives the exact verified commit; failed gates stop; migration/recovery evidence required; no elaborate enterprise release platform.

**Option A — CI evidence plus operator-approved immutable promotion:**

- CI builds one immutable artifact/version from the pinned commit and dependencies, records commit and artifact digest, deploys it to STAGING, and owns the gate evidence bundle.
- An authorized operator reviews the evidence and explicitly approves promotion of that same immutable artifact/version with PRODUCTION bindings/secrets.
- PRODUCTION does not rebuild from source. Post-deploy revision/digest smoke must match the approved record.
- Rollback authority may select a prior known-good application version/config; database recovery follows the documented compatibility/forward-correction rule.

**Impact:** Strongest audit trail and separation of automated evidence from Production authority; adds a manual approval step.

**Option B — Automatic immutable promotion:**

- CI owns evidence and automatically promotes the same immutable artifact/version immediately after all STAGING gates pass.
- Revision/digest equality and rollback rules are identical; no human approval is required.

**Impact:** Faster and fully deterministic, but a faulty gate definition can immediately reach Production and there is no explicit operator checkpoint.

**Evidence:** `AUD-FINAL-05` requires exact verified commit promotion but records environment promotion as absent; GAP-008/ACC-031 define revision equality and evidence without ownership; STS-020 F-009.

**Recommended option:** `Option A — CI evidence plus operator-approved immutable promotion`.

**Recommendation confidence:** `HIGH`. It adds one bounded approval boundary without introducing an enterprise release system and removes rebuild ambiguity.

**Unchanged regardless of option:** Same immutable artifact/version and exact commit, isolated environment bindings, mandatory STAGING gates, failed-gate stop, migration compatibility evidence, post-deploy smoke, and documented rollback/recovery.

**Exact later correction targets:** Detailed Spec sections 7/8/21/24/25/31/32; CAP-002/CAP-003/CAP-005/CAP-029/CAP-031; GAP-008; ACC-002/003/005/029/031; release traceability.

## 8. Authority Conflicts

None (`R4=0`).

STS-020 found omissions and ambiguities but no competing frozen decisions. This packet does not establish precedence or alter A-001, A-002, `AUDIT-001`, `KSS-DS-AUTH-R1`, or `KSS-STS020-AUDIT-R1`.

## 9. Evidence Gaps

None (`R5=0`).

All nine findings can be resolved at design level from existing repository evidence plus the five user decisions. Real Cloudflare, provider, OAuth, email, payment, database, browser, and release execution remains future implementation/environment verification and does not block preparation or correction of the Detailed Spec.

No Neon, PlanetScale, Supabase, Cloudflare token, Hyperdrive, Staging/Production resource, or provider credential is requested.

## 10. Correction Dependency Order

1. **Record independent user decisions:** F-001, F-002, F-003, F-006, and F-009 may be decided in parallel; record exact selected option and any approved parameter value.
2. **Apply independent mechanical rules:** F-005 exact upgrade policy and the ID-only portion of F-007 need no prior decision.
3. **Resolve domain contracts:** apply F-001 payment semantics, F-002 Magic Link lifecycle, F-003 session policy, F-006 visual/fidelity model, and F-009 release ownership to the master capability contracts.
4. **Complete evidence-derived mechanics:** apply F-008 after F-001 so CAP-006 references rather than duplicates payment atomicity; apply F-004 after F-002/F-003/F-009 so all chosen Auth/release settings and owners appear in the configuration matrix.
5. **Finish consistency updates:** finalize F-007 payment wording, update affected Gap/Acceptance rows and section 32 traceability, and replace `Open Decisions / Ambiguities: NONE` only when every selected decision is fully represented.
6. **Run deterministic document checks:** preserve 32 CAPs, 32 ACCs, 19 gaps, priorities, actions, no REFACTOR/DELETE, A-001/A-002, and no product leakage.
7. **Rerun STS-020 in fresh context:** only a passing independent re-audit may make STS-030 eligible.

No correction task ID or execution contract is created by this ordering.

## 11. Expected Correction Touch Set

A later explicitly authorized correction task is expected to modify only:

- `docs/starter/KYD_SAAS_STARTER_DETAILED_SPEC.md`
- `docs/starter/KYD_SAAS_STARTER_GAP_CLOSURE_MATRIX.md`
- `docs/starter/KYD_SAAS_STARTER_ACCEPTANCE_MATRIX.md`
- Runtime/trace/index documents explicitly authorized for that later task

It may add a repository-local visual reference manifest only if the user selects F-006 Option A or C and the later task Authority registers the exact artifact. It must not modify application code, dependencies, schema/migrations, build/deployment/environment configuration, or external resources while correcting the design.

Frozen Authority documents are inputs, not correction targets. Any new decision Authority must be separately planner/user authorized and registered rather than silently editing an existing FROZEN Authority.

## 12. Re-audit Requirements

The fresh-context STS-020 rerun must verify:

1. F-001 through F-009 each have an exact correction trace and no unresolved user choice.
2. The payment state/event table exists and ACC-012/016/017 test exactly that table.
3. Magic Link TTL/outstanding-token/consume/throttle semantics and session resolved values are explicit and testable.
4. The configuration ownership matrix covers all Core and optional logical settings without values or mandatory OFF secrets.
5. Snapshot + Controlled Patch and no automatic project merge are exact.
6. UI reference ownership and fresh-context Fidelity Audit procedure are explicit, product-neutral, and observable.
7. GAP-007/GAP-010/GAP-019 Capability IDs match the master table without count/priority/action changes.
8. User/onboarding and invite invariants are named and do not duplicate payment rules.
9. Release CI/operator ownership, immutable artifact identity, promotion, stop, and rollback boundaries are explicit.
10. Capability count remains 32; acceptance count remains 32; gap count remains 19 with P0=8/P1=8/P2=3.
11. Reuse actions remain justified and no REFACTOR/DELETE/product-specific leakage appears.
12. Candidate document traceability is internally consistent and `Open Decisions / Ambiguities` is truthful.
13. No real provider/environment validation is mislabeled as design evidence.
14. Runtime execution/closeout validation and documentation-only Git scope pass.

STS-030 remains `NOT_READY` until this re-audit returns PASS (or PASS WITH MINOR FINDINGS with every freeze-blocking correction resolved) and Runtime marks STS-020 `VERIFIED`.

## 13. Final Decision Checklist

- [ ] F-001: choose shared verified transition service or webhook-only durable authority.
- [ ] F-002: choose one active 15-minute token or multiple 30-minute outstanding tokens, including approved bounds.
- [ ] F-003: choose pinned Auth.js defaults or explicit Starter session values.
- [ ] F-006: choose Starter-neutral, project-only, or two-layer Visual Authority.
- [ ] F-009: choose operator-approved or automatic immutable Production promotion.
- [ ] Record each selected option in explicit user/planner decision evidence.
- [ ] Authorize a bounded correction task; do not reuse STS-021 for corrections.
- [ ] Apply F-004/F-005/F-007/F-008 mechanical corrections in dependency order.
- [ ] Update all affected master/gap/acceptance/traceability locations without changing counts or actions.
- [ ] Confirm candidate corrections contain no application/environment work.
- [ ] Execute a fresh-context STS-020 re-audit.
- [ ] Keep STS-030 non-executable until STS-020 is VERIFIED.
