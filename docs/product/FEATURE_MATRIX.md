# FEATURE_MATRIX

<!-- KYD_RUNTIME_DATA_START -->
{
  "runtime_schema": "kyd.feature-matrix.v1",
  "project": "sa-template",
  "runtime_version": "KPR-V1",
  "features": [
    {
      "feature_id": "AUD-F000",
      "name": "Repository Inventory / Audit Bootstrap",
      "scope": "IN_SCOPE",
      "priority": "P0",
      "status": "VERIFIED",
      "authority": [
        "AUDIT-001"
      ],
      "implementation": [
        "docs/audit/work/00_REPOSITORY_INVENTORY.md"
      ],
      "verification": [
        "AUD-000"
      ]
    },
    {
      "feature_id": "AUD-F010",
      "name": "Framework / Cloudflare / Env / Config Audit",
      "scope": "IN_SCOPE",
      "priority": "P0",
      "status": "VERIFIED",
      "authority": [
        "AUDIT-001"
      ],
      "implementation": [
        "docs/audit/work/10_FRAMEWORK_CLOUDFLARE_ENV_CONFIG.md"
      ],
      "verification": [
        "AUD-010"
      ]
    },
    {
      "feature_id": "AUD-F020",
      "name": "Database / Drizzle / Migration Audit",
      "scope": "IN_SCOPE",
      "priority": "P0",
      "status": "VERIFIED",
      "authority": [
        "AUDIT-001"
      ],
      "implementation": [
        "docs/audit/work/20_DATABASE_DRIZZLE_MIGRATIONS.md"
      ],
      "verification": [
        "AUD-020"
      ]
    },
    {
      "feature_id": "AUD-F030",
      "name": "Auth / Email / Session / Account Audit",
      "scope": "IN_SCOPE",
      "priority": "P0",
      "status": "VERIFIED",
      "authority": [
        "AUDIT-001"
      ],
      "implementation": [
        "docs/audit/work/30_AUTH_EMAIL_SESSION_ACCOUNT.md"
      ],
      "verification": [
        "AUD-030"
      ]
    },
    {
      "feature_id": "AUD-F040",
      "name": "Payment / Orders / Webhook / Entitlement Audit",
      "scope": "IN_SCOPE",
      "priority": "P0",
      "status": "VERIFIED",
      "authority": [
        "AUDIT-001"
      ],
      "implementation": [
        "docs/audit/work/40_PAYMENT_ORDERS_WEBHOOK_ENTITLEMENT.md"
      ],
      "verification": [
        "AUD-040"
      ]
    },
    {
      "feature_id": "AUD-F050",
      "name": "Optional Platform Capabilities Audit",
      "scope": "IN_SCOPE",
      "priority": "P0",
      "status": "VERIFIED",
      "authority": [
        "AUDIT-001"
      ],
      "implementation": [
        "docs/audit/work/50_OPTIONAL_PLATFORM_CAPABILITIES.md"
      ],
      "verification": [
        "AUD-050"
      ]
    },
    {
      "feature_id": "AUD-F060",
      "name": "UI Foundation Audit",
      "scope": "IN_SCOPE",
      "priority": "P0",
      "status": "VERIFIED",
      "authority": [
        "AUDIT-001"
      ],
      "implementation": [
        "docs/audit/work/60_UI_FOUNDATION.md"
      ],
      "verification": [
        "AUD-060"
      ]
    },
    {
      "feature_id": "AUD-F070",
      "name": "Tests / Security / Logging / Build / Deploy Audit",
      "scope": "IN_SCOPE",
      "priority": "P0",
      "status": "VERIFIED",
      "authority": [
        "AUDIT-001"
      ],
      "implementation": [
        "docs/audit/work/70_TEST_SECURITY_LOGGING_BUILD_DEPLOY.md"
      ],
      "verification": [
        "AUD-070"
      ]
    },
    {
      "feature_id": "AUD-F080",
      "name": "Final Audit Synthesis",
      "scope": "IN_SCOPE",
      "priority": "P0",
      "status": "VERIFIED",
      "authority": [
        "AUDIT-001"
      ],
      "implementation": [
        "docs/audit/00_AUDIT_SUMMARY.md",
        "docs/audit/01_CAPABILITY_MATRIX.md",
        "docs/audit/02_REUSE_GAP_MATRIX.md",
        "docs/audit/03_CLOUDFLARE_RUNTIME_AUDIT.md",
        "docs/audit/04_UI_FOUNDATION_AUDIT.md",
        "docs/audit/05_TEST_AND_RELEASE_AUDIT.md",
        "docs/audit/06_RISK_AND_BLOCKERS.md",
        "docs/audit/07_DELETION_REVIEW_CANDIDATES.md",
        "docs/audit/08_REFACTOR_JUSTIFICATION.md"
      ],
      "verification": [
        "AUD-080"
      ]
    }
  ]
}
<!-- KYD_RUNTIME_DATA_END -->

`IMPLEMENTED != VERIFIED`. For this audit, a workstream is complete only when its Task and evidence are VERIFIED.
