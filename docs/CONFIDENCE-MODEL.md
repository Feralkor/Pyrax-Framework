# Pyrax Framework — Confidence Model

## Purpose

Confidence communicates how strongly the system can support a statement or recommendation from available evidence.

## Default states

- `CERTIFIED` — supported by production-certified semantics and required validations.
- `ASSISTED` — useful and evidence-backed, but one or more non-critical assumptions/semantics remain partially validated.
- `INSUFFICIENT_DATA` — the system must abstain from a stronger statement.

Products may extend the vocabulary, but must preserve the distinction between certainty, assistance and abstention.

## Component-level confidence

Confidence should be granular. A recommendation may have:
- demand: CERTIFIED;
- current state: CERTIFIED;
- impact: ASSISTED;
- candidate source: INSUFFICIENT_DATA.

Uncertainty in one component must not erase facts already supported by stronger evidence.

## Confidence inputs

Possible contributors:
- semantic certification;
- data coverage;
- reconciliation status;
- source freshness;
- sample adequacy;
- rule/model validation;
- unresolved unknowns.

## Prohibitions

Do not invent percentage confidence scores unless a calibrated method exists.
Do not use confidence to hide data-quality failures.
Do not present `ASSISTED` as equivalent to certified automation.
