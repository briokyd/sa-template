# Kyd SaaS Starter STS-021A Existing Implementation Mapping Authority R1

Authority ID: `KSS-STS021A-MAPPING-R1`  
Version: `R1`  
Status: `FROZEN`

## Purpose

This Authority governs the Planner-authorized `STS-021A` recovery task. Its purpose is to map every `STS-020` finding `F-001` through `F-009` to actual `sa-template` source, configuration, schema, routes, defaults, and registered audit evidence before any correction or new design decision is requested.

The task prevents unnecessary reinvention. It must distinguish an implementation gap from a candidate-spec documentation gap and assign the smallest evidence-supported reuse action.

## Governing Policy

`KPS-CAP-REUSE-R1` controls this task:

```text
audit objective = reuse discovery, gap discovery, bounded hardening
reuse unit = capability
existing implementation must be mapped before redesign
future templates may be additional capability sources
new templates do not trigger repository rewrites
```

`sa-template` is the only implementation baseline evaluated in `STS-021A`.

## Recovery Lane

The authorized lane is:

```text
STS-010 = VERIFIED
STS-021 = VERIFIED
  -> STS-021A Map STS-020 Findings to Existing sa-template Implementation
```

`STS-020` retains its failed/blocked result. `STS-030` remains `NOT_READY`. `STS-021A` does not satisfy the `STS-030` dependency and does not authorize a correction task.

## Required Inputs

The task must use:

- `docs/starter/KYD_SAAS_STARTER_DETAILED_SPEC_AUDIT.md`;
- `docs/starter/KYD_SAAS_STARTER_STS020_FINDINGS_RESOLUTION_PACKET.md`;
- the candidate Detailed Spec, Gap Closure Matrix, and Acceptance Matrix as read-only context;
- `KPS-CAP-REUSE-R1`;
- `KSS-DS-AUTH-R1`;
- `KSS-STS020-AUDIT-R1`;
- `KSS-STS021-RESOLUTION-R1`;
- `DEC-A001-POLICY`;
- A-002 as registered by `PROJECT_INDEX`;
- only the additional audit evidence and source paths needed for `F-001` through `F-009`.

## Required Mapping

For each finding record:

```text
Finding ID
Affected capability
Existing implementation: YES / PARTIAL / NO
Exact repository paths
Current behavior
Current config/defaults
Current tests/evidence
Frozen target
Actual delta
Minimum justified reuse action
Decision still required: YES / NO
Decision owner if YES
Reason
```

Every finding must be evaluated in this order:

```text
KEEP
KEEP + TEST
KEEP-DISABLED
WRAP
PATCH
REFACTOR
DELETE
```

If source behavior already satisfies the target but the candidate spec failed to describe it, the normal result is `KEEP` or `KEEP + TEST` plus a later documentation correction. Specification ambiguity alone does not justify `PATCH`.

## Finding-Specific Scope

- `F-001`: trace Stripe and Creem checkout, callback, webhook, order state, credits/entitlement, replay, idempotency, and transaction behavior; determine whether a shared path already exists and whether a new transition abstraction is proven necessary.
- `F-002`: establish whether real Magic Link provider, token persistence, lifecycle, callback, and Auth email delivery exist; identify lifecycle choices source evidence cannot resolve.
- `F-003`: record the exact Auth.js package/config, explicit and implicit session settings, JWT/session callbacks, and whether preserving pinned behavior is sufficient.
- `F-004`: map current environment/config ownership, validation, defaults, and optional-secret behavior.
- `F-005`: map the frozen Snapshot + Controlled Patch policy and determine whether the finding is an implementation gap or candidate-spec omission.
- `F-006`: map the reusable UI foundation and product-specific exclusions separately from the Visual Authority/Fidelity Audit process requirement.
- `F-007`: verify capability IDs and the disputed gap mappings against existing artifacts and evidence.
- `F-008`: trace the exact user/onboarding, invite/affiliate, and payment multi-write paths and transaction evidence.
- `F-009`: map existing Vercel, Docker, Cloudflare/OpenNext, CI, release, environment-promotion, and exact-commit evidence without implementing deployment.

## Reclassification

Each finding receives exactly one current class:

```text
R1 - MECHANICAL CORRECTION
R2 - PLANNER DECISION
R3 - USER DECISION
R4 - AUTHORITY CONFLICT
R5 - EVIDENCE GAP
```

Earlier user-decision classifications are claims to re-evaluate. Reclassification requires exact repository evidence. Remaining true user decisions must be bounded to choices that existing implementation and frozen Authority cannot resolve.

## Required Output

Create only the mapping artifact:

`docs/starter/KYD_SAAS_STARTER_STS020_EXISTING_IMPLEMENTATION_MAPPING.md`

It must contain:

1. Executive Summary
2. Governing Reuse Policy
3. Mapping Method
4. F-001 Mapping
5. F-002 Mapping
6. F-003 Mapping
7. F-004 Mapping
8. F-005 Mapping
9. F-006 Mapping
10. F-007 Mapping
11. F-008 Mapping
12. F-009 Mapping
13. Finding Reclassification
14. Remaining True User Decisions
15. Minimum Correction Plan
16. Capability Provenance / Repository Paths

The mapping must preserve all nine finding IDs, record exact source paths, assign minimum actions, identify whether a decision remains, and state whether any new abstraction is actually proven necessary.

## Protected Artifacts

`STS-021A` must not modify:

- `docs/starter/KYD_SAAS_STARTER_DETAILED_SPEC.md`;
- `docs/starter/KYD_SAAS_STARTER_GAP_CLOSURE_MATRIX.md`;
- `docs/starter/KYD_SAAS_STARTER_ACCEPTANCE_MATRIX.md`;
- application code, dependencies, schema/migrations, build/deployment configuration, or external resources.

No correction, install, deploy, provisioning, provider validation, production validation, simulated-production validation, or `STS-030` execution is authorized.

## Completion

`STS-021A` may be `VERIFIED` only when all nine findings are mapped to actual source/evidence, minimum reuse actions and reclassifications are explicit, remaining decisions are bounded, protected candidate artifacts are unchanged, application code is unchanged, and Runtime closeout validation passes.

After closeout Runtime must expose no unauthorized executable next task. `STS-030` remains `NOT_READY`, and any unresolved planner/user decision remains a blocker for a later explicitly authorized correction task.
