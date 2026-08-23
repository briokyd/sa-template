# Kyd Project Runtime V1 Minimal Spec — R1

> **System Layer:** C — Kyd Project Runtime  
> **Purpose:** Deterministic, index-driven execution for Codex sessions  
> **Status:** FROZEN — Runtime V1 R1 conformance verified
> **Date:** 2026-08-19  
> **Controlled Reconciliation Date:** 2026-08-22
> **CURRENT_TASK Zero-State Clarification Date:** 2026-08-23
> **Conformance Evidence:** `KPR-V1-R1-CONFORMANCE-20260822`
> **Source Decisions:** RT-001 ～ RT-007 FROZEN  
> **Planning Memory:** `Kyd_Project_System_完整合并备忘录` is NOT a normal Codex input.

---

# 1. System Position

```text
A. Kyd SaaS Starter
   = reusable CODE

B. Kyd Delivery Protocol
   = reusable PROCESS

C. Kyd Project Runtime
   = reusable EXECUTION ENGINE   ← THIS SPEC

D. Product-Specific Design
   = variable PRODUCT DEFINITION
```

Delivery Protocol decides:

```text
what phases exist
what artifacts are required
what must be frozen
what gates must exist
what changes require approval
```

Project Runtime decides:

```text
what the current Codex session reads
what task is executable
what Authority versions apply
what dependencies/gates must pass
what scope is allowed
how state is closed out for a fresh session
```

Runtime does not replace Delivery Protocol or Product-Specific Design.

---

# 2. V1 Core Principles

```text
Single-Level PROJECT_INDEX
+
Small Mandatory Bootstrap
+
Preplanned Full Task Contracts
+
Task-Pinned Authority Versions
+
On-Demand Exact Authority Loading
+
Explicit Dependency Only
+
Deny By Default
+
Canonical Gate State
+
Deterministic Validator
+
Repository Closeout
```

Hard rules:

1. Chat history is not Authority.
2. Resume Session is convenience only.
3. `Kyd_Project_System_完整合并备忘录` is planning memory, not Runtime Authority.
4. V1 uses exactly one `PROJECT_INDEX`; no Domain INDEX.
5. Implementation Codex does not invent missing task metadata.
6. Every dependency in V1 requires the dependency Task to be `VERIFIED`.
7. Required Gate state has one canonical source.
8. Mandatory Authority versions are exact-pinned by each Task.
9. Frozen Authority content is hash-locked.
10. Any ambiguity that can affect execution means BLOCKED.
11. Runtime V1 does not build a workflow engine or automatic dependency inference.

---

# 3. Runtime V1 Core Files

Every Runtime-enabled project has:

```text
AGENTS.md

docs/
├── PROJECT_INDEX.md
├── CURRENT_STATE.md
├── product/
│   └── FEATURE_MATRIX.md
├── tasks/
│   ├── TASK_INDEX.md
│   └── CURRENT_TASK.md
└── execution/
    └── IMPLEMENTATION_TRACE.md

tools/
└── kyd_runtime_validate.py
```

Delivery Protocol / Product-Specific Design may create additional Authority files.

Any formal Authority consumed by Runtime must be registered directly in `PROJECT_INDEX`.

---

# 4. Machine Data Format

Runtime V1 project Markdown files use a deterministic JSON data block:

```text
<!-- KYD_RUNTIME_DATA_START -->
{ ... valid JSON ... }
<!-- KYD_RUNTIME_DATA_END -->
```

Rules:

- exactly one Runtime data block per Runtime core file;
- the block must be valid JSON;
- Runtime Validator parses only the block for machine checks;
- human-readable Markdown outside the block may explain content but cannot override the JSON;
- unresolved placeholders such as `<TASK_ID>` are invalid in instantiated project Runtime data.

Reason:

```text
human-readable Markdown
+
strict machine-readable data
+
no YAML parser dependency
```

---

# 5. RT-001 — PROJECT_INDEX

## 5.1 Routing

V1 routing is only:

```text
PROJECT_INDEX
→ Exact Authority / Evidence
```

Forbidden:

```text
PROJECT_INDEX
→ Domain INDEX
→ ...
```

There is no model decision about index hierarchy in V1.

## 5.2 Entry Schema

Each entry contains:

```text
authority_id
area
name
path
kind
version
status
sha256
purpose
```

`kind` fixed enum:

```text
AUTHORITY
EVIDENCE
```

`status` fixed enum:

```text
DRAFT
ACTIVE
FROZEN
SUPERSEDED
RETIRED
```

Rules:

- `authority_id` unique;
- `path` must exist;
- `version` must be explicit;
- `kind=AUTHORITY` means it may be used as mandatory task Authority;
- `kind=EVIDENCE` cannot be a mandatory task Authority;
- mandatory task Authority status must be `ACTIVE` or `FROZEN`;
- `FROZEN` requires exact `sha256`;
- `SUPERSEDED` / `RETIRED` cannot be mandatory for a new/current Task;
- grouping by `area` is readability only.

## 5.3 Frozen Content Lock

For every:

```text
status = FROZEN
```

`sha256` is mandatory.

Validator computes SHA-256 of the file bytes and requires an exact match.

Changing frozen content requires:

```text
explicit Authority update
+
new version
+
new sha256
+
Task version updates where applicable
```

No silent frozen-file edits.

## 5.4 Authority Conflict

If Codex detects contradictory requirements among mandatory Authorities:

```text
BLOCKED — AUTHORITY_CONFLICT
```

Runtime V1 has no automatic precedence resolution.

The conflict must return to Planning / Authority Maintenance.

---

# 6. RT-002 — FEATURE_MATRIX

File:

```text
docs/product/FEATURE_MATRIX.md
```

Fixed fields per feature:

```text
feature_id
name
scope
priority
status
authority
implementation
verification
```

Fixed status enum:

```text
NOT_STARTED
READY
IN_PROGRESS
IMPLEMENTED
VERIFIED
BLOCKED
DEFERRED
OUT_OF_SCOPE
```

Hard semantic:

```text
IMPLEMENTED != VERIFIED
```

`IMPLEMENTED` = implementation exists.

`VERIFIED` = declared acceptance / verification / required Gate has passed.

No percentages or fuzzy completion states.

---

# 7. RT-003 — CURRENT_STATE

File:

```text
docs/CURRENT_STATE.md
```

Purpose:

```text
Current Pointer
+
Canonical Gate State
+
Current Blockers
+
Next Step
```

Machine fields:

```text
project
starter_version
delivery_profile
runtime_version
product_freeze_version
ui_freeze_version
current_phase
current_task
last_verified_commit
blocked
gates
known_deviations
next_task
release_status
```

## 7.1 Canonical Gate Registry

`CURRENT_STATE.gates` is the Runtime V1 canonical Gate-status source.

Each entry:

```text
gate_id
status
evidence
```

Gate status enum:

```text
NOT_RUN
PASS
FAIL
BLOCKED
NOT_APPLICABLE
```

Rules:

- `gate_id` unique;
- every `CURRENT_TASK.gates_required` ID must exist here;
- every required Gate must have `status=PASS`;
- `NOT_APPLICABLE` never satisfies `gates_required`;
- evidence is a list of registered Authority/Evidence IDs or repository paths, as defined by Delivery Protocol.

There is no separate `open_gates` field in R1; it would duplicate canonical Gate state.

## 7.2 Current Pointer Rules

`current_task` is:

```text
a Task ID
or
NONE
```

`next_task` is:

```text
a Task ID
NONE
BLOCKED
```

If a Task ID is used, it must exist in `TASK_INDEX`.

`CURRENT_STATE` does not store full task history.

---

# 8. RT-004 — TASK_INDEX

File:

```text
docs/tasks/TASK_INDEX.md
```

Purpose:

```text
All Planned Tasks
+
Full Preplanned Execution Contracts
+
Task Status
+
Explicit Dependency Graph
```

## 8.1 Why Full Contracts Live Here

Implementation must not decide its own:

```text
authority_inputs
depends_on
touches
shared_resources
gates_required
allowed_changes
forbidden_changes
acceptance
verification
```

Therefore every planned Task stores the full contract in `TASK_INDEX` before it becomes executable.

## 8.2 Task Entry

Each Task has:

```text
task_id
title
type
status
contract
```

`contract` contains:

```text
goal
depends_on

authority_inputs:
  mandatory
  reference

touches
shared_resources
gates_required

allowed_changes
forbidden_changes

acceptance
verification
```

Task status enum:

```text
NOT_READY
READY
IN_PROGRESS
IMPLEMENTED
VERIFIED
BLOCKED
DEFERRED
CANCELLED
```

## 8.3 Dependency Rule

In Runtime V1:

```text
every task_id in depends_on
MUST have status VERIFIED
```

No partial-satisfaction exception exists in V1.

If work can safely proceed without a Task being VERIFIED, that Task must not be declared as a dependency; Planning must define the graph correctly before implementation.

## 8.4 Dependency Cycles

Validator must reject any dependency cycle.

Example:

```text
TASK-A -> TASK-B -> TASK-A
```

Result:

