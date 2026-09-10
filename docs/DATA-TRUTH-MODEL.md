# Pyrax Framework — Data Truth Model

## Objective

Define when data can be treated as an operational fact.

## Certification ladder

- `DISCOVERED` — source/object/field exists.
- `STRUCTURALLY_MAPPED` — keys, types and grain are understood.
- `SEMANTICALLY_VALIDATED` — business meaning is confirmed.
- `RECONCILED` — result matches an independent trusted reference within defined tolerance.
- `PRODUCTION_CERTIFIED` — safe for product decisions under documented conditions.

Never collapse these states into one generic "mapped" status.

## Required fact metadata

Every canonical fact should carry or be traceable to:
- source system;
- source object/query/API;
- extraction timestamp/cutoff;
- entity and grain;
- business key;
- unit;
- semantic version;
- quality state;
- reconciliation state;
- provenance/evidence reference.

## Missing-data rule

`UNKNOWN`, `UNAVAILABLE`, `NOT_IDENTIFIED`, `NOT_APPLICABLE` and observed `0` are different states.

A missing value must never become zero through convenience defaults.

## Join rule

For every important join, validate:
- key uniqueness;
- expected cardinality;
- unmatched population;
- row multiplication/fanout;
- duplicate business facts;
- temporal compatibility.

## Population rule

Rates and ratios must use compatible eligible populations. Do not mix complete numerators with partial denominators.

## Source-of-record rule

Each fact must name its system of record or authoritative derivation. Secondary sources may reconcile, enrich or provide fallback only when explicitly modeled.
