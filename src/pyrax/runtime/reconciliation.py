from __future__ import annotations

from decimal import Decimal


class ReconciliationGate:
    @staticmethod
    def compare(observed: Decimal | int | float, reference: Decimal | int | float, *, tolerance: Decimal | float = Decimal("0")) -> tuple[bool, Decimal]:
        observed_d = Decimal(str(observed))
        reference_d = Decimal(str(reference))
        tolerance_d = Decimal(str(tolerance))
        delta = observed_d - reference_d
        return abs(delta) <= tolerance_d, delta
