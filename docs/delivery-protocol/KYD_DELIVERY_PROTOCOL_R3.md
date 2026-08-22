# Kyd Delivery Protocol R3

> **Authority ID:** KPS-DP-R3
> **Version:** R3
> **Status:** FROZEN
> **Freeze Date:** 2026-08-22
> **Reviewed Candidate:** KPS-DP-CANDIDATE-R3
> **Source Input SHA-256:** `9f1c8ceb2daac6ae6a7b4a7be314838bddb13b8dfc5e4e153be7c858d2cfa185`
> **Scope:** Generic project delivery protocol
> **Applies to:** All Kyd-managed projects unless an approved Product-Specific Authority narrows or extends a stage
> **Does NOT define:** product features, technology stack, provider choices, repository implementation details, or Kyd Project Runtime internals
> **Provenance Note:** Candidate-state labels retained in the approved semantic body record review provenance; formal state is governed by this header, `PROJECT_INDEX`, and `KPS-DP-FREEZE-R3`.

---

# 0. Purpose

Kyd Delivery Protocol defines how a project moves safely from idea to verified release and closeout.

Its primary purpose is to reduce:

- implementation before design is complete;
- late discovery of missing product behavior;
- repeated redesign during coding;
- scope expansion by implementation agents;
- context drift between sessions;
- early discussion being mistaken for final decisions;
- missing dependencies discovered after implementation starts;
- verification being deferred until the end;
- unverified release promotion;
- rollback uncertainty;
- repeated rebuilding of reusable capabilities.

The Delivery Protocol is intentionally project-type agnostic.

It must not contain rules tied to SaaS-specific features, particular providers, particular frameworks, or a specific repository.

---

# 1. Core Lifecycle

```text
Project Intake
    ↓
Product Definition
    ↓
Design Completeness
    ↓
Design Freeze
    ↓
Implementation Planning
    ↓
Implementation & Verification
    ↓
Release & Promotion
    ↓
Closeout
```

A later phase must not silently finish work that belongs to an earlier phase.

## Universal Forward-Progression Rule

Except for initial Project Intake and an explicitly controlled re-entry, a later lifecycle stage may begin only after the preceding required Gate is `PASS`.

```text
PASS    → forward progression may become eligible
FAIL    → forward progression is prohibited until correction and re-evaluation
BLOCKED → forward progression is prohibited until the blocker is resolved and the Gate is evaluated
```

A later stage may not be used to bypass a failed or blocked earlier stage.

```text
Coding is not a substitute for design.
Testing is not a substitute for acceptance definition.
Staging is not a substitute for implementation verification.
Production deployment is not a substitute for release approval.
Chat history is not a substitute for Authority.
```

---

# 2. Responsibility Boundaries

## 2.1 Kyd Delivery Protocol owns

- lifecycle stages;
- stage entry requirements;
- required outputs;
- phase gates;
- role responsibilities;
- design completeness expectations;
- freeze rules;
- implementation-planning requirements;
- verification expectations;
- release eligibility;
- production approval requirements;
- rollback readiness;
- milestone/project closeout;
- controlled change path between frozen stages.

## 2.2 Kyd Project Runtime owns

The Runtime enforces execution inside the repository.

Runtime responsibilities include:

- current execution state;
- current task;
- task index;
- task dependencies;
- exact Authority loading;
- allowed modification scope;
- task gates;
- deny-by-default blocking;
- execution trace;
- task verification state;
- session bootstrap and recovery.

The Delivery Protocol says what must be true before work may advance.

The Runtime says whether a concrete repository task is allowed to execute.

## 2.3 Product-Specific Design owns

- product goals;
- user behavior;
- business rules;
- user journeys;
- product states;
- UI/UX;
- data semantics;
- product-specific architecture decisions;
- product-specific integrations;
- product-specific acceptance criteria.

The Delivery Protocol must never invent these details.

---

# 3. Authority States

```text
Discussion
    ↓
Candidate Decision
    ↓
Confirmed Decision
    ↓
Registered Authority
    ↓
Frozen Authority
```

## 3.1 Discussion

Exploration only. Discussion has no execution authority.

## 3.2 Candidate Decision

A proposed decision that may affect future implementation. It must be clearly labeled as candidate.

