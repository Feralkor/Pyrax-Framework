# Pyrax Operational Intelligence Framework

Reusable framework and product template for building deterministic-first, evidence-driven operational intelligence systems.

## Purpose

Pyrax Framework reduces architecture, governance and engineering that would otherwise be reinvented for every operational solution. The framework standardizes the common core and leaves domain truth, integrations, rules and UX for fine-tuning.

`Pyrax Framework + Domain Pack + Integrations + Domain Rules + UX = Operational Product`

Reference patterns were distilled from XPM Inteligência Operacional, Route Engineer and NeuroGear. They are examples, not runtime dependencies.

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

## Start a new solution

1. Fill `templates/DISCOVERY-WORKSHEET.template.md`.
2. Copy `domain-packs/_template/domain-pack.yaml` and customize the domain.
3. Validate it:

```bash
pyrax validate domain-pack.yaml
```

4. Assess maturity:

```bash
pyrax assess domain-pack.yaml
```

5. Scaffold the solution:

```bash
pyrax scaffold my-solution --domain-pack domain-pack.yaml --destination ../
```

6. Implement the smallest vertical slice from source to evidence-backed decision support.
7. Add Golden Cases, contract/reconciliation tests and integration tests.
8. Re-run `pyrax assess` until readiness matches the intended release mode.

## Repository structure

- `src/pyrax/` — installable CLI, readiness engine and domain-neutral runtime.
- `docs/` — canonical method, architecture and standards.
- `schemas/` — machine-readable contracts.
- `templates/` — reusable discovery/product artifacts.
- `domain-packs/` — domain customization template.
- `patterns/` — composable analytical/decision patterns.
- `bootstrap/` — optional technology profiles.
- `examples/` — reference patterns distilled from prior products.
- `tests/` — framework regression and Golden-Case-style tests.
- `.github/workflows/` — framework quality gates.

## CLI

### `pyrax validate`
Checks structural validity against the canonical Domain Pack schema.

### `pyrax assess`
Evaluates design, semantic, QA, runtime, integration and deployment readiness. A valid Domain Pack is not automatically production-ready.

### `pyrax scaffold`
Generates a domain-aware project skeleton and pre-populates core artifacts from the Domain Pack.

## Runtime primitives

The reusable runtime currently provides:

- Truth Engine;
- Operational State;
- Quality Gate;
- Reconciliation Gate;
- Evidence;
- granular Confidence;
- Signal Engine;
- deterministic anticipation helpers: aging, coverage, deficit and dead reckoning;
- Decision Engine with abstention on insufficient data;
- Operational Memory.

The runtime defines mechanics, not business semantics. Domain-specific meaning remains in each product/Domain Pack.

## Quality

```bash
make quality
```

CI runs on Python 3.11 and 3.12, performs Ruff + pytest, validates and assesses the canonical fixture, runs a scaffold smoke test and builds the Python package.

## Canonical reading

1. `AGENTS.md`
2. `docs/FRAMEWORK-CHARTER.md`
3. `docs/PRINCIPLES.md`
4. `docs/ARCHITECTURE.md`
5. `docs/DEVELOPMENT-LIFECYCLE.md`
6. `docs/DATA-TRUTH-MODEL.md`
7. `docs/EVIDENCE-STANDARD.md`
8. `docs/CONFIDENCE-MODEL.md`
9. `docs/DECISION-MODEL.md`
10. `docs/READINESS-MODEL.md`
11. `docs/RUNTIME-CONTRACT.md`
12. `docs/QA-STANDARD.md`
13. `docs/CLI-AND-SCAFFOLDING.md`

`docs/MCP-SPECIFICATION.md` is retained as a future interface specification. The MCP implementation is intentionally deferred.

## Status

Framework baseline: **v0.2 — Executable Foundation**.
