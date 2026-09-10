# Pyrax Operational Intelligence Framework

Reusable framework and product template for building deterministic-first, evidence-driven operational intelligence systems across industries, companies, startups and operational contexts.

## Purpose

Pyrax Framework reduces architecture, governance and engineering that would otherwise be reinvented for every new solution. The framework standardizes the common recipe and leaves organization context, domain truth, integrations, rules, deployment and UX for fine-tuning.

`Pyrax Framework + Organization Context + Domain Pack + Integrations + Domain Rules + UX = Operational Product`

Reference patterns were distilled from XPM Inteligência Operacional, Route Engineer and NeuroGear. They are examples, not runtime dependencies.

## Why Pyrax

Pyrax is not intended to be another generic dashboard platform or an AI wrapper over unverified data. Its differentiation is the path from an unknown organization to an evidence-backed operational decision system.

The framework is designed around these competitive principles:

- **deterministic-first** — use explicit rules and operational constraints before adding statistical/ML complexity when deterministic methods are sufficient;
- **truth before intelligence** — source availability never implies semantic certification;
- **UNKNOWN is first-class** — unknown, unavailable and null are never silently converted to zero or false;
- **Evidence by default** — decision-support outputs preserve provenance, grain, time/cutoff, method/rule and confidence;
- **abstention over fabrication** — insufficient data blocks or downgrades decisions instead of producing false precision;
- **domain fine-tuning** — reusable engineering stays in the framework while business meaning remains in Domain Packs;
- **vendor-neutral** — ERP, WMS, CRM, databases, spreadsheets, APIs, telemetry, cloud or local infrastructure can all participate through explicit contracts/adapters;
- **scenario before action** — candidate actions may be evaluated against projected states without mutating canonical truth;
- **outcome learning** — decisions and outcomes can become governed Operational Memory for continuous improvement.

The long-term compounding advantage is the reusable body of Patterns, Domain Packs, Golden Cases, ontologies, decision graphs and reference implementations accumulated across projects without copying customer-specific semantics into the core.

## Universal recipe

`Organization Context -> Problem Discovery -> Decision Discovery -> Data Discovery -> Semantic Mapping -> Domain Pack -> Validate -> Assess -> Scaffold -> Vertical Slice -> Evidence -> Decision Support -> Outcome -> Iteration`

The framework is intentionally industry-agnostic. It must work whether the organization uses ERP, WMS, CRM, spreadsheets, APIs, telemetry, event streams, local databases, cloud services or a combination of them.

## Core model

Every solution evolves through four layers:

1. **Truth Engine** — reconstruct what is actually known from source systems.
2. **Anticipation Engine** — detect risk, pressure, deviation and opportunity.
3. **Decision Engine** — produce constrained, explainable decision support.
4. **Operational Memory** — retain observations, decisions and outcomes for continuous improvement.

AI/LLM capability is optional and must sit downstream of deterministic truth, semantics, evidence and guardrails.

## v0.4 capability model

The v0.4 line extends the universal recipe with four reusable decision-intelligence primitives:

### Operational Ontology
Represents the operational world as **entities, relationships, events, actions, state and constraints**, instead of treating source-system tables as the business model.

### Decision Graph
Models dependencies from facts/states to signals, decisions, actions and outcomes, making downstream operational impact traceable.

### Scenario Engine
Runs deterministic what-if projections from explicit baselines and assumptions without mutating canonical operational state.

### Pyrax Maturity Model
Provides cumulative levels from discovery to closed-loop intelligence:

`P0 Discovery -> P1 Truth Mapped -> P2 Operational State -> P3 Assisted Intelligence -> P4 Predictive Operations -> P5 Closed-loop Intelligence`

Maturity is separate from production readiness: a bounded P2 or P3 product may be production-ready for its intended scope.

## Fundamental rule

> Reconstruct reality first. Calculate second. Explain third. Recommend last.

## Install

```bash
python -m pip install -e ".[dev]"
```

The package exposes the `pyrax` CLI.

## Start in a new company

When the domain is still unknown, start with discovery instead of fabricating a Domain Pack:

```bash
pyrax bootstrap "Example Company" --destination ../
```

Optionally provide an initial solution-archetype hypothesis:

```bash
pyrax bootstrap "Example Company" --archetype predictive-operations --destination ../
```

