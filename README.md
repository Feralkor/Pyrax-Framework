# Pyrax Operational Intelligence Framework

Reusable framework and product template for building deterministic-first, evidence-driven operational intelligence systems across industries, companies, startups and operational contexts.

## Purpose

Pyrax Framework reduces architecture, governance and engineering that would otherwise be reinvented for every new solution. The framework standardizes the common recipe and leaves domain truth, integrations, rules, deployment and UX for fine-tuning.

`Pyrax Framework + Organization Context + Domain Pack + Integrations + Domain Rules + UX = Operational Product`

Reference patterns were distilled from XPM Inteligência Operacional, Route Engineer and NeuroGear. They are examples, not runtime dependencies.

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
5. Validate it:

```bash
pyrax validate domain-pack.yaml
```

6. Assess maturity:

```bash
pyrax assess domain-pack.yaml
```

7. Scaffold the implementation:

```bash
pyrax scaffold my-solution --domain-pack domain-pack.yaml --destination ../
```

8. Implement the smallest vertical slice from source to evidence-backed decision support.
9. Add Golden Cases, contract/reconciliation tests and integration tests.
10. Re-run `pyrax assess` until readiness matches the intended release mode.

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

- `src/pyrax/` — installable CLI, bootstrap, readiness engine and domain-neutral runtime.
- `docs/` — canonical recipe, discovery/data playbooks, architecture and standards.
- `schemas/` — machine-readable contracts.
- `templates/` — reusable discovery/product/engineering artifacts.
- `domain-packs/` — domain customization template.
- `patterns/` — composable analytical/decision patterns.
- `bootstrap/` — optional technology profiles.
- `examples/` — reference patterns distilled from prior products.
- `tests/` — framework regression and Golden-Case-style tests.
- `.github/workflows/` — framework quality gates.

## CLI

### `pyrax bootstrap`
Creates a discovery workspace before the company/domain is understood.

### `pyrax validate`
Checks structural and cross-reference validity against canonical Domain Pack contracts.

### `pyrax assess`
Evaluates design, semantic, QA, runtime, integration and deployment readiness. A valid Domain Pack is not automatically production-ready.

### `pyrax scaffold`
Generates a domain-aware project skeleton and pre-populates core artifacts from the validated Domain Pack.

## Runtime primitives

The reusable runtime currently provides:
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
- domain-neutral observability.

The runtime defines mechanics, not business semantics.

## Quality

```bash
make quality
```

CI runs on Python 3.11 and 3.12, performs Ruff + pytest, validates canonical fixtures/examples, runs readiness/scaffold/bootstrap smoke tests and builds the Python package.

## Canonical reading

1. `AGENTS.md`
2. `docs/UNIVERSAL-SOLUTION-RECIPE.md`
3. `docs/FRAMEWORK-CHARTER.md`
4. `docs/PRINCIPLES.md`
5. `docs/DISCOVERY-PLAYBOOK.md`
6. `docs/DATA-ACQUISITION-PLAYBOOK.md`
7. `docs/SOLUTION-ARCHETYPES.md`
8. `docs/ARCHITECTURE.md`
9. `docs/DEVELOPMENT-LIFECYCLE.md`
10. `docs/DATA-TRUTH-MODEL.md`
11. `docs/EVIDENCE-STANDARD.md`
12. `docs/CONFIDENCE-MODEL.md`
13. `docs/DECISION-MODEL.md`
14. `docs/READINESS-MODEL.md`
15. `docs/RUNTIME-CONTRACT.md`
16. `docs/QA-STANDARD.md`
17. `docs/CLI-AND-SCAFFOLDING.md`

`docs/MCP-SPECIFICATION.md` is retained as a deferred future interface specification.

## Status

Framework baseline: **v0.3 — Universal Solution Recipe**.
