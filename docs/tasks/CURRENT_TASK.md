# CURRENT_TASK

<!-- KYD_RUNTIME_DATA_START -->
{
  "runtime_schema": "kyd.current-task.v1",
  "project": "sa-template",
  "runtime_version": "KPR-V1",
  "task_id": "BS-IMPL-010",
  "status": "VERIFIED",
  "contract": {
    "goal": "Create the minimal reusable Bootstrap source manifest and universal agent-neutral AGENTS.md source template required by the frozen Bootstrap Pack specification, without implementing project initialization yet.",
    "depends_on": [],
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
        "tools/kyd-bootstrap/bootstrap_pack_r3.json",
        "tools/kyd-bootstrap/templates/AGENTS.md",
        "docs/bootstrap/implementation/evidence/BS-IMPL-010_EVIDENCE.md",
        "docs/CURRENT_STATE.md",
        "docs/tasks/TASK_INDEX.md",
        "docs/tasks/CURRENT_TASK.md",
        "docs/execution/IMPLEMENTATION_TRACE.md"
      ],
      "data": [
        "Bootstrap pinned-source manifest metadata"
      ],
      "api": [],
      "other": []
    },
    "shared_resources": [
      "Bootstrap source manifest",
      "Bootstrap AGENTS source template",
      "Runtime task closeout state"
    ],
    "gates_required": [],
    "allowed_changes": [
      "Create tools/kyd-bootstrap/bootstrap_pack_r3.json with exact frozen source identities, versions, source paths, target paths, and hashes.",
      "Create tools/kyd-bootstrap/templates/AGENTS.md as an agent-neutral universal repository entry contract.",
      "Record task-scoped implementation/verification evidence and normal Runtime task closeout state only."
    ],
    "forbidden_changes": [
      "Modify current repository root AGENTS.md.",
      "Modify frozen Delivery Protocol R3, Execution Playbook R3, Runtime R1, or Bootstrap Pack Spec R3.",
      "Modify tools/kyd_runtime_validate.py.",
      "Modify current project product/task/history content except normal Runtime task status/trace closeout for BS-IMPL-010.",
      "Modify Starter/application/package/deployment files.",
      "Introduce Codex-, ChatGPT-, model-, vendor-, AUD-, STS-, or sa-template-specific normative bindings into the generated AGENTS source."
    ],
    "acceptance": [
      "bootstrap_pack_r3.json parses deterministically.",
      "Manifest pins KPS-DP-R3, KPS-DP-PLAYBOOK-R3, RUNTIME-001 and tools/kyd_runtime_validate.py to exact source paths and exact hashes.",
      "Runtime validator manifest hash equals aab284d3b4a76c691d327f0ccef27be2035fd697978be5e1bf8578fe40bb29b7.",
      "Manifest contains no mutable latest resolution.",
      "AGENTS source implements the frozen always-read chain and repository-first/deny-by-default rules.",
      "AGENTS source is agent-neutral and contains no source-project history/bindings.",
      "Only declared touch paths and normal Runtime closeout records change."
    ],
    "verification": [
      "Parse bootstrap_pack_r3.json using Python standard library JSON parser.",
      "Recompute SHA-256 for every pinned frozen Authority and Runtime validator source and compare with manifest.",
      "Run targeted required/prohibited-clause checks on AGENTS source.",
      "Run git diff --check.",
      "Record evidence at docs/bootstrap/implementation/evidence/BS-IMPL-010_EVIDENCE.md.",
      "Run Runtime closeout validation before marking BS-IMPL-010 IMPLEMENTED/VERIFIED."
    ]
  },
  "verification_evidence": [
    "docs/bootstrap/implementation/evidence/BS-IMPL-010_EVIDENCE.md",
    "BS-VER-010 independent verification at fa66ca5d66f0c03b6e8409c20d32a9e2680acb8d PASS",
    "Manifest JSON parse and pinned source hash verification PASS",
    "AGENTS required-clause and prohibited-binding checks PASS",
    "Implementation commit scope verification PASS",
    "Runtime structure and closeout validation PASS"
  ]
}
<!-- KYD_RUNTIME_DATA_END -->

BS-IMPL-010 remains the selected Runtime task and is VERIFIED. BS-IMPL-020 is READY for separate mechanical activation.
