# Pyrax Framework — Decision Model

## Objective

Transform evidence-backed operational signals into constrained candidate actions without confusing observation, inference and recommendation.

## Decision chain

`Known State -> Signal -> Anticipated Impact -> Candidate Action -> Constraints -> Confidence -> Evidence -> Outcome`

## Required fields

A decision-support record should define:
- decision/subject id;
- decision owner;
- observed state;
- triggering signal(s);
- anticipated impact;
- candidate action;
- expected benefit;
- constraints and exclusions;
- urgency/severity;
- confidence by component;
- evidence references;
- approval policy;
- outcome status when available.

## Separation of concerns

Always separate:
1. **Observation** — what the system knows.
2. **Inference** — what may follow from those facts.
3. **Recommendation** — what action could be considered.
4. **Authority** — who or what is allowed to execute it.

## Decision policies

Default policy is `HUMAN_ASSISTED`.

Other policies may include:
- `INFORMATION_ONLY`;
- `HUMAN_ASSISTED`;
- `HUMAN_APPROVAL_REQUIRED`;
- `AUTOMATED_WITH_GUARDRAILS`.

Automation is never inherited from the framework by default; the Domain Pack must explicitly define and certify it.

## Need / Impact / Source pattern

Where applicable, split decision logic into independent engines:
- **Need** — is intervention necessary?
- **Impact** — what benefits or risks are affected?
- **Source/Action** — which feasible action/resource/origin should be considered?

Uncertainty in Source must not erase a certified Need.
