# Pyrax Framework — Principles

1. **Reality before intelligence** — reconstruct the operational truth before calculating or recommending.
2. **Semantics before metrics** — a column name is not a business definition.
3. **Unknown is a valid state** — `UNKNOWN`, `UNAVAILABLE` and `NULL` are never silently converted to zero.
4. **Deterministic first** — use rules, state transitions, thresholds, aging, constraint propagation and robust statistics before heavy ML when sufficient.
5. **Evidence with every decision** — important outputs must expose source, grain, rule, timestamp, quality and confidence.
6. **Human-centered automation** — recommendations are assisted by default; autonomous actions require explicit certification and policy.
7. **One population per rate** — numerators, denominators and temporal eligibility must refer to the same eligible population.
8. **No hidden fanout** — joins, duplication and cardinality changes must be measured.
9. **State is versioned** — snapshots and derived facts must be reproducible and traceable.
10. **Domain logic stays local** — reusable framework behavior remains generic; industry-specific assumptions live in Domain Packs.
11. **Abstention beats fabrication** — insufficient evidence produces a clear abstention, not a guessed answer.
12. **Outcome closes the loop** — decision-support systems should record what happened after recommendations.
13. **Lean by design** — remove duplicated decisions, historical clutter and unnecessary abstraction.
14. **Progressive disclosure** — operational UX should show what needs attention first and technical detail on demand.
15. **AI is downstream of truth** — LLMs may explain, summarize or assist; they do not redefine canonical facts.
