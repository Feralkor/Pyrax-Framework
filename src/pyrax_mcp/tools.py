from __future__ import annotations

from typing import Any, Literal

from pyrax.api import (
    assess_maturity,
    assess_readiness,
    get_catalog,
    get_solution_profile,
    validate_domain_pack,
    validate_solution_manifest,
)


def pyrax_validate_domain_pack(domain_pack: dict[str, Any]) -> dict[str, Any]:
    """Validate a Domain Pack without mutating files, state, or external systems."""
    return validate_domain_pack(domain_pack)


def pyrax_assess_readiness(domain_pack: dict[str, Any]) -> dict[str, Any]:
    """Assess production-readiness gates for a validated in-memory Domain Pack."""
    return assess_readiness(domain_pack)


def pyrax_assess_maturity(domain_pack: dict[str, Any]) -> dict[str, Any]:
    """Assess cumulative Pyrax maturity P0-P5 for an in-memory Domain Pack."""
    return assess_maturity(domain_pack)


def pyrax_validate_solution_manifest(solution_manifest: dict[str, Any]) -> dict[str, Any]:
    """Validate a Solution Manifest and its references to reusable Pyrax catalogs."""
    return validate_solution_manifest(solution_manifest)


def pyrax_get_solution_profile(profile_id: str | None = None) -> dict[str, Any]:
    """List Solution Profile identifiers or inspect one reusable profile by id."""
    return get_solution_profile(profile_id)


def pyrax_get_catalog(kind: Literal["blocks", "adapters", "ui"]) -> dict[str, Any]:
    """Read one closed Pyrax catalog: building blocks, adapters, or UI components."""
    return get_catalog(kind)
