from __future__ import annotations

from typing import Any

from pyrax.models import ConfidenceLevel, Evidence, OperationalFact


class TruthEngine:
    """Build operational facts without converting missing data into zero."""

    @staticmethod
    def fact(
        fact_id: str,
        value: Any,
        *,
        confidence: ConfidenceLevel,
        evidence: tuple[Evidence, ...] = (),
        unknown_reason: str | None = None,
    ) -> OperationalFact:
        return OperationalFact(
            fact_id=fact_id,
            value=value,
            confidence=confidence,
            evidence=evidence,
            unknown_reason=unknown_reason,
        )
