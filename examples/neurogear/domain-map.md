# Reference Pattern — NeuroGear

## Domain
Industrial equipment and OEE-oriented operational intelligence.

## Core entities
- Machine/Asset
- Production Run
- Cycle
- Downtime Event
- Quality Event
- Maintenance Event
- Operator/Team

## Example decision chain
`Observed Equipment State -> Availability/Performance/Quality Signals -> Degradation or Constraint Pattern -> Candidate Intervention -> Evidence -> Assisted Maintenance/Operations Decision`

## Reusable patterns
- State/event reconstruction before prediction.
- OEE dimensions kept semantically distinct.
- Trend and degradation signals before heavy ML.
- Evidence-backed intervention recommendations.
- Outcome capture for later calibration.

## Do not reuse blindly
Machine-specific thresholds, failure modes, sensors and OEE conventions belong to the manufacturing domain pack.
