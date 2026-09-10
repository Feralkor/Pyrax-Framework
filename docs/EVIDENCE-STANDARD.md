# Pyrax Framework — Evidence Standard

## Principle

A decision-support output is incomplete if the user cannot understand why it exists.

## Minimum Evidence Contract

Every important signal or recommendation should expose:
- `evidence_id`;
- subject/entity;
- source(s);
- period/cutoff;
- snapshot/state version;
- rule or model version;
- inputs used;
- excluded/unknown inputs;
- quality status;
- reconciliation status when applicable;
- confidence;
- explanation suitable for the operational user.

## Evidence levels

- `SOURCE_EVIDENCE` — raw or source-proximate fact.
- `DERIVED_EVIDENCE` — deterministic transformation of certified facts.
- `INFERRED_EVIDENCE` — statistical/model-based inference.
- `HUMAN_EVIDENCE` — explicit operational validation or annotation.

## Explainability rule

The UI should answer:
1. What happened or may happen?
2. Which facts support that statement?
3. Which rule/model generated it?
4. What is uncertain?
5. What action is being suggested?
6. What is the expected impact?

## Audit rule

Evidence is immutable for a published decision instance. Corrections create a new version rather than silently overwriting the old explanation.
