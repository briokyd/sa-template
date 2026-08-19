# CURRENT_TASK

<!-- KYD_RUNTIME_DATA_START -->
{
  "runtime_schema": "kyd.current-task.v1",
  "project": "sa-template",
  "runtime_version": "KPR-V1",
  "task_id": "AUD-080",
  "status": "VERIFIED",
  "contract": {
    "goal": "Synthesize all verified workstreams into the final Full Repository Audit outputs and evidence packages for A-001/A-002.",
    "depends_on": [
      "AUD-070"
    ],
    "authority_inputs": {
      "mandatory": [
        {
          "authority_id": "AUDIT-001",
          "version": "v1"
        }
      ],
      "reference": [
        {
          "authority_id": "AUD-WORK-000",
          "version": "v1"
        },
        {
          "authority_id": "AUD-WORK-010",
          "version": "v1"
        },
        {
          "authority_id": "AUD-WORK-020",
          "version": "v1"
        },
        {
          "authority_id": "AUD-WORK-030",
          "version": "v1"
        },
        {
          "authority_id": "AUD-WORK-040",
          "version": "v1"
        },
        {
          "authority_id": "AUD-WORK-050",
          "version": "v1"
        },
        {
          "authority_id": "AUD-WORK-060",
          "version": "v1"
        },
        {
          "authority_id": "AUD-WORK-070",
          "version": "v1"
        }
      ]
    },
    "touches": {
      "routes": [],
      "components": [],
      "files": [
        "docs/audit/00_AUDIT_SUMMARY.md",
        "docs/audit/01_CAPABILITY_MATRIX.md",
        "docs/audit/02_REUSE_GAP_MATRIX.md",
        "docs/audit/03_CLOUDFLARE_RUNTIME_AUDIT.md",
        "docs/audit/04_UI_FOUNDATION_AUDIT.md",
        "docs/audit/05_TEST_AND_RELEASE_AUDIT.md",
        "docs/audit/06_RISK_AND_BLOCKERS.md",
        "docs/audit/07_DELETION_REVIEW_CANDIDATES.md",
        "docs/audit/08_REFACTOR_JUSTIFICATION.md",
        "docs/CURRENT_STATE.md",
        "docs/product/FEATURE_MATRIX.md",
        "docs/tasks/TASK_INDEX.md",
        "docs/tasks/CURRENT_TASK.md",
        "docs/execution/IMPLEMENTATION_TRACE.md"
      ],
      "data": [],
      "api": [],
      "other": [
        "Repository read-only inspection for the declared audit workstream"
      ]
    },
    "shared_resources": [
      "AUDIT_RUNTIME_STATE"
    ],
    "gates_required": [
      "RUNTIME_V1_FREEZE",
      "AUDIT_BOOTSTRAP"
    ],
    "allowed_changes": [
      "Modify only the designated docs/audit output file(s) for this Task",
      "Update Runtime state/task/feature/trace files only as required for deterministic closeout and next-task activation"
    ],
    "forbidden_changes": [
      "Any application or product source-code modification",
      "Any database schema or migration modification",
      "Any package dependency or lockfile modification",
      "Any existing route/API/UI/runtime configuration modification",
      "Any change outside the designated audit output and Runtime state files"
    ],
    "acceptance": [
      "All AUD-000 through AUD-070 dependencies are VERIFIED before synthesis starts",
      "All nine final synthesis documents are completed from workstream evidence without silently weakening findings",
      "01_CAPABILITY_MATRIX covers all mandatory audit capability areas with an allowed Action or explicit UNKNOWN / NOT VERIFIED evidence state",
      "Every REFACTOR item is represented in 08_REFACTOR_JUSTIFICATION with all required proof fields",
      "Every DELETE candidate is represented in 07_DELETION_REVIEW_CANDIDATES with a complete Deletion Review",
      "A-001 and A-002 evidence summaries are explicit and ready for later user decision; Codex does not silently freeze those decisions",
      "No application/product implementation file was modified during the Full Repository Audit",
      "AUD-F080 and AUD-080 become VERIFIED; CURRENT_STATE.current_task becomes NONE; next_task becomes NONE; Audit phase is complete"
    ],
    "verification": [
      "python3 tools/kyd_runtime_validate.py --root . --mode closeout",
      "Confirm all AUD-000..AUD-080 Task statuses are VERIFIED",
      "Confirm all required docs/audit/00..08 final outputs exist and are non-empty",
      "Review git diff --name-only for the complete audit branch and confirm no business/application implementation changes were introduced by audit Tasks"
    ]
  },
  "verification_evidence": [
    "All AUD-000 through AUD-070 dependencies are VERIFIED",
    "All nine registered final audit synthesis artifacts are non-empty and repository-evidence-based",
    "Capability roles, allowed Actions, Cloudflare statuses, and P0/P1/P2 backlog counts were checked",
    "A-001 is BLOCKED — EXTERNAL FACT VERIFICATION REQUIRED; A-002 is FROZEN — KEEP LIST",
    "No application/product implementation file was modified",
    "python3 tools/kyd_runtime_validate.py --root . --mode closeout => KYD_RUNTIME_VALIDATE: PASS; RUNTIME_STATE_VALID = TRUE"
  ]
}
<!-- KYD_RUNTIME_DATA_END -->

This is the low-context execution snapshot for `AUD-080`.

Its `contract` must exactly match the AUD-080 contract in `TASK_INDEX`.
