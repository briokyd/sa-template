# Kyd SaaS Starter Detailed Spec Authoring Authority R1

Authority ID: `KSS-DS-AUTH-R1`  
Version: `R1`  
Status: `FROZEN`

## Purpose

This Authority governs `STS-010`, `STS-020`, and `STS-030`. It converts the completed `sa-template` Full Repository Audit and frozen Starter decisions into a complete, reviewable, and eventually frozen Kyd SaaS Starter Detailed Spec.

The objective is to extract and harden a reusable Starter from `sa-template`. The work does not rewrite `sa-template`, create a new SaaS framework, or require production or simulated-production infrastructure validation during design.

## Governing Order

1. Reuse the audited `sa-template` implementation.
2. Prefer `KEEP` before any change.
3. Prefer `KEEP + TEST` or `KEEP-DISABLED` when behavior can remain unchanged.
4. Use a thin `WRAP` only where an explicit boundary is required.
5. Use a bounded `PATCH` before considering structural change.
6. Do not use `REFACTOR` unless `KEEP`, `KEEP + TEST`, `KEEP-DISABLED`, `WRAP`, and `PATCH` are all proven insufficient.
7. Do not use `DELETE` without a complete Deletion Review and explicit user approval.

Allowed reuse actions are exactly:

```text
KEEP
KEEP + TEST
KEEP-DISABLED
WRAP
PATCH
REFACTOR
DELETE
```

The completed Full Repository Audit found no proven `REFACTOR` and no justified `DELETE`. Detailed Spec authoring may not overturn those results by preference.

## Design Boundary

The three STS tasks are design and authority work only. They may create or update registered Starter design artifacts and the Runtime documents required to route, verify, and freeze those artifacts.

They must not:

- modify application implementation;
- modify dependencies or lockfiles;
- modify database schema or migrations;
- modify build or deployment configuration;
- provision database, Cloudflare, Hyperdrive, payment, email, AI, storage, or other provider resources;
- deploy an application or run production/simulated-production validation;
- create implementation Tasks during this design sequence;
- introduce product-specific branding, copy, imagery, pricing, navigation, legal text, or provider claims as Starter Authority.

Repository inspection and repository-local evidence analysis are allowed.

## Frozen Inputs

The design must preserve:

- Full Repository Audit result: `YES — PATCH`;
- A-001: PostgreSQL Provider Policy R1, PostgreSQL + Drizzle + generic `DATABASE_URL`, vendor `UNPINNED`, provider qualification deferred to a real implementation/environment;
- A-002: the frozen UI Foundation keep list from `AUD-FINAL-04` and `AUD-WORK-060`;
- Cloudflare Workers + OpenNext as the primary deployment target;
- `DEVELOPMENT`, `STAGING`, and `PRODUCTION` as the standard environments;
- Google OAuth plus Email Magic Link with trusted same-email canonical identity;
- Stripe and Creem one-time payments with operator-controlled provider selection and no request-level automatic failover;
- cleanly optional AI, i18n, ads, analytics, storage/R2, Turnstile, non-default Auth providers, credits/subscriptions, content, and non-core UI surfaces;
- no product-specific ShipAny content in the reusable Starter contract.

## Required Task Graph

The graph is fixed:

```text
STS-010 Detailed Spec Authoring
  -> STS-020 Completeness / Ambiguity Audit
  -> STS-030 Detailed Spec Freeze
```

`STS-020` cannot execute until `STS-010` is `VERIFIED`. `STS-030` cannot execute until `STS-020` is `VERIFIED`. `STS-010` authors but does not freeze the Detailed Spec.

## Required Design Artifacts

`STS-010` must create:

- `docs/starter/KYD_SAAS_STARTER_DETAILED_SPEC.md`;
- `docs/starter/KYD_SAAS_STARTER_GAP_CLOSURE_MATRIX.md`;
- `docs/starter/KYD_SAAS_STARTER_ACCEPTANCE_MATRIX.md`.

The master specification must cover every audited domain and identify goals, non-goals, boundaries, environments, deployment, database, Auth/account, payments/orders/entitlement, email, optional modules, UI, SEO, security, configuration, testing, logging, migration/rollback, release gates, reuse actions, gap closure, acceptance, open decisions, do-not-do rules, and evidence traceability.

## Capability Contract

Every material capability must define:

```text
Capability ID
Name
Starter role: CORE / OPTIONAL / KEEP-DISABLED
Current sa-template state
Reuse action
Frozen target behavior
Allowed implementation delta
Forbidden implementation delta
Configuration
Security requirements
Failure/retry behavior
Test requirements
Release/verification gate
Audit evidence
Dependencies
```

An implementation-affecting ambiguity must be recorded as an open decision; it must not be silently guessed.

## Gap and Acceptance Discipline

The Gap Closure Matrix must contain exactly the 19 final audit gaps, preserving `GAP-001` through `GAP-019` and the audited counts `P0=8`, `P1=8`, `P2=3`. Every gap appears once and has observable acceptance and verification.

Every Core capability and every implementation-relevant optional capability must map to mechanically observable acceptance. Subjective terms such as “clean”, “good”, “secure”, “fast”, “proper”, or “user friendly” are not sufficient acceptance evidence.

## No New Architecture

The Detailed Spec must derive target behavior from existing repository boundaries. It must not introduce a provider plugin framework, an Auth.js Adapter migration, a payment schema rewrite, PostgreSQL + D1 dual golden paths, mandatory Hyperdrive/R2/Turnstile/i18n, automatic payment failover, a replacement UI framework, or an enterprise observability platform unless later evidence and Authority explicitly require one.

## Validation Timing

Design-stage completion requires repository evidence traceability and internal consistency. Real provider, Cloudflare, OAuth, payment, email, AI, storage, browser, and release validation belongs to implementation/environment verification and must be represented as future acceptance or release gates, not performed during `STS-010`, `STS-020`, or `STS-030`.

## Completion Rules

`STS-010` can be `VERIFIED` only when all three design artifacts are populated, all 19 gaps are represented exactly once, all material capabilities use the required schema and allowed actions, acceptance is observable, A-001 and A-002 are preserved, product-specific leakage is excluded, and no application implementation file changed.

`STS-020` must independently challenge completeness, ambiguity, traceability, frozen-decision coverage, architecture drift, product-specific leakage, and acceptance quality. Implementation-affecting unresolved decisions block freeze.

`STS-030` may freeze the Detailed Spec only after `STS-020` is `VERIFIED` and all blocking ambiguity is resolved by repository Authority or explicit planner/user decision.
