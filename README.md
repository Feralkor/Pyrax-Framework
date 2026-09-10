# Pyrax Operational Intelligence Framework

Reusable framework and product template for building deterministic-first, evidence-driven operational intelligence systems.

## Purpose

Pyrax Framework exists to reduce the amount of architecture, governance and engineering that must be reinvented for every new operational solution.

The framework standardizes the common core and leaves the domain-specific work for fine-tuning.

`Pyrax Framework + Domain Pack + Integrations + Domain Rules = Operational Product`

Reference products that inspired the framework include XPM Inteligência Operacional, Route Engineer and NeuroGear.

## Core model

Every solution should evolve through four layers:

1. **Truth Engine** — reconstruct what is actually known from source systems.
2. **Anticipation Engine** — detect risk, pressure, deviation and opportunity.
3. **Decision Engine** — produce constrained, explainable decision support.
4. **Operational Memory** — retain observations, decisions and outcomes for continuous improvement.

AI/LLM capability is optional and must sit after deterministic truth, semantics, evidence and guardrails.

## Repository structure

- `docs/` — canonical method, architecture and standards.
- `schemas/` — machine-readable contracts for reusable concepts.
- `templates/` — starting artifacts for a new product or domain.
- `domain-packs/` — reusable domain customization layer.
- `examples/` — reference implementations distilled from prior products.
- `framework/` — reserved implementation surface for reusable runtime components.
- `tools/` — reserved generators, validators and bootstrap tooling.

## Start a new solution

1. Read `AGENTS.md` and `docs/FRAMEWORK-CHARTER.md`.
2. Run the discovery process in `docs/DEVELOPMENT-LIFECYCLE.md`.
3. Copy `domain-packs/_template/domain-pack.yaml` and customize the domain.
4. Instantiate the templates in `templates/`.
5. Define sources, entities, states, signals, decisions, evidence and outcomes.
6. Implement the smallest vertical slice from source to decision-support UI.
7. Validate with Golden Cases before expanding scope.

## Fundamental rule

> Reconstruct reality first. Calculate second. Explain third. Recommend last.

## Status

Framework baseline: **v0.1 — Method and Template Foundation**.