```text
DEPENDENCY_GAP
EXECUTION_ALLOWED = FALSE
```

---

# 9. RT-004 — CURRENT_TASK

File:

```text
docs/tasks/CURRENT_TASK.md
```

Purpose:

```text
low-context execution snapshot
of one already-planned TASK_INDEX contract
```

Machine structure:

```text
project
runtime_version

task_id
status

contract
verification_evidence
```

The `contract` must exactly match the same Task's contract in `TASK_INDEX`.

Implementation Codex cannot alter the contract.

Status in `CURRENT_TASK` must equal the same Task status in `TASK_INDEX`.

## 9.1 Authority Input Schema

Every input is version-pinned:

```text
{
  "authority_id": "UI-002",
  "version": "v3"
}
```

Mandatory inputs:

- must resolve in `PROJECT_INDEX`;
- `kind` must be `AUTHORITY`;
- version must exactly match;
- status must be `ACTIVE` or `FROZEN`;
- if `FROZEN`, file hash must verify.

Reference inputs:

- must resolve in `PROJECT_INDEX`;
- version must exactly match;
- may reference `AUTHORITY` or `EVIDENCE`;
- cannot override mandatory Authority.

`mandatory` may be empty only when the preplanned Task contract genuinely has no additional formal Authority beyond Runtime files.

## 9.2 Executable CURRENT_TASK Status

Execution-mode behavior:

```text
READY
→ executable
→ must become IN_PROGRESS before code modification

IN_PROGRESS
→ executable / resumable

IMPLEMENTED
→ executable only for declared verification and necessary task-scoped fixes

VERIFIED
→ no further task execution
→ another Task must be activated before new implementation

BLOCKED
NOT_READY
DEFERRED
CANCELLED
→ execution forbidden
```

## 9.3 One Primary Task

One `CURRENT_TASK` = one primary `task_id`.

No “while here” expansion to unrelated tasks.

## 9.4 CURRENT_TASK Zero-State

`docs/tasks/CURRENT_TASK.md` remains a required physical Runtime core file and part of
the always-read bootstrap set.

`CURRENT_STATE.current_task` is the canonical selector for whether a current Task is
selected.

When:

```text
CURRENT_STATE.current_task = NONE
```

the Runtime semantics are:

```text
no current Task is selected
no Task contract is active through CURRENT_TASK
implementation execution eligibility is FALSE
CURRENT_TASK content cannot create or imply execution eligibility
no fake Task ID, Authority, dependency, scope, acceptance, or verification is required
```

In this state, `CURRENT_TASK.md` may use a canonical no-Task sentinel document rather
than a Task contract. The Kyd Project Bootstrap Pack may standardize that sentinel only
when it:

```text
clearly states that no current Task is selected
contains no fabricated Task or Authority data
does not conflict with CURRENT_STATE.current_task = NONE
cannot be interpreted as an executable Task contract
```

Runtime validation continues to treat `CURRENT_STATE.current_task = NONE` as the
authoritative execution selector and need not parse Task-contract fields from
`CURRENT_TASK.md` in this state.

When `CURRENT_STATE.current_task != NONE`, all existing Runtime R1 CURRENT_TASK
identity, status, contract, dependency, Authority, Gate, scope, acceptance, and
verification rules remain unchanged.

This clarification records the zero-state behavior fact-checked by `KPS-BS-004` and
independently reviewed by `KPS-RT-005`. It does not change Runtime semantics or
architecture.

---

# 10. Task Scope Fields

## 10.1 touches

Explicit anticipated task surface:

```text
routes
components
files
data
api
other
```

Empty arrays are allowed when a category does not apply.

## 10.2 shared_resources

Explicit list.

At minimum Planning must consider:

```text
database schema / migration
API contract
auth / session
payment / entitlement
shared UI
shared asset
global config / env
routing / middleware
common state / store
```

No shared resource:

```text
[]
```

Unknown shared impact:

```text
BLOCKED
```

## 10.3 allowed_changes / forbidden_changes

Both must be explicit and non-empty for executable Tasks.

Recommended default boundary:

```text
forbidden_changes:
- Any change outside allowed_changes unless a new Planning-approved Task contract is created.
```

## 10.4 acceptance / verification

Both must be explicit and non-empty before a Task can become `READY`.

---

# 11. RT-005 — Authority Loading Algorithm

Every execution Session:

