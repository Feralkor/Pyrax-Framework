# Pyrax Framework v0.4.0 — Release Candidate

Status: **RELEASE CANDIDATE / ACTIVE VALIDATION**

## Theme

**Ontology, Decision Graph, Scenario & Maturity**

v0.4 extends the Universal Solution Recipe with reusable structures for modeling operational reality and reasoning about decisions without weakening the deterministic-first, Evidence-driven foundation established in v0.3.

## New capabilities

### Operational Ontology
- Entity, Relationship, Event and Action primitives.
- Domain-neutral graph mechanics.
- Relationship/event/action references must point to known entities.
- Source tables are not automatically ontology objects.

### Decision Graph
- Facts/states/signals/decisions/actions/outcomes can be represented as dependency nodes.
- Edges require known nodes.
- Self-loops and evaluation-cycle graph cycles are rejected.
- The graph supports impact tracing but does not claim causal certification by itself.

### Scenario Engine
- Explicit baseline + assumptions + deterministic projector.
- Canonical baseline is not mutated.
- Projected states remain hypothetical until later observation/reconciliation.

### Pyrax Maturity Model
- P0_DISCOVERY
- P1_TRUTH_MAPPED
- P2_OPERATIONAL_STATE
- P3_ASSISTED_INTELLIGENCE
- P4_PREDICTIVE_OPERATIONS
- P5_CLOSED_LOOP_INTELLIGENCE

Maturity is cumulative and independent of production readiness.

## CLI

v0.4 adds:

```bash
pyrax maturity domain-pack.yaml
```

Existing commands remain:

```bash
pyrax bootstrap
pyrax validate
pyrax assess
pyrax scaffold
```

## Domain Pack v0.4 extension

Optional configuration surfaces were added for:
- `ontology`;
- `decision_graph`;
- `scenarios`;
- `maturity.target`;
- implementation flags for quality, anticipation, scenarios, Operational Memory and feedback loop.

These additions are optional to preserve compatibility with simpler or lower-maturity products.

## Release invariants

- UNKNOWN/UNAVAILABLE/NULL are not silently zero/false.
- Scenario results never become canonical truth automatically.
- Decision Graph does not fabricate causality.
- Ontology does not infer business meaning from database shape alone.
- Higher maturity does not override Evidence, confidence, QA or production-readiness gates.
- Human approval remains the default for critical actions.
- AI/LLM remains downstream of Truth, semantics, Evidence and guardrails.

## Stable gate

Do not label v0.4.0 stable until the HEAD workflow passes:
- Ruff;
- pytest including v0.4 capability tests;
- bootstrap smoke;
- Domain Pack validation;
- readiness assessment;
- maturity assessment;
- scaffold smoke;
- package build on the configured Python matrix.

## Deferred

The MCP remains deferred and is not part of v0.4.0.