The bootstrap workspace contains:
- `organization-profile.yaml`;
- `DISCOVERY-WORKSHEET.md`;
- `DATA-INVENTORY.md`;
- `SOLUTION-ARCHETYPE.md`;
- `domain-pack.draft.yaml`;
- `NEXT-STEPS.md`.

The draft intentionally starts incomplete and with explicit unknowns.

## Move from discovery to product

1. Complete organization and process discovery.
2. Map sources and semantic unknowns.
3. Select one decision-support vertical.
4. Promote the draft to a real `domain-pack.yaml` only when supported by evidence.
5. Validate it with `pyrax validate domain-pack.yaml`.
6. Assess release readiness with `pyrax assess domain-pack.yaml`.
7. Assess intelligence maturity with `pyrax maturity domain-pack.yaml`.
8. Scaffold with `pyrax scaffold my-solution --domain-pack domain-pack.yaml --destination ../`.
9. Implement the smallest vertical slice from source to evidence-backed decision support.
10. Add Golden Cases, contract/reconciliation tests and integration tests.
11. Re-run readiness and maturity as the solution evolves.

## Solution archetypes

The framework includes reusable problem shapes such as:
- exception management;
- predictive operations;
- constraint and coverage;
- asset/condition intelligence;
- customer/account intelligence;
- workflow/process intelligence;
- commercial/revenue intelligence;
- risk/compliance intelligence;
- capacity/resource intelligence;
- strategic intelligence.

Archetypes are starting hypotheses, never certified business semantics.

## Repository structure

- `src/pyrax/` — installable CLI, bootstrap, readiness/maturity engines and domain-neutral runtime;
- `docs/` — canonical recipe, playbooks, architecture and standards;
- `schemas/` — machine-readable contracts;
- `templates/` — reusable discovery/product/engineering artifacts;
- `domain-packs/` — domain customization template;
- `patterns/` — composable analytical/decision patterns;
- `bootstrap/` — optional technology profiles;
- `examples/` — reference patterns distilled from prior products;
- `golden-cases/` — deterministic framework reference scenarios;
- `tests/` — framework regression tests;
- `.github/workflows/` — framework quality gates.

## CLI

### `pyrax bootstrap`
Creates a discovery workspace before the company/domain is understood.

### `pyrax validate`
Checks structural and cross-reference validity against canonical Domain Pack contracts.

### `pyrax assess`
Evaluates design, semantic, QA, runtime, integration and deployment readiness.

### `pyrax maturity`
Reports the cumulative Pyrax maturity level P0-P5 without treating maturity as release certification.

### `pyrax scaffold`
Generates a domain-aware project skeleton and pre-populates core artifacts from the validated Domain Pack.

## Runtime and modeling primitives

The reusable framework currently provides:
- Source/Snapshot ports;
- Truth Engine;
- Operational State;
- Quality Gate;
- Reconciliation Gate;
- Evidence;
- granular Confidence;
- Signal Engine;
- deterministic anticipation helpers;
- Decision Engine with abstention on insufficient data/evidence;
- Operational Memory;
- domain-neutral observability;
- Operational Ontology;
- Decision Graph;
- Scenario Engine;
- Pyrax Maturity Model.

The framework defines mechanics, not customer-specific business semantics.

## Quality

```bash
make quality
```

CI runs on Python 3.11 and 3.12, performs Ruff + pytest, validates canonical fixtures/examples, runs readiness/maturity/scaffold/bootstrap smoke tests and builds the Python package.

## Canonical reading

1. `AGENTS.md`
2. `docs/UNIVERSAL-SOLUTION-RECIPE.md`
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
13. `docs/DEVELOPMENT-LIFECYCLE.md`
14. `docs/DATA-TRUTH-MODEL.md`
15. `docs/EVIDENCE-STANDARD.md`
16. `docs/CONFIDENCE-MODEL.md`
17. `docs/DECISION-MODEL.md`
18. `docs/READINESS-MODEL.md`
19. `docs/RUNTIME-CONTRACT.md`
20. `docs/QA-STANDARD.md`
21. `docs/CLI-AND-SCAFFOLDING.md`

`docs/MCP-SPECIFICATION.md` is retained as a deferred future interface specification.

## Status

Framework line: **v0.4 — Ontology, Decision Graph, Scenario & Maturity**.

The v0.4 line is under active validation. Do not call it stable until CI and the release gates for this version are green.
