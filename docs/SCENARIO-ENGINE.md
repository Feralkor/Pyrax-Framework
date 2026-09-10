# Pyrax Scenario Engine

## Purpose

The Scenario Engine evaluates deterministic what-if projections without mutating canonical operational state.

## Contract

Inputs:
- certified/qualified baseline state;
- explicit scenario assumptions;
- a versioned projection function.

Outputs:
- baseline snapshot;
- assumptions;
- projected state;
- changed fields.

## Rules

1. Scenario output is never canonical truth.
2. Assumptions must be explicit and inspectable.
3. UNKNOWN inputs remain UNKNOWN unless the scenario explicitly defines an assumption for them.
4. A scenario must not silently write back to a system of record.
5. Scenario results should carry Evidence/Confidence in product implementations when used for decision support.
6. ML-based simulation, when added, must be separately versioned and evaluated; deterministic scenarios remain the baseline.

## Examples

- Warehouse: if 40 units are replenished, which known waves become covered?
- Fleet: if driver X receives load Y, how do HOS/ETA constraints change?
- Manufacturing: if throughput falls 8%, where does capacity risk emerge?
- Strategy: if margin trend continues for eight weeks, which accounts cross the defined risk threshold?

## Competitive role

Scenario reasoning lets Pyrax move from monitoring to operational decision support while preserving explainability.