```text
SESSION START

1. Read AGENTS.md
2. Read docs/PROJECT_INDEX.md
3. Read docs/CURRENT_STATE.md
4. Read docs/tasks/CURRENT_TASK.md

5. Run Runtime Validator in execution mode.

6. Resolve CURRENT_TASK contract:
   - depends_on
   - authority_inputs
   - touches
   - shared_resources
   - gates_required
   - allowed_changes
   - forbidden_changes
   - acceptance
   - verification

7. Load every mandatory Exact Authority
   directly through PROJECT_INDEX.

8. Load only declared reference inputs when needed.

9. If mandatory Authorities conflict:
   BLOCKED — AUTHORITY_CONFLICT

10. Inspect only code relevant to CURRENT_TASK.

11. Execute CURRENT_TASK only.

12. Run declared verification.

13. Record verification evidence / Implementation Trace.

14. Session Closeout.
```

Codex may not use “read all docs” as a substitute for task-declared Authority routing.

---

# 12. RT-006 — Mandatory Bootstrap

Always-read:

```text
AGENTS.md
PROJECT_INDEX.md
CURRENT_STATE.md
CURRENT_TASK.md
```

Then Exact Authority on demand.

Context-budget target:

```text
Always-read human/runtime content should stay approximately <= 300 lines
before Exact Authority loading.
```

This is a maintenance target, not a hard token limit.

Explanatory material belongs in this Spec / Template-Pack README, not duplicated into every project Runtime file.

Before code modification:

```text
Runtime Validator execution mode MUST PASS
```

---

# 13. RT-006 — Session Closeout

Before ending an execution Session:

```text
1. Update CURRENT_TASK status.
2. Update the same Task status in TASK_INDEX.
3. Record verification_evidence.
4. Update IMPLEMENTATION_TRACE.
5. Update FEATURE_MATRIX where the Task changes feature state.
6. Update CURRENT_STATE:
   - current_task
   - blockers
   - canonical gates if this Task owns Gate evidence
   - last_verified_commit when applicable
   - next_task
   - release_status when applicable
7. Run Runtime Validator closeout/structure validation.
```

Chat summary cannot replace Repository Closeout.

Git commit granularity is owned by Delivery Protocol / Git policy, not Runtime.

---

# 14. Task Activation

Task activation is a mechanical Runtime operation, not an implementation-design decision.

A Task may be activated only if:

```text
Task exists in TASK_INDEX
status == READY
full contract exists
contract validates
all dependencies == VERIFIED
all required Gates == PASS
all mandatory Authority versions resolve
```

Activation copies the preplanned Task contract into `CURRENT_TASK` and sets:

```text
CURRENT_STATE.current_task = task_id
```

Implementation Codex must not construct a new Task contract during activation.

If the current Task is `VERIFIED` and `CURRENT_STATE.next_task` names a READY Task, the next Task still requires this mechanical activation step before execution.

---

# 15. IMPLEMENTATION_TRACE

File:

```text
docs/execution/IMPLEMENTATION_TRACE.md
```

Purpose:

```text
Requirement / Feature / Design
→ Task
→ Implementation
→ Verification
→ Evidence
```

Each trace:

```text
trace_id
source_id
task_id
implementation
verification
evidence
status
```

Trace status:

```text
OPEN
IMPLEMENTED
VERIFIED
BLOCKED
SUPERSEDED
```

`VERIFIED` requires concrete verification and evidence.

---

# 16. RT-007 — Dependency / Gate Enforcement

Model:

```text
LOCAL BLOCKING
+
DENY BY DEFAULT
+
EXPLICIT DEPENDENCY ONLY
```

Any of:

```text
task manifest incomplete
dependency missing
dependency ambiguous
dependency cycle
dependency status != VERIFIED
mandatory authority missing
mandatory authority version mismatch
mandatory authority invalid status/kind
frozen authority hash mismatch
authority conflict
required gate missing
required gate != PASS
shared-resource impact unknown
current-task/task-index contract mismatch
runtime state inconsistency
```

means:

```text
EXECUTION_ALLOWED = FALSE
```

Allowed gap/failure classes:

```text
RUNTIME_SCHEMA_INVALID
AUTHORITY_GAP
AUTHORITY_CONFLICT
TASK_GAP
DEPENDENCY_GAP
GATE_FAILURE
STATE_INCONSISTENCY
TRACE_GAP
```

Codex has no waiver authority.

---

# 17. Validator Contract

Validator is part of C — Project Runtime.

It is not a separate system layer.

## 17.1 Required Checks

### Core Files

```text
AGENTS exists
PROJECT_INDEX exists and parses
CURRENT_STATE exists and parses
FEATURE_MATRIX exists and parses
TASK_INDEX exists and parses
CURRENT_TASK exists and parses when current_task != NONE
IMPLEMENTATION_TRACE exists and parses
```

### Schema / Identity

