# Pyrax Runtime Contract

The reusable runtime is intentionally small. It standardizes safety and evidence behavior without importing assumptions from any product domain.

## Components

### Truth Engine
Creates operational facts while preserving `None/UNKNOWN` explicitly. Missing values require an `unknown_reason`.

### Operational State
Groups facts under one observed state and timestamp without mutating source meaning.

### Quality Gate
Runs product-provided deterministic quality checks before facts are promoted.

### Reconciliation Gate
Compares observed and independent reference values using explicit tolerance.

### Evidence
Carries source, grain, observation time, rule version, quality and lineage.

### Confidence
Combines component confidence conservatively:

- any `INSUFFICIENT_DATA` → `INSUFFICIENT_DATA`;
- all `CERTIFIED` → `CERTIFIED`;
- otherwise → `ASSISTED`.

### Signal Engine
Produces attention signals from facts and deterministic predicates. Signal confidence derives from the facts that support it.

### Anticipation helpers
Initial reusable deterministic patterns include:

- aging;
- coverage;
- deficit;
- dead reckoning.

Unknown inputs return unknown outputs instead of numerical defaults.

### Decision Engine
Turns a supported signal into a recommendation while carrying confidence and Evidence. It abstains when signal confidence is `INSUFFICIENT_DATA`.

Human approval defaults to `true`.

### Operational Memory
Stores observation/decision/outcome events for later evaluation. The initial implementation is in-memory by design; products define durable persistence behind their own boundary.

## Boundary rule

The runtime defines mechanics, not business truth.

For example, `coverage(available, demand)` is reusable. What counts as *eligible available stock*, *available driver hours*, *available machine capacity* or *commercial capacity* belongs to the Domain Pack/product.

## AI boundary

No LLM is part of the canonical runtime path. AI may consume certified/assisted facts downstream but may not promote uncertain values into facts or weaken decision guardrails.
