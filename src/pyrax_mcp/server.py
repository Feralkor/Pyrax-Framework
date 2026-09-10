from __future__ import annotations

from typing import Any, Literal

from mcp.server import MCPServer
from mcp.types import ToolAnnotations

from pyrax_mcp.tools import (
    pyrax_assess_maturity,
    pyrax_assess_readiness,
    pyrax_get_catalog,
    pyrax_get_solution_profile,
    pyrax_validate_domain_pack,
    pyrax_validate_solution_manifest,
)

mcp = MCPServer("Pyrax MCP Internal")
READ_ONLY = ToolAnnotations(read_only_hint=True, open_world_hint=False)


@mcp.tool(
    name="pyrax_validate_domain_pack",
    title="Validate Pyrax Domain Pack",
    annotations=READ_ONLY,
)
def validate_domain_pack_tool(domain_pack: dict[str, Any]) -> dict[str, Any]:
    """Validate a Domain Pack against canonical Pyrax schema and integrity rules."""
    return pyrax_validate_domain_pack(domain_pack)


@mcp.tool(
    name="pyrax_assess_readiness",
    title="Assess Pyrax Readiness",
    annotations=READ_ONLY,
)
def assess_readiness_tool(domain_pack: dict[str, Any]) -> dict[str, Any]:
    """Assess production readiness without changing the supplied Domain Pack."""
    return pyrax_assess_readiness(domain_pack)


@mcp.tool(
    name="pyrax_assess_maturity",
    title="Assess Pyrax Maturity",
    annotations=READ_ONLY,
)
def assess_maturity_tool(domain_pack: dict[str, Any]) -> dict[str, Any]:
    """Assess cumulative Pyrax maturity P0-P5 for a valid Domain Pack."""
    return pyrax_assess_maturity(domain_pack)


@mcp.tool(
    name="pyrax_validate_solution_manifest",
    title="Validate Pyrax Solution Manifest",
    annotations=READ_ONLY,
)
def validate_solution_manifest_tool(solution_manifest: dict[str, Any]) -> dict[str, Any]:
    """Validate a Solution Manifest and its references to Pyrax reusable catalogs."""
    return pyrax_validate_solution_manifest(solution_manifest)


@mcp.tool(
    name="pyrax_get_solution_profile",
    title="Get Pyrax Solution Profile",
    annotations=READ_ONLY,
)
def get_solution_profile_tool(profile_id: str | None = None) -> dict[str, Any]:
    """List available Solution Profiles or return one reusable profile by identifier."""
    return pyrax_get_solution_profile(profile_id)


@mcp.tool(
    name="pyrax_get_catalog",
    title="Get Pyrax Catalog",
    annotations=READ_ONLY,
)
def get_catalog_tool(kind: Literal["blocks", "adapters", "ui"]) -> dict[str, Any]:
    """Return a closed Pyrax catalog for building blocks, adapters, or UI components."""
    return pyrax_get_catalog(kind)


def main() -> None:
    """Run the internal Pyrax MCP server using the SDK's default stdio transport."""
    mcp.run()


if __name__ == "__main__":
    main()