```text
runtime_schema exact
project consistent across Runtime files
runtime_version consistent across Runtime files
no unresolved <...> placeholders in machine data
```

### PROJECT_INDEX

```text
authority_id unique
kind enum valid
status enum valid
path exists
version present
FROZEN requires sha256
FROZEN sha256 matches
```

### CURRENT_STATE / Gates

```text
gate_id unique
gate status enum valid
current_task valid
next_task valid
```

### TASK_INDEX

```text
task_id unique
status enum valid
full contract present
dependency IDs exist
no dependency cycle
READY contract complete
```

### CURRENT_TASK

```text
task exists in TASK_INDEX
contract exactly matches TASK_INDEX
status matches TASK_INDEX
mandatory authority exact version resolves
mandatory kind/status valid
reference exact version resolves
depends_on all VERIFIED
required gates all exist and PASS
scope/acceptance/verification complete
```

### Cross-State

```text
CURRENT_STATE.current_task == CURRENT_TASK.task_id
or current_task == NONE

CURRENT_STATE project/runtime match all Runtime files
```

## 17.2 Validator Modes

Reference implementation supports:

```text
structure
execution
closeout
```

`structure`:

- validates repository Runtime consistency;
- does not claim a Task is executable.

`execution`:

- requires a current Task;
- requires an executable status;
- requires all dependency/Authority/Gate checks to PASS.

`closeout`:

- validates consistency after task state/evidence updates;
- permits terminal or blocked current states.

## 17.3 Exit Behavior

Hard failure:

```text
exit != 0
EXECUTION_ALLOWED = FALSE
```

Execution-mode PASS:

```text
exit == 0
EXECUTION_ALLOWED = TRUE
```

---

# 18. Runtime Data vs Human Notes

Machine execution decisions come only from:

```text
KYD_RUNTIME_DATA JSON blocks
+
registered Exact Authority content
```

Human Markdown notes may explain but cannot override machine fields.

If notes and machine data conflict:

```text
STATE_INCONSISTENCY
```

and Planning must correct it.

---

# 19. Runtime / Delivery Boundary

Runtime does not decide whether a project should have:

```text
UI_USER_FLOW
UI_STATE_MATRIX
ASSET_MANIFEST
PAYMENT_SPEC
SEO_SPEC
```

Delivery Protocol Artifact Policy decides what must exist.

Once such a file becomes formal Authority:

```text
register it in PROJECT_INDEX
pin it in Task contracts when required
Runtime validates and loads it
```

---

# 20. Runtime / Starter Boundary

Using SaaS Starter:

```text
A USED
B USED
C USED
D USED
```

Not using SaaS Starter:

```text
A NOT USED
B USED
C USED
D USED
```

Runtime has no Next.js / Cloudflare / PostgreSQL dependency.

The supplied validator is a reference enforcement implementation of the Runtime contract, not an application runtime dependency.

---

# 21. Non-Goals

V1 does not introduce:

```text
Domain INDEX
multi-level index
workflow engine
automatic dependency inference
automatic task planning
automatic Authority conflict resolution
dashboard
database-backed project Runtime
request-level orchestration service
```

---

# 22. Freeze Gate

Kyd Project Runtime V1 Minimal Freeze requires:

```text
RT-001 ～ RT-007 represented
R0 Critical/High audit findings closed
schemas deterministic
canonical Gate state exists
dependency satisfaction exact
Authority versions pinned
Frozen Authority lock enforced
Task contracts preplanned
CURRENT_TASK contract checked against TASK_INDEX
validator executable
positive conformance fixture PASS
negative fixtures FAIL as expected
Fresh Session execution simulation PASS
no Domain INDEX
no implementation-critical rule exists only in chat
```

After PASS:

```text
Kyd Project Runtime V1 Minimal Freeze
```

First real use:

```text
sa-template Full Repository Audit
```

---

## DOCUMENT STATUS

```text
Document:
Kyd Project Runtime V1 Minimal Spec R1

System Layer:
C — Kyd Project Runtime

RT-001 ～ RT-007:
FROZEN

R0 Audit Corrections:
INTEGRATED

Runtime Alignment Audit:
PASS — KPS-RT-001

Runtime Conformance Repair / Evidence:
PASS — KPS-RT-002 / KPR-V1-R1-CONFORMANCE-20260822

Freeze Status:
FROZEN — R1

Controlled Reconciliation Date:
2026-08-22

CURRENT_TASK Zero-State Clarification:
FROZEN — KPS-RT-006 / 2026-08-23

Semantic / Architecture Change:
NONE

First Real Use:
sa-template Full Repository Audit — COMPLETE
```