## 3.3 Confirmed Decision

The project owner or authorized decision-maker explicitly approves the decision.

Confirmation alone does not automatically make it executable repository Authority.

## 3.4 Registered Authority

The confirmed decision is written into the controlled project Authority system.

Only registered Authority may be used by execution tasks when Authority is required.

## 3.5 Frozen Authority

A Registered Authority is not Frozen Authority merely because it is being prepared for freeze.

The transition is:

```text
Registered Authority
    ↓
Candidate Freeze Package
    ↓
Freeze Gate evaluation
    ↓ PASS
New identifiable Frozen Authority version
```

A Frozen Authority version is immutable.

It must not be silently changed or mutated in place during implementation.

---

# 4. Controlled Change Rule

If implementation discovers a real design defect:

```text
Implementation stops at the affected boundary
    ↓
Issue is recorded
    ↓
Affected Frozen Authority scope is identified
    ↓
A successor Candidate revision is created
    ↓
Change is discussed
    ↓
Authorized owner confirms the successor revision
    ↓
The confirmed successor is registered as a new Registered Authority revision
    ↓
Affected completeness / freeze checks are rerun
    ↓ PASS
A new identifiable Frozen Authority version is created
    ↓
Dependent implementation tasks are re-evaluated
```

The controlled-change state order is therefore:

```text
Candidate successor revision
    ↓
Discussion / review
    ↓
Authorized confirmation
    ↓
Registered Authority successor revision
    ↓
Affected completeness / freeze checks
    ↓ PASS
New Frozen Authority version
```

A successor revision must not be treated as Registered Authority before authorized confirmation.

The previous Frozen Authority version remains immutable and traceable.

Unaffected execution may continue only when independence from the changed scope is explicitly established.

An implementation agent must not repair a design gap by inventing product behavior.

A frozen design change is not a normal code patch.

---

# 5. Universal Roles

Roles are logical responsibilities, not required job titles or tools.

One person or agent may hold multiple roles when appropriate, but responsibilities remain distinct.

## 5.1 Project Owner

Owns project intent, major product decisions, scope approval, frozen-decision approval, and production promotion approval unless explicitly delegated.

## 5.2 Planner

Owns converting goals into structured design/planning work, identifying ambiguity, preparing completeness reviews, preparing implementation boundaries, and maintaining separation between design and execution.

## 5.3 Executor

Owns implementing authorized task scope, following exact Authority, not expanding scope, and producing implementation evidence.

## 5.4 Verifier

Owns independently checking acceptance, validating evidence, distinguishing IMPLEMENTED from VERIFIED, and rejecting insufficient evidence.

## 5.5 Release Approver

Owns explicit approval of production promotion and confirmation of release eligibility and rollback readiness.

The Release Approver may be the Project Owner.

---

# 6. Gate Model

Canonical gate outcomes:

```text
PASS
FAIL
BLOCKED
```

## PASS

All mandatory conditions are satisfied with sufficient evidence.

## FAIL

The evaluated work is complete enough to evaluate, but one or more mandatory conditions are not satisfied.

## BLOCKED

The gate cannot be evaluated because required inputs, decisions, dependencies, environment access, or Authority are missing.

A BLOCKED state must not be treated as PASS.

## Gate Ownership

Every Gate must have an identified authorized **Gate Owner** who is accountable for recording the Gate result and its supporting evidence.

A Gate may also have a separate evaluator/reviewer.

One person may hold multiple logical roles when project size/risk permits, but the responsibility must remain explicit.

Default Gate Owners:

```text
Intake Gate                  → Project Owner
Product Definition Gate      → Project Owner
Design Completeness Gate     → Verifier
Design Freeze Gate           → Project Owner
Implementation Planning Gate → Planner
Implementation/Verification  → Verifier
Release/Delivery Gate        → Release Approver
Closeout Gate                → Project Owner
```

A project may delegate a Gate Owner if the delegation is explicit.

For medium/high-risk work, a Gate authored substantially by the same role that produced the evaluated artifact should use an independent reviewer where practical.

---

# 7. Stage 1 — Project Intake

## Purpose

Create a minimum stable starting point before detailed design begins.

## Required Inputs

At minimum:

- project/problem statement;
- intended outcome;
- known decision owner;
- known constraints;
- known reusable sources, if any;
- materially relevant deadlines or commitments.

