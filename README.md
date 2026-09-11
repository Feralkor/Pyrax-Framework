# Pyrax Operational Intelligence Framework

Reusable framework and product-composition system for building deterministic-first, evidence-driven operational intelligence solutions across industries, companies, startups and operational contexts.

## Purpose

Pyrax reduces architecture, governance and engineering that would otherwise be reinvented for every new solution. It standardizes the common recipe and reusable product mechanics while leaving organization context, domain truth, integrations, rules, deployment and UX for fine-tuning.

`Pyrax Framework + Organization Context + Domain Pack + Solution Profile + Building Blocks + Adapters + UI Composition = Operational Product`

Reference patterns were distilled from Inteligência Operacional, Route Engineer, NeuroGear and related portfolio products. They are examples, not runtime dependencies.

## Why Pyrax

Pyrax is not intended to be another generic dashboard platform or an AI wrapper over unverified data. Its differentiation is the path from an unknown organization to an evidence-backed operational decision system.

Competitive principles:

- **deterministic-first** — explicit rules and operational constraints before statistical/ML complexity when deterministic methods are sufficient;
- **truth before intelligence** — source availability never implies semantic certification;
- **UNKNOWN is first-class** — unknown, unavailable and null are never silently converted to zero or false;
- **Evidence by default** — decision-support outputs preserve provenance, grain, time/cutoff, method/rule and confidence;
- **abstention over fabrication** — insufficient data blocks or downgrades decisions instead of producing false precision;
- **domain fine-tuning** — reusable engineering stays in the framework while business meaning remains in Domain Packs;
- **vendor-neutral** — ERP, WMS, CRM, databases, spreadsheets, APIs, telemetry, cloud or local infrastructure can all participate through explicit adapters;
- **scenario before action** — candidate actions may be evaluated against projected states without mutating canonical truth;
- **outcome learning** — decisions and outcomes can become governed Operational Memory for continuous improvement;
- **product composition** — recurring solution shapes can reuse profiles, building blocks, adapters and UI contracts without copying customer semantics.

The compounding advantage is the reusable body of Patterns, Solution Profiles, Domain Packs, Golden Cases, ontologies, decision graphs, adapters and reference compositions accumulated across projects.

## Universal recipe

`Organization Context -> Problem Discovery -> Decision Discovery -> Data Discovery -> Semantic Mapping -> Domain Pack -> Validate -> Assess -> Compose -> Scaffold -> Vertical Slice -> Evidence -> Decision Support -> Outcome -> Iteration`

The framework is intentionally industry-agnostic.

## Core model

Every solution evolves through four layers:

1. **Truth Engine** — reconstruct what is actually known from source systems.
2. **Anticipation Engine** — detect risk, pressure, deviation and opportunity.
3. **Decision Engine** — produce constrained, explainable decision support.
4. **Operational Memory** — retain observations, decisions and outcomes for continuous improvement.

AI/LLM capability is optional and must sit downstream of deterministic truth, semantics, evidence and guardrails.

## V0.4 intelligence primitives

V0.4 introduced:

- **Operational Ontology** — entities, relationships, events, actions, state and constraints;
- **Decision Graph** — traceable dependencies from facts/states to signals, decisions, actions and outcomes;
- **Scenario Engine** — deterministic what-if projections isolated from canonical operational state;
- **Pyrax Maturity Model** — `P0 Discovery -> P1 Truth Mapped -> P2 Operational State -> P3 Assisted Intelligence -> P4 Predictive Operations -> P5 Closed-loop Intelligence`.

Maturity is separate from production readiness.

## V0.5 productization & composition

V0.5 turns Pyrax from a reusable engineering method into a reusable product-composition system.

### Solution Profiles
Reusable starting configurations for recurring product shapes:

- `fleet-intelligence`
- `asset-radar`
- `predictive-maintenance`
- `industrial-performance`
- `decision-intelligence`

Profiles suggest blocks, adapter classes, UI components and a maturity target. They never certify customer-specific semantics.

### Composable Building Blocks
Reusable mechanics include aging, coverage, deficit propagation, dead reckoning, constraint propagation, baseline deviation, rate of change, bottleneck detection, capacity risk and outcome feedback.

### Solution Manifest
The Solution Manifest records how one product is assembled:

`Profile + Blocks + Adapters + UI Components + Technology Profile + Overrides`

The Domain Pack remains separate and owns business meaning.

