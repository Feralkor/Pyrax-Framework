# Pyrax Framework — Reference Architecture

## Conceptual flow

`Sources -> Source Gateway -> Semantic Contracts -> Quality -> Reconciliation -> Canonical State -> Signals -> Anticipation -> Decision Support -> Evidence -> UX -> Outcome -> Operational Memory`

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

### 3. Operational State Layer
Represents current and historical entities, relationships and states.

Examples: wave, vehicle, machine, customer, contract, asset, order, task.

### 4. Anticipation Layer
Produces signals without modifying canonical facts.

Preferred methods:
- deterministic rules;
- aging;
- thresholds;
- rate of change;
- rolling windows;
- constraint propagation;
- dead reckoning;
- robust statistical baselines;
- scenario projection.

ML is optional and versioned as a separate method.

### 5. Decision Layer
Maps signals and constraints into candidate actions.

A decision output should contain:
- subject;
- observed state;
- signal;
- candidate action;
- expected impact;
- constraints;
- confidence;
- evidence;
- approval policy.

### 6. Experience Layer
Operational interfaces prioritize exceptions, context and actionability.

UI never becomes the source of business truth.

### 7. Memory & Outcome Layer
Stores the sequence:

`Observation -> Signal -> Recommendation -> Human/Automated Action -> Outcome`

This is the foundation for calibration and future learning.

## Deployment neutrality

Products may use desktop, web, edge or cloud deployments. The framework defines boundaries and contracts rather than enforcing one runtime topology.

## AI boundary

LLMs may consume certified context through an explicit gateway. They may explain and summarize, but must not silently mutate canonical state, source facts or certified calculations.