Unknown items may remain unknown if explicitly marked.

For maintenance work on an existing project, stable inherited context may be reused. The Intake artifact may record only the current change/delta, affected scope, decision owner, constraints, and open questions rather than restating the entire project.

## Required Output

A Project Intake Record containing:

```text
Project identity
Problem / opportunity
Primary goal
Initial scope
Explicit non-goals if known
Decision owner
Known constraints
Known reusable assets/sources
Open questions
```

## Prohibited Behavior

Do not choose architecture merely to make intake look complete, infer undecided product behavior, create implementation tasks, or treat brainstorming as Product Authority.

## Exit Gate — Intake Gate

**Default Gate Owner:** Project Owner.

PASS when project identity, primary goal, decision ownership, major known constraints, and unresolved questions are visible.

---

# 8. Stage 2 — Product Definition

## Purpose

Define what the project must do before implementation design is frozen.

## Required Coverage

Applicable items include:

- users / actors;
- goals and use cases;
- workflows / journeys;
- functional scope;
- non-goals;
- business rules;
- permissions / ownership semantics;
- user-visible states;
- success criteria;
- applicable external systems;
- applicable data concepts;
- applicable product constraints.

Not every project needs every category.

A category may be marked `N/A` with a brief reason where ambiguity could otherwise result.

## Required Output

A controlled Product Definition / Product-Specific Authority set.

## Exit Gate — Product Definition Gate

**Default Gate Owner:** Project Owner.

PASS when committed/in-scope delivery scope is defined, implementation-affecting semantics are known or explicitly deferred, deferred items do not block the next stage, and ownership of major product decisions is resolved.

---

# 9. Stage 3 — Design Completeness

## Purpose

Prevent implementation from becoming the place where missing design is discovered and invented.

## Completeness Domains

Evaluate applicable domains:

```text
A. Product behavior
B. User / actor flows
C. State model
D. Error / retry / recovery behavior
E. Permission / ownership / authorization semantics
F. Data semantics and persistence
G. Interfaces / APIs / integration contracts
H. Configuration / environment behavior
I. Security / abuse boundaries
J. UI / interaction behavior
K. Responsive / accessibility behavior where applicable
L. Migration / compatibility behavior where applicable
M. Observability / operational behavior where applicable
N. Verification / acceptance criteria
O. Release / rollback constraints where applicable
P. Reuse / compatibility constraints
```

Projects may add domains or mark a domain N/A.

## Finding Severity

```text
BLOCKER
MAJOR
MINOR
INFORMATIONAL
```

BLOCKER means implementation cannot safely begin.

MAJOR means a meaningful implementation decision is undefined or contradictory.

MINOR may remain only if it does not materially change implementation semantics and has an owner/disposition.

## Design Completeness Gate

**Default Gate Owner:** Verifier.

PASS requires:

```text
BLOCKER = 0
MAJOR = 0
implementation-affecting ambiguity = 0
```

## Independent Review

For medium/high-risk projects, or when the Planner authored most of the design, review should use a fresh context or independent reviewer perspective.

The objective is to expose hidden assumptions, not create ceremony.

---

# 10. Stage 4 — Design Freeze

## Purpose

Create an implementation baseline that cannot drift silently.

## Freeze Preconditions

- Design Completeness Gate PASS;
- exact controlled Authority inputs identified;
- residual non-blocking findings recorded;
- acceptance criteria available;
- decision ownership resolved.

## Candidate Freeze Package

Before the Freeze Gate, prepare a Candidate Freeze Package identifying:

```text
Registered Authority documents proposed for freeze
Candidate version / identity
Integrity reference where supported
Proposed freeze scope
Prerequisite gate evidence
Known accepted limitations
Change-control rule
```

These inputs are not yet Frozen Authority.

## Freeze Meaning

Freeze does not mean the design can never change.

Freeze means implementation may rely on an identifiable immutable baseline and changes require controlled re-entry through a successor revision.

## Exit Gate — Freeze Gate

**Default Gate Owner:** Project Owner.

PASS when the candidate baseline is identifiable, reproducible, internally consistent, and traceable to a passed completeness review.

Only after PASS is a new identifiable Frozen Authority version created and the freeze date recorded.

