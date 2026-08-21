# Kyd SaaS Starter STS-022 Correction Authority R1

Authority ID: `KSS-STS022-CORRECTION-R1`  
Version: `R1`  
Status: `FROZEN`

## Purpose

This Authority governs the bounded design-correction task `STS-022`. It authorizes correction of the candidate Kyd SaaS Starter Detailed Spec, Gap Closure Matrix, and Acceptance Matrix for `F-001` through `F-009` using the STS-021A source mapping and frozen Resolution Decisions R2.

It does not authorize application implementation, dependency changes, schema or migration changes, build/deployment implementation, external infrastructure, provider provisioning, testing execution, production/simulated-production validation, or Detailed Spec freeze.

## Required Inputs

Mandatory inputs are:

- `KSS-STS022-CORRECTION-R1`;
- `KSS-STS021A-RESOLUTION-R2`;
- `KPS-CAP-REUSE-R1`;
- `KSS-STS021A-MAPPING-R1`;
- `KSS-DS-AUTH-R1`;
- `KSS-STS020-AUDIT-R1`;
- `KSS-STS021-RESOLUTION-R1`;
- `DEC-A001-POLICY`;
- `AUDIT-001`.

Required evidence includes the STS-020 audit result, STS-021 packet, STS-021A mapping result, A-002 evidence, and the three candidate design artifacts.

## Correction Discipline

Apply the smallest evidence-backed delta:

```text
KEEP before PATCH
PATCH before REFACTOR
no new abstraction without proof
preserve mapped sa-template implementation
```

The task must correct all nine findings and synchronize all three candidate artifacts. It must not change the 32 capabilities, 19 gaps, priority counts, or allowed action taxonomy.

Specific correction requirements are frozen in `KSS-STS021A-RESOLUTION-R2`, including:

- preserve the existing payment routes/services/shared mutation path while specifying bounded idempotency, atomicity, lifecycle, entitlement, and retry semantics;
- freeze the one-active-token, sliding 15-minute, single-use Magic Link lifecycle;
- retain pinned Auth.js session defaults without inventing numeric values;
- add the redacted configuration ownership contract;
- restore Snapshot + Controlled Patch and no automatic merge;
- add the two-layer Visual Authority and fresh-context Fidelity Audit boundary;
- repair exact gap-to-capability mappings;
- name only evidenced user/onboarding and invite/affiliate atomicity invariants;
- add operator-approved exact immutable Staging-to-Production promotion policy while preserving the implementation gap.

## Allowed Files

- `docs/starter/KYD_SAAS_STARTER_DETAILED_SPEC.md`;
- `docs/starter/KYD_SAAS_STARTER_GAP_CLOSURE_MATRIX.md`;
- `docs/starter/KYD_SAAS_STARTER_ACCEPTANCE_MATRIX.md`;
- `docs/starter/KYD_SAAS_STARTER_STS021A_RESOLUTION_DECISIONS.md`;
- `docs/starter/KYD_SAAS_STARTER_STS022_CORRECTION_AUTHORITY.md`;
- `docs/PROJECT_INDEX.md`;
- `docs/CURRENT_STATE.md`;
- `docs/tasks/TASK_INDEX.md`;
- `docs/tasks/CURRENT_TASK.md`;
- `docs/execution/IMPLEMENTATION_TRACE.md`;
- `docs/product/FEATURE_MATRIX.md` only when Runtime schema requires it.

## Forbidden Work

Do not modify application code, components, assets, dependencies, lockfiles, database schema/migrations, Next.js/Drizzle/Wrangler/OpenNext/Docker/build/deploy configuration, provider resources, or external environments.

Do not install, deploy, provision, execute a fresh-context re-audit, or activate `STS-030`.

## Acceptance

`STS-022` may be `VERIFIED` only when:

- all `F-001` through `F-009` corrections are present and mutually consistent;
- Magic Link acceptance explicitly covers the frozen sliding 15-minute lifecycle;
- all three candidate design artifacts are synchronized;
- 32 capabilities, 32 acceptance records, 19 gaps, and `P0=8/P1=8/P2=3` remain intact;
- no new abstraction, `REFACTOR`, or `DELETE` is introduced;
- mapped existing capabilities remain preserved;
- no application/dependency/build/deploy/external-resource file changes;
- Runtime closeout validation passes.

Successful correction must route to a registered fresh-context re-audit task. It must not make `STS-030` executable before that re-audit is `VERIFIED`.
