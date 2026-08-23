# BS-IMPL-030 Evidence

- Step ID: `BS-IMPL-030`
- Pre-step HEAD: `60510ab8278bf93a9c2e8950abb0a1fbbc581b1b`
- Bootstrap validator: `tools/kyd_bootstrap_validate.py`
- Bootstrap validator SHA-256: `a0485f335fb3e0faaf99a44142c32c38912e80ac725ce644a15d7f2540d7ae1d`
- Initializer: `tools/kyd-bootstrap/init_project.py`
- Initializer SHA-256: `efa5e65dfb16e4a3f8e888fd6a675fd888bd172f4a548a8868c40bf9447a0bb5`
- Source manifest SHA-256: `a4185032b8c8daa756a338b28e39ba6533f93c20c598333aad94620dc8e20da0`

## Integration

- The generated project installs `tools/kyd_bootstrap_validate.py` from an exact pinned source hash.
- The Bootstrap validator invokes the generated project-local `tools/kyd_runtime_validate.py` for Runtime structure, closeout, and execution checks.
- Runtime execution rejection at `current_task=NONE` is accepted only with the canonical `TASK_GAP` and `EXECUTION_ALLOWED = FALSE` evidence.
- The initializer leaves `KYD_BOOTSTRAP_MANIFEST.json` at `PENDING` during validation and records `PASS` only after Bootstrap and wrapped Runtime validation succeed.
- Validation failure exits non-zero and cannot finalize the manifest as `PASS`.

## Positive Verification

- Command: `python3 tools/kyd-bootstrap/init_project.py --project-id bs030-final --target TEMP_TARGET`
- Initializer result: PASS
- Mandatory generated files: `13/13` - PASS
- Pinned Protocol, Playbook, Runtime, Runtime validator, and Bootstrap validator hashes: PASS
- Generated Runtime structure: PASS
- Generated Runtime closeout: PASS
- Generated Runtime execution at `current_task=NONE`: expected rejection, exit `2` - PASS
- Bootstrap-specific validation: PASS
- Final manifest `validation_state`: `PASS`
- Final manifest validation evidence: Runtime structure PASS, Runtime closeout PASS, Runtime execution eligibility FALSE, Bootstrap PASS
- Forced generated-validator failure in a disposable source copy: initializer exit `2`, target manifest remained `PENDING` - PASS

## Negative Verification

Each case used a separate disposable copy of a valid generated project.

| Case | Mutation | Expected invariant | Result |
| --- | --- | --- | --- |
| N1 | Remove `docs/product/FEATURE_MATRIX.md` | Mandatory file required | Rejected, exit `2` - PASS |
| N2 | Mutate Protocol R3 target bytes | Frozen hash must match | Rejected, exit `2` - PASS |
| N3 | Add `AUD-999` history to dynamic CURRENT_STATE | Stale project state forbidden | Rejected, exit `2` - PASS |
| N4 | Add a Codex-only execution rule to AGENTS | Agent-neutral contract required | Rejected, exit `2` - PASS |
| N5 | Add `task_id` while `current_task=NONE` | No active task contract in sentinel | Rejected, exit `2` - PASS |

## Regression and Scope

- Existing managed-path collision: rejected, exit `2`; pre-existing `AGENTS.md` bytes unchanged; no extra files created - PASS
- `python3 -m json.tool tools/kyd-bootstrap/bootstrap_pack_r3.json`: PASS
- Python source compilation: PASS
- `git diff --check`: PASS
- Runtime validator SHA-256 remains `aab284d3b4a76c691d327f0ccef27be2035fd697978be5e1bf8578fe40bb29b7`.
- Frozen Protocol, Playbook, Runtime, and Bootstrap Spec hashes remain unchanged.
- No Starter/application/package/deployment file changed.
- `BS-IMPL-040` was not implemented or activated.

## Result

BS-IMPL-030 implementation and task-local verification pass. The task is
`IMPLEMENTED` pending independent verification; `BS-IMPL-040` remains
`NOT_READY`.
