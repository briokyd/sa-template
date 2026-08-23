# BS-IMPL-020 Evidence

- Step ID: `BS-IMPL-020`
- Pre-step HEAD: `6719bc52b0790f14cf99005af77f7c75a58c01d7`
- Initializer: `tools/kyd-bootstrap/init_project.py`
- Initializer SHA-256: `335d893385450dea84423a281dedfa5c48eeb43590287c0cfc66e839415ce98e`
- CLI: `python3 tools/kyd-bootstrap/init_project.py --project-id PROJECT_ID --target TARGET`

## Positive Initialization

- Initial implementation SHA-256: `64f027806c69c02a9907fc091da078871da0ec8875243e8ce7cc5af26701bfa2`
- Command: `python3 tools/kyd-bootstrap/init_project.py --project-id kyd-zero-state-fixture --target /tmp/bs-impl-020-final-positive.co53pk`
- Result: `KYD_BOOTSTRAP_INIT: COMPLETE`
- Generated required files: `12/12` — PASS
- Generated Bootstrap timestamp: `2026-08-23T11:20:19Z`
- Bootstrap manifest `validation_state`: `PENDING` — PASS

| Pinned target | SHA-256 | Result |
| --- | --- | --- |
| `docs/delivery-protocol/KYD_DELIVERY_PROTOCOL_R3.md` | `5dddfe4baf827be59e3b730a45642503d74b5913131606f2b60f6a2d4ec7bea0` | PASS |
| `docs/delivery-protocol/KYD_DELIVERY_PROTOCOL_EXECUTION_PLAYBOOK_R3.md` | `e4039755860173a5bfb409f737710be0b9ad0e8a5654e22329ff23970372a02c` | PASS |
| `docs/kyd-runtime/Kyd_Project_Runtime_V1_Minimal_Spec_R1.md` | `fe78677830b5a24c0eeea43a70c6fc266687f9f37cec1e747ad679ebaa12e10a` | PASS |
| `tools/kyd_runtime_validate.py` | `aab284d3b4a76c691d327f0ccef27be2035fd697978be5e1bf8578fe40bb29b7` | PASS |

## Zero-State and Routing

- Original `PROJECT_INDEX` routing: three pinned Authority IDs plus six dynamic routes; all nine paths resolved, but BS-VER-020 found a Section 6 metadata mismatch later corrected and reproduced below
- Dynamic `PROJECT_INDEX` routes are `ACTIVE`, not `FROZEN` — PASS
- `CURRENT_STATE.current_task = NONE`, `next_task = NONE`, Gates empty, blockers empty, release `NOT_READY` — PASS
- `TASK_INDEX.tasks = []` — PASS
- `CURRENT_TASK` contains only Runtime schema/project/runtime identity and the explicit non-executable sentinel note — PASS
- `FEATURE_MATRIX.features = []` — PASS
- `IMPLEMENTATION_TRACE.traces = []` — PASS
- Generated dynamic files contain no `AUD-`, `STS-`, `sa-template`, or source task history markers — PASS

## Runtime Verification

- Generated target structure mode: `KYD_RUNTIME_VALIDATE: PASS` — PASS
- Generated target closeout mode: `KYD_RUNTIME_VALIDATE: PASS` — PASS
- Generated target execution mode: rejected with `TASK_GAP: execution mode requires current_task`; exit `2`, `EXECUTION_ALLOWED = FALSE` — expected PASS

## Collision Verification

- Collision target: `/tmp/bs-impl-020-final-collision.qHYgig`
- Pre-existing managed path: `docs/tasks/`
- Initializer result: `KYD_BOOTSTRAP_INIT: FAIL`; exit `2`
- Error: `managed control paths already exist: ['docs/tasks']`
- No `AGENTS.md`, `KYD_BOOTSTRAP_MANIFEST.json`, or `docs/PROJECT_INDEX.md` was created — PASS

## Bounded PROJECT_INDEX Correction Reproduction

- Correction task: `BS-CORR-020`
- Independent reproduction target: `/tmp/bs-corr-020-final.DpaANC`
- Static Authority metadata matched Section 6 field-for-field: `3/3` — PASS
- Dynamic routes used `kind=EVIDENCE`, `version=v1`, `status=ACTIVE`, and `sha256=""`: `6/6` — PASS
- All static and dynamic paths resolved: `9/9` — PASS
- Product-Specific Authority absent and Domain Index absent — PASS
- Generated target Runtime structure mode — PASS
- Generated target Runtime closeout mode — PASS
- Generated target Runtime execution mode rejected at `current_task=NONE`, exit `2` — expected PASS
- `validation_state` remained `PENDING` — PASS
- Corrected initializer Python compilation — PASS
- Source repository `git diff --check` — PASS
- Source repository Runtime structure and closeout modes — PASS

## Source Repository Checks

- Runtime execution eligibility before implementation: `PASS`; `EXECUTION_ALLOWED = TRUE`
- Python source compilation: PASS
- `git diff --check`: PASS
- Bootstrap-specific validator created: NO
- Frozen Authority or Runtime validator modified: NO

## Result

The generic initializer creates the pinned Kyd control layer and a clean Runtime
zero-state with fail-closed collision handling. BS-IMPL-020 is implemented and
awaits independent verification; Bootstrap validation remains `PENDING`.
