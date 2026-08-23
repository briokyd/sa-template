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
    },
    {
      "task_id": "STS-010",
      "title": "Kyd SaaS Starter Detailed Spec Authoring",
      "type": "DESIGN",
      "status": "VERIFIED",
      "contract": {
        "goal": "Author a complete, traceable Kyd SaaS Starter Detailed Spec from the completed sa-template audit and frozen Starter decisions. The resulting spec describes the target reusable Starter without implementing it.",
        "depends_on": [
          "AUD-080"
        ],
        "authority_inputs": {
          "mandatory": [
            {
              "authority_id": "KSS-DS-AUTH-R1",
              "version": "R1"
            },
            {
              "authority_id": "DEC-A001-POLICY",
              "version": "R1"
            },
            {
              "authority_id": "AUDIT-001",
              "version": "v1"
            }
          ],
          "reference": [
            { "authority_id": "AUD-FINAL-00", "version": "v1" },
            { "authority_id": "AUD-FINAL-01", "version": "v1" },
            { "authority_id": "AUD-FINAL-02", "version": "v1" },
            { "authority_id": "AUD-FINAL-03", "version": "v1" },
            { "authority_id": "AUD-FINAL-04", "version": "v1" },
            { "authority_id": "AUD-FINAL-05", "version": "v1" },
            { "authority_id": "AUD-FINAL-06", "version": "v1" },
            { "authority_id": "AUD-FINAL-07", "version": "v1" },
            { "authority_id": "AUD-FINAL-08", "version": "v1" },
            { "authority_id": "AUD-WORK-000", "version": "v1" },
            { "authority_id": "AUD-WORK-010", "version": "v1" },
            { "authority_id": "AUD-WORK-020", "version": "v1" },
            { "authority_id": "AUD-WORK-030", "version": "v1" },
            { "authority_id": "AUD-WORK-040", "version": "v1" },
            { "authority_id": "AUD-WORK-050", "version": "v1" },
            { "authority_id": "AUD-WORK-060", "version": "v1" },
            { "authority_id": "AUD-WORK-070", "version": "v1" }
          ]
        },
        "touches": {
          "routes": [],
          "components": [],
          "files": [
            "docs/starter/KYD_SAAS_STARTER_DETAILED_SPEC_AUTHORING_AUTHORITY.md",
            "docs/starter/KYD_SAAS_STARTER_DETAILED_SPEC.md",
            "docs/starter/KYD_SAAS_STARTER_GAP_CLOSURE_MATRIX.md",
            "docs/starter/KYD_SAAS_STARTER_ACCEPTANCE_MATRIX.md",
            "docs/PROJECT_INDEX.md",
            "docs/CURRENT_STATE.md",
            "docs/product/FEATURE_MATRIX.md",
            "docs/tasks/TASK_INDEX.md",
            "docs/tasks/CURRENT_TASK.md",
            "docs/execution/IMPLEMENTATION_TRACE.md"
          ],
          "data": [],
          "api": [],
          "other": [
            "Repository read-only inspection for design evidence traceability"
          ]
        },
        "shared_resources": [
          "STARTER_DESIGN_RUNTIME_STATE",
          "STARTER_DETAILED_SPEC_ARTIFACTS"
        ],
        "gates_required": [
          "RUNTIME_V1_FREEZE",
          "AUDIT_BOOTSTRAP"
        ],
        "allowed_changes": [
          "Create or update the registered docs/starter design and Authority artifacts",
          "Register Starter design Authority and evidence in docs/PROJECT_INDEX.md",
          "Update Runtime state/task/feature/trace files only for STS-010 execution and deterministic STS-020 activation"
        ],
        "forbidden_changes": [
          "Any application implementation change",
          "Any dependency or lockfile change",
          "Any build or deployment configuration change",
          "Any database schema, migration, or external resource change",
          "Any Cloudflare, PostgreSQL provider, payment, email, AI, storage, or other provider provisioning",
          "Any production or simulated-production validation",
          "Any implementation Task creation or STS-020 execution"
        ],
        "acceptance": [
          "The master Detailed Spec contains all 32 required non-empty sections and a complete material-capability contract",
          "The Gap Closure Matrix contains GAP-001 through GAP-019 exactly once with P0=8, P1=8, and P2=3",
          "The Acceptance Matrix maps every Core and implementation-relevant optional capability to observable evidence",
          "A-001 and A-002 are represented without vendor pinning, product-specific leakage, or architecture replacement",
          "Every capability uses one allowed reuse action and no REFACTOR or DELETE is introduced",
          "Audit evidence, frozen decisions, gaps, and acceptance IDs are traceable",
          "No application, dependency, build, deploy, schema, migration, or external resource change occurs",
          "STS-F010 and STS-010 become VERIFIED and STS-020 becomes READY at closeout"
        ],
        "verification": [
          "python3 tools/kyd_runtime_validate.py --root . --mode closeout",
          "Confirm all registered Starter design artifacts exist and are non-empty",
          "Verify exact GAP-001 through GAP-019 uniqueness and P0/P1/P2 counts",
          "Verify capability schema, allowed action vocabulary, evidence links, and acceptance coverage",
          "Review git diff --name-only and confirm no application/dependency/build/deploy/schema/migration file changed"
        ]
      }
    },
    {
      "task_id": "STS-020",
      "title": "Starter Detailed Spec Completeness / Ambiguity Audit",
      "type": "AUDIT",
      "status": "BLOCKED",
      "contract": {
        "goal": "Independently audit the authored Starter Detailed Spec for completeness, implementation-affecting ambiguity, traceability, frozen-decision coverage, architecture drift, product-specific leakage, and mechanically testable acceptance.",
        "depends_on": [
          "STS-010"
        ],
        "authority_inputs": {
          "mandatory": [
            { "authority_id": "KSS-STS020-AUDIT-R1", "version": "R1" },
            { "authority_id": "KSS-DS-AUTH-R1", "version": "R1" },
            { "authority_id": "DEC-A001-POLICY", "version": "R1" },
            { "authority_id": "AUDIT-001", "version": "v1" }
          ],
          "reference": [
            { "authority_id": "AUD-FINAL-00", "version": "v1" },
            { "authority_id": "AUD-FINAL-02", "version": "v1" },
            { "authority_id": "AUD-FINAL-04", "version": "v1" },
            { "authority_id": "AUD-FINAL-05", "version": "v1" },
            { "authority_id": "KSS-DS-SPEC-R1", "version": "R1" },
            { "authority_id": "KSS-DS-GAPS-R1", "version": "R1" },
            { "authority_id": "KSS-DS-ACCEPT-R1", "version": "R1" }
          ]
        },
        "touches": {
          "routes": [],
          "components": [],
          "files": [
            "docs/starter/**",
            "docs/PROJECT_INDEX.md",
            "docs/CURRENT_STATE.md",
            "docs/product/FEATURE_MATRIX.md",
            "docs/tasks/TASK_INDEX.md",
            "docs/tasks/CURRENT_TASK.md",
            "docs/execution/IMPLEMENTATION_TRACE.md"
          ],
          "data": [],
          "api": [],
          "other": ["Repository read-only evidence review"]
        },
        "shared_resources": ["STARTER_DESIGN_RUNTIME_STATE", "STARTER_DETAILED_SPEC_ARTIFACTS"],
        "gates_required": ["RUNTIME_V1_FREEZE", "AUDIT_BOOTSTRAP"],
        "allowed_changes": [
          "Create or update registered docs/starter design review artifacts",
          "Update Runtime state/task/feature/trace files for deterministic audit closeout"
        ],
        "forbidden_changes": [
          "Any application, dependency, database, build, deployment, or external resource change",
          "Any Detailed Spec freeze before all implementation-affecting ambiguity is resolved",
          "Any implementation Task creation or STS-030 execution"
        ],
        "acceptance": [
          "All material domains, 19 gaps, frozen decisions, capability contracts, acceptance, and traceability are independently checked",
          "Every implementation-affecting ambiguity is resolved or explicitly blocks STS-030",
          "No application implementation file is changed",
          "STS-020 becomes VERIFIED and STS-030 becomes READY only when the audit passes"
        ],
        "verification": [
          "python3 tools/kyd_runtime_validate.py --root . --mode closeout",
          "Review the complete Starter design artifact set against KSS-DS-AUTH-R1 and audit evidence",
          "Review git diff --name-only for design-only scope"
        ]
      }
    },
    {
      "task_id": "STS-021",
      "title": "Build STS-020 Findings Resolution Packet",
      "type": "DESIGN",
      "status": "VERIFIED",
      "contract": {
        "goal": "Convert F-001 through F-009 into a complete, evidence-backed mechanical/planner/user decision packet without modifying candidate design artifacts.",
        "depends_on": ["STS-010"],
        "authority_inputs": {
          "mandatory": [
            { "authority_id": "KSS-STS021-RESOLUTION-R1", "version": "R1" },
            { "authority_id": "KSS-STS020-AUDIT-R1", "version": "R1" },
            { "authority_id": "KSS-DS-AUTH-R1", "version": "R1" },
            { "authority_id": "DEC-A001-POLICY", "version": "R1" },
            { "authority_id": "AUDIT-001", "version": "v1" }
          ],
          "reference": [
            { "authority_id": "KSS-STS020-AUDIT-RESULT-R1", "version": "R1" },
            { "authority_id": "KSS-DS-SPEC-R1", "version": "R1" },
            { "authority_id": "KSS-DS-GAPS-R1", "version": "R1" },
            { "authority_id": "KSS-DS-ACCEPT-R1", "version": "R1" },
            { "authority_id": "AUD-WORK-010", "version": "v1" },
            { "authority_id": "AUD-WORK-020", "version": "v1" },
            { "authority_id": "AUD-WORK-030", "version": "v1" },
            { "authority_id": "AUD-WORK-040", "version": "v1" },
            { "authority_id": "AUD-WORK-060", "version": "v1" },
            { "authority_id": "AUD-FINAL-04", "version": "v1" },
            { "authority_id": "AUD-FINAL-05", "version": "v1" }
          ]
        },
        "touches": {
          "routes": [],
          "components": [],
          "files": [
            "docs/starter/KYD_SAAS_STARTER_STS020_FINDINGS_RESOLUTION_PACKET.md",
            "docs/starter/KYD_SAAS_STARTER_STS021_FINDINGS_RESOLUTION_AUTHORITY.md",
            "docs/PROJECT_INDEX.md",
            "docs/CURRENT_STATE.md",
            "docs/tasks/TASK_INDEX.md",
            "docs/tasks/CURRENT_TASK.md",
            "docs/execution/IMPLEMENTATION_TRACE.md"
          ],
          "data": [],
          "api": [],
          "other": ["Repository read-only review of finding-cited evidence"]
        },
        "shared_resources": ["STARTER_DESIGN_RUNTIME_STATE", "STARTER_DETAILED_SPEC_FINDINGS"],
        "gates_required": ["RUNTIME_V1_FREEZE", "AUDIT_BOOTSTRAP"],
        "allowed_changes": [
          "Create and register the STS-021 Authority and STS-020 Findings Resolution Packet",
          "Update Runtime state/task/trace files only for recovery-task activation and closeout"
        ],
        "forbidden_changes": [
          "Modify docs/starter/KYD_SAAS_STARTER_DETAILED_SPEC.md",
          "Modify docs/starter/KYD_SAAS_STARTER_GAP_CLOSURE_MATRIX.md",
          "Modify docs/starter/KYD_SAAS_STARTER_ACCEPTANCE_MATRIX.md",
          "Any application, dependency, database, build, deployment, environment, or external resource change",
          "Any candidate design correction, correction-task creation, Detailed Spec freeze, or STS-030 activation/execution"
        ],
        "acceptance": [
          "F-001 through F-009 each appear once and use exactly one R1/R2/R3/R4/R5 resolution class",
          "F-001, F-002, F-003, F-006, and F-009 have complete bounded user decision packets",
          "Every non-user finding has a deterministic evidence-backed resolution path",
          "Correction dependency order, later touch set, re-audit requirements, and final decision checklist are explicit",
          "Candidate Detailed Spec, Gap Closure Matrix, and Acceptance Matrix remain unchanged",
          "No application implementation file is changed and STS-030 remains NOT_READY"
        ],
        "verification": [
          "python3 tools/kyd_runtime_validate.py --root . --mode closeout",
          "Verify all nine finding classifications and five user decision packets",
          "Compare candidate artifact SHA-256 values with the pre-STS-021 values",
          "Review git diff --name-only and git status --short for authorized documentation-only scope"
        ]
      }
    },
    {
      "task_id": "STS-021A",
      "title": "Map STS-020 Findings to Existing sa-template Implementation",
      "type": "AUDIT",
      "status": "VERIFIED",
      "contract": {
        "goal": "Re-evaluate F-001 through F-009 against actual sa-template code, configuration, and evidence before asking for new design decisions.",
        "depends_on": ["STS-021"],
        "authority_inputs": {
          "mandatory": [
            { "authority_id": "KPS-CAP-REUSE-R1", "version": "R1" },
            { "authority_id": "KSS-STS021A-MAPPING-R1", "version": "R1" },
            { "authority_id": "KSS-STS020-AUDIT-R1", "version": "R1" },
            { "authority_id": "KSS-STS021-RESOLUTION-R1", "version": "R1" },
            { "authority_id": "KSS-DS-AUTH-R1", "version": "R1" },
            { "authority_id": "DEC-A001-POLICY", "version": "R1" },
            { "authority_id": "AUDIT-001", "version": "v1" }
          ],
          "reference": [
            { "authority_id": "KSS-STS020-AUDIT-RESULT-R1", "version": "R1" },
            { "authority_id": "KSS-STS021-PACKET-R1", "version": "R1" },
            { "authority_id": "KSS-DS-SPEC-R1", "version": "R1" },
            { "authority_id": "KSS-DS-GAPS-R1", "version": "R1" },
            { "authority_id": "KSS-DS-ACCEPT-R1", "version": "R1" },
            { "authority_id": "AUD-WORK-010", "version": "v1" },
            { "authority_id": "AUD-WORK-020", "version": "v1" },
            { "authority_id": "AUD-WORK-030", "version": "v1" },
            { "authority_id": "AUD-WORK-040", "version": "v1" },
            { "authority_id": "AUD-WORK-060", "version": "v1" },
            { "authority_id": "AUD-WORK-070", "version": "v1" },
            { "authority_id": "AUD-FINAL-04", "version": "v1" },
            { "authority_id": "AUD-FINAL-05", "version": "v1" }
          ]
        },
        "touches": {
          "routes": [],
          "components": [],
          "files": [
            "docs/decisions/KYD_CAPABILITY_FIRST_MULTI_TEMPLATE_REUSE_POLICY.md",
            "docs/starter/KYD_SAAS_STARTER_STS021A_EXISTING_IMPLEMENTATION_MAPPING_AUTHORITY.md",
            "docs/starter/KYD_SAAS_STARTER_STS020_EXISTING_IMPLEMENTATION_MAPPING.md",
            "docs/PROJECT_INDEX.md",
            "docs/CURRENT_STATE.md",
            "docs/tasks/TASK_INDEX.md",
            "docs/tasks/CURRENT_TASK.md",
            "docs/execution/IMPLEMENTATION_TRACE.md"
          ],
          "data": [],
          "api": [],
          "other": ["Repository read-only inspection of finding-related source, configuration, and registered evidence"]
        },
        "shared_resources": ["STARTER_DESIGN_RUNTIME_STATE", "STARTER_DETAILED_SPEC_FINDINGS"],
        "gates_required": ["RUNTIME_V1_FREEZE", "AUDIT_BOOTSTRAP"],
        "allowed_changes": [
          "Create and register the capability-first reuse and STS-021A mapping Authorities",
          "Create the STS-020 Existing Implementation Mapping artifact",
          "Update Runtime state/task/trace files only for STS-021A activation and closeout"
        ],
        "forbidden_changes": [
          "Modify docs/starter/KYD_SAAS_STARTER_DETAILED_SPEC.md",
          "Modify docs/starter/KYD_SAAS_STARTER_GAP_CLOSURE_MATRIX.md",
          "Modify docs/starter/KYD_SAAS_STARTER_ACCEPTANCE_MATRIX.md",
          "Any application, dependency, database, build, deployment, environment, or external resource change",
          "Any candidate design correction, user-decision selection, correction-task creation, Detailed Spec freeze, or STS-030 activation/execution"
        ],
        "acceptance": [
          "F-001 through F-009 are each mapped to actual sa-template implementation and exact repository paths",
          "Every finding records current behavior/defaults/tests, frozen target, actual delta, minimum reuse action, and decision status",
          "Former user decisions are independently re-evaluated and every reclassification is evidence-backed",
          "Remaining true user decisions and the minimum later correction plan are explicit",
          "Candidate Detailed Spec, Gap Closure Matrix, and Acceptance Matrix remain unchanged",
          "No application implementation file is changed and STS-030 remains NOT_READY"
        ],
        "verification": [
          "python3 tools/kyd_runtime_validate.py --root . --mode closeout",
          "Verify all nine finding mappings, reuse actions, reclassifications, provenance paths, and remaining decisions",
          "Compare candidate artifact SHA-256 values with the pre-STS-021A values",
          "Review git diff --name-only and git status --short for authorized documentation-only scope"
        ]
      }
    },
    {
      "task_id": "STS-022",
      "title": "Correct Starter Detailed Spec from STS-020 Findings",
      "type": "DESIGN",
      "status": "VERIFIED",
      "contract": {
        "goal": "Apply all resolved F-001 through F-009 corrections to the candidate Starter design artifacts while preserving mapped sa-template implementation and avoiding application work.",
        "depends_on": ["STS-021A"],
        "authority_inputs": {
          "mandatory": [
            { "authority_id": "KSS-STS022-CORRECTION-R1", "version": "R1" },
            { "authority_id": "KSS-STS021A-RESOLUTION-R2", "version": "R2" },
            { "authority_id": "KPS-CAP-REUSE-R1", "version": "R1" },
            { "authority_id": "KSS-STS021A-MAPPING-R1", "version": "R1" },
            { "authority_id": "KSS-DS-AUTH-R1", "version": "R1" },
            { "authority_id": "KSS-STS020-AUDIT-R1", "version": "R1" },
            { "authority_id": "KSS-STS021-RESOLUTION-R1", "version": "R1" },
            { "authority_id": "DEC-A001-POLICY", "version": "R1" },
            { "authority_id": "AUDIT-001", "version": "v1" }
          ],
          "reference": [
            { "authority_id": "KSS-STS020-AUDIT-RESULT-R1", "version": "R1" },
            { "authority_id": "KSS-STS021-PACKET-R1", "version": "R1" },
            { "authority_id": "KSS-STS021A-MAPPING-RESULT-R1", "version": "R1" },
            { "authority_id": "KSS-DS-SPEC-R1", "version": "R1" },
            { "authority_id": "KSS-DS-GAPS-R1", "version": "R1" },
            { "authority_id": "KSS-DS-ACCEPT-R1", "version": "R1" },
            { "authority_id": "AUD-FINAL-04", "version": "v1" },
            { "authority_id": "AUD-WORK-010", "version": "v1" },
            { "authority_id": "AUD-WORK-020", "version": "v1" },
            { "authority_id": "AUD-WORK-030", "version": "v1" },
            { "authority_id": "AUD-WORK-040", "version": "v1" },
            { "authority_id": "AUD-WORK-060", "version": "v1" },
            { "authority_id": "AUD-WORK-070", "version": "v1" }
          ]
        },
        "touches": {
          "routes": [],
          "components": [],
          "files": [
            "docs/starter/KYD_SAAS_STARTER_DETAILED_SPEC.md",
            "docs/starter/KYD_SAAS_STARTER_GAP_CLOSURE_MATRIX.md",
            "docs/starter/KYD_SAAS_STARTER_ACCEPTANCE_MATRIX.md",
            "docs/starter/KYD_SAAS_STARTER_STS021A_RESOLUTION_DECISIONS.md",
            "docs/starter/KYD_SAAS_STARTER_STS022_CORRECTION_AUTHORITY.md",
            "docs/PROJECT_INDEX.md",
            "docs/CURRENT_STATE.md",
            "docs/tasks/TASK_INDEX.md",
            "docs/tasks/CURRENT_TASK.md",
            "docs/execution/IMPLEMENTATION_TRACE.md",
            "docs/product/FEATURE_MATRIX.md"
          ],
          "data": [],
          "api": [],
          "other": []
        },
        "shared_resources": ["STARTER_DESIGN_RUNTIME_STATE", "STARTER_DETAILED_SPEC_ARTIFACTS"],
        "gates_required": ["RUNTIME_V1_FREEZE", "AUDIT_BOOTSTRAP"],
        "allowed_changes": [
          "Create and register the STS-021A resolution and STS-022 correction Authorities",
          "Correct the candidate Detailed Spec, Gap Closure Matrix, and Acceptance Matrix for F-001 through F-009",
          "Update Runtime state/task/feature/trace files only for STS-022 activation and closeout",
          "Register a fresh-context re-audit task without executing it"
        ],
        "forbidden_changes": [
          "Any application, dependency, database, build, deployment, environment, or external resource change",
          "Any new abstraction not proven by mapped sa-template evidence",
          "Any capability or gap count change without stopping on a proven baseline conflict",
          "Any re-audit or STS-030 execution"
        ],
        "acceptance": [
          "F-001 through F-009 are corrected according to the frozen resolution decisions and mapped sa-template evidence",
          "The Detailed Spec, Gap Closure Matrix, and Acceptance Matrix are synchronized",
          "The capability count remains 32 and the gap inventory remains P0=8, P1=8, P2=3, total=19",
          "No new abstraction is introduced and the mapped existing capabilities are preserved",
          "No application implementation file is changed",
          "A fresh-context re-audit remains required before STS-030"
        ],
        "verification": [
          "python3 tools/kyd_runtime_validate.py --root . --mode closeout",
          "Verify the F-001 through F-009 correction checklist against all three candidate artifacts",
          "Verify capability and gap counts and cross-artifact traceability",
          "Review git diff --name-only and git status --short for authorized design-document scope"
        ]
      }
    },
    {
      "task_id": "STS-023",
      "title": "Starter Detailed Spec Completeness / Ambiguity Re-audit",
      "type": "AUDIT",
      "status": "BLOCKED",
      "contract": {
        "goal": "Independently re-audit the STS-022-corrected Starter Detailed Spec, Gap Closure Matrix, and Acceptance Matrix against the STS-020 completeness and ambiguity criteria before freeze.",
        "depends_on": ["STS-022"],
        "authority_inputs": {
          "mandatory": [
            { "authority_id": "KSS-STS020-AUDIT-R1", "version": "R1" },
            { "authority_id": "KSS-STS021A-RESOLUTION-R2", "version": "R2" },
            { "authority_id": "KSS-DS-AUTH-R1", "version": "R1" },
            { "authority_id": "KPS-CAP-REUSE-R1", "version": "R1" },
            { "authority_id": "DEC-A001-POLICY", "version": "R1" },
            { "authority_id": "AUDIT-001", "version": "v1" }
          ],
          "reference": [
            { "authority_id": "KSS-STS020-AUDIT-RESULT-R1", "version": "R1" },
            { "authority_id": "KSS-STS021-PACKET-R1", "version": "R1" },
            { "authority_id": "KSS-STS021A-MAPPING-RESULT-R1", "version": "R1" },
            { "authority_id": "KSS-DS-SPEC-R1", "version": "R1" },
            { "authority_id": "KSS-DS-GAPS-R1", "version": "R1" },
            { "authority_id": "KSS-DS-ACCEPT-R1", "version": "R1" },
            { "authority_id": "AUD-FINAL-00", "version": "v1" },
            { "authority_id": "AUD-FINAL-02", "version": "v1" },
            { "authority_id": "AUD-FINAL-04", "version": "v1" },
            { "authority_id": "AUD-FINAL-05", "version": "v1" }
          ]
        },
        "touches": {
          "routes": [],
          "components": [],
          "files": [
            "docs/starter/KYD_SAAS_STARTER_DETAILED_SPEC_REAUDIT.md",
            "docs/PROJECT_INDEX.md",
            "docs/CURRENT_STATE.md",
            "docs/tasks/TASK_INDEX.md",
            "docs/tasks/CURRENT_TASK.md",
            "docs/execution/IMPLEMENTATION_TRACE.md",
            "docs/product/FEATURE_MATRIX.md"
          ],
          "data": [],
          "api": [],
          "other": ["Read-only inspection of the corrected candidate design artifacts and registered Audit/Authority evidence"]
        },
        "shared_resources": ["STARTER_DESIGN_RUNTIME_STATE", "STARTER_DETAILED_SPEC_ARTIFACTS"],
        "gates_required": ["RUNTIME_V1_FREEZE", "AUDIT_BOOTSTRAP"],
        "allowed_changes": [
          "Create and register a fresh-context re-audit artifact",
          "Update Runtime state/task/feature/trace files only for STS-023 closeout"
        ],
        "forbidden_changes": [
          "Modify the candidate Detailed Spec, Gap Closure Matrix, or Acceptance Matrix during audit",
          "Any application, dependency, database, build, deployment, environment, or external resource change",
          "Any finding suppression, implementation work, or STS-030 execution"
        ],
        "acceptance": [
          "All STS-020 audit dimensions are independently re-evaluated against the corrected artifacts",
          "All F-001 through F-009 corrections and their cross-artifact traceability are tested",
          "Capability, acceptance, gap, priority, and reuse-action counts are verified",
          "No unresolved BLOCKER or MAJOR remains before STS-030 can become READY",
          "No candidate design or application implementation file is changed"
        ],
        "verification": [
          "python3 tools/kyd_runtime_validate.py --root . --mode closeout",
          "Verify the re-audit result follows the STS-020 deterministic result rule",
          "Review git diff --name-only and candidate artifact hashes for audit-only scope"
        ]
      }
    },
    {
      "task_id": "STS-024",
      "title": "Close STS-023 Residual Design Ambiguities",
      "type": "DESIGN",
      "status": "VERIFIED",
      "contract": {
        "goal": "Close only F-001, F-003, F-004, F-006, R-001, and R-002 through the smallest evidence-backed documentation corrections while preserving mapped sa-template implementation.",
        "depends_on": ["STS-022"],
        "authority_inputs": {
          "mandatory": [
            { "authority_id": "KSS-STS024-RESIDUAL-CORRECTION-R1", "version": "R1" },
            { "authority_id": "KPS-CAP-REUSE-R1", "version": "R1" },
            { "authority_id": "KSS-DS-AUTH-R1", "version": "R1" },
            { "authority_id": "KSS-STS021A-RESOLUTION-R2", "version": "R2" },
            { "authority_id": "DEC-A001-POLICY", "version": "R1" },
            { "authority_id": "AUDIT-001", "version": "v1" }
          ],
          "reference": [
            { "authority_id": "KSS-STS023-REAUDIT-RESULT-R1", "version": "R1" },
            { "authority_id": "KSS-STS021A-MAPPING-RESULT-R1", "version": "R1" },
            { "authority_id": "KSS-DS-SPEC-R1", "version": "R1" },
            { "authority_id": "KSS-DS-GAPS-R1", "version": "R1" },
            { "authority_id": "KSS-DS-ACCEPT-R1", "version": "R1" },
            { "authority_id": "AUD-FINAL-04", "version": "v1" },
            { "authority_id": "AUD-WORK-060", "version": "v1" },
            { "authority_id": "AUD-WORK-010", "version": "v1" },
            { "authority_id": "AUD-WORK-050", "version": "v1" },
            { "authority_id": "AUD-FINAL-05", "version": "v1" }
          ]
        },
        "touches": {
          "routes": [],
          "components": [],
          "files": [
            "docs/starter/KYD_SAAS_STARTER_DETAILED_SPEC.md",
            "docs/starter/KYD_SAAS_STARTER_GAP_CLOSURE_MATRIX.md",
            "docs/starter/KYD_SAAS_STARTER_ACCEPTANCE_MATRIX.md",
            "docs/starter/KYD_SAAS_STARTER_STS024_RESIDUAL_CORRECTION_AUTHORITY.md",
            "docs/PROJECT_INDEX.md",
            "docs/CURRENT_STATE.md",
            "docs/tasks/TASK_INDEX.md",
            "docs/tasks/CURRENT_TASK.md",
            "docs/execution/IMPLEMENTATION_TRACE.md"
          ],
          "data": [],
          "api": [],
          "other": ["Read-only source inspection for Replicate credential and construction evidence"]
        },
        "shared_resources": ["STARTER_DESIGN_RUNTIME_STATE", "STARTER_DETAILED_SPEC_ARTIFACTS"],
        "gates_required": ["RUNTIME_V1_FREEZE", "AUDIT_BOOTSTRAP"],
        "allowed_changes": [
          "Create and register the STS-024 residual correction Authority",
          "Correct only F-001, F-003, F-004, F-006, R-001, and R-002 in the three candidate design artifacts",
          "Update Runtime state/task/trace files only for STS-024 activation and closeout",
          "Register STS-025 as the required fresh-context re-audit without executing it"
        ],
        "forbidden_changes": [
          "Any application, dependency, database, build, deployment, environment, or external resource change",
          "Any capability or gap ID/count/priority change",
          "Any new abstraction, closed-finding regression, STS-025 execution, or STS-030 execution"
        ],
        "acceptance": [
          "F-001, F-003, F-004, F-006, R-001, and R-002 are closed with deterministic evidence-backed wording",
          "The Detailed Spec, Gap Closure Matrix, and Acceptance Matrix are synchronized",
          "Capabilities remain 32; acceptance records remain 32; gaps remain P0=8, P1=8, P2=3, total=19",
          "F-002, F-005, F-007, F-008, and F-009 do not regress",
          "Capability-first reuse remains PASS and no new abstraction is introduced",
          "No application implementation file is changed",
          "STS-025 is registered for fresh-context re-audit while STS-030 remains NOT_READY"
        ],
        "verification": [
          "python3 tools/kyd_runtime_validate.py --root . --mode closeout",
          "Verify each residual finding against the STS-023 re-audit and STS-024 Authority",
          "Verify capability, acceptance, gap, and priority counts plus closed-finding invariants",
          "Review git diff --name-only and git status --short for authorized documentation-only scope"
        ]
      }
    },
    {
      "task_id": "STS-025",
      "title": "Fresh-Context Re-Audit After STS-024",
      "type": "AUDIT",
      "status": "VERIFIED",
      "contract": {
        "goal": "Independently re-audit the STS-024-corrected Starter Detailed Spec, Gap Closure Matrix, and Acceptance Matrix against the STS-020 and STS-023 completeness and ambiguity criteria before freeze.",
        "depends_on": ["STS-024"],
        "authority_inputs": {
          "mandatory": [
            { "authority_id": "KSS-STS020-AUDIT-R1", "version": "R1" },
            { "authority_id": "KSS-STS024-RESIDUAL-CORRECTION-R1", "version": "R1" },
            { "authority_id": "KSS-DS-AUTH-R1", "version": "R1" },
            { "authority_id": "KPS-CAP-REUSE-R1", "version": "R1" },
            { "authority_id": "DEC-A001-POLICY", "version": "R1" },
            { "authority_id": "AUDIT-001", "version": "v1" }
          ],
          "reference": [
            { "authority_id": "KSS-STS023-REAUDIT-RESULT-R1", "version": "R1" },
            { "authority_id": "KSS-STS021A-RESOLUTION-R2", "version": "R2" },
            { "authority_id": "KSS-STS021A-MAPPING-RESULT-R1", "version": "R1" },
            { "authority_id": "KSS-DS-SPEC-R1", "version": "R1" },
            { "authority_id": "KSS-DS-GAPS-R1", "version": "R1" },
            { "authority_id": "KSS-DS-ACCEPT-R1", "version": "R1" },
            { "authority_id": "AUD-FINAL-04", "version": "v1" },
            { "authority_id": "AUD-FINAL-05", "version": "v1" },
            { "authority_id": "AUD-WORK-010", "version": "v1" },
            { "authority_id": "AUD-WORK-040", "version": "v1" },
            { "authority_id": "AUD-WORK-050", "version": "v1" }
          ]
        },
        "touches": {
          "routes": [],
          "components": [],
          "files": [
            "docs/starter/KYD_SAAS_STARTER_DETAILED_SPEC_REAUDIT_STS025.md",
            "docs/PROJECT_INDEX.md",
            "docs/CURRENT_STATE.md",
            "docs/tasks/TASK_INDEX.md",
            "docs/tasks/CURRENT_TASK.md",
            "docs/execution/IMPLEMENTATION_TRACE.md"
          ],
          "data": [],
          "api": [],
          "other": ["Read-only inspection of the STS-024-corrected candidate design artifacts and exact registered evidence"]
        },
        "shared_resources": ["STARTER_DESIGN_RUNTIME_STATE", "STARTER_DETAILED_SPEC_ARTIFACTS"],
        "gates_required": ["RUNTIME_V1_FREEZE", "AUDIT_BOOTSTRAP"],
        "allowed_changes": [
          "Create and register the STS-025 fresh-context re-audit artifact",
          "Update Runtime state/task/trace files only for STS-025 closeout"
        ],
        "forbidden_changes": [
          "Modify the candidate Detailed Spec, Gap Closure Matrix, or Acceptance Matrix during audit",
          "Any application, dependency, database, build, deployment, environment, or external resource change",
          "Any finding suppression, implementation work, or STS-030 execution"
        ],
        "acceptance": [
          "All STS-020 and STS-023 audit dimensions are independently re-evaluated against the STS-024-corrected artifacts",
          "F-001, F-003, F-004, F-006, R-001, and R-002 closure and cross-artifact traceability are tested",
          "F-002, F-005, F-007, F-008, and F-009 remain closed",
          "Capability, acceptance, gap, priority, and reuse-action counts are verified",
          "No unresolved BLOCKER, MAJOR, or implementation-affecting ambiguity remains before STS-030 can become READY",
          "No candidate design or application implementation file is changed"
        ],
        "verification": [
          "python3 tools/kyd_runtime_validate.py --root . --mode closeout",
          "Verify the re-audit result follows the STS-020 deterministic result rule",
          "Review git diff --name-only and candidate artifact hashes for audit-only scope"
        ]
      }
    },
    {
      "task_id": "STS-030",
      "title": "Starter Detailed Spec Freeze",
      "type": "DECISION",
      "status": "VERIFIED",
      "contract": {
        "goal": "Freeze the audited Kyd SaaS Starter Detailed Spec as implementation planning Authority without starting implementation.",
        "depends_on": ["STS-025"],
        "authority_inputs": {
          "mandatory": [
            { "authority_id": "KSS-DS-AUTH-R1", "version": "R1" },
            { "authority_id": "KSS-STS020-AUDIT-R1", "version": "R1" },
            { "authority_id": "KSS-STS021A-RESOLUTION-R2", "version": "R2" },
            { "authority_id": "KSS-STS024-RESIDUAL-CORRECTION-R1", "version": "R1" },
            { "authority_id": "DEC-A001-POLICY", "version": "R1" },
            { "authority_id": "AUDIT-001", "version": "v1" }
          ],
          "reference": [
            { "authority_id": "AUD-FINAL-00", "version": "v1" },
            { "authority_id": "AUD-FINAL-02", "version": "v1" },
            { "authority_id": "AUD-FINAL-04", "version": "v1" },
            { "authority_id": "AUD-FINAL-05", "version": "v1" },
            { "authority_id": "KSS-DS-SPEC-R1", "version": "R1" },
            { "authority_id": "KSS-DS-GAPS-R1", "version": "R1" },
            { "authority_id": "KSS-DS-ACCEPT-R1", "version": "R1" }
          ]
        },
        "touches": {
          "routes": [],
          "components": [],
          "files": [
            "docs/starter/**",
            "docs/PROJECT_INDEX.md",
            "docs/CURRENT_STATE.md",
            "docs/product/FEATURE_MATRIX.md",
            "docs/tasks/TASK_INDEX.md",
            "docs/tasks/CURRENT_TASK.md",
            "docs/execution/IMPLEMENTATION_TRACE.md"
          ],
          "data": [],
          "api": [],
          "other": []
        },
        "shared_resources": ["STARTER_DESIGN_RUNTIME_STATE", "STARTER_DETAILED_SPEC_ARTIFACTS"],
        "gates_required": ["RUNTIME_V1_FREEZE", "AUDIT_BOOTSTRAP"],
        "allowed_changes": [
          "Freeze registered Starter design artifacts after verified review",
          "Update Runtime state/task/feature/trace files for deterministic closeout"
        ],
        "forbidden_changes": [
          "Any application, dependency, database, build, deployment, or external resource change",
          "Any freeze with unresolved implementation-affecting ambiguity",
          "Any implementation Task creation or execution"
        ],
        "acceptance": [
          "STS-025 is VERIFIED with no unresolved implementation-affecting ambiguity",
          "The exact reviewed design artifact versions and hashes are registered as FROZEN Authority",
          "No application implementation file is changed",
          "STS-030 becomes VERIFIED without starting implementation"
        ],
        "verification": [
          "python3 tools/kyd_runtime_validate.py --root . --mode closeout",
          "Verify frozen artifact hashes against docs/PROJECT_INDEX.md",
          "Review git diff --name-only for design-only scope"
        ]
      }
    },
    {
      "task_id": "BS-IMPL-010",
      "title": "Bootstrap Source Manifest and Agent-Neutral Entry Template",
      "type": "IMPLEMENTATION",
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
      }
    },
    {
      "task_id": "BS-IMPL-020",
      "title": "Generic Bootstrap Initializer and Zero-State Generation",
      "type": "IMPLEMENTATION",
      "status": "VERIFIED",
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
      }
    },
    {
      "task_id": "BS-CORR-020",
      "title": "Correct Bootstrap PROJECT_INDEX Metadata",
      "type": "IMPLEMENTATION",
      "status": "VERIFIED",
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
      }
    },
    {
      "task_id": "BS-IMPL-030",
      "title": "Bootstrap-Specific Validation and Final Initializer Integration",
      "type": "IMPLEMENTATION",
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
      }
    },
    {
      "task_id": "BS-IMPL-040",
      "title": "Independent End-to-End Bootstrap Verification",
      "type": "VERIFICATION",
      "status": "NOT_READY",
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
      }
    }
  ]
}
<!-- KYD_RUNTIME_DATA_END -->

