from __future__ import annotations

from copy import deepcopy
from typing import Any, Literal

from pyrax import __version__
from pyrax.catalogs import ADAPTER_CATALOG, BUILDING_BLOCKS, SOLUTION_PROFILES, UI_COMPONENTS
from pyrax.catalogs import get_solution_profile as _get_solution_profile
from pyrax.composition import validate_solution_manifest as _validate_solution_manifest
from pyrax.maturity import assess_domain_maturity as _assess_domain_maturity
from pyrax.readiness import assess_domain_pack as _assess_domain_pack
from pyrax.validation import validate_domain_pack as _validate_domain_pack

API_VERSION = "0.1.0"
CatalogKind = Literal["blocks", "adapters", "ui"]


def _metadata() -> dict[str, str]:
    return {"framework_version": __version__, "api_version": API_VERSION}


def _invalid_document(message: str) -> dict[str, Any]:
    return {
        **_metadata(),
        "valid": False,
        "errors": [message],
    }


def validate_domain_pack(domain_pack: dict[str, Any]) -> dict[str, Any]:
    """Validate an in-memory Domain Pack against canonical Pyrax contracts."""
    if not isinstance(domain_pack, dict):
        return _invalid_document("Domain Pack must be a mapping/object")

    errors = _validate_domain_pack(domain_pack)
    return {
        **_metadata(),
        "valid": not errors,
        "errors": errors,
    }


def assess_readiness(domain_pack: dict[str, Any]) -> dict[str, Any]:
    """Assess production readiness after validating the supplied Domain Pack."""
    validation = validate_domain_pack(domain_pack)
    if not validation["valid"]:
        return {
            **_metadata(),
            "valid": False,
            "production_ready": False,
            "validation_errors": validation["errors"],
            "items": [],
        }

    report = _assess_domain_pack(domain_pack)
    return {
        **_metadata(),
        "valid": True,
        "production_ready": report.production_ready,
        "items": [
            {"area": item.area, "status": item.status.value, "reason": item.reason}
            for item in report.items
        ],
    }


def assess_maturity(domain_pack: dict[str, Any]) -> dict[str, Any]:
    """Assess cumulative Pyrax maturity P0-P5 for a valid Domain Pack."""
    validation = validate_domain_pack(domain_pack)
    if not validation["valid"]:
        return {
            **_metadata(),
            "valid": False,
            "validation_errors": validation["errors"],
            "level": None,
            "level_value": None,
            "reasons": [],
        }

    assessment = _assess_domain_maturity(domain_pack)
    return {
        **_metadata(),
        "valid": True,
        "level": assessment.level.name,
        "level_value": int(assessment.level),
        "reasons": list(assessment.reasons),
    }


def validate_solution_manifest(solution_manifest: dict[str, Any]) -> dict[str, Any]:
    """Validate an in-memory Solution Manifest and its catalog references."""
    if not isinstance(solution_manifest, dict):
        return {
            **_metadata(),
            "valid": False,
            "errors": ["Solution Manifest must be a mapping/object"],
        }

    errors = _validate_solution_manifest(solution_manifest)
    return {
        **_metadata(),
        "valid": not errors,
        "errors": errors,
    }


def get_solution_profile(profile_id: str | None = None) -> dict[str, Any]:
    """List available Solution Profiles or return one profile by identifier."""
    if profile_id is None:
        return {
            **_metadata(),
            "found": True,
            "profiles": sorted(SOLUTION_PROFILES),
        }

    try:
        profile = _get_solution_profile(profile_id)
    except KeyError:
        return {
            **_metadata(),
            "found": False,
            "profile_id": profile_id,
            "available_profiles": sorted(SOLUTION_PROFILES),
        }

    return {
        **_metadata(),
        "found": True,
        "profile_id": profile_id,
        "profile": profile,
    }


def get_catalog(kind: CatalogKind) -> dict[str, Any]:
    """Return one closed Pyrax catalog used during product composition."""
    catalogs: dict[str, dict[str, dict[str, Any]]] = {
        "blocks": BUILDING_BLOCKS,
        "adapters": ADAPTER_CATALOG,
        "ui": UI_COMPONENTS,
    }
    if kind not in catalogs:
        return {
            **_metadata(),
            "found": False,
            "kind": kind,
            "available_kinds": sorted(catalogs),
            "items": {},
        }

    return {
        **_metadata(),
        "found": True,
        "kind": kind,
        "items": deepcopy(catalogs[kind]),
    }
