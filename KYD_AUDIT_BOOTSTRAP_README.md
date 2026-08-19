# Kyd sa-template Full Repository Audit Bootstrap R1

This pack instantiates the frozen Kyd Project Runtime V1 for the first real use case: Full Repository Audit of `sa-template`.

## Destination

Extract the ZIP into the **repository root** — the directory that contains the project's `package.json` / `.git`.

After extraction the important paths must be:

```text
<sa-template-root>/AGENTS.md
<sa-template-root>/docs/PROJECT_INDEX.md
<sa-template-root>/docs/CURRENT_STATE.md
<sa-template-root>/docs/tasks/TASK_INDEX.md
<sa-template-root>/docs/tasks/CURRENT_TASK.md
<sa-template-root>/docs/audit/SA_TEMPLATE_AUDIT_AUTHORITY.md
<sa-template-root>/tools/kyd_runtime_validate.py
```

Do NOT extract into `docs/` or into a nested `sa_template_Kyd_.../` directory.

## Before extraction: existing AGENTS.md

If the repository already has `AGENTS.md`, preserve it first:

```bash
cp AGENTS.md AGENTS.pre-kyd-audit.md
```

The new Runtime `AGENTS.md` explicitly instructs Codex to read that preserved file too.

## Initial validation

From repository root:

```bash
python3 tools/kyd_runtime_validate.py --root . --mode execution
```

Expected:

```text
KYD_RUNTIME_VALIDATE: PASS
MODE = execution
EXECUTION_ALLOWED = TRUE
```

The initial active Task is:

```text
AUD-000 — Repository Inventory / Audit Bootstrap
```

Do not manually activate AUD-010 before AUD-000 is VERIFIED.
