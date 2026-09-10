# Pyrax Framework — Reference Architecture

## Conceptual flow

`Sources -> Source Gateway -> Semantic Contracts -> Quality -> Reconciliation -> Canonical State -> Signals -> Anticipation -> Decision Support -> Evidence -> UX -> Outcome -> Operational Memory`

## Executable framework mapping

- Source boundary: `src/pyrax/runtime/ports.py`
- Truth facts: `src/pyrax/runtime/truth.py`
- Canonical state: `src/pyrax/runtime/state.py`
- Quality: `src/pyrax/runtime/quality.py`
- Reconciliation: `src/pyrax/runtime/reconciliation.py`
- Evidence: `src/pyrax/runtime/evidence.py`
- Confidence: `src/pyrax/runtime/confidence.py`
- Signals: `src/pyrax/runtime/signals.py`
- Deterministic anticipation: `src/pyrax/runtime/anticipation.py`
- Decisions: `src/pyrax/runtime/decision.py`
- Operational memory: `src/pyrax/runtime/memory.py`
- Observability: `src/pyrax/runtime/observability.py`
- Domain Pack validation: `src/pyrax/validation.py`
- Readiness: `src/pyrax/readiness.py`
- Scaffolding: `src/pyrax/scaffold.py`
- CLI: `src/pyrax/cli.py`

## Layers

### 1. Source Layer
Connectors to systems of record, telemetry, files, APIs and event streams.

Responsibilities:
- authenticated read access;
- bounded extraction;
- source identity;
- timestamps/cutoff;
- retries and failure classification;
- no semantic invention.

The generic framework exposes the `SourceAdapter` port. Concrete Oracle, PostgreSQL, CRM, telematics, ERP or API adapters belong to products/domain integrations.

### 2. Truth Layer
Normalizes and validates what the source actually means.

Components:
- contracts;
- semantic mapping;
- unit normalization;
- grain and keys;
- quality gates;
- reconciliation;
- lineage;
- snapshots.

A value absent from a source remains absent. `UNKNOWN != ZERO` is a runtime and product invariant.

### 3. Operational State Layer
Represents current and historical entities, relationships and states.

Examples: wave, vehicle, machine, customer, contract, asset, order, task.

The generic `OperationalState` only groups facts; products own entity semantics and persistence.

### 4. Anticipation Layer
Produces signals/projections without modifying canonical facts.

Preferred methods:
- deterministic rules;
- aging;
- coverage/deficit;
- thresholds;
- rate of change;
- rolling windows;
- constraint propagation;
- dead reckoning;
- robust statistical baselines;
- scenario projection.

The initial executable runtime implements aging, coverage, deficit and dead reckoning. Additional patterns are specified in `patterns/catalog.yaml` and are promoted to reusable code only when they remain domain-neutral.

ML is optional and versioned as a separate downstream method.

### 5. Decision Layer
Maps supported signals and constraints into candidate actions.

A decision output should contain:
- subject;
- observed state;
- signal;
- candidate action;
- expected impact where supported;
- constraints;
- confidence;
- evidence;
- approval policy.

The generic Decision Engine abstains when required confidence is insufficient or Evidence is absent. Human approval defaults to true.

### 6. Experience Layer
Operational interfaces prioritize exceptions, context and actionability.

UI never becomes the source of business truth. The Framework does not mandate React, Electron or another presentation stack.

### 7. Memory & Outcome Layer
Stores the sequence:

`Observation -> Signal -> Recommendation -> Human/Automated Action -> Outcome`

This is the foundation for calibration and future learning. The framework ships a simple in-memory contract; production persistence is product-owned.

### 8. Observability Layer
Every product should be able to trace a run through source, quality, reconciliation, signal and decision stages without exposing secrets. The generic runtime supplies `RuntimeEvent` and `EventCollector` as a minimal contract.

## Deployment neutrality

Products may use desktop, web, edge, hybrid or cloud deployments. `bootstrap/technology-profiles.yaml` contains optional starting profiles; domain constraints and security determine the final topology.

## AI boundary

LLMs may consume certified/assisted context through an explicit downstream gateway. They may explain and summarize, but must not silently mutate canonical state, source facts, semantic status, quality gates or certified calculations.

The MCP implementation is intentionally outside the current executable baseline.
