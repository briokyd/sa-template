# Kyd Project Bootstrap Pack — Bounded Packaging Specification R3

> **Authority ID:** KPS-BS-PACK-SPEC-R3
> **Version:** R3
> **Status:** FROZEN
> **Freeze Date:** 2026-08-23
> **Reviewed Candidate:** KPS-BS-PACK-SPEC-CANDIDATE-R3
> **Candidate Step ID:** KPS-BS-007
> **Freeze Registration Step:** KPS-BS-010
> **Independent Review:** KPS-BS-008 — PASS FOR USER FREEZE DECISION
> **Parent Authorities:** KPS-DP-R3 / KPS-DP-PLAYBOOK-R3 / RUNTIME-001 R1
> **Purpose:** Define the minimum portable bootstrap package required to initialize a new Kyd-managed project safely and reproducibly.

---

# 1. Scope

This specification defines the Project Bootstrap Pack only.

It does NOT:

- redesign Delivery Protocol R3;
- redesign Execution Playbook R3;
- redesign Runtime V1 R1;
- define Product-Specific Design;
- define SaaS Starter application capabilities;
- copy current Kyd template-project runtime state into a new project.

The Bootstrap Pack exists to install and initialize the already-frozen Kyd control system inside a new project repository.

---

# 2. Frozen Design Requirement

A new Kyd-managed project MUST receive the minimum control layer and runtime entry files required to operate independently from chat history or a specific agent.

The Bootstrap Pack is not complete if it only provides:

```text
README instructions
external references
chat prompts
manual explanations
```

It MUST materially initialize the project repository.

---

# 3. Minimum New-Project Structure

The minimum target structure is:

```text
new-project/
│
├── AGENTS.md
│
├── docs/
│   ├── PROJECT_INDEX.md
│   ├── CURRENT_STATE.md
│   │
│   ├── delivery-protocol/
│   │   ├── KYD_DELIVERY_PROTOCOL_R3.md
│   │   └── KYD_DELIVERY_PROTOCOL_EXECUTION_PLAYBOOK_R3.md
│   │
│   ├── kyd-runtime/
│   │   └── Kyd_Project_Runtime_V1_Minimal_Spec_R1.md
│   │
│   ├── product/
│   │   └── FEATURE_MATRIX.md
│   │
│   ├── tasks/
│   │   ├── TASK_INDEX.md
│   │   └── CURRENT_TASK.md
│   │
│   └── execution/
│       └── IMPLEMENTATION_TRACE.md
│
└── tools/
    └── kyd_runtime_validate.py
```

The exact FEATURE_MATRIX and Runtime-support paths MUST follow frozen Runtime R1 conventions.

No alternate parallel layout may be invented merely for packaging convenience.

---

# 4. Static Frozen Control Assets

The following assets are portable control Authorities and MUST enter the new project with explicit identity/version/hash traceability:

```text
Kyd Delivery Protocol R3
KPS-DP-R3

Kyd Delivery Protocol Execution Playbook R3
KPS-DP-PLAYBOOK-R3

Kyd Project Runtime V1 R1
RUNTIME-001
```

These assets MUST be pinned to the exact bootstrap-selected version.

A project initialized with:

```text
Protocol R3
Playbook R3
Runtime R1
```

must not silently drift when the Kyd template repository later publishes a newer version.

Control-layer upgrade is a separate explicit action.

---

# 5. Static Asset Packaging Rule

For each frozen static Authority, Bootstrap must preserve:

```text
Authority/document identity
version
content identity/hash
source/provenance
registered project path
```

The implementation may use exact copy or another content-preserving packaging mechanism, but the initialized project MUST end with a locally resolvable, pinned, auditable Authority.

A new project must not depend on:

```text
the planner remembering which version was used
a mutable external "latest" file
chat history
hidden agent reasoning
```

---

# 6. Dynamic Runtime State Rule

The following are PROJECT-INSTANCE state and MUST NOT be copied from the current Kyd template project as historical content:

```text
CURRENT_STATE
TASK_INDEX
CURRENT_TASK
FEATURE_MATRIX
IMPLEMENTATION_TRACE
```

They MUST be generated/initialized for the new project.

Historical:

```text
AUD-*
STS-*
sa-template
completed Kyd template project tasks
current template project blockers
current template project feature states
current template project implementation traces
```

must not appear in the new project zero-state.

---

# 7. New-Project Zero-State

A freshly bootstrapped project MUST safely represent:

