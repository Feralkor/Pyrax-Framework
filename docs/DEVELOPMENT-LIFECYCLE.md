# Pyrax Framework — Development Lifecycle

## Phase 0 — Problem & Decision
Define the operational problem before the technology.

Required outputs:
- problem statement;
- decision owner;
- decision to improve;
- action available to that owner;
- success and harm criteria;
- initial scope.

## Phase 1 — Discovery
Map the operational environment.

Questions:
1. What must be anticipated?
2. Who acts on the result?
3. What systems are sources of record?
4. What entities exist?
5. What is the operational grain?
6. Which states and timestamps are observable?
7. Which relationships can be proven?
8. What is still unknown?

Outputs:
- source map;
- domain map;
- semantic inventory;
- uncertainty register.

## Phase 2 — Truth Foundation
Create contracts and validate sources.

Order:
`Metadata -> Sample -> Relationship -> Temporal -> Reconciliation -> Certification`

Outputs:
- data contracts;
- query/API manifests;
- quality rules;
- reconciliation strategy;
- lineage/evidence requirements.

## Phase 3 — Canonical State
Build the smallest state model needed for one decision.

Avoid modeling the entire enterprise before proving one useful vertical.

## Phase 4 — Signals
Define observable conditions that deserve attention.

Every signal must declare:
- subject;
- population;
- rule;
- threshold/baseline if applicable;
- severity;
- evidence;
- false-positive risks.

## Phase 5 — Anticipation
Project what can happen next using the lightest sufficient method.

Method preference:
1. deterministic state/rules;
2. constraint propagation;
3. aging/rate-of-change;
4. robust descriptive statistics;
5. probabilistic/statistical models;
6. ML only when justified by data and decision value.

## Phase 6 — Decision Support
Map signal + constraints + context into candidate action.

Separate:
- what is known;
- what is inferred;
- what is recommended;
- what remains unknown.

## Phase 7 — Operational UX
Build around the user's next decision.

Sequence:
`Risk/Opportunity -> Where -> Why -> Impact -> Candidate Action -> Confidence -> Evidence`

## Phase 8 — Validation
Use Golden Cases, negative cases, reconciliation and end-to-end tests.

A demo is not production certification.

## Phase 9 — Outcome & Memory
Record what happened after the recommendation.

Use outcomes to calibrate rules, thresholds and future models.

## Phase 10 — Productization
Only after the vertical is reliable:
- expand entities;
- add domains;
- automate scaffolding;
- package/deploy;
- introduce MCP/agent workflows;
- consider ML or autonomous policies.

## Vertical-slice rule

Prefer one complete decision chain over many disconnected modules.

`Source -> Fact -> Signal -> Decision -> Evidence -> UX -> Outcome`
