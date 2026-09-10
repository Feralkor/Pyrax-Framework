from __future__ import annotations

from decimal import Decimal


def aging(reference_epoch_seconds: int | float, current_epoch_seconds: int | float) -> Decimal:
    return Decimal(str(current_epoch_seconds)) - Decimal(str(reference_epoch_seconds))


def coverage(available: int | float | Decimal | None, demand: int | float | Decimal | None) -> Decimal | None:
    if available is None or demand is None:
        return None
    demand_d = Decimal(str(demand))
    if demand_d <= 0:
        return None
    return Decimal(str(available)) / demand_d


def deficit(available: int | float | Decimal | None, demand: int | float | Decimal | None) -> Decimal | None:
    if available is None or demand is None:
        return None
    return max(Decimal(str(demand)) - Decimal(str(available)), Decimal("0"))


def dead_reckoning(current_value: int | float | Decimal | None, rate_per_unit: int | float | Decimal | None, horizon: int | float | Decimal | None) -> Decimal | None:
    if current_value is None or rate_per_unit is None or horizon is None:
        return None
    return Decimal(str(current_value)) + Decimal(str(rate_per_unit)) * Decimal(str(horizon))