### Domain Pack composition
`pyrax compose` can combine a reusable base Domain Pack with organization-specific overlays. Mapping values merge recursively; lists/scalars are explicitly replaced by the overlay. Reuse never certifies transplanted semantics.

### UI composition
Reusable presentation contracts include Control Tower, Andon, Heatmap, Timeline, Object360, Evidence Drawer, Scenario Panel and Decision Card.

### Adapter catalog
Reusable adapter classes cover SQL, REST APIs, telemetry, files and event streams while preserving source identity, grain, freshness, quality and lineage boundaries.

## MCP v0.1 — Internal Agent Interface

Pyrax includes an intentionally narrow MCP interface for internal validation with AI agents.

Architecture:

`Pyrax Core -> pyrax.api -> CLI / MCP / future adapters`

The MCP does not call the CLI or parse console output. `src/pyrax/api.py` is the public programmatic boundary and `src/pyrax_mcp/` is a protocol adapter over that same logic.

V0.1 exposes six read-only tools over local stdio:

- `pyrax_validate_domain_pack`
- `pyrax_assess_readiness`
- `pyrax_assess_maturity`
- `pyrax_validate_solution_manifest`
- `pyrax_get_solution_profile`
- `pyrax_get_catalog`

Every public API/MCP result carries `framework_version` and `api_version`. Validation failures are returned as structured data rather than protocol failures.

Run locally:

```bash
pyrax-mcp
```

The v0.1 MCP deliberately has no Oracle/WMS/database access, no scaffold/file-writing tool, no remote HTTP deployment, no OAuth, no billing and no multi-tenancy. See `docs/MCP-INTERNAL.md` and `docs/MCP-SPECIFICATION.md`.

## MCP v0.1.1 — Validation Instrumentation

The validation track measures whether native Pyrax tools materially improve agent behavior before any MCP v0.2 expansion.

`src/pyrax/evaluation.py` implements a deterministic evaluation harness. Golden Cases declare normalized required findings, forbidden claims, expected UNKNOWNs, expected decisions and deterministic calculations. The harness scores structured agent observations without using an LLM as judge.

The first product-validation case is:

`golden-cases/inteligencia-operacional-d1.yaml`

It uses synthetic, company-neutral operational data. The case requires the agent to detect a 35-unit D+1 deficit while abstaining from selecting replenishment origin, lot, FIFO or FEFO because those semantics remain UNKNOWN.

Public reference and benchmark artifacts must remain company-neutral. Internal-origin cases are anonymized as **Inteligência Operacional** and use synthetic/minimized values before commit.

See `docs/MCP-EVALUATION.md`.

## Fundamental rule

> Reconstruct reality first. Calculate second. Explain third. Recommend last.

## Install

```bash
python -m pip install -e ".[dev]"
```

The package installs both `pyrax` and `pyrax-mcp`. The MCP runtime uses the official Python SDK v2.

## Start in a new company

```bash
pyrax bootstrap "Example Company" --destination ../
```

Optionally provide an initial archetype hypothesis:

```bash
pyrax bootstrap "Example Company" --archetype predictive-operations --destination ../
```

The generated draft intentionally starts incomplete and preserves explicit unknowns.

## From discovery to composed product

1. Complete organization/process discovery.
2. Map sources and semantic unknowns.
3. Select one decision-support vertical.
4. Build and validate the Domain Pack.
5. Inspect reusable profiles with `pyrax profiles`.
6. Inspect blocks/adapters/UI with `pyrax catalog blocks|adapters|ui`.
7. Create a Solution Manifest or use a profile directly.
8. Compose Domain Pack overlays if needed.
9. Run readiness and maturity assessments.
10. Scaffold the implementation.
11. Bind reusable mechanics to certified domain semantics.
12. Add Golden Cases, reconciliation and integration tests.

Example:

```bash
pyrax profiles fleet-intelligence
pyrax compose base-domain-pack.yaml --overlay customer.yaml --output domain-pack.yaml
pyrax manifest solution-manifest.yaml
pyrax scaffold route-ops --manifest solution-manifest.yaml --domain-pack domain-pack.yaml --destination ../
```

Or directly from a preset:

```bash
pyrax scaffold route-ops --profile fleet-intelligence --domain-pack domain-pack.yaml --destination ../
```

## CLI

