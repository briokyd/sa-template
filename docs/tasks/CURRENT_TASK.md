# CURRENT_TASK

<!-- KYD_RUNTIME_DATA_START -->
{
  "runtime_schema": "kyd.current-task.v1",
  "project": "sa-template",
  "runtime_version": "KPR-V1",
  "task_id": "BS-IMPL-040",
  "status": "READY",
  "contract": {
    "goal": "Independently verify the completed Bootstrap Pack against every frozen acceptance requirement using a real disposable new-project initialization, without modifying implementation source.",
    "depends_on": [
      "BS-IMPL-030"
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
      "reference": [
        {
          "authority_id": "KPS-DP-R3",
          "version": "R3"
        },
        {
          "authority_id": "KPS-DP-PLAYBOOK-R3",
          "version": "R3"
        }
      ]
    },
    "touches": {
      "routes": [],
      "components": [],
      "files": [
        "docs/bootstrap/verification/KYD_PROJECT_BOOTSTRAP_PACK_R3_E2E_VERIFICATION.md",
        "docs/CURRENT_STATE.md",
        "docs/tasks/TASK_INDEX.md",
        "docs/tasks/CURRENT_TASK.md",
        "docs/execution/IMPLEMENTATION_TRACE.md"
      ],
      "data": [
        "Independent Bootstrap verification evidence"
      ],
      "api": [],
      "other": [
        "Disposable temporary generated-project verification targets"
      ]
    },
    "shared_resources": [
      "Runtime task closeout state"
    ],
    "gates_required": [],
    "allowed_changes": [
      "Create only the deterministic end-to-end verification evidence document.",
      "Create/discard temporary external verification targets.",
      "Record normal Runtime verification/closeout state for BS-IMPL-040."
    ],
    "forbidden_changes": [
      "Modify any Bootstrap implementation source, including tools/kyd-bootstrap/** and tools/kyd_bootstrap_validate.py.",
      "Modify tools/kyd_runtime_validate.py.",
      "Modify frozen Protocol, Playbook, Runtime, or Bootstrap Spec.",
      "Modify generated-project source templates to make verification pass.",
      "Repair defects discovered during verification.",
      "Modify docs/PROJECT_INDEX.md or register evidence while acting as Verifier.",
      "Modify Starter/application/package/deployment files.",
      "Make any change outside the evidence file, disposable targets, and normal Runtime task closeout state."
    ],
    "acceptance": [
      "Real initializer creates every mandatory new-project file.",
      "Protocol, Playbook, Runtime and Runtime validator pinned identities/hashes resolve and match.",
      "Generated PROJECT_INDEX exactly matches the required static and dynamic routing baseline.",
      "Generated AGENTS is agent-neutral and contains the required universal entry contract.",
      "CURRENT_STATE, TASK_INDEX, CURRENT_TASK sentinel, FEATURE_MATRIX and IMPLEMENTATION_TRACE form a clean zero-state.",
      "No stale source-project metadata exists in generated dynamic files.",
      "Runtime structure and closeout validation PASS.",
      "Bootstrap-specific validation PASS.",
      "Runtime execution mode remains ineligible because no current task is selected.",
      "Fail-closed collision behavior PASS.",
      "Fresh-session/replacement-agent recovery PASS using repository-controlled sources only.",
      "No BLOCKER or MAJOR implementation defect remains."
    ],
    "verification": [
      "Run the real final initializer against a new disposable target.",
      "Run the installed Runtime validator and installed Bootstrap validator from the generated target.",
      "Recompute all pinned hashes, including Runtime validator hash.",
      "Verify all PROJECT_INDEX routes resolve.",
      "Verify zero-state and no-task sentinel behavior.",
      "Verify expected execution rejection at current_task=NONE.",
      "Run fail-closed collision test.",
      "Perform fresh-session recovery check using AGENTS.md, PROJECT_INDEX.md, CURRENT_STATE.md, CURRENT_TASK.md and routed frozen Authorities only.",
      "Write reproducible evidence only to docs/bootstrap/verification/KYD_PROJECT_BOOTSTRAP_PACK_R3_E2E_VERIFICATION.md.",
      "If any defect is found, return FAIL/BLOCKED and route correction to a separately Planning-authorized correction task; do not modify implementation source.",
      "Run Runtime closeout validation before marking BS-IMPL-040 VERIFIED."
    ]
  },
  "verification_evidence": []
}
<!-- KYD_RUNTIME_DATA_END -->

BS-IMPL-040 is the only selected Runtime task. Its contract exactly matches TASK_INDEX; independent end-to-end verification has not started.
