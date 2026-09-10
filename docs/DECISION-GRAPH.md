# Pyrax Decision Graph

## Purpose

The Decision Graph expresses how operational facts, signals, decisions, candidate actions and outcomes depend on one another.

## Node types

Typical node types include:
- FACT
- STATE
- SIGNAL
- DECISION
- ACTION
- OUTCOME
- CONSTRAINT

## Edge examples

- FACT -> informs -> SIGNAL
- SIGNAL -> triggers -> DECISION
- CONSTRAINT -> limits -> ACTION
- ACTION -> changes -> STATE
- STATE -> affects -> DECISION
- ACTION -> produces -> OUTCOME

## Rules

1. Every edge must reference known nodes.
2. Self-loops are invalid.
3. Cycles are rejected by the baseline implementation because they obscure causal/order reasoning. Feedback is represented through Operational Memory and subsequent observations, not an in-run cycle.
4. The graph explains dependencies; it does not by itself certify causal truth.
5. Confidence and Evidence remain attached to the underlying Pyrax facts/signals/decisions.

## Why it matters

A graph enables impact tracing such as:

`Picking deficit -> D+1 wave risk -> customer impact -> replenishment decision`

or:

`HOS constraint -> ETA risk -> appointment risk -> downstream load impact`.

This pattern is reusable across domains.