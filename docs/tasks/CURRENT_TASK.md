# CURRENT_TASK

<!-- KYD_RUNTIME_DATA_START -->
{
  "runtime_schema": "kyd.current-task.v1",
  "project": "sa-template",
  "runtime_version": "KPR-V1",
  "task_id": "BS-CORR-020",
  "status": "IMPLEMENTED",
  "contract": {
    "goal": "Correct only the generated docs/PROJECT_INDEX.md metadata emitted by the Bootstrap initializer so it exactly matches the approved Section 6 baseline after BS-VER-020, without redesigning or implementing Bootstrap validation.",
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
        "Generated PROJECT_INDEX metadata"
      ],
      "api": [],
      "other": [
        "Disposable temporary target repositories used only for correction verification"
      ]
    },
    "shared_resources": [
      "Bootstrap initializer",
      "Generated PROJECT_INDEX contract",
      "Runtime task closeout state"
    ],
    "gates_required": [],
    "allowed_changes": [
      "Patch tools/kyd-bootstrap/init_project.py only to emit the exact approved static and dynamic PROJECT_INDEX metadata.",
      "Update docs/bootstrap/implementation/evidence/BS-IMPL-020_EVIDENCE.md with reproducible corrected PROJECT_INDEX evidence.",
      "Record task-scoped evidence and normal Runtime task closeout state only."
    ],
    "forbidden_changes": [
      "Modify frozen Delivery Protocol R3, Execution Playbook R3, Runtime R1, or Bootstrap Pack Spec R3.",
      "Modify tools/kyd_runtime_validate.py.",
      "Modify tools/kyd-bootstrap/bootstrap_pack_r3.json or tools/kyd-bootstrap/templates/AGENTS.md.",
      "Create or implement a Bootstrap validator.",
      "Modify Starter/application/package/deployment files.",
      "Implement or activate BS-IMPL-030."
    ],
    "acceptance": [
      "Generated PROJECT_INDEX contains the exact approved metadata for KPS-DP-R3, KPS-DP-PLAYBOOK-R3, and RUNTIME-001.",
      "All six dynamic/provenance entries use kind EVIDENCE, version v1, status ACTIVE, and sha256 as an empty string.",
      "All nine PROJECT_INDEX routes resolve without Product-Specific Authority or a Domain Index.",
      "Generated Runtime structure and closeout validation pass.",
      "Generated Runtime execution remains rejected because current_task is NONE.",
      "BS-IMPL-020 evidence records reproducible corrected PROJECT_INDEX results.",
      "BS-IMPL-020 remains IMPLEMENTED and BS-IMPL-030 remains NOT_READY."
    ],
    "verification": [
      "Initialize a fresh disposable project with the real initializer.",
      "Verify the three static PROJECT_INDEX entries field-for-field against the approved metadata.",
      "Verify all six dynamic PROJECT_INDEX entries use the exact required kind, version, status, and sha256 values.",
      "Verify all nine PROJECT_INDEX routes resolve.",
      "Run the generated Runtime validator in structure and closeout modes; both must pass.",
      "Run the generated Runtime validator in execution mode and verify expected rejection at current_task=NONE.",
      "Run git diff --check.",
      "Run source repository Runtime structure and closeout validation before marking BS-CORR-020 IMPLEMENTED."
    ]
  },
  "verification_evidence": [
    "docs/bootstrap/implementation/evidence/BS-IMPL-020_EVIDENCE.md",
    "Static PROJECT_INDEX metadata exact match 3/3",
    "Dynamic PROJECT_INDEX metadata exact match 6/6",
    "PROJECT_INDEX routes resolve 9/9",
    "Generated Runtime structure and closeout PASS",
    "Generated Runtime execution rejected at current_task=NONE as expected"
  ]
}
<!-- KYD_RUNTIME_DATA_END -->

BS-CORR-020 is the only selected Runtime task. Its contract exactly matches TASK_INDEX; correction implementation is complete and awaits independent verification.