```text
no implementation task yet
no executable task
no inherited historical task
no inherited implementation trace
no Product-Specific Authority unless separately created
no claim that Implementation Planning Gate has passed
```

At minimum the zero-state must semantically represent:

```text
current_task = NONE
implementation execution eligible = NO
task collection = EMPTY
implementation trace = EMPTY
project-specific feature state = INITIAL / EMPTY according to Runtime schema
blockers = NONE unless a real bootstrap blocker exists
```

The exact syntax follows frozen Runtime R1 schemas.

No fake task or fake Authority may be created solely to satisfy validation.

---

# 8. AGENTS.md Universal Entry Contract

Bootstrap MUST generate an agent-neutral root `AGENTS.md`.

It must define the project entry contract without permanently binding to ChatGPT, Codex, a particular model, vendor, or AI product.

It MUST establish at least:

```text
Repository-controlled Authority > chat/model memory
```

Required bootstrap reading order:

```text
1. AGENTS.md
2. docs/PROJECT_INDEX.md
3. docs/CURRENT_STATE.md
4. docs/tasks/CURRENT_TASK.md
5. task-declared Authority inputs when a current task is selected
6. required Runtime validation / eligibility checks
```

`docs/tasks/CURRENT_TASK.md` is always read as a required physical Runtime file.

Task-contract activation is conditional:

```text
if CURRENT_STATE.current_task = NONE
→ CURRENT_TASK.md is the canonical no-task sentinel
→ no task contract is active
→ execution eligibility remains FALSE

if CURRENT_STATE.current_task != NONE
→ CURRENT_TASK.md is the active task boundary
→ normal Runtime R1 identity/status/contract matching applies
```

It MUST state:

- `PROJECT_INDEX` is the Authority/navigation entry point;
- `CURRENT_STATE` is current repository truth;
- `CURRENT_TASK.md` is always present/read; it is the canonical no-task sentinel when no current task is selected, and the active task boundary when `CURRENT_STATE.current_task != NONE`;
- only task-declared Authority is loaded as required;
- Frozen Authority must not be silently changed;
- missing Authority/dependency/Gate/scope is BLOCKED;
- dependencies are explicit;
- deny-by-default applies;
- task scope must not expand silently;
- implementation agent must not invent product/design semantics;
- `IMPLEMENTED != VERIFIED`;
- Planner Memory/chat history is not Runtime Authority;
- replacement agents recover from controlled repository state.

The root `AGENTS.md` must not contain:

```text
AUD-specific execution sequences
STS-specific execution sequences
sa-template-specific rules
Codex-only wording as normative system behavior
current Kyd template project state
```

---

# 9. PROJECT_INDEX Skeleton

Bootstrap MUST generate a new-project `docs/PROJECT_INDEX.md`.

It must preserve the frozen single-level index model.

The generated index MUST:

- route to pinned Delivery Protocol;
- route to pinned Execution Playbook;
- route to pinned Runtime;
- route to dynamic Runtime state files;
- provide slots/routing for later Product-Specific Authority;
- preserve identity/version/hash semantics where applicable;
- contain no stale current-template project entries.

The 47-entry current project index is evidence/schema input only and MUST NOT be copied as new-project state.

No Domain Index layer may be added.

---

# 10. CURRENT_STATE Skeleton

Bootstrap MUST generate a concise zero-state `docs/CURRENT_STATE.md`.

It must remain:

```text
short
operational
pointer-oriented
current-truth only
```

It MUST be capable of representing:

- current task pointer;
- blocker;
- next step;
- relevant Gate state;
- current control-layer identities/status;
- implementation eligibility state.

It MUST NOT become:

```text
project history
design specification
Planner memo
duplicate PROJECT_INDEX
```

---

# 11. TASK_INDEX Skeleton

Bootstrap MUST generate an empty `docs/tasks/TASK_INDEX.md` using frozen Runtime R1 semantics.

The schema must preserve support for:

```text
task identity
status
hard dependencies
Authority inputs
touch scope
shared resources where applicable
required Gates
allowed/forbidden changes
acceptance
verification
```

Initial task collection MUST be empty.

Priority must not imply dependency.

---

# 12. CURRENT_TASK Zero-State

Bootstrap MUST create:

```text
docs/tasks/CURRENT_TASK.md
```

because frozen Runtime R1 defines it as a required physical core file and part of the always-read bootstrap set.

Frozen Runtime R1 clarification registered by KPS-RT-006 establishes:

```text
CURRENT_STATE.current_task
= canonical current-task selector
```

