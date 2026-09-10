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
7. `docs/DECISION-MODEL.md`
8. `docs/CONFIDENCE-MODEL.md`
9. `docs/QA-STANDARD.md`
10. `docs/MCP-SPECIFICATION.md` when altering agent/MCP behavior.

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
- Historical reference implementations are examples, not executable product dependencies.

## New product rule

Do not start from UI. Start from:

`Problem -> Decision -> Source -> Semantics -> Contracts -> State -> Quality -> Evidence -> Signals -> Anticipation -> Decision Support -> Outcome -> UX`

## Reuse rule

Reuse framework patterns and contracts. Do not copy product-specific assumptions across domains without explicit semantic validation.

## Definition of ready

A product is ready to implement only when it has at least:

- problem statement;
- decision owner;
- system(s) of record;
- domain entities;
- operational grain;
- source map;
- known/unknown semantics;
- first decision-support use case;
- evidence requirements;
- guardrails;
- Golden Cases.

## Definition of done

A framework or template change is done when it:

- remains domain-agnostic;
- preserves backward-compatible schemas or versions breaking changes explicitly;
- includes examples where ambiguity is likely;
- is testable or machine-validatable when practical;
- does not weaken provenance, confidence or evidence requirements.

## North Star

> Standardize the engineering decisions so new products spend their time on domain truth and fine-tuning.
