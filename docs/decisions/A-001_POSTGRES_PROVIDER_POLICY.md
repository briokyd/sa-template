# A-001 — PostgreSQL Provider Policy R1

Status: FROZEN

## Decision

Kyd SaaS Starter V1 freezes the database application contract, not a permanent vendor.

Database:

PostgreSQL

ORM:

Drizzle

Application-facing connection contract:

generic DATABASE_URL

Provider-specific coupling in reusable business/domain code:

FORBIDDEN by default

Default provider vendor:

UNPINNED at Starter design phase

Provider validation:

DEFERRED UNTIL REAL IMPLEMENTATION / ENVIRONMENT VALIDATION

## Purpose

Kyd SaaS Starter is extracted from sa-template.

The goal is to reuse and harden the existing PostgreSQL + Drizzle capability with
minimal delta.

The Starter is not rewritten merely to select a database vendor.

The design phase does not require provisioning Neon, PlanetScale, Supabase,
Cloudflare Hyperdrive, or other production/simulated-production infrastructure.

## Repository Evidence

The completed Repository Audit established:

- PostgreSQL + Drizzle already exist;
- DATABASE_URL is generic;
- no PostgreSQL provider SDK coupling was found;
- database access is centralized;
- a Cloudflare-specific connection branch exists;
- real provider/runtime behavior remains an implementation/environment validation concern.

## Stable Provider Contract

A provider used by a real project must preserve:

- standard PostgreSQL behavior;
- Drizzle compatibility;
- existing migration compatibility;
- generic application boundary;
- no required provider SDK in business/domain logic;
- environment isolation capability;
- real target-runtime compatibility.

## Provider Qualification Gate

When a real implementation/environment needs a provider, validate:

PQ-01 Standard PostgreSQL connectivity
PQ-02 Drizzle compatibility
PQ-03 Existing migration path
PQ-04 CRUD
PQ-05 transaction support
PQ-06 required concurrency behavior
PQ-07 target Cloudflare runtime when applicable
PQ-08 Hyperdrive only when actually selected
PQ-09 no permanent provider-specific business-code coupling
PQ-10 DEVELOPMENT / STAGING / PRODUCTION isolation capability
PQ-11 secret/config handling
PQ-12 observable failure behavior
PQ-13 Auth/payment DB smoke when those features are enabled

Allowed result:

PASS
FAIL
BLOCKED
NOT_APPLICABLE

## Validation Timing

Provider Qualification does not block:

- Starter Detailed Spec;
- Delivery Protocol Detailed Spec;
- Design Completeness / Ambiguity Audit;
- Design Freeze.

It becomes mandatory when a real provider/environment is provisioned and before
that environment is relied on for release.

## No Mandatory Vendor Bake-Off

Starter V1 does not require a Neon-vs-PlanetScale-vs-Supabase comparison before
design can proceed.

A comparison may be performed later only for a concrete project/operational need.

## Hyperdrive

Hyperdrive is an optional environment/runtime integration.

It is not part of the stable database application contract.

## Reuse Direction

KEEP:
- PostgreSQL
- Drizzle
- generic DATABASE_URL
- centralized DB access
- existing schema/migrations
- reusable model modules
- existing Cloudflare-aware connection branch when valid

KEEP + TEST:
- migrations
- provider connectivity
- transactions
- representative CRUD
- actual target runtime

PATCH only when evidenced:
- multi-write atomicity
- environment/config normalization
- Cloudflare runtime adapter/config
- qualification smoke coverage

Do not REFACTOR unless smaller actions are proven insufficient.

## Do Not Do

Do not:

- rewrite the DB layer to select a vendor;
- add Neon-specific business logic;
- add PlanetScale-specific business logic;
- add Supabase-specific business logic;
- create a provider plugin framework without evidence;
- introduce PostgreSQL + D1 dual golden paths;
- require production/simulated-production provisioning during Starter design;
- make Hyperdrive mandatory;
- block Starter Detailed Spec on a vendor bake-off.

## Final State

A-001:

FROZEN — PostgreSQL Provider Policy R1

Vendor:

UNPINNED

Starter Detailed Spec:

NOT BLOCKED