For a newly initialized project with no current task selected:

```text
CURRENT_STATE.current_task = NONE
```

and:

```text
implementation execution eligibility = FALSE
```

`CURRENT_TASK.md` MUST use one canonical Bootstrap no-task sentinel document.

That sentinel MUST:

```text
clearly state that no current task is selected
contain no fabricated task ID
contain no fabricated Authority
contain no fabricated dependency
contain no fabricated scope
contain no fabricated acceptance criteria
contain no fabricated verification record
not be interpretable as an executable task contract
not conflict with CURRENT_STATE.current_task = NONE
```

Bootstrap validation MUST verify that this sentinel cannot authorize execution.

When:

```text
CURRENT_STATE.current_task != NONE
```

all existing frozen Runtime R1 CURRENT_TASK identity/status/contract matching rules apply unchanged.

---

# 13. FEATURE_MATRIX Zero-State

Bootstrap MUST generate:

```text
docs/product/FEATURE_MATRIX.md
```

This file is MANDATORY for a Runtime R1 bootstrapped project.

It MUST contain no current Kyd template project feature history.

It must preserve Runtime semantics, including:

```text
IMPLEMENTED != VERIFIED
```

No feature may be pre-marked IMPLEMENTED/VERIFIED unless the new project has real evidence.

---

# 14. IMPLEMENTATION_TRACE Zero-State

Bootstrap MUST generate an empty Runtime-conformant implementation trace structure.

It MUST use the frozen Runtime R1 trace schema.

It must not copy any of the existing Kyd template project historical trace records.

No fabricated trace may be introduced.

---

# 15. Runtime Validator

The Runtime validator is a required Bootstrap Pack asset.

KPS-BS-001 established:

```text
Runtime validator portability:
PORTABLE AS-IS
```

Therefore default action is:

```text
KEEP + TEST
```

Bootstrap packaging must install the validator in the standard Runtime path expected by the frozen system.

No Runtime semantic fork may be introduced.

---

# 16. Generic Initialization Mechanism

KPS-BS-001 established:

```text
Current initialization mechanism:
MANUAL ONLY
```

Therefore Bootstrap Pack MUST provide a generic initialization mechanism.

It may be:

```text
script
command
template generator
controlled extraction wrapper
```

but it MUST be capable of producing a clean project instance without manual copy/paste of internal runtime state.

The initializer must:

1. accept/resolve new-project metadata;
2. install pinned static control Authorities;
3. generate dynamic zero-state files;
4. substitute project metadata only where allowed;
5. avoid stale Kyd-template project IDs/history;
6. install Runtime validator;
7. create/record Bootstrap manifest/provenance;
8. run bootstrap-specific validation;
9. fail closed if validation fails.

A human may initiate the command, but should not manually assemble the control layer file-by-file.

---

# 17. Bootstrap Manifest / Provenance

Each initialized project MUST have a machine- or human-readable bootstrap provenance record or equivalent controlled metadata.

It must identify at least:

```text
bootstrap pack version
bootstrap date
Protocol identity/version/hash
Playbook identity/version/hash
Runtime identity/version/hash
initializer/package identity
validation result
```

It must not duplicate dynamic Runtime state.

Its exact file/path is to be chosen during implementation based on repository conventions.

---

# 18. Bootstrap-Specific Validation

KPS-BS-001 established current capability as PARTIAL.

Bootstrap Pack MUST add bounded bootstrap validation beyond generic Runtime validation.

Bootstrap PASS must verify at least:

## Structure

- required files exist;
- required directories resolve;
- standard paths are correct.

## Authority

- Protocol identity/version/hash resolve;
- Playbook identity/version/hash resolve;
- Runtime identity/version/hash resolve;
- PROJECT_INDEX routes them correctly.

## Zero-State

- no current executable task;
- task index is empty/valid;
- trace is empty/valid;
- feature state is clean/valid;
- CURRENT_STATE represents legitimate pre-implementation state.

## Stale Metadata

Reject:

```text
sa-template-specific IDs
AUD-* task/history leakage
STS-* task/history leakage
current Kyd template project state/history
source-template CURRENT_STATE/task/trace data
```

except where literal terms appear only in test fixtures intentionally proving stale-data rejection.

## Agent Neutrality

- AGENTS.md contains no permanent specific-agent binding;
- required universal entry rules are present.

## Runtime

- existing Runtime validation PASS;
- zero-state validation PASS;
- no implementation execution eligibility exists.

## Fresh Session Recovery

