# Reference Pattern — Route Engineer

## Domain
Fleet and transportation operational intelligence.

## Core entities
- Driver
- Vehicle
- Load
- Route
- Stop
- HOS state
- Fuel event
- Maintenance event

## Example decision chain
`Current Route State -> HOS/Fuel/ETA Constraints -> Projected Risk -> Candidate Operational Adjustment -> Evidence -> Dispatch Decision Support`

## Reusable patterns
- Dead reckoning and state projection before heavy ML.
- Constraint propagation across driver, vehicle, route and load.
- Multi-source reconciliation.
- Driver360 / asset context around a decision.
- Decision support with explicit confidence and evidence.

## Do not reuse blindly
Carrier rules, HOS regulation, ETA providers and fleet-system semantics remain transportation-domain concerns.
