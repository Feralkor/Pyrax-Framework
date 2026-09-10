# AGENTS.md — Pyrax Framework

This file governs coding and design agents operating in this repository.

## Mission

Maintain Pyrax Framework as a reusable, deterministic-first, evidence-driven foundation and product-composition system for operational intelligence products across industries and organization types.

## Mandatory reading order

1. `docs/UNIVERSAL-SOLUTION-RECIPE.md`
2. `docs/PRODUCTIZATION-AND-COMPOSITION.md`
3. `docs/FRAMEWORK-CHARTER.md`
4. `docs/PRINCIPLES.md`
5. `docs/DISCOVERY-PLAYBOOK.md`
6. `docs/DATA-ACQUISITION-PLAYBOOK.md`
7. `docs/SOLUTION-ARCHETYPES.md`
8. `docs/ARCHITECTURE.md`
9. `docs/OPERATIONAL-ONTOLOGY.md`
10. `docs/DECISION-GRAPH.md`
11. `docs/SCENARIO-ENGINE.md`
12. `docs/MATURITY-MODEL.md`
13. `docs/UI-COMPOSITION-CONTRACT.md`
14. `docs/INTEGRATION-ADAPTER-CATALOG.md`
15. `docs/DEVELOPMENT-LIFECYCLE.md`
16. `docs/DATA-TRUTH-MODEL.md`
17. `docs/EVIDENCE-STANDARD.md`
18. `docs/CONFIDENCE-MODEL.md`
19. `docs/DECISION-MODEL.md`
20. `docs/READINESS-MODEL.md`
21. `docs/RUNTIME-CONTRACT.md`
22. `docs/QA-STANDARD.md`
23. `docs/CLI-AND-SCAFFOLDING.md`
24. `docs/MCP-SPECIFICATION.md` only when working on the future MCP interface.

## Framework invariants

- A source system is not trusted merely because it exists.
- Field existence does not imply semantic certification.
- Unknown, unavailable and null must never be silently converted to zero.
- Rules, calculations and recommendations require explicit grain, population and provenance.
- Deterministic logic is preferred before statistical or ML approaches when sufficient.
- AI/LLM output must not overwrite canonical facts.
- Evidence must accompany decision-support outputs.
- Critical actions remain human-approved unless a product explicitly defines a separately certified automation policy.
- Domain-specific logic belongs in a Domain Pack or product implementation, not in the generic framework core.
- Historical/reference products are examples, not executable dependencies.
- A structurally valid Domain Pack or Solution Manifest is not automatically production-ready.
- Organization type, industry and technology stack must never be hard-coded as framework assumptions.
- Ontology objects must not be inferred merely from source tables.
- Decision Graph edges must reference known nodes and remain acyclic inside one evaluation run.
- Scenario projections must never mutate canonical state or be labeled as observed truth.
- Maturity levels are cumulative and separate from production readiness.

## Canonical workflow for a new organization

`bootstrap -> discovery -> Domain Pack -> validate -> profile/manifest -> compose -> assess -> maturity -> scaffold -> vertical slice -> Golden Cases -> reconciliation/integration -> deployment -> reassess`

Do not create a supposedly complete Domain Pack before discovering the organization, decisions and sources.

## V0.5 composition boundary

### Solution Profiles
Profiles are reusable starting hypotheses. They may select common blocks, adapter classes, UI components and a maturity target. They must never contain customer-specific business truth, credentials or certified semantics.

### Building Blocks
Building blocks represent reusable mechanics. Every production use must bind the block to domain-specific inputs, Evidence, UNKNOWN behavior and prohibited interpretations.

### Solution Manifest
The Solution Manifest describes how a product is assembled. It does not replace the Domain Pack.

- Domain Pack = business/domain meaning and truth contracts.
- Solution Manifest = reusable Pyrax pieces selected for this product.

### Domain Pack composition
`pyrax compose` exists to reduce duplication. Composition must never be treated as semantic certification. Every inherited or overlaid business meaning remains subject to local validation.

### UI components
Reusable UI contracts consume validated runtime/domain outputs. They never own formulas, semantics or truth. Scenario UI must remain visually distinct from observed state.

### Adapters
Adapters isolate source systems and preserve identity, grain, freshness, quality, lineage and classified errors. They do not infer business meaning from names or payload shape.

## Reuse boundary

Safe to reuse across products:
- process and lifecycle;
- architecture boundaries;
- schemas and templates;
- runtime mechanics;
- generic building blocks;
- Solution Profiles;
- adapter classes;
- UI composition contracts;
- QA methods and Golden Case structure;
- tooling.

Must be fine-tuned and revalidated per organization:
- source semantics;
- ontology identity/relationships;
- KPIs and units;
- thresholds and rules;
- population/grain;
- decisions and workflows;
- regulatory constraints;
- UI vocabulary;
- deployment/security constraints.

Never transplant another company's semantics merely because the data structure looks similar.

## CLI contract

- `pyrax bootstrap` creates an intentionally incomplete discovery workspace.
- `pyrax validate` checks Domain Pack structure and cross-references.
- `pyrax assess` reports production-readiness gates.
- `pyrax maturity` reports cumulative intelligence maturity P0-P5.
- `pyrax profiles` lists/inspects reusable Solution Profiles.
- `pyrax catalog` exposes building-block, adapter and UI catalogs.
- `pyrax manifest` validates/materializes a Solution Manifest.
- `pyrax compose` combines a base Domain Pack with explicit overlays.
- `pyrax scaffold` generates a starting project from Domain Pack/profile/manifest; generated files are not certified facts.
- Never weaken validation/readiness/maturity or composition checks merely to make a project pass.

## Runtime contract

Reusable runtime components must preserve explicit unknowns, deterministic behavior, Evidence, granular confidence, abstention when required facts/evidence are insufficient, human approval defaults, scenario isolation and provider/domain isolation.

## Pattern rule

Patterns in `patterns/` and blocks in V0.5 catalogs are composable mechanics. Before production use, a product must define domain inputs, semantic assumptions, Evidence requirements, UNKNOWN behavior and prohibited interpretations.

## Definition of production-ready

Follow `docs/READINESS-MODEL.md`. Full production readiness requires all assessed gates to be `PASS`; do not reinterpret `PARTIAL`, `BLOCKED` or `NOT_STARTED` as success.

## Definition of done for framework changes

A framework/template/composition change is done when it remains domain- and industry-agnostic, preserves/version contracts explicitly, includes tests/examples where ambiguity is likely, does not weaken provenance/confidence/evidence/abstention, keeps CLI/schemas/templates/catalogs/docs coherent and passes framework CI.

## MCP boundary

The MCP implementation is intentionally deferred. `docs/MCP-SPECIFICATION.md` is a future integration contract only.

## North Star

> Turn proven operational-intelligence engineering into reusable product composition, so each new company spends effort on domain truth and fine-tuning instead of rebuilding the foundation.