---

# 11. Stage 5 — Implementation Planning

## Purpose

Convert frozen design into the smallest safe executable work graph.

Frozen design must not jump directly to coding.

## Required Planning Sequence

```text
Frozen Authority
    ↓
Existing Implementation / Reusable Asset Inspection
    ↓
Gap / Delta Identification
    ↓
Dependency Analysis
    ↓
Task Boundary Definition
    ↓
Task Contract Drafting
    ↓
Task Graph Review
```

## Reuse Rule

```text
KEEP
→ KEEP + TEST
→ KEEP-DISABLED
→ WRAP
→ PATCH
→ REFACTOR
→ DELETE
```

REFACTOR requires evidence that smaller actions are insufficient.

DELETE requires explicit review and approval.

## Task Boundary Rule

A task must be the smallest unit that has:

- one clear goal;
- bounded Authority;
- bounded touch scope;
- explicit dependencies;
- testable acceptance;
- a coherent verification boundary.

Avoid umbrella tasks and unnecessary microtasks.

## Dependency Rule

Priority is not dependency.

Recommended sequencing is not dependency.

A hard dependency exists only when downstream work cannot be safely implemented or verified without the upstream result.

## Logical Task Contract Requirements

Every executable task must logically identify, at minimum:

- a stable task identity;
- one clear goal;
- hard dependencies;
- exact Authority inputs;
- bounded modification/touch scope;
- shared-resource collisions where relevant;
- required gates;
- allowed changes;
- forbidden changes;
- acceptance criteria;
- verification requirements.

The Runtime owns the exact canonical field names and schema.

## Implementation Planning Gate

**Default Gate Owner:** Planner.

PASS when all mandatory scope maps to tasks or explicit deferrals, hard dependencies are explicit, Authority inputs are known, shared-resource collisions are controlled, acceptance is testable, no task must invent unresolved design, and reusable capability was considered first.

---

# 12. Stage 6 — Implementation & Verification

## Purpose

Execute bounded work while continuously proving correctness.

## Execution Rule

A task may execute only when Runtime authorizes it, required dependencies are satisfied, exact Authority is available, scope is bounded, and required gates are satisfiable.

## Scope Rule

The Executor must not broaden scope, redesign frozen behavior, perform unrelated refactors, delete reusable capability without approval, convert optional capability into mandatory capability, or modify Authority to make implementation easier.

## Discovery During Implementation

Implementation defect: fix within scope if allowed.

Missing design/product decision: stop the affected path and route it through controlled design change.

Independent issue: record separately; do not silently expand the active task.

## Continuous Verification

Use the smallest practical evidence boundary.

Applicable evidence may include automated tests, static checks, integration tests, browser/manual verification, environment smoke tests, migration verification, security negative tests, or artifact/revision evidence.

## Status Semantics

```text
IMPLEMENTED ≠ VERIFIED
```

## Exit Gate

**Default Gate Owner:** Verifier.

PASS when acceptance is satisfied, required evidence exists, regressions are within accepted limits, trace is complete, and no unresolved task-scope blocker remains.

---

# 13. Stage 7 — Release / Delivery & Promotion

## Purpose

Move a verified candidate to its approved **release/delivery target** without introducing unverified changes.

A release/delivery target may be, for example:

- a production environment;
- an approved job execution;
- activation of an internal tool or automation;
- handoff/publication of an identifiable artifact or content set;
- another explicitly defined delivery destination.

The Protocol does not require every project to have a production environment.

## Release / Delivery Eligibility

A candidate is eligible only when required implementation tasks are VERIFIED, required integration/system verification is complete, release-blocking issues are resolved or explicitly accepted, the candidate revision/artifact/release set is identifiable, delivery prerequisites are known, and rollback/recovery or equivalent recovery handling is ready where applicable.

## Staging Rule

Where staging exists, it validates the release candidate and environment-specific behavior.

Staging must not become a separate redesign environment.

Projects without staging must use the applicable pre-delivery verification required by their risk and delivery target.

## Candidate Integrity Rule

The delivered/activated result should be the same verified immutable candidate or release set that passed the required pre-delivery verification.

No silent code/content mutation, dependency drift, or equivalent material change may occur after final verification without invalidating the prior approval.