All Full Repository Audit and current Starter Detailed Spec design Tasks are fully preplanned here.

The sequence is intentionally deterministic:

```text
AUD-000 → AUD-010 → AUD-020 → AUD-030 → AUD-040 → AUD-050 → AUD-060 → AUD-070 → AUD-080
```

Do not reorder or parallelize in Runtime V1 pilot. Every `depends_on` Task must be `VERIFIED`.

The authorized design and recovery sequence is:

```text
STS-010 → STS-020 (historical failed audit)
    └────→ STS-021 findings-resolution recovery
              └────→ STS-021A existing-implementation mapping recovery
                        └────→ STS-022 correction → STS-023 failed re-audit
                                  └────→ STS-024 residual correction → STS-025 fresh-context re-audit → STS-030 freeze
```

STS-020 and STS-023 remain historical BLOCKED audit results. STS-024, STS-025, and STS-030 are VERIFIED. The Kyd SaaS Starter Detailed Spec R1 is FROZEN.

The Planner-approved Bootstrap implementation sequence is registered as:

```text
BS-IMPL-010 → BS-IMPL-020 → BS-IMPL-030 → BS-IMPL-040
```

BS-IMPL-010 is VERIFIED. BS-IMPL-020 is READY for separate mechanical activation; BS-IMPL-030 and BS-IMPL-040 remain NOT_READY until their explicit dependencies are VERIFIED.