- a fresh/replacement agent can recover required project state only from repository-controlled sources.

---

# 19. Bootstrap PASS Definition

A project is not considered safely initialized until:

```text
initializer/package completes
+
bootstrap-specific validation PASS
+
Runtime zero-state validation PASS
```

If bootstrap validation fails:

```text
Project Bootstrap = BLOCKED
Implementation execution = NOT ELIGIBLE
```

No implementation task may be run merely because files were copied successfully.

---

# 20. Source-vs-Template Decisions

## COPY EXACTLY / CONTENT-PRESERVING PINNED INSTALL

```text
Frozen Delivery Protocol R3
Frozen Execution Playbook R3
Frozen Runtime R1
Runtime validator
```

subject to exact hash/integrity validation.

## GENERATE FROM TEMPLATE / SKELETON

```text
AGENTS.md
PROJECT_INDEX.md
CURRENT_STATE.md
TASK_INDEX.md
CURRENT_TASK.md
FEATURE_MATRIX
IMPLEMENTATION_TRACE.md
Bootstrap manifest/provenance
```

## DO NOT PREPOPULATE

```text
Product-Specific Authority
project-specific implementation tasks
project-specific feature truth
implementation traces
release state
business/product decisions
```

---

# 21. Mandatory Bootstrap Pack Contents

The minimum Bootstrap Pack MUST contain or be able to generate/install:

```text
1. Agent-neutral AGENTS.md
2. PROJECT_INDEX skeleton
3. CURRENT_STATE zero-state skeleton
4. TASK_INDEX empty skeleton
5. CURRENT_TASK explicit zero-state form
6. FEATURE_MATRIX zero-state form where required by Runtime R1
7. IMPLEMENTATION_TRACE zero-state form
8. Frozen Delivery Protocol R3
9. Frozen Execution Playbook R3
10. Frozen Runtime V1 R1
11. Runtime validator
12. Generic initializer/packaging mechanism
13. Bootstrap manifest/provenance
14. Bootstrap-specific validation
```

These are normative minimum capabilities.

Exact internal implementation may use fewer physical source-template files if generation produces the same required initialized result.

---

# 22. Optional Bootstrap / Provenance Assets

The following are OPTIONAL PROVENANCE for a newly initialized project and are not required for Bootstrap PASS unless a later controlled Bootstrap version explicitly promotes them:

```text
Delivery Protocol freeze record
Runtime freeze record
Runtime conformance runner
Runtime conformance report
bootstrap README / human operator guide
```

They may be included when useful for provenance, validation maintenance, or operator support.

They MUST NOT be treated as mandatory merely for ceremony.

The mandatory frozen Authorities themselves remain:

```text
Delivery Protocol R3
Execution Playbook R3
Runtime V1 R1
```

---

# 23. Do-Not-Include Set

The Bootstrap Pack MUST NOT carry project-instance historical state from the current Kyd template project.

Do not include as initialized project truth:

```text
current CURRENT_STATE contents
current TASK_INDEX history
current CURRENT_TASK terminal snapshot
current FEATURE_MATRIX project truth
current IMPLEMENTATION_TRACE history
AUD-* task graphs/history
STS-* task graphs/history
sa-template-specific metadata
Starter implementation history
Product-Specific Authority
Planner Memory
application code unless separately selected as the code-template layer
```

The code-template layer and Project Bootstrap Pack are conceptually separate, even when a project initialization workflow applies both.

---

# 24. Code Template Separation

Project Bootstrap Pack initializes the Kyd control/execution layer.

SaaS/application code template selection initializes the product code foundation.

They may be executed in one project-creation workflow, but they remain distinct sources:

```text
Code Template
= application/reusable code capability

Bootstrap Pack
= Kyd governance/execution control layer
```

The Bootstrap Pack must remain usable for non-SaaS projects.

---

# 25. Control-Layer Upgrade Rule

A project initialized against a frozen control set must remain pinned until an explicit controlled upgrade.

Example:

```text
Project created with:
Protocol R3
Playbook R3
Runtime R1
```

A future Kyd template repository update must NOT silently change that project to newer Authorities.

Upgrade requires an explicit migration/reconciliation step with validation.

---

# 26. Agent Replacement Requirement

Bootstrap is successful only if agent continuity does not depend on hidden reasoning.

A replacement agent must be able to recover from:

```text
AGENTS.md
PROJECT_INDEX.md
CURRENT_STATE.md
CURRENT_TASK.md
task-declared Authorities
task/dependency state
verification/trace evidence
```