If the delivery platform requires rebuilding or regeneration, equivalent reproducibility/integrity evidence must be established.

## Release / Delivery Approval Rule

Delivery or activation requires explicit approval from the Release Approver when the project has a controlled release/delivery event.

The approval must identify the exact candidate/revision/artifact/release set being approved.

Verification eligibility does not equal permission to deliver or activate.

Any material change to the approved candidate requires renewed verification as applicable and renewed approval.

For projects with a production environment, production promotion is a controlled release/delivery event and this approval is mandatory.

## Recovery / Rollback Readiness

Record applicable recovery information:

- recovery target or rollback point;
- rollback/recovery trigger;
- rollback/recovery method;
- irreversible changes, if any;
- migration or data-recovery considerations where applicable.

If rollback is not meaningful for the delivery type, record the equivalent recovery or containment strategy.

## Post-Delivery Validation

Perform applicable checks such as candidate identity, health/readiness, critical path smoke, critical integration smoke, migration/data state, artifact integrity, and monitoring/log evidence.

## Release / Delivery Gate

**Default Gate Owner:** Release Approver.

PASS when:

- the exact candidate/release set was explicitly approved where a controlled delivery event exists;
- the expected candidate was delivered/activated to the approved target;
- required post-delivery validation passes;
- applicable recovery/rollback information is recorded.

For a project with no production environment, the Gate is satisfied by the equivalent approved delivery/handoff/activation evidence rather than production-specific evidence.

---

# 14. Stage 8 — Closeout

## Purpose

End a milestone/project phase with a recoverable, auditable state.

## Required Closeout Record

```text
Delivered scope
Verified scope
Deferred scope
Known limitations
Release / baseline reference
Rollback / recovery reference
Open follow-up items
Authority changes during the phase
Final execution state
Recommended next phase / NONE
```

Runtime task/session closeout is not the same as project/milestone closeout.

Runtime closes execution units.

Delivery Protocol closes delivery phases/milestones.

## Closeout Gate

**Default Gate Owner:** Project Owner.

PASS when completed work is traceable, verification state is explicit, deferred work is not disguised as completed, recovery/baseline reference is known, and the next state is explicit.

---

# 15. Project Size / Risk Scaling

The lifecycle applies to all projects, but artifact depth may scale.

Simplified artifacts are acceptable when scope and risk are low.

Stronger review/evidence is appropriate when product behavior is complex, security/privacy risk is material, data migration is material, rollback is difficult, multiple executors run in parallel, or irreversible external effects exist.

Scaling affects artifact depth, not core safety rules.

The following cannot be skipped merely because a project is small:

```text
Authority clarity
No coding through unresolved design ambiguity
Explicit implementation scope
Verification before VERIFIED
Explicit release/delivery approval when a controlled delivery event exists
Traceable closeout
```

---

# 16. Rework-Prevention Rules

```text
RP-01 No Coding Through Design Ambiguity
RP-02 Discussion Is Not Authority
RP-03 Design Before Implementation
RP-04 Freeze Before Implementation Execution
RP-05 Reuse Before Rewrite
RP-06 Explicit Dependencies
RP-07 Bounded Task Scope
RP-08 Verification Is Continuous
RP-09 Implemented Is Not Verified
RP-10 Exact Verified Delivery Candidate
RP-11 Explicit Release / Delivery Approval
RP-12 Recoverable State
RP-13 Controlled Frozen-Decision Change
RP-14 Repository Truth Over Planner Memory
```

These are lifecycle safety rules, not product-specific implementation rules.

---

# 17. Planner Memory Rule

Planner context may retain stable rationale, confirmed long-term decisions, historical decision evolution, and protocol background.

Planner memory must not replace current project state, current task, current dependency state, current gate evidence, or exact implementation Authority.

Dynamic execution truth belongs to Runtime/repository execution sources.

---

# 18. Protocol Artifact Model

The protocol requires logical artifacts, not necessarily one file per artifact.

Logical artifacts:

```text
Project Intake
Product Definition / Product-Specific Authority
Design Completeness Evidence
Design Freeze Record
Implementation Plan / Task Graph
Runtime Task Contracts
Verification Evidence
Release / Delivery Record
Closeout Record
```

Projects may combine artifacts if traceability remains clear.

