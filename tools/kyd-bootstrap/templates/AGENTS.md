# AGENTS.md

## Kyd Repository Entry Contract

This repository is governed by repository-controlled Authority. Chat history,
model memory, and external planning memory are context only and do not override
the controlled repository state.

### Mandatory Bootstrap

Before changing any file, always read and validate in this order:

```text
1. AGENTS.md
2. docs/PROJECT_INDEX.md
3. docs/CURRENT_STATE.md
4. docs/tasks/CURRENT_TASK.md
5. Task-declared Authority inputs, when a current task is selected
6. Required Runtime validation and execution-eligibility checks
```

`docs/PROJECT_INDEX.md` is the single Authority and navigation entry point.
`docs/CURRENT_STATE.md` is the current repository truth.
`docs/tasks/CURRENT_TASK.md` is always read as the current task boundary or
the canonical no-task sentinel.

When `CURRENT_STATE.current_task = NONE`:

```text
no current task is selected
CURRENT_TASK is the no-task sentinel
no task contract is active
execution eligibility is FALSE
```

When a current task is selected, load only its declared Authority inputs and
execute only its registered contract after Runtime execution validation passes.

### Execution Rules

- Repository-controlled Authority takes precedence over chat or model memory.
- Planner Memory and chat history are not Runtime Authority.
- Deny-by-default applies to execution, dependencies, Authority, Gates, scope,
  and file changes.
- Dependencies must be explicit and satisfied exactly as Runtime requires.
- Missing, mismatched, or conflicting Authority, dependency, Gate, or scope is
  `BLOCKED`; do not infer or invent a resolution.
- Do not silently expand task scope or modify undeclared files and resources.
- Do not invent product, design, business, or acceptance semantics during
  implementation.
- Frozen Authority must not be silently modified or superseded.
- `IMPLEMENTED != VERIFIED`; implementation completion does not replace
  independent verification or required evidence.

### Session Recovery

Replacement executors recover state from `AGENTS.md`, `PROJECT_INDEX`,
`CURRENT_STATE`, `CURRENT_TASK`, task-declared Authority, dependency state, and
repository verification evidence. Hidden prior reasoning is never required for
safe continuation.
