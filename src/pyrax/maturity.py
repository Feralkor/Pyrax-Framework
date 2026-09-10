from __future__ import annotations

from dataclasses import dataclass
from enum import IntEnum


class MaturityLevel(IntEnum):
    P0_DISCOVERY = 0
    P1_TRUTH_MAPPED = 1
    P2_OPERATIONAL_STATE = 2
    P3_ASSISTED_INTELLIGENCE = 3
    P4_PREDICTIVE_OPERATIONS = 4
    P5_CLOSED_LOOP_INTELLIGENCE = 5


@dataclass(frozen=True)
class MaturityAssessment:
    level: MaturityLevel
    reasons: tuple[str, ...]


def assess_maturity(capabilities: dict[str, bool]) -> MaturityAssessment:
    """Return the highest contiguous maturity level supported by declared capabilities."""

    gates = [
        (MaturityLevel.P0_DISCOVERY, ["discovery"]),
        (MaturityLevel.P1_TRUTH_MAPPED, ["discovery", "sources", "semantics", "evidence"]),
        (MaturityLevel.P2_OPERATIONAL_STATE, ["state", "quality", "reconciliation"]),
        (MaturityLevel.P3_ASSISTED_INTELLIGENCE, ["signals", "decisions", "human_approval"]),
        (MaturityLevel.P4_PREDICTIVE_OPERATIONS, ["anticipation", "scenarios"]),
        (MaturityLevel.P5_CLOSED_LOOP_INTELLIGENCE, ["outcomes", "operational_memory", "feedback_loop"]),
    ]

    current = MaturityLevel.P0_DISCOVERY
    reasons: list[str] = []
    for level, required in gates:
        missing = [item for item in required if not capabilities.get(item, False)]
        if missing:
            reasons.append(f"{level.name} blocked by: {', '.join(missing)}")
            break
        current = level
        reasons.append(f"{level.name} achieved")
    return MaturityAssessment(current, tuple(reasons))


def capabilities_from_domain_pack(pack: dict) -> dict[str, bool]:
    """Derive conservative maturity signals from a Domain Pack without inventing capability."""

    semantics = pack.get("semantics", {}) if isinstance(pack.get("semantics"), dict) else {}
    implementation = (
        pack.get("implementation", {}) if isinstance(pack.get("implementation"), dict) else {}
    )
    qa = pack.get("qa", {}) if isinstance(pack.get("qa"), dict) else {}
    approval = pack.get("approval_policy", {}) if isinstance(pack.get("approval_policy"), dict) else {}

    unknowns = semantics.get("unknowns", []) or []
    certified = semantics.get("certified", []) or []
    evidence = pack.get("evidence", {}) if isinstance(pack.get("evidence"), dict) else {}

    return {
        "discovery": bool(pack.get("problem")),
        "sources": bool(pack.get("sources")),
        "semantics": bool(certified) and not unknowns,
        "evidence": bool(evidence.get("required")) and bool(evidence.get("fields")),
        "state": bool(pack.get("states")) or bool(implementation.get("runtime")),
        "quality": bool(implementation.get("quality", implementation.get("runtime", False))),
        "reconciliation": bool(qa.get("reconciliation_tests")),
        "signals": bool(pack.get("signals")),
        "decisions": bool(pack.get("decisions")),
        "human_approval": approval.get("mode") in {"HUMAN_ASSISTED", "HUMAN_APPROVED"},
        "anticipation": bool(implementation.get("anticipation")),
        "scenarios": bool(implementation.get("scenarios")),
        "outcomes": bool(pack.get("outcomes")),
        "operational_memory": bool(implementation.get("operational_memory")),
        "feedback_loop": bool(implementation.get("feedback_loop")),
    }


def assess_domain_maturity(pack: dict) -> MaturityAssessment:
    return assess_maturity(capabilities_from_domain_pack(pack))
