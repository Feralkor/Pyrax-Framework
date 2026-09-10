# AGENTS.md — Pyrax Framework

This file governs coding and design agents operating in this repository.

## Mission

Maintain Pyrax Framework as a reusable, deterministic-first, evidence-driven foundation for operational intelligence products.

## Mandatory reading order

1. `docs/FRAMEWORK-CHARTER.md`
2. `docs/PRINCIPLES.md`
3. `docs/ARCHITECTURE.md`
4. `docs/DEVELOPMENT-LIFECYCLE.md`
5. `docs/DATA-TRUTH-MODEL.md`
6. `docs/EVIDENCE-STANDARD.md`
7. `docs/CONFIDENCE-MODEL.md`
8. `docs/DECISION-MODEL.md`
9. `docs/READINESS-MODEL.md`
10. `docs/RUNTIME-CONTRACT.md`
11. `docs/QA-STANDARD.md`
12. `docs/CLI-AND-SCAFFOLDING.md`
13. `docs/MCP-SPECIFICATION.md` only when working on the future MCP interface.

## Framework invariants

- A source system is not trusted merely because it exists.
- Field existence does not imply semantic certification.
- Unknown, unavailable and null must never be silently converted to zero.
- Rules, calculations and recommendations require explicit grain, population and provenance.
- Deterministic logic is preferred before statistical or ML approaches when sufficient.
- AI/LLM output must not overwrite canonical facts.
- Evidence must accompany decision-support outputs.
- Critical operational actions remain human-approved unless a product explicitly defines a separately certified automation policy.
- Domain-specific logic belongs in a Domain Pack or product implementation, not in the generic framework core.
- Historical/reference products are examples, not executable dependencies.
- A structurally valid Domain Pack is not automatically production-ready.
- The generic runtime may implement mechanics; it must not encode warehouse, fleet, manufacturing, strategy or other domain semantics.

## Canonical workflow for a new product

`Discovery -> Domain Pack -> validate -> assess -> scaffold -> vertical slice -> Golden Cases -> contract/reconciliation tests -> integration -> deployment -> reassess`

Do not start from UI. The reasoning order is:

`Problem -> Decision -> Source -> Semantics -> Contracts -> State -> Quality -> Reconciliation -> Evidence -> Signals -> Anticipation -> Decision Support -> Outcome -> UX`

## CLI contract

- `pyrax validate` checks schema/structural validity.
- `pyrax assess` reports design, semantic, QA and implementation maturity.
- `pyrax scaffold` generates a starting project; generated files are not certified facts.
- Never weaken validation/readiness just to make a project pass.

## Runtime contract

Reusable runtime components must preserve:

- explicit unknowns;
- deterministic behavior;
- immutable/evidence-carrying facts where practical;
- granular confidence;
- abstention when required facts are insufficient;
- human approval as the default decision policy;
- provider/domain isolation.

## Pattern rule

Patterns in `patterns/` are composable mechanics. Before production use, a product must define the pattern's domain inputs, semantic assumptions, evidence requirements, UNKNOWN behavior and prohibited interpretations.

## Schema rule

Changes to machine-readable contracts must be backward-compatible or explicitly versioned as breaking changes. The packaged canonical schema under `src/pyrax/resources/` must stay synchronized with the root schema used by repository tooling/tests.

## Definition of ready to implement

A product should have at least:

- problem and decision owner;
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

- remains domain-agnostic;
- preserves or versions contracts explicitly;
- includes examples where ambiguity is likely;
- is testable/machine-validatable when practical;
- does not weaken provenance, confidence, evidence or abstention requirements;
- keeps CLI, schemas, templates and documentation coherent;
- passes framework CI.

## MCP boundary

The MCP implementation is intentionally deferred. Do not build an MCP server as part of ordinary framework/runtime work. `docs/MCP-SPECIFICATION.md` is a future integration contract only.

## North Star

> Standardize the engineering decisions so new products spend their time on domain truth and fine-tuning.