Avoid files created only for ceremonial completeness.

---

# 19. Protocol-to-Runtime Relationship

Runtime may support repository execution state, planning state, controlled documents, and enforcement before Stage 5.

The Delivery Protocol does not restrict Runtime to post-planning use.

However:

```text
implementation execution must not become eligible
until the Implementation Planning Gate is PASS
and the relevant implementation task satisfies Runtime eligibility rules.
```

At implementation handoff, the Protocol/planning outputs must provide enough logical information for Runtime to enforce:

- which implementation task is active;
- its hard dependencies;
- its exact Authority inputs;
- its bounded modification scope;
- its forbidden changes;
- its required gates;
- its completion/verification evidence.

Runtime owns the concrete schema and enforcement mechanism.

Runtime must not infer missing product/design semantics.

---

# 20. Runtime-to-Protocol Feedback

Runtime may surface blocked dependencies, missing Authority, ambiguous acceptance, scope collision, failed verification, or environment blockers.

Runtime reports those facts.

The Delivery Protocol determines which earlier phase must be reopened.

Runtime does not redesign the lifecycle.

---

# 21. Protocol Change Classification

Future Protocol changes should be classified:

```text
Clarification
Compatibility-preserving improvement
Behavior-changing protocol change
```

Behavior-changing changes require explicit rationale, impact review, Runtime compatibility review, authorized approval, and a new version/freeze record.

No implementation task may silently change the Delivery Protocol.

---

# 22. Candidate Freeze Criteria

Candidate R3 may become frozen only after independent review confirms:

```text
1. Project-type agnostic.
2. No SaaS Starter specifics.
3. Protocol and Runtime responsibilities do not conflict.
4. Product-Specific Design ownership is clear.
5. All 8 lifecycle stages have clear entry/output/exit semantics.
6. Authority-state transitions are unambiguous.
7. Design ambiguity cannot silently pass into implementation.
8. Implementation Planning is required before coding.
9. Reuse-first planning is preserved.
10. Verification and release eligibility are distinct.
11. Controlled release/delivery requires explicit approval bound to the exact candidate/release set.
12. Rollback and Closeout are defined.
13. Small projects can scale artifact depth without bypassing safety rules.
14. No redundant governance layer is created.
15. No major rework-prevention gap remains.
```

Until then:

```text
Status = CANDIDATE / NOT FROZEN
```

---

# 23. Candidate R3 Revision Record

Candidate R3 preserves the 8-stage architecture and makes only localized corrections from the independent KPS-DP-002 review:

```text
M-01 Added universal forward-progression rule.
M-02 Added explicit Gate Owner semantics and defaults.
M-03 Made Frozen Authority versions immutable and clarified successor/re-freeze flow.
M-04 Generalized Stage 7 to release/delivery targets, not only production.
M-05 Clarified Runtime may operate before Stage 5; only implementation execution waits for Planning PASS.
m-01 Replaced P0 terminology with committed/in-scope delivery scope.
m-02 Bound release/delivery approval to the exact candidate/release set.
m-03 Converted task contract fields into logical requirements; Runtime owns canonical schema.
```

No lifecycle stage was added or removed.

No SaaS/template-specific rule was introduced.

---

# 24. Candidate Long-Term Decision Summary

The following are proposed, not yet frozen:

```text
Kyd Delivery Protocol uses 8 macro lifecycle stages.

Delivery Protocol owns lifecycle, phase gates, freeze, release/delivery eligibility,
approval requirements, recovery/rollback readiness, and project closeout.

Runtime owns repository execution enforcement.

Product-Specific Design owns product behavior.

Discussion ≠ Authority.

Design Completeness PASS requires:
BLOCKER = 0
MAJOR = 0
implementation-affecting ambiguity = 0

Frozen Design must pass through Implementation Planning before coding.

Implementation Planning is reuse-first and dependency-explicit.

IMPLEMENTED ≠ VERIFIED.

Release/delivery eligibility ≠ release/delivery approval.

The approved delivery target should receive the exact verified candidate/release set, or equivalent reproducible output.

Project/milestone Closeout is distinct from Runtime task/session closeout.

Frozen-decision changes use controlled re-entry.
```

These require independent review and user confirmation before becoming formal Delivery Protocol Authority.
