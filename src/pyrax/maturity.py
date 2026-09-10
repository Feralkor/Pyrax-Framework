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
