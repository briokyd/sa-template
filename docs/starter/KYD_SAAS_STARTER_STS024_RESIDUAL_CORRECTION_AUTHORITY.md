# Kyd SaaS Starter STS-024 Residual Design Correction Authority R1

Authority ID: `KSS-STS024-RESIDUAL-CORRECTION-R1`  
Version: `R1`  
Status: `FROZEN`

## Purpose

This Authority governs `STS-024`, a bounded design recovery task after the failed `STS-023` fresh-context re-audit. It authorizes only the smallest evidence-backed documentation corrections needed to close `F-001`, `F-003`, `F-004`, `F-006`, `R-001`, and `R-002`.

It does not authorize application implementation, dependency changes, build or deployment implementation, external infrastructure, provider provisioning, production or simulated-production validation, `STS-025` execution, or `STS-030` execution.

## Recovery Dependency

`STS-024` depends on verified `STS-022`. The blocked `STS-023` result is required evidence rather than a verified dependency. This explicit recovery lane preserves deny-by-default and explicit-dependency-only Runtime behavior without rewriting the failed audit history.

## Governing Discipline

- Preserve capability-first extraction from `sa-template` under `KPS-CAP-REUSE-R1`.
- Use `KEEP` before `PATCH` and `PATCH` before `REFACTOR`.
- Do not redesign an existing capability before mapping its source implementation.
- Do not add a new abstraction from specification ambiguity alone.
- Preserve all findings already closed by `STS-023` unless an exact contradiction is discovered.
- Keep 32 capability IDs, 32 acceptance IDs, 19 gap IDs, and priorities `P0=8`, `P1=8`, `P2=3`.

## F-001 Payment Terminal and Retry Contract

Preserve the existing payment routes, services, shared order mutation path, provider-specific route security, and existing state model. Freeze these semantic outcomes:

- `created` is non-terminal.
- `paid` is durable success; only an explicitly allowed refund transition may follow.
- `failed` and `cancelled` are terminal attempt states.
- `refunded` is the terminal refunded state.
- A verified duplicate or already-applied event causes no durable mutation, is an idempotent no-op, and receives the provider-appropriate success acknowledgement.
- A verified stale or incompatible event with no legal transition causes no durable mutation, records reconciliation/anomaly evidence, and receives the provider-appropriate success acknowledgement.
- An invalid or untrusted request is rejected under existing provider/route security semantics and causes no durable mutation.
- A valid allowed transition that fails internally before atomic commit rolls back, does not durably complete idempotency, reports the provider-route retryable failure, and converges on retry.

Do not define one universal numeric HTTP status and do not create a payment transition service.

## F-003 Session Override Ownership

Pinned Auth.js session strategy and default behavior are the Kyd Starter V1 baseline. Any custom product-specific session lifetime, update, or cookie override belongs to Product-Specific Design. Such an override must be explicit, documented, and tested; it must not silently alter the Starter baseline or be inferred by an implementation model. Do not invent `maxAge`, `updateAge`, or other numeric policy.

## F-004 Replicate Configuration Mapping

Inspect the actual repository provider implementation before correction. Record the provider path, construction function, credential source, model/endpoint source, and whether credentials are explicit constructor input or environment reads.

If a usable current credential/config boundary exists, preserve its exact name and injection, classify it server-only, require it only while Replicate is enabled/selected, and prohibit initialization while OFF. If the path lacks a usable credential boundary, mark it `PARTIAL` and define the smallest logical server-only credential input at the existing constructor boundary. Do not invent a physical environment-variable name that repository evidence cannot establish, and do not create a provider/plugin framework. Acceptance must test Replicate OFF and ON behavior.

## F-006 Fidelity Audit Adjudication

Required reference items use only this rule vocabulary:

```text
EXACT_SEMANTIC
TOKEN
STRUCTURAL
RESPONSIVE_STATE
ASSET_IDENTITY
EXPLICIT_TOLERANCE
APPROVED_DEVIATION
```

Each item declares its applicable rules. `EXPLICIT_TOLERANCE` must already be recorded by the applicable Authority, reference, or manifest and may not be invented during audit. An approved deviation records deviation ID, affected item/reference, owner, reason, scope, and approval/evidence.

Rendering noise may be ignored only when it does not alter a governed token, structure or geometry relationship, content, asset identity, interaction, overflow/clipping, or responsive state. An undeclared difference against a required rule creates a finding. A failed required rule without an approved deviation fails or blocks the gate. Acceptance must support the same gate result from two fresh reviewers applying the same manifest.

## R-001 Public Configuration and Immutable Artifact Boundary

Preserve exact immutable STAGING-to-PRODUCTION artifact promotion, explicit operator approval, and no rebuild or code mutation.

Every relevant public value is classified as:

- `ARTIFACT_BOUND`: compile-time or client-inlined and therefore identical between STAGING and PRODUCTION for the promoted artifact.
- `ENVIRONMENT_RUNTIME_BOUND`: legitimately environment-specific and resolved through the smallest server/runtime injection boundary rather than environment-varying compile-time client inlining.

Prefer an existing server-rendered/runtime mechanism. If implementation support is absent, record a bounded future `PATCH`; do not create a general runtime-config framework. Acceptance proves artifact identity, an unchanged artifact-bound public-config fingerprint, correct target runtime config, no STAGING public-value leakage to PRODUCTION, and no secret exposure.

## R-002 Technical SEO Acceptance

Technical SEO acceptance must verify required favicon/icon metadata and assets, and route-applicable structured data where stable route-owned facts warrant it. Structured data must be syntactically valid and match stable facts visible or owned by the route. Do not add product keyword strategy, content strategy, product-specific schema claims, or product information architecture.

## Allowed Files

- `docs/starter/KYD_SAAS_STARTER_DETAILED_SPEC.md`
- `docs/starter/KYD_SAAS_STARTER_GAP_CLOSURE_MATRIX.md`
- `docs/starter/KYD_SAAS_STARTER_ACCEPTANCE_MATRIX.md`
- `docs/starter/KYD_SAAS_STARTER_STS024_RESIDUAL_CORRECTION_AUTHORITY.md`
- `docs/PROJECT_INDEX.md`
- `docs/CURRENT_STATE.md`
- `docs/tasks/TASK_INDEX.md`
- `docs/tasks/CURRENT_TASK.md`
- `docs/execution/IMPLEMENTATION_TRACE.md`
- minimum related decision/traceability documents only when required by Runtime schema

## Forbidden Work

Do not modify application code, components, public assets, dependencies, lockfiles, database schema/migrations, Next.js/Drizzle/Wrangler/OpenNext/Docker/build/deployment configuration, or external resources. Do not install, deploy, provision, or run production/simulated-production validation. Do not execute `STS-025` or `STS-030`.

## Acceptance

`STS-024` may be `VERIFIED` only when all six residual findings are closed across the Detailed Spec, Gap Closure Matrix, Acceptance Matrix, and traceability; closed findings do not regress; capability-first reuse still passes; no new abstraction is introduced; all counts remain fixed; no application implementation file changes; and Runtime closeout validation passes.

Successful correction must register `STS-025` as a fresh-context re-audit depending on `STS-024`. `STS-030` remains `NOT_READY` until that re-audit is verified.
