# Integration Adapter Catalog

Adapters isolate external systems from Pyrax domain/runtime mechanics.

## Adapter classes

### `sql`
For relational systems such as PostgreSQL, Oracle, SQL Server and MySQL.

Default posture:
- read-only;
- bounded/selective queries;
- explicit grain and cutoff;
- source identity and query/contract versioning;
- no semantic inference from column names alone.

### `rest-api`
For JSON/HTTP APIs.

Default posture:
- preserve provider identifiers and timestamps;
- classify partial/error responses;
- record request contract/version where relevant;
- avoid interpreting missing fields as zero or false.

### `telemetry`
For GPS, IoT, machine and vehicle telemetry.

Default posture:
- preserve event time and ingest time separately;
- track freshness/staleness;
- distinguish observed state from projected state;
- reconcile duplicate/out-of-order events where required.

### `files`
For CSV, Excel, JSON, Parquet and similar sources.

Default posture:
- preserve source filename/version/hash when practical;
- validate schema, grain, duplicates, missingness and temporal coverage;
- never silently coerce malformed data into valid operational facts.

### `event-stream`
For queues, Kafka-like streams and event buses.

Default posture:
- explicit event identity/idempotency;
- ordering assumptions documented;
- replay behavior defined;
- event loss/lag surfaced as data quality state.

## Adapter contract

Every product-specific adapter should expose, where applicable:
- source identity;
- access mode;
- observation/cutoff time;
- grain;
- keys;
- freshness;
- raw/normalized payload boundary;
- quality status;
- lineage metadata;
- classified errors.

Adapters provide observations. They do not certify business meaning; semantic certification belongs to the Domain Pack/product layer.
