from __future__ import annotations

from pyrax.models import ConfidenceLevel, Recommendation, Signal


class DecisionEngine:
    @staticmethod
    def recommend(
        signal: Signal | None,
        *,
        decision_id: str,
        action: str,
        human_approval_required: bool = True,
    ) -> Recommendation | None:
        if signal is None or signal.confidence == ConfidenceLevel.INSUFFICIENT_DATA:
            return None
        evidence = tuple(e for fact in signal.facts for e in fact.evidence)
        return Recommendation(
            decision_id=decision_id,
            action=action,
            confidence=signal.confidence,
            evidence=evidence,
            human_approval_required=human_approval_required,
        )
