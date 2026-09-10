# Pyrax Framework — QA Standard

## Objective

Protect semantic correctness, data integrity, decision safety and product reliability.

## Minimum QA layers

1. **Contract tests** — types, required fields, units, keys and nullability.
2. **Semantic tests** — business meaning, status mappings and population rules.
3. **Quality tests** — missing data, duplicates, invalid values, stale data and grain violations.
4. **Reconciliation tests** — compare derived results against an independent trusted reference.
5. **Rule/formula tests** — deterministic calculations and boundaries.
6. **Golden Cases** — known end-to-end examples with expected output.
7. **Negative cases** — insufficient data, invalid joins, source failure and contradictory facts.
8. **Integration tests** — source gateway through application contracts.
9. **UX/E2E tests** — decision journey, confidence and evidence visibility.
10. **Packaging/deployment tests** — where applicable.

## Golden Case contract

Every Golden Case should define:
- case id;
- scenario;
- input facts;
- unknowns;
- expected signal;
- expected recommendation or abstention;
- expected confidence;
- expected evidence;
- prohibited outcomes.

## Certification rule

A passing test suite does not automatically certify source semantics. Test evidence and source/business validation are distinct.

## Regression rule

Every corrected P0/P1 data or decision defect should receive a regression test when technically practical.

## Release gate

A release should never hide failing quality, reconciliation or semantic gates behind UI defaults or mock data.
