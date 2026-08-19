# AGENTS.md

## Kyd Project Runtime V1 — sa-template Full Repository Audit Pilot

This branch is running the first real Kyd Project Runtime V1 pilot: the Full Repository Audit of `sa-template` for Kyd SaaS Starter.

### Mandatory Bootstrap

Before modifying any file:

```text
1. Read AGENTS.md
2. Read docs/PROJECT_INDEX.md
3. Read docs/CURRENT_STATE.md
4. Read docs/tasks/CURRENT_TASK.md
5. Run: python3 tools/kyd_runtime_validate.py --root . --mode execution
6. Load only CURRENT_TASK-declared Exact Authority/reference inputs
7. Execute CURRENT_TASK only
```

If execution validation fails:

```text
DO NOT MODIFY CODE
```

### Audit branch hard rule

During AUD-000 through AUD-080:

```text
APPLICATION / PRODUCT IMPLEMENTATION CHANGES = FORBIDDEN
```

You may inspect any repository file required for factual audit evidence.

You may modify only:

```text
docs/audit/**
docs/CURRENT_STATE.md
docs/product/FEATURE_MATRIX.md
docs/tasks/TASK_INDEX.md
docs/tasks/CURRENT_TASK.md
docs/execution/IMPLEMENTATION_TRACE.md
```

Do not fix discovered product/platform defects during the audit. Record them.

### Runtime hard rules

- Chat history and resume are not Authority.
- V1 has one `PROJECT_INDEX`; no Domain INDEX.
- Do not invent missing Task metadata, dependencies, Authority, Gate state, or shared-resource independence.
- Any execution ambiguity is BLOCKED.
- Every `depends_on` Task must be `VERIFIED`.
- Mandatory Authority version must match exactly.
- FROZEN Authority SHA-256 mismatch is BLOCKED.
- A mandatory Authority conflict is `AUTHORITY_CONFLICT / BLOCKED`; do not choose precedence yourself.
- Do not change the preplanned Task contract during implementation/audit execution.
- CURRENT_TASK.contract must exactly match TASK_INDEX.
- Do not expand work outside `allowed_changes`.

### Audit authority

Every Audit Task has mandatory Authority:

```text
AUDIT-001
= docs/audit/SA_TEMPLATE_AUDIT_AUTHORITY.md
```

Follow its fixed Action taxonomy exactly.

### Deterministic Task sequence

```text
AUD-000
→ AUD-010
→ AUD-020
→ AUD-030
→ AUD-040
→ AUD-050
→ AUD-060
→ AUD-070
→ AUD-080
```

Do not reorder, parallelize, or skip Tasks during this first Runtime pilot.

### Closeout

At successful Task closeout:

```text
1. Finish only the designated audit output(s)
2. Add verification evidence / IMPLEMENTATION_TRACE
3. Mark current Task VERIFIED in TASK_INDEX
4. Update the related FEATURE_MATRIX item to VERIFIED
5. If not AUD-080:
   - move only the exact next Task from NOT_READY to READY
   - replace CURRENT_TASK with an exact low-context snapshot of that next Task contract
   - update CURRENT_STATE.current_task to that next Task
   - update CURRENT_STATE.next_task to the following Task (or NONE for AUD-080)
6. If AUD-000 passes, set CURRENT_STATE.gates[AUDIT_BOOTSTRAP] = PASS with evidence
7. If AUD-080 passes, set CURRENT_STATE.current_task = NONE and next_task = NONE
8. Run: python3 tools/kyd_runtime_validate.py --root . --mode closeout
```

If acceptance/verification does not pass, do not activate the next Task. Set explicit BLOCKED state and evidence.

### Existing AGENTS instructions

If installation preserved a previous repository instruction file as `AGENTS.pre-kyd-audit.md`, read it immediately after this file. If it conflicts with this frozen Audit/Runtime execution contract in a way that affects execution, report `AUTHORITY_CONFLICT` and BLOCK.
