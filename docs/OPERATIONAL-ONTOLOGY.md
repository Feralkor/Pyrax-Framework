# Pyrax Operational Ontology

## Purpose

The Operational Ontology is the domain-neutral model used to represent the operational world as objects, relationships, events and allowed actions instead of treating source tables as the business model.

## Core primitives

- **Entity** — identifiable operational object such as customer, order, wave, vehicle, machine, contract, asset, project or task.
- **Relationship** — validated relation between two entities.
- **Event** — observed occurrence associated with an entity and, when known, a time.
- **Action** — candidate action that may affect an entity and is subject to constraints and approval policy.
- **State** — current reconstructed condition of an entity; state remains downstream of source truth and semantics.
- **Constraint** — condition that limits or invalidates actions/decisions.

## Rules

1. Source-system tables are inputs, not ontology objects by default.
2. An entity must have a stable domain identity before relationships are trusted.
3. A relationship must reference known entities.
4. Events must not fabricate timestamps or state transitions.
5. Actions are candidates until authorization policy allows execution.
6. Ontology must preserve provenance outside this graph through normal Pyrax Evidence/Truth contracts.
7. Domain Packs define business meaning; the generic ontology only provides mechanics.

## Example

`Customer -> has Contract -> creates Order -> affects Resource -> generates Event -> may trigger Signal -> informs Decision`

## Competitive role

The ontology lets Pyrax reuse one architecture across different industries while allowing each domain to define its own object vocabulary and semantics.