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
8. `docs/DEVELOPMENT-LIFECYCLE.md`
9. `docs/DATA-TRUTH-MODEL.md`
10. `docs/EVIDENCE-STANDARD.md`
11. `docs/CONFIDENCE-MODEL.md`
12. `docs/DECISION-MODEL.md`
13. `docs/READINESS-MODEL.md`
14. `docs/RUNTIME-CONTRACT.md`
15. `docs/QA-STANDARD.md`
16. `docs/CLI-AND-SCAFFOLDING.md`
17. `docs/MCP-SPECIFICATION.md` only when working on the future MCP interface.

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
- The generic runtime may implement mechanics; it must not encode warehouse, fleet, manufacturing, strategy or other domain semantics.
- Organization type, industry and technology stack must never be hard-coded as framework assumptions.

## Canonical workflow for a new organization

`bootstrap -> organization discovery -> decision discovery -> data discovery -> Domain Pack -> validate -> assess -> scaffold -> vertical slice -> Golden Cases -> contract/reconciliation tests -> integration -> deployment -> reassess`

When entering a new company or domain, start with:

```bash
pyrax bootstrap "Organization Name"
```

Do not create a supposedly complete Domain Pack before discovering the organization, decisions and sources.

## Reasoning order

Do not start from UI or technology selection. Use:

`Organization -> Problem -> Decision -> Source -> Semantics -> Contracts -> State -> Quality -> Reconciliation -> Evidence -> Signals -> Anticipation -> Decision Support -> Outcome -> UX`

## Reuse boundary

Reuse:
- process;
- architecture boundaries;
- schemas;
- runtime mechanics;
- patterns;
- QA methods;
- templates;
- tooling.

Fine-tune and revalidate:
- business semantics;
- source meaning;
- entity relationships;
- KPIs;
- thresholds;
- rules;
- decisions;
- workflows;
- UX vocabulary;
- deployment constraints.

Never transplant another company's semantics merely because the data structure looks similar.

## CLI contract

- `pyrax bootstrap` creates an intentionally incomplete discovery workspace.
- `pyrax validate` checks schema, structural integrity and cross-references.
- `pyrax assess` reports design, semantic, QA and implementation maturity.
- `pyrax scaffold` generates a starting project; generated files are not certified facts.
- Never weaken validation/readiness just to make a project pass.

## Runtime contract

Reusable runtime components must preserve:
- explicit unknowns;
- deterministic behavior;
- immutable/evidence-carrying facts where practical;
- granular confidence;
- abstention when required facts/evidence are insufficient;
- human approval as the default decision policy;
- provider/domain isolation.

## Pattern rule

Patterns in `patterns/` are composable mechanics. Before production use, a product must define each pattern's domain inputs, semantic assumptions, evidence requirements, UNKNOWN behavior and prohibited interpretations.

## Schema rule

Changes to machine-readable contracts must be backward-compatible or explicitly versioned as breaking changes. The packaged canonical schema under `src/pyrax/resources/` must stay synchronized with the root schema used by repository tooling/tests.

## Definition of ready to implement

A product should have at least:
- organization/problem context;
- decision owner;
- system(s) of record;
- domain entities and operational grain;
- source map;
- known/candidate/unknown semantics;
- first signal and decision-support use case;
- evidence requirements;
- guardrails;
- initial Golden Cases.

This is implementation readiness, not production certification.

## Definition of production-ready

Follow `docs/READINESS-MODEL.md`. Full production readiness requires all assessed gates to be `PASS`; do not reinterpret `PARTIAL`, `BLOCKED` or `NOT_STARTED` as success.

## Definition of done for framework changes

A framework or template change is done when it:
- remains domain- and industry-agnostic;
- preserves or versions contracts explicitly;
- includes examples where ambiguity is likely;
- is testable/machine-validatable when practical;
- does not weaken provenance, confidence, evidence or abstention requirements;
- keeps CLI, schemas, templates and documentation coherent;
- passes framework CI.

## MCP boundary

The MCP implementation is intentionally deferred. Do not build an MCP server as part of ordinary framework/runtime work. `docs/MCP-SPECIFICATION.md` is a future integration contract only.

## North Star

> Standardize the recipe so a new company starts from proven engineering structure and spends its time on domain truth, data discovery and fine-tuning.
