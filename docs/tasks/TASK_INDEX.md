# TASK_INDEX

<!-- KYD_RUNTIME_DATA_START -->
{
  "runtime_schema": "kyd.task-index.v1",
  "project": "sa-template",
  "runtime_version": "KPR-V1",
  "tasks": [
    {
      "task_id": "AUD-000",
      "title": "Repository Inventory / Audit Bootstrap",
      "type": "AUDIT",
      "status": "VERIFIED",
      "contract": {
        "goal": "Capture a factual repository inventory and prove the Runtime/Audit bootstrap is executable.",
        "depends_on": [],
        "authority_inputs": {
          "mandatory": [
            {
              "authority_id": "AUDIT-001",
              "version": "v1"
            }
          ],
          "reference": []
        },
        "touches": {
          "routes": [],
          "components": [],
          "files": [
            "docs/audit/work/00_REPOSITORY_INVENTORY.md",
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
          "RUNTIME_V1_FREEZE"
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
          "docs/audit/work/00_REPOSITORY_INVENTORY.md contains repository-grounded findings for every declared workstream area or an explicit UNKNOWN / NOT VERIFIED entry",
          "Every recommendation uses exactly one allowed Action: KEEP, KEEP + TEST, KEEP-DISABLED, WRAP, PATCH, REFACTOR, or DELETE",
          "Every finding includes concrete repository evidence/path/symbol/command evidence where available",
          "No application/product implementation file was modified",
          "AUD-F000 is VERIFIED at closeout when all acceptance criteria pass",
          "Current Task becomes VERIFIED and next Task AUD-010 is activated as READY during closeout",
          "CURRENT_STATE gate AUDIT_BOOTSTRAP is set to PASS with evidence only after repository inventory and Runtime execution validation succeed",
          "Repository branch name and HEAD commit are recorded in the inventory and CURRENT_STATE.last_verified_commit is set to the audited bootstrap HEAD when appropriate"
        ],
        "verification": [
          "python3 tools/kyd_runtime_validate.py --root . --mode closeout",
          "Review git diff --name-only and confirm changes are restricted to docs/audit/** and Runtime state/task/trace files",
          "Confirm docs/audit/work/00_REPOSITORY_INVENTORY.md is non-empty and contains evidence-based findings"
        ]
      }
    },
    {
      "task_id": "AUD-010",
      "title": "Framework / Cloudflare / Env / Config Audit",
      "type": "AUDIT",
      "status": "VERIFIED",
      "contract": {
        "goal": "Audit framework, Cloudflare/OpenNext, build/deploy entry points, and environment/config behavior.",
        "depends_on": [
          "AUD-000"
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
            }
          ]
        },
        "touches": {
          "routes": [],
          "components": [],
          "files": [
            "docs/audit/work/10_FRAMEWORK_CLOUDFLARE_ENV_CONFIG.md",
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
          "docs/audit/work/10_FRAMEWORK_CLOUDFLARE_ENV_CONFIG.md contains repository-grounded findings for every declared workstream area or an explicit UNKNOWN / NOT VERIFIED entry",
          "Every recommendation uses exactly one allowed Action: KEEP, KEEP + TEST, KEEP-DISABLED, WRAP, PATCH, REFACTOR, or DELETE",
          "Every finding includes concrete repository evidence/path/symbol/command evidence where available",
          "No application/product implementation file was modified",
          "AUD-F010 is VERIFIED at closeout when all acceptance criteria pass",
          "Current Task becomes VERIFIED and next Task AUD-020 is activated as READY during closeout"
        ],
        "verification": [
          "python3 tools/kyd_runtime_validate.py --root . --mode closeout",
          "Review git diff --name-only and confirm changes are restricted to docs/audit/** and Runtime state/task/trace files",
          "Confirm docs/audit/work/10_FRAMEWORK_CLOUDFLARE_ENV_CONFIG.md is non-empty and contains evidence-based findings"
        ]
      }
    },
    {
      "task_id": "AUD-020",
      "title": "Database / Drizzle / Migration Audit",
      "type": "AUDIT",
      "status": "VERIFIED",
      "contract": {
        "goal": "Audit PostgreSQL/Drizzle/database access/migrations and collect evidence needed for A-001.",
        "depends_on": [
          "AUD-010"
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
            }
          ]
        },
        "touches": {
          "routes": [],
          "components": [],
          "files": [
            "docs/audit/work/20_DATABASE_DRIZZLE_MIGRATIONS.md",
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
          "docs/audit/work/20_DATABASE_DRIZZLE_MIGRATIONS.md contains repository-grounded findings for every declared workstream area or an explicit UNKNOWN / NOT VERIFIED entry",
          "Every recommendation uses exactly one allowed Action: KEEP, KEEP + TEST, KEEP-DISABLED, WRAP, PATCH, REFACTOR, or DELETE",
          "Every finding includes concrete repository evidence/path/symbol/command evidence where available",
          "No application/product implementation file was modified",
          "AUD-F020 is VERIFIED at closeout when all acceptance criteria pass",
          "Current Task becomes VERIFIED and next Task AUD-030 is activated as READY during closeout"
        ],
        "verification": [
          "python3 tools/kyd_runtime_validate.py --root . --mode closeout",
          "Review git diff --name-only and confirm changes are restricted to docs/audit/** and Runtime state/task/trace files",
          "Confirm docs/audit/work/20_DATABASE_DRIZZLE_MIGRATIONS.md is non-empty and contains evidence-based findings"
        ]
      }
    },
    {
      "task_id": "AUD-030",
      "title": "Auth / Email / Session / Account Audit",
      "type": "AUDIT",
      "status": "VERIFIED",
      "contract": {
        "goal": "Audit Auth.js, Google, Magic Link/Resend, session, identity semantics, profile/account/logout, and other existing auth paths.",
        "depends_on": [
          "AUD-020"
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
            }
          ]
        },
        "touches": {
          "routes": [],
          "components": [],
          "files": [
            "docs/audit/work/30_AUTH_EMAIL_SESSION_ACCOUNT.md",
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
          "docs/audit/work/30_AUTH_EMAIL_SESSION_ACCOUNT.md contains repository-grounded findings for every declared workstream area or an explicit UNKNOWN / NOT VERIFIED entry",
          "Every recommendation uses exactly one allowed Action: KEEP, KEEP + TEST, KEEP-DISABLED, WRAP, PATCH, REFACTOR, or DELETE",
          "Every finding includes concrete repository evidence/path/symbol/command evidence where available",
          "No application/product implementation file was modified",
          "AUD-F030 is VERIFIED at closeout when all acceptance criteria pass",
          "Current Task becomes VERIFIED and next Task AUD-040 is activated as READY during closeout"
        ],
        "verification": [
          "python3 tools/kyd_runtime_validate.py --root . --mode closeout",
          "Review git diff --name-only and confirm changes are restricted to docs/audit/** and Runtime state/task/trace files",
          "Confirm docs/audit/work/30_AUTH_EMAIL_SESSION_ACCOUNT.md is non-empty and contains evidence-based findings"
        ]
      }
    },
    {
      "task_id": "AUD-040",
      "title": "Payment / Orders / Webhook / Entitlement Audit",
      "type": "AUDIT",
      "status": "VERIFIED",
      "contract": {
        "goal": "Audit orders, Creem, Stripe, checkout, callbacks/webhooks, idempotency, provider switching, entitlement and credits relationships.",
        "depends_on": [
          "AUD-030"
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
            }
          ]
        },
        "touches": {
          "routes": [],
          "components": [],
          "files": [
            "docs/audit/work/40_PAYMENT_ORDERS_WEBHOOK_ENTITLEMENT.md",
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
          "docs/audit/work/40_PAYMENT_ORDERS_WEBHOOK_ENTITLEMENT.md contains repository-grounded findings for every declared workstream area or an explicit UNKNOWN / NOT VERIFIED entry",
          "Every recommendation uses exactly one allowed Action: KEEP, KEEP + TEST, KEEP-DISABLED, WRAP, PATCH, REFACTOR, or DELETE",
          "Every finding includes concrete repository evidence/path/symbol/command evidence where available",
          "No application/product implementation file was modified",
          "AUD-F040 is VERIFIED at closeout when all acceptance criteria pass",
          "Current Task becomes VERIFIED and next Task AUD-050 is activated as READY during closeout"
        ],
        "verification": [
          "python3 tools/kyd_runtime_validate.py --root . --mode closeout",
          "Review git diff --name-only and confirm changes are restricted to docs/audit/** and Runtime state/task/trace files",
          "Confirm docs/audit/work/40_PAYMENT_ORDERS_WEBHOOK_ENTITLEMENT.md is non-empty and contains evidence-based findings"
        ]
      }
    },
    {
      "task_id": "AUD-050",
      "title": "Optional Platform Capabilities Audit",
      "type": "AUDIT",
      "status": "VERIFIED",
      "contract": {
        "goal": "Audit Ads, Analytics, SEO, i18n, AI, Storage/R2, Turnstile, content/docs, API keys, affiliate/referral, dashboard/pricing and related existing capabilities.",
        "depends_on": [
          "AUD-040"
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
            }
          ]
        },
        "touches": {
          "routes": [],
          "components": [],
          "files": [
            "docs/audit/work/50_OPTIONAL_PLATFORM_CAPABILITIES.md",
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
          "docs/audit/work/50_OPTIONAL_PLATFORM_CAPABILITIES.md contains repository-grounded findings for every declared workstream area or an explicit UNKNOWN / NOT VERIFIED entry",
          "Every recommendation uses exactly one allowed Action: KEEP, KEEP + TEST, KEEP-DISABLED, WRAP, PATCH, REFACTOR, or DELETE",
          "Every finding includes concrete repository evidence/path/symbol/command evidence where available",
          "No application/product implementation file was modified",
          "AUD-F050 is VERIFIED at closeout when all acceptance criteria pass",
          "Current Task becomes VERIFIED and next Task AUD-060 is activated as READY during closeout"
        ],
        "verification": [
          "python3 tools/kyd_runtime_validate.py --root . --mode closeout",
          "Review git diff --name-only and confirm changes are restricted to docs/audit/** and Runtime state/task/trace files",
          "Confirm docs/audit/work/50_OPTIONAL_PLATFORM_CAPABILITIES.md is non-empty and contains evidence-based findings"
        ]
      }
    },
    {
      "task_id": "AUD-060",
      "title": "UI Foundation Audit",
      "type": "AUDIT",
      "status": "VERIFIED",
      "contract": {
        "goal": "Audit shared UI primitives/surfaces, responsive/accessibility baseline, and collect evidence needed for A-002.",
        "depends_on": [
          "AUD-050"
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
            }
          ]
        },
        "touches": {
          "routes": [],
          "components": [],
          "files": [
            "docs/audit/work/60_UI_FOUNDATION.md",
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
          "docs/audit/work/60_UI_FOUNDATION.md contains repository-grounded findings for every declared workstream area or an explicit UNKNOWN / NOT VERIFIED entry",
          "Every recommendation uses exactly one allowed Action: KEEP, KEEP + TEST, KEEP-DISABLED, WRAP, PATCH, REFACTOR, or DELETE",
          "Every finding includes concrete repository evidence/path/symbol/command evidence where available",
          "No application/product implementation file was modified",
          "AUD-F060 is VERIFIED at closeout when all acceptance criteria pass",
          "Current Task becomes VERIFIED and next Task AUD-070 is activated as READY during closeout"
        ],
        "verification": [
          "python3 tools/kyd_runtime_validate.py --root . --mode closeout",
          "Review git diff --name-only and confirm changes are restricted to docs/audit/** and Runtime state/task/trace files",
          "Confirm docs/audit/work/60_UI_FOUNDATION.md is non-empty and contains evidence-based findings"
        ]
      }
    },
    {
      "task_id": "AUD-070",
      "title": "Tests / Security / Logging / Build / Deploy Audit",
      "type": "AUDIT",
      "status": "VERIFIED",
      "contract": {
        "goal": "Audit verification tooling, security, logging/error handling, staging/release support and real-provider smoke readiness.",
        "depends_on": [
          "AUD-060"
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
            }
          ]
        },
        "touches": {
          "routes": [],
          "components": [],
          "files": [
            "docs/audit/work/70_TEST_SECURITY_LOGGING_BUILD_DEPLOY.md",
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
          "docs/audit/work/70_TEST_SECURITY_LOGGING_BUILD_DEPLOY.md contains repository-grounded findings for every declared workstream area or an explicit UNKNOWN / NOT VERIFIED entry",
          "Every recommendation uses exactly one allowed Action: KEEP, KEEP + TEST, KEEP-DISABLED, WRAP, PATCH, REFACTOR, or DELETE",
          "Every finding includes concrete repository evidence/path/symbol/command evidence where available",
          "No application/product implementation file was modified",
          "AUD-F070 is VERIFIED at closeout when all acceptance criteria pass",
          "Current Task becomes VERIFIED and next Task AUD-080 is activated as READY during closeout"
        ],
        "verification": [
          "python3 tools/kyd_runtime_validate.py --root . --mode closeout",
          "Review git diff --name-only and confirm changes are restricted to docs/audit/** and Runtime state/task/trace files",
          "Confirm docs/audit/work/70_TEST_SECURITY_LOGGING_BUILD_DEPLOY.md is non-empty and contains evidence-based findings"
        ]
      }
    },
    {
      "task_id": "AUD-080",
      "title": "Final Audit Synthesis",
      "type": "AUDIT",
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
      }
    }
  ]
}
<!-- KYD_RUNTIME_DATA_END -->

All Audit Tasks are fully preplanned here.

The sequence is intentionally deterministic:

```text
AUD-000 → AUD-010 → AUD-020 → AUD-030 → AUD-040 → AUD-050 → AUD-060 → AUD-070 → AUD-080
```

Do not reorder or parallelize in Runtime V1 pilot. Every `depends_on` Task must be `VERIFIED`.
