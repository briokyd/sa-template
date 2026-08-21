# Kyd Project System - Capability-First Multi-Template Reuse Policy R1

Authority ID: `KPS-CAP-REUSE-R1`  
Version: `R1`  
Status: `FROZEN`

## Decision

Kyd Starter work is capability-first and extraction-first. The audit objective is reuse discovery, gap discovery, and bounded hardening. It is not repository redesign.

The unit of reuse is a capability, not an entire template, repository layout, provider, or model-preferred architecture.

An existing implementation must be mapped before its capability is redesigned. The required decision order is:

```text
KEEP
KEEP + TEST
KEEP-DISABLED
WRAP
PATCH
REFACTOR
DELETE
```

`KEEP` is the default. `REFACTOR` requires proof that all smaller actions are insufficient. `DELETE` requires Deletion Review and explicit user approval.

## Current Source Baseline

`sa-template` is the current primary implementation baseline for Kyd SaaS Starter. Current work must identify:

- what can be reused directly;
- what only needs verification or tests;
- what is absent;
- what requires a bounded patch;
- what is product-specific and must not become Starter Authority.

A design ambiguity is not evidence that the implementation is absent. Source code, configuration, schema, routes, helpers, tests, and existing audit evidence must be inspected before proposing new behavior or structure.

## Future Template Sources

Future paid or otherwise authorized templates may become additional capability sources. Each new source is evaluated capability by capability against frozen Starter requirements and the implementations already retained.

Adding a template does not trigger a repository rewrite, directory unification, provider migration, framework replacement, or automatic adoption of the template's product semantics. A stronger implementation may be selected or adapted only when evidence shows a concrete capability advantage and the minimum-delta rule is preserved.

## Provenance

Every retained or changed capability must record:

- source template or repository;
- exact implementation paths and relevant symbols;
- current behavior and defaults;
- current evidence/tests;
- frozen target behavior;
- actual delta;
- minimum justified reuse action.

Capability provenance must remain explicit when implementations from additional templates are evaluated later.

## Boundaries

This policy does not authorize application implementation, dependency changes, deployment changes, provider provisioning, production or simulated-production validation, or a multi-template plugin framework.

Do not:

- redesign a capability before mapping its existing implementation;
- treat specification ambiguity as proof that source capability is missing;
- rewrite `sa-template` to accommodate a future template;
- copy product-specific brand, copy, pricing, workflow, prompts, legal text, or visual identity into reusable Starter Authority;
- select `REFACTOR` for naming, directory aesthetics, modernization, or architectural preference;
- delete a reusable non-default capability merely because it is not Core.

## Application to STS-021A

`STS-021A` re-evaluates `F-001` through `F-009` against actual `sa-template` implementation. It may revise earlier resolution classes when repository evidence proves that a purported design decision is already determined by existing behavior or frozen Authority.

It does not correct the candidate Detailed Spec, make user decisions, modify application code, or activate `STS-030`.
