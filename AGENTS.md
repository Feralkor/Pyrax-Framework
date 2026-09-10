# AGENTS.md — Pyrax Framework

This file governs coding and design agents operating in this repository.

## Mission

Maintain Pyrax Framework as a reusable, deterministic-first, evidence-driven foundation for operational intelligence products across industries and organization types.

## Mandatory reading order

1. `docs/UNIVERSAL-SOLUTION-RECIPE.md`
2. `docs/FRAMEWORK-CHARTER.md`
3. `docs/PRINCIPLES.md`
4. `docs/DISCOVERY-PLAYBOOK.md`
5. `docs/DATA-ACQUISITION-PLAYBOOK.md`
6. `docs/SOLUTION-ARCHETYPES.md`
7. `docs/ARCHITECTURE.md`
8. `docs/OPERATIONAL-ONTOLOGY.md`
9. `docs/DECISION-GRAPH.md`
10. `docs/SCENARIO-ENGINE.md`
11. `docs/MATURITY-MODEL.md`
12. `docs/DEVELOPMENT-LIFECYCLE.md`
13. `docs/DATA-TRUTH-MODEL.md`
14. `docs/EVIDENCE-STANDARD.md`
15. `docs/CONFIDENCE-MODEL.md`
16. `docs/DECISION-MODEL.md`
17. `docs/READINESS-MODEL.md`
18. `docs/RUNTIME-CONTRACT.md`
19. `docs/QA-STANDARD.md`
20. `docs/CLI-AND-SCAFFOLDING.md`
21. `docs/MCP-SPECIFICATION.md` only when working on the future MCP interface.

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
- A structurally valid Domain Pack is not automatically production-ready.
- Organization type, industry and technology stack must never be hard-coded as framework assumptions.
- Ontology objects must not be inferred merely from source tables.
- Decision Graph edges must reference known nodes and remain acyclic inside one evaluation run.
- Scenario projections must never mutate canonical state or be labeled as observed truth.
- Maturity levels are cumulative and separate from production readiness.

## Canonical workflow for a new organization

`bootstrap -> organization discovery -> decision discovery -> data discovery -> Domain Pack -> validate -> assess -> maturity -> scaffold -> vertical slice -> Golden Cases -> contract/reconciliation tests -> integration -> deployment -> reassess`

When entering a new company or domain, start with:

```bash
pyrax bootstrap "Organization Name"
```

Do not create a supposedly complete Domain Pack before discovering the organization, decisions and sources.

## Reasoning order

Do not start from UI or technology selection. Use:

`Organization -> Problem -> Decision -> Source -> Semantics -> Contracts -> Ontology -> State -> Quality -> Reconciliation -> Evidence -> Signals -> Decision Graph -> Anticipation -> Scenario -> Decision Support -> Outcome -> UX`

## Reuse boundary

Reuse process, architecture boundaries, schemas, runtime mechanics, patterns, QA methods, templates and tooling. Fine-tune and revalidate business semantics, source meaning, ontology relationships, KPIs, thresholds, rules, decisions, workflows, UX vocabulary and deployment constraints.

Never transplant another company's semantics merely because the data structure looks similar.

## CLI contract

- `pyrax bootstrap` creates an intentionally incomplete discovery workspace.
- `pyrax validate` checks schema, structural integrity and cross-references.
- `pyrax assess` reports production-readiness gates.
- `pyrax maturity` reports cumulative intelligence maturity P0-P5.
- `pyrax scaffold` generates a starting project; generated files are not certified facts.
- Never weaken validation/readiness/maturity criteria merely to make a project pass.

## V0.4 contracts

### Operational Ontology
Generic mechanics may represent Entity, Relationship, Event and Action. Business identity and meaning remain domain-owned.

### Decision Graph
Use the graph for dependency/impact tracing. It does not prove causality by itself. Feedback across time belongs in Operational Memory, not in an evaluation-cycle loop.

### Scenario Engine
Every projection must preserve baseline and assumptions. A projected state is hypothetical until observed/reconciled later.

### Maturity Model
P0-P5 is descriptive guidance. Higher maturity is not automatically more valuable or safer. Production readiness remains governed independently by `docs/READINESS-MODEL.md`.

## Runtime contract

Reusable runtime components must preserve explicit unknowns, deterministic behavior, Evidence, granular confidence, abstention when required facts/evidence are insufficient, human approval defaults and provider/domain isolation.

## Pattern rule

Patterns in `patterns/` are composable mechanics. Before production use, a product must define each pattern's domain inputs, semantic assumptions, evidence requirements, UNKNOWN behavior and prohibited interpretations.

## Schema rule

Changes to machine-readable contracts must be backward-compatible or explicitly versioned as breaking changes. The packaged canonical schema under `src/pyrax/resources/` must stay synchronized with the root schema used by repository tooling/tests.

## Definition of production-ready

Follow `docs/READINESS-MODEL.md`. Full production readiness requires all assessed gates to be `PASS`; do not reinterpret `PARTIAL`, `BLOCKED` or `NOT_STARTED` as success.

## Definition of done for framework changes

A framework or template change is done when it remains domain- and industry-agnostic, preserves/version contracts explicitly, includes examples where ambiguity is likely, is testable when practical, does not weaken provenance/confidence/evidence/abstention, keeps CLI/schemas/templates/docs coherent and passes framework CI.

## MCP boundary

The MCP implementation is intentionally deferred. `docs/MCP-SPECIFICATION.md` is a future integration contract only.

## North Star

> Standardize the recipe so a new company starts from proven engineering structure and spends its time on domain truth, data discovery and fine-tuning.