- `pyrax bootstrap` — create a discovery workspace for a new organization.
- `pyrax validate` — validate Domain Pack structure and cross-references.
- `pyrax assess` — evaluate production-readiness gates.
- `pyrax maturity` — report Pyrax maturity P0-P5.
- `pyrax profiles` — list or inspect reusable Solution Profiles.
- `pyrax catalog` — inspect reusable blocks, adapters or UI components.
- `pyrax manifest` — validate/materialize a Solution Manifest.
- `pyrax compose` — merge a base Domain Pack with explicit overlays.
- `pyrax scaffold` — generate a project from a Domain Pack, profile or manifest.

## Reference compositions

`examples/v0.5-reference-compositions/` proves the composition model against representative portfolio shapes without copying their original implementations:

- Route Engineer
- Asset Radar
- Predictive Maintenance
- OEE Intelligence
- Decision Engine

These are reusable composition examples, not certified customer Domain Packs.

## Repository structure

- `src/pyrax/` — public API, CLI, evaluation, composition, catalogs, runtime, readiness and maturity;
- `src/pyrax_mcp/` — MCP v0.1 internal agent adapter;
- `solution-profiles/` — reusable product presets;
- `docs/` — canonical recipe, architecture, productization, MCP and evaluation contracts;
- `schemas/` — Domain Pack and Solution Manifest contracts;
- `templates/` — discovery/product/engineering templates;
- `domain-packs/` — domain customization template;
- `patterns/` — analytical/decision mechanics;
- `bootstrap/` — optional technology profiles;
- `examples/` — reference patterns and V0.5 reference compositions;
- `golden-cases/` — deterministic framework and MCP evaluation scenarios;
- `tests/` — regression, public API, composition, MCP and evaluation tests;
- `.github/workflows/` — quality gates.

## Guardrails preserved

- UNKNOWN/UNAVAILABLE/NULL are not zero.
- Profiles and reference compositions are hypotheses, not business truth.
- Evidence remains mandatory for published decision support.
- Human approval remains the default for consequential actions.
- Scenario projections never mutate canonical state.
- Ontology and Decision Graph integrity remain enforced.
- Customer-specific semantics stay outside generic catalogs and runtime.
- A valid composition is not automatically production-ready.
- MCP v0.1 is read-only and cannot access external operational systems.
- Public reference cases must not expose private company identity or proprietary operational data.

## Quality

```bash
make quality
```

CI runs on Python 3.11 and 3.12, performs Ruff + pytest, validates canonical fixtures/examples, exercises bootstrap/readiness/maturity/composition/scaffolding/MCP/evaluation behavior and builds the package.

## Canonical reading

1. `AGENTS.md`
2. `docs/UNIVERSAL-SOLUTION-RECIPE.md`
3. `docs/PRODUCTIZATION-AND-COMPOSITION.md`
4. `docs/FRAMEWORK-CHARTER.md`
5. `docs/PRINCIPLES.md`
6. `docs/DISCOVERY-PLAYBOOK.md`
7. `docs/DATA-ACQUISITION-PLAYBOOK.md`
8. `docs/SOLUTION-ARCHETYPES.md`
9. `docs/ARCHITECTURE.md`
10. `docs/OPERATIONAL-ONTOLOGY.md`
11. `docs/DECISION-GRAPH.md`
12. `docs/SCENARIO-ENGINE.md`
13. `docs/MATURITY-MODEL.md`
14. `docs/UI-COMPOSITION-CONTRACT.md`
15. `docs/INTEGRATION-ADAPTER-CATALOG.md`
16. `docs/DEVELOPMENT-LIFECYCLE.md`
17. `docs/DATA-TRUTH-MODEL.md`
18. `docs/EVIDENCE-STANDARD.md`
19. `docs/CONFIDENCE-MODEL.md`
20. `docs/DECISION-MODEL.md`
21. `docs/READINESS-MODEL.md`
22. `docs/RUNTIME-CONTRACT.md`
23. `docs/QA-STANDARD.md`
24. `docs/CLI-AND-SCAFFOLDING.md`
25. `docs/MCP-SPECIFICATION.md`
26. `docs/MCP-INTERNAL.md`
27. `docs/MCP-EVALUATION.md`

## Status

Framework line: **v0.5 — Productization & Composition**.

Agent interface: **Pyrax MCP v0.1 — technically validated**.

Validation instrumentation: **Pyrax MCP v0.1.1 — active product-validation track**.
