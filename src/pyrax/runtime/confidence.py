from __future__ import annotations

from collections.abc import Iterable

from pyrax.models import ConfidenceLevel


def resolve_confidence(levels: Iterable[ConfidenceLevel]) -> ConfidenceLevel:
    values = tuple(levels)
    if not values or ConfidenceLevel.INSUFFICIENT_DATA in values:
        return ConfidenceLevel.INSUFFICIENT_DATA
    if all(value == ConfidenceLevel.CERTIFIED for value in values):
        return ConfidenceLevel.CERTIFIED
    return ConfidenceLevel.ASSISTED
