# Kyd SaaS Starter STS-021 Findings Resolution Authority R1

Authority ID: `KSS-STS021-RESOLUTION-R1`  
Version: `R1`  
Status: `FROZEN`

## Purpose

This Authority governs the Planner-authorized recovery task `STS-021`. Its sole purpose is to convert the completed `STS-020` findings `F-001` through `F-009` into a deterministic findings Resolution Packet for planner/user review.

`STS-021` does not correct the candidate Starter Detailed Spec, implement application code, freeze the design, create a correction task, activate `STS-030`, provision environments, or perform production/simulated-production validation.

## Recovery Lane

Kyd Runtime remains deny-by-default and explicit-dependency-only. `STS-020` retains its `FAIL — CORRECTION REQUIRED` audit result and `BLOCKED` Runtime status. `STS-030` remains `NOT_READY` because it still depends on `STS-020 = VERIFIED`.

The explicitly authorized recovery lane is:

```text
STS-010 = VERIFIED
  -> STS-021 Build STS-020 Findings Resolution Packet
```

`STS-021` deliberately does not depend on `STS-020 = VERIFIED`; it consumes the completed STS-020 audit artifact as evidence. No `STS-022`, `STS-023`, correction, implementation, or freeze task is authorized by this Authority.

## Controlling Inputs

The task must read and preserve:

- `docs/starter/KYD_SAAS_STARTER_DETAILED_SPEC_AUDIT.md`;
- `docs/starter/KYD_SAAS_STARTER_DETAILED_SPEC.md`;
- `docs/starter/KYD_SAAS_STARTER_GAP_CLOSURE_MATRIX.md`;
- `docs/starter/KYD_SAAS_STARTER_ACCEPTANCE_MATRIX.md`;
- `docs/starter/KYD_SAAS_STARTER_DETAILED_SPEC_AUTHORING_AUTHORITY.md`;
- `docs/starter/KYD_SAAS_STARTER_STS020_AUDIT_AUTHORITY.md`;
- `docs/decisions/A-001_POSTGRES_PROVIDER_POLICY.md`;
- A-002 as registered in `docs/PROJECT_INDEX.md`;
- only the additional audit evidence specifically cited by `F-001` through `F-009`.

Finding details must be taken from the registered STS-020 audit result, not inferred from chat history.

## Required Classification

Each finding must receive exactly one class:

```text
R1 — MECHANICAL CORRECTION
R2 — PLANNER DECISION
R3 — USER DECISION
R4 — AUTHORITY CONFLICT
R5 — EVIDENCE GAP
```

The known user-decision findings `F-001`, `F-002`, `F-003`, `F-006`, and `F-009` must remain user decisions unless exact repository evidence proves the STS-020 classification itself wrong. Any reclassification requires exact evidence.

No finding may be merged, renumbered, omitted, or replaced, and no new `F-` finding may be created by `STS-021`.

## Required Resolution Packet

Create only:

`docs/starter/KYD_SAAS_STARTER_STS020_FINDINGS_RESOLUTION_PACKET.md`

It must contain:

1. Executive Summary
2. STS-020 Result
3. Finding Inventory
4. Resolution Classification
5. Mechanical Corrections
6. Planner Decisions
7. User Decisions
8. Authority Conflicts
9. Evidence Gaps
10. Correction Dependency Order
11. Expected Correction Touch Set
12. Re-audit Requirements
13. Final Decision Checklist

The Finding Inventory must contain exactly one row for every finding `F-001` through `F-009` and preserve severity, type, artifacts, capability/gap/acceptance scope, problem, resolution class, user-decision state, and correction dependency.

## User Decision Packets

Each `R3` finding must include:

```text
Finding ID
Decision question
Why it matters
Frozen constraints
Option A
Option B
Option C only when genuinely necessary
Impact of each option
Evidence
Recommended option
Recommendation confidence
What remains unchanged regardless of option
Exact later correction targets
```

Recommendations must follow repository evidence, minimal delta, `KEEP` before `PATCH`, `PATCH` before `REFACTOR`, Cloudflare-first, optional-module rules, and frozen Kyd decisions. When evidence does not favor an option, the recommendation must be `NONE — USER DECISION`.

## Non-User Resolution Paths

Every `R1` finding must define the violated requirement, evidence, deterministic correction, exact target files/sections/IDs, expected corrected state, and re-audit check. These corrections are planned only and must not be applied in `STS-021`.

Every `R2` finding must define the question, constraints, options, recommended planner decision, evidence, why user input is not required, and affected artifacts. A recommendation is not silently frozen.

Every `R5` finding must state whether it blocks design freeze or belongs to real implementation/environment validation. Provider, Cloudflare, Hyperdrive, or production/Staging provisioning must not be requested merely to close design.

## Correction Ordering

The packet must explicitly order decision, mechanical correction, consistency update, and fresh-context re-audit work so a later authorized correction task does not invent sequencing.

## Candidate Artifact Protection

`STS-021` must not modify:

- `docs/starter/KYD_SAAS_STARTER_DETAILED_SPEC.md`;
- `docs/starter/KYD_SAAS_STARTER_GAP_CLOSURE_MATRIX.md`;
- `docs/starter/KYD_SAAS_STARTER_ACCEPTANCE_MATRIX.md`.

It must also not modify application implementation, dependencies, schema/migrations, build/deployment/environment configuration, or external resources. No installs, deployments, credentials, provider resources, Cloudflare resources, or simulated-production validation are allowed.

## Completion

`STS-021` may be `VERIFIED` only when:

- all nine findings are classified;
- all five required user decision packets are complete;
- every non-user finding has a deterministic resolution path;
- correction dependency order is explicit;
- candidate Detailed Spec artifacts are unchanged;
- application implementation is unchanged;
- the Runtime closeout validator passes.

Successful closeout does not unblock `STS-030`. Runtime must expose no unauthorized executable next task and must record that planner/user decisions are required before a correction task can be authorized.

The Implementation Trace must state:

```text
STS-021 produced a findings resolution/decision packet.
No candidate Starter design corrections were applied.
No application code changed.
Awaiting planner/user decisions before correction.
```