No predecessor conversation is required as execution truth.

---

# 27. Minimal-Delta Mapping From KPS-BS-001

KPS-BS-001 established:

```text
BS-GAP-01 neutral universal entry contract
→ PATCH

BS-GAP-02 generated Runtime skeletons
→ PATCH

BS-GAP-03 explicit CURRENT_TASK zero-state convention
→ PATCH

BS-GAP-04 generic packaging/initialization mechanism
→ WRAP

BS-GAP-05 bootstrap-specific acceptance validation
→ WRAP
```

No architecture change is required.

Existing frozen Protocol, Playbook, Runtime, validator, hash-locking model, single-level routing, zero-state capability, and fresh-session recovery are to be reused.

---

# 28. Bootstrap Acceptance Criteria

A candidate Bootstrap implementation is acceptable only if an isolated test project proves:

```text
A. required initialized file set exists
B. Protocol / Playbook / Runtime pinned identities resolve
C. hashes match
D. PROJECT_INDEX routing is valid
E. AGENTS.md is agent-neutral and contains required entry rules
F. CURRENT_STATE is clean zero-state
G. TASK_INDEX is clean/empty
H. CURRENT_TASK cannot authorize execution
I. FEATURE_MATRIX is clean zero-state where required
J. IMPLEMENTATION_TRACE is clean/empty
K. no stale template-project metadata exists
L. Runtime validator PASS
M. bootstrap-specific validator PASS
N. implementation eligibility remains false
O. fresh-session recovery PASS
```

---

# 29. Implementation Boundary

The eventual implementation step may create:

```text
bootstrap source templates
generic initializer/wrapper
bootstrap validation
test fixture/new-project sandbox
operator README if useful
```

It must not modify frozen Protocol/Playbook/Runtime semantics.

If implementation reveals a semantic gap in a frozen Authority:

```text
BLOCKED
→ return to controlled Authority change
```

Do not silently fix it in Bootstrap code.

---

# 30. Candidate Freeze Criteria

This Bootstrap Packaging Specification Candidate R3 may become frozen only after independent review confirms:

1. mandatory initialized project structure is sufficient;
2. static-vs-dynamic classification is correct;
3. pinned frozen Authority requirement is explicit;
4. dynamic state cannot leak from template project;
5. zero-state cannot accidentally authorize implementation;
6. AGENTS.md contract is agent-neutral and sufficiently strict;
7. Runtime validator reuse is preserved;
8. bootstrap-specific validation is sufficient;
9. fresh-session recovery is preserved;
10. no SaaS/application-specific coupling exists;
11. code-template and control-bootstrap responsibilities remain separate;
12. no unnecessary architecture layer was added;
13. implementation can remain bounded to PATCH/WRAP actions proven by KPS-BS-001.

Until then:

```text
Status = CANDIDATE / NOT FROZEN
```


---

# 31. Candidate R3 Revision Record

Candidate R2 makes only the revisions required by KPS-BS-003 and the repository fact-check / Runtime clarification sequence KPS-BS-004 through KPS-RT-006.

Resolved items:

```text
MAJOR:
CURRENT_TASK zero-state is now grounded in frozen Runtime R1 clarification.

MINOR:
FEATURE_MATRIX exact mandatory path is fixed as:
docs/product/FEATURE_MATRIX.md

Optional provenance classification is fixed for:
- Delivery Protocol freeze record
- Runtime freeze record
- Runtime conformance runner
- Runtime conformance report
```

No architecture change was introduced.

No Bootstrap implementation was performed.

No Delivery Protocol / Playbook semantic change was introduced.

Runtime remains:

```text
RUNTIME-001 / R1 / FROZEN
```

with the KPS-RT-006 CURRENT_TASK zero-state clarification effective.


---

# 32. Candidate R3 Local Revision Record

Candidate R3 changes only the three conditional-reading inconsistencies identified by KPS-BS-006.

Resolved wording:

```text
1. CURRENT_TASK.md is unconditionally always-read in the bootstrap chain.
2. The physical always-read file is distinguished from task-contract activation:
   - current_task = NONE → canonical no-task sentinel; no task contract active; execution ineligible
   - current_task != NONE → CURRENT_TASK.md is the active task boundary
3. Replacement-agent recovery always includes CURRENT_TASK.md; "when applicable" was removed.
```

No Bootstrap architecture change was introduced.

No Runtime semantic change was introduced.

No validator change was introduced.

No mandatory project-initialization requirement was weakened.
