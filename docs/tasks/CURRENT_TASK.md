# CURRENT_TASK

<!-- KYD_RUNTIME_DATA_START -->
{
  "runtime_schema": "kyd.current-task.v1",
  "project": "sa-template",
  "runtime_version": "KPR-V1",
  "task_id": "BS-IMPL-030",
  "status": "IMPLEMENTED",
  "contract": {
    "goal": "Implement the Bootstrap-specific validation wrapper around the existing Runtime validator and complete the final initializer integration so every generated project installs and invokes Bootstrap validation before Bootstrap PASS can be recorded.",
    "depends_on": [
      "BS-IMPL-020"
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
        "tools/kyd_bootstrap_validate.py",
        "tools/kyd-bootstrap/init_project.py",
        "tools/kyd-bootstrap/bootstrap_pack_r3.json",
        "docs/bootstrap/implementation/evidence/BS-IMPL-030_EVIDENCE.md",
        "docs/CURRENT_STATE.md",
        "docs/tasks/TASK_INDEX.md",
        "docs/tasks/CURRENT_TASK.md",
        "docs/execution/IMPLEMENTATION_TRACE.md"
      ],
      "data": [
        "Bootstrap validation result",
        "Bootstrap manifest validation state"
      ],
      "api": [],
      "other": [
        "Disposable positive and negative generated-project copies"
      ]
    },
    "shared_resources": [
      "Bootstrap initializer",
      "Bootstrap source manifest",
      "Runtime validator invocation boundary",
      "Bootstrap generated-project path contract",
      "Runtime task closeout state"
    ],
    "gates_required": [],
    "allowed_changes": [
      "Create tools/kyd_bootstrap_validate.py as a bounded wrapper around the existing Runtime validator.",
      "Patch tools/kyd-bootstrap/init_project.py only as required to install and invoke the Bootstrap validator after generation.",
      "Patch tools/kyd-bootstrap/bootstrap_pack_r3.json only as required to include the installed Bootstrap validator source/target mapping.",
      "Make final Bootstrap PASS depend on successful Runtime validation plus Bootstrap-specific validation.",
      "Record task-scoped evidence and normal Runtime task closeout state."
    ],
    "forbidden_changes": [
      "Modify tools/kyd_runtime_validate.py or Runtime validator semantics.",
      "Modify frozen Protocol, Playbook, Runtime, or Bootstrap Spec.",
      "Duplicate or fork Runtime dependency/Authority/Gate semantics inside Bootstrap validation.",
      "Record Bootstrap PASS when Runtime or Bootstrap validation fails.",
      "Broaden stale-state scans into immutable frozen Authority bodies or intentional test fixtures.",
      "Modify current project state/history except normal Runtime task closeout for BS-IMPL-030.",
      "Modify Starter/application/package/deployment files."
    ],
    "acceptance": [
      "tools/kyd_bootstrap_validate.py wraps, rather than patches or replaces, tools/kyd_runtime_validate.py.",
      "Final initializer installs tools/kyd_bootstrap_validate.py into the generated target.",
      "Final initializer invokes the installed target Bootstrap validator before finalizing initialization.",
      "Bootstrap validator invokes Runtime validation and additionally validates required structure, routing, pinned hashes, clean zero-state, CURRENT_TASK sentinel safety, stale-state rejection, and AGENTS neutrality.",
      "Runtime validator target copy remains exact hash aab284d3b4a76c691d327f0ccef27be2035fd697978be5e1bf8578fe40bb29b7.",
      "A positive generated project passes Runtime structure/closeout validation and Bootstrap validation while execution remains ineligible.",
      "Negative cases reject at least: missing mandatory file, wrong pinned Authority hash, stale project-state leakage, non-neutral AGENTS binding, unsafe active-task-like CURRENT_TASK content while current_task=NONE.",
      "KYD_BOOTSTRAP_MANIFEST.json records PASS only after both Runtime and Bootstrap-specific validation succeed.",
      "Any validation failure leaves Bootstrap result non-PASS and initializer exits fail-closed."
    ],
    "verification": [
      "Generate a fresh disposable target with the real final initializer.",
      "Verify target contains both tools/kyd_runtime_validate.py and tools/kyd_bootstrap_validate.py.",
      "Verify target Runtime validator hash exactly matches aab284d3b4a76c691d327f0ccef27be2035fd697978be5e1bf8578fe40bb29b7.",
      "Run positive Bootstrap validation and verify manifest PASS is recorded only after success.",
      "Run each required negative mutation in disposable copies and verify rejection for the intended invariant.",
      "Confirm execution-mode Runtime validation remains rejected at current_task=NONE.",
      "Run git diff --check.",
      "Record evidence at docs/bootstrap/implementation/evidence/BS-IMPL-030_EVIDENCE.md.",
      "Run Runtime closeout validation before marking BS-IMPL-030 IMPLEMENTED/VERIFIED."
    ]
  },
  "verification_evidence": [
    "docs/bootstrap/implementation/evidence/BS-IMPL-030_EVIDENCE.md",
    "Positive disposable initialization generated 13/13 mandatory files and completed Bootstrap validation with manifest PASS",
    "N1-N5 negative fixtures were rejected for their intended invariants",
    "Generated Runtime structure and closeout PASS; execution rejected as expected at current_task=NONE",
    "Managed-path collision was rejected without modifying pre-existing content"
  ]
}
<!-- KYD_RUNTIME_DATA_END -->

BS-IMPL-030 is the only selected Runtime task. Its contract exactly matches TASK_INDEX; implementation is complete and awaits independent verification.
