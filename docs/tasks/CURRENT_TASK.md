# CURRENT_TASK

<!-- KYD_RUNTIME_DATA_START -->
{
  "runtime_schema": "kyd.current-task.v1",
  "project": "sa-template",
  "runtime_version": "KPR-V1",
  "task_id": "BS-IMPL-020",
  "status": "IMPLEMENTED",
  "contract": {
    "goal": "Implement a generic standard-library Python initializer that materially installs pinned Kyd control assets and generates a clean Runtime zero-state in a new target repository, while leaving final Bootstrap-validator integration for BS-IMPL-030.",
    "depends_on": [
      "BS-IMPL-010"
    ],
    "authority_inputs": {
      "mandatory": [
        {
          "authority_id": "KPS-BS-PACK-SPEC-R3",
          "version": "R3"
        },
        {
          "authority_id": "RUNTIME-001",
          "version": "R1"
        }
      ],
      "reference": []
    },
    "touches": {
      "routes": [],
      "components": [],
      "files": [
        "tools/kyd-bootstrap/init_project.py",
        "docs/bootstrap/implementation/evidence/BS-IMPL-020_EVIDENCE.md",
        "docs/CURRENT_STATE.md",
        "docs/tasks/TASK_INDEX.md",
        "docs/tasks/CURRENT_TASK.md",
        "docs/execution/IMPLEMENTATION_TRACE.md"
      ],
      "data": [
        "Generated Runtime zero-state",
        "Generated PROJECT_INDEX baseline",
        "Generated Bootstrap provenance manifest"
      ],
      "api": [],
      "other": [
        "Disposable temporary target repositories used only for verification"
      ]
    },
    "shared_resources": [
      "tools/kyd-bootstrap/bootstrap_pack_r3.json",
      "tools/kyd-bootstrap/templates/AGENTS.md",
      "Bootstrap generated-project path contract",
      "Runtime task closeout state"
    ],
    "gates_required": [],
    "allowed_changes": [
      "Create tools/kyd-bootstrap/init_project.py using Python standard library.",
      "Generate the mandatory new-project file set defined by KPS-BS-PACK-SPEC-R3.",
      "Copy exact pinned bytes for Protocol R3, Playbook R3, Runtime R1, and Runtime validator.",
      "Generate deterministic PROJECT_INDEX, CURRENT_STATE, TASK_INDEX, CURRENT_TASK sentinel, FEATURE_MATRIX, IMPLEMENTATION_TRACE, and KYD_BOOTSTRAP_MANIFEST.json zero-state.",
      "Implement fail-closed controlled-path collision handling.",
      "Record task-scoped evidence and normal Runtime task closeout state."
    ],
    "forbidden_changes": [
      "Modify any frozen Authority source.",
      "Modify tools/kyd_runtime_validate.py.",
      "Modify current repository root AGENTS.md or current project dynamic state/history except normal Runtime task closeout for BS-IMPL-020.",
      "Implement Bootstrap-specific validator logic in this task.",
      "Record final Bootstrap PASS in KYD_BOOTSTRAP_MANIFEST.json.",
      "Silently overwrite an existing managed-project control path.",
      "Copy current Kyd project AUD/STS/Starter/task/feature/trace history into a target.",
      "Modify Starter/application/package/deployment files."
    ],
    "acceptance": [
      "Initializer succeeds on an empty disposable target.",
      "Initializer creates AGENTS.md, PROJECT_INDEX.md, CURRENT_STATE.md, Protocol R3, Playbook R3, Runtime R1, FEATURE_MATRIX.md, TASK_INDEX.md, CURRENT_TASK.md, IMPLEMENTATION_TRACE.md, tools/kyd_runtime_validate.py, and KYD_BOOTSTRAP_MANIFEST.json.",
      "Protocol, Playbook, Runtime and Runtime validator source hashes are verified before copy and copied bytes are verified after copy.",
      "Copied Runtime validator SHA-256 is exactly aab284d3b4a76c691d327f0ccef27be2035fd697978be5e1bf8578fe40bb29b7.",
      "Generated PROJECT_INDEX matches Section 6 of this plan exactly.",
      "CURRENT_STATE.current_task is NONE and implementation eligibility is false.",
      "TASK_INDEX tasks collection is empty.",
      "CURRENT_TASK is a non-contract no-task sentinel with no fabricated task/Authority/dependency/scope/acceptance/verification fields.",
      "FEATURE_MATRIX feature collection is empty.",
      "IMPLEMENTATION_TRACE trace collection is empty.",
      "KYD_BOOTSTRAP_MANIFEST.json records validation state as PENDING, not PASS.",
      "No stale AUD/STS/sa-template/current-project metadata exists in generated dynamic files.",
      "Controlled-path collision is rejected without destructive overwrite."
    ],
    "verification": [
      "Run initializer against a disposable empty temporary target.",
      "Verify every mandatory output path exists.",
      "Recompute copied pinned hashes including Runtime validator hash.",
      "Run generated target Runtime validator in structure mode and closeout mode; both must PASS.",
      "Run generated target Runtime validator in execution mode and verify execution is rejected because current_task=NONE.",
      "Verify generated PROJECT_INDEX routes all three static Authorities and six dynamic/provenance entries.",
      "Run a collision negative case and verify fail-closed behavior.",
      "Scan generated dynamic files only for prohibited inherited AUD/STS/sa-template/current-project metadata.",
      "Run git diff --check.",
      "Record evidence at docs/bootstrap/implementation/evidence/BS-IMPL-020_EVIDENCE.md.",
      "Run Runtime closeout validation before marking BS-IMPL-020 IMPLEMENTED/VERIFIED."
    ]
  },
  "verification_evidence": [
    "docs/bootstrap/implementation/evidence/BS-IMPL-020_EVIDENCE.md",
    "Positive initialization generated all 12 mandatory paths",
    "Pinned source and target SHA-256 verification PASS",
    "Generated PROJECT_INDEX routing and Runtime zero-state checks PASS",
    "Generated target Runtime structure and closeout validation PASS",
    "Generated target execution rejection at current_task=NONE PASS",
    "Managed-path collision fail-closed verification PASS",
    "git diff --check PASS"
  ]
}
<!-- KYD_RUNTIME_DATA_END -->

BS-IMPL-020 is the only selected Runtime task. Its contract exactly matches TASK_INDEX; implementation is complete and awaits independent verification.
