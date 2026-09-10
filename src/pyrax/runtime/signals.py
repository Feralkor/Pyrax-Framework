from __future__ import annotations

from collections.abc import Callable

from pyrax.models import ConfidenceLevel, OperationalFact, Signal


class SignalEngine:
    @staticmethod
    def evaluate(
        signal_id: str,
        facts: tuple[OperationalFact, ...],
        *,
        predicate: Callable[[tuple[OperationalFact, ...]], bool],
        severity: str = "ATTENTION",
    ) -> Signal | None:
        if not facts or not predicate(facts):
            return None
        if any(f.confidence == ConfidenceLevel.INSUFFICIENT_DATA for f in facts):
            confidence = ConfidenceLevel.INSUFFICIENT_DATA
        elif all(f.confidence == ConfidenceLevel.CERTIFIED for f in facts):
            confidence = ConfidenceLevel.CERTIFIED
        else:
            confidence = ConfidenceLevel.ASSISTED
        return Signal(signal_id=signal_id, severity=severity, facts=facts, confidence=confidence)
