# Pyrax Framework — Data Acquisition Playbook

Status: CANONICAL
Version: 0.3

## Purpose

Standardize how a new solution discovers, accesses and certifies data without coupling the framework to a specific vendor or database.

## Source classes

- System of Record
- Reference system
- Derived/internal analytical source
- External/public source
- Human-maintained source
- Telemetry/event stream
- File/spreadsheet/manual export

## Source assessment

For every source record:
- owner;
- authority;
- access mode;
- authentication boundary;
- grain;
- business keys;
- timestamps;
- freshness;
- retention;
- mutability;
- expected volume;
- query/API limits;
- failure modes;
- sensitive fields;
- semantic unknowns.

## Preferred discovery sequence

`Metadata -> Sample -> Relationship -> Temporal behavior -> Reconciliation -> Certification`

### Metadata
Confirm objects, fields, types, keys and constraints.

### Sample
Inspect bounded representative records. Sampling does not certify business meaning.

### Relationship
Test joins, cardinality, fanout, duplicates and row loss.

### Temporal behavior
Understand event time, processing time, corrections, late arrivals and mutable history.

### Reconciliation
Compare against an independent trusted reference when possible.

### Certification
Promote only the semantics actually supported by evidence.

## Data acquisition strategy

Prefer the least invasive mechanism that satisfies freshness and scale:
- read-only database access;
- bounded APIs;
- event subscription;
- CDC/read replicas when appropriate;
- scheduled exports;
- governed file ingestion;
- external data feeds.

Never require direct production-database access when another source can meet the need safely.

## UNKNOWN policy

Missing or semantically unresolved data remains unknown. Do not:
- infer from field names;
- convert NULL to zero;
- fill absent categories with defaults without a documented rule;
- infer joins solely from similar identifiers;
- declare a source authoritative without an owner or reconciliation path.

## Output

The playbook produces:
- Source Map;
- Data Contracts;
- Query/API manifests;
- semantic registry;
- reconciliation plan;
- source-specific guardrails;
- Evidence lineage requirements.
