# Reference Pattern — XPM Inteligência Operacional

## Domain
Warehouse operational intelligence.

## Core entities
- Wave
- Product/SKU
- Depositor/Client
- Picking Position
- Buffer Position
- Collaborator
- Sector

## Example decision chain
`Known D+1 Demand -> Picking Availability -> Deficit -> Benefited Waves -> Candidate Buffer Source -> Evidence -> Assisted Replenishment Decision`

## Reusable patterns
- Need / Impact / Source separation.
- UNKNOWN != ZERO.
- Candidate source uncertainty must not erase a known replenishment need.
- Aging/Andon as operational prioritization.
- Read-only system-of-record integration.
- Evidence and semantic certification before recommendation.

## Do not reuse blindly
Warehouse-specific FIFO/FEFO, depositor, lot, picking and buffer semantics belong to the XPM domain and must not be generalized into the framework core.
