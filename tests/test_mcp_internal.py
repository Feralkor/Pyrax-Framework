import asyncio
from pathlib import Path

from mcp import Client

from pyrax.validation import load_document
from pyrax_mcp.server import mcp

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests" / "fixtures" / "minimal-domain-pack.yaml"
EXPECTED_TOOLS = {
    "pyrax_validate_domain_pack",
    "pyrax_assess_readiness",
    "pyrax_assess_maturity",
    "pyrax_validate_solution_manifest",
    "pyrax_get_solution_profile",
    "pyrax_get_catalog",
}


def test_mcp_lists_exact_internal_v01_tool_surface() -> None:
    async def scenario() -> None:
        async with Client(mcp) as client:
            result = await client.list_tools()
            tools = {tool.name: tool for tool in result.tools}

            assert set(tools) == EXPECTED_TOOLS
            for tool in tools.values():
                assert tool.annotations is not None
                assert tool.annotations.read_only_hint is True
                assert tool.annotations.open_world_hint is False

    asyncio.run(scenario())


def test_mcp_calls_public_api_with_structured_output() -> None:
    pack = load_document(FIXTURE)

    async def scenario() -> None:
        async with Client(mcp) as client:
            validation = await client.call_tool(
                "pyrax_validate_domain_pack", {"domain_pack": pack}
            )
            readiness = await client.call_tool(
                "pyrax_assess_readiness", {"domain_pack": pack}
            )
            catalog = await client.call_tool("pyrax_get_catalog", {"kind": "blocks"})

            assert validation.is_error is False
            assert validation.structured_content is not None
            assert validation.structured_content["valid"] is True
            assert validation.structured_content["framework_version"] == "0.5.0"

            assert readiness.is_error is False
            assert readiness.structured_content is not None
            assert readiness.structured_content["production_ready"] is True

            assert catalog.is_error is False
            assert catalog.structured_content is not None
            assert "dead-reckoning" in catalog.structured_content["items"]

    asyncio.run(scenario())


def test_mcp_returns_invalid_domain_pack_as_data_not_protocol_failure() -> None:
    async def scenario() -> None:
        async with Client(mcp) as client:
            result = await client.call_tool("pyrax_validate_domain_pack", {"domain_pack": {}})

            assert result.is_error is False
            assert result.structured_content is not None
            assert result.structured_content["valid"] is False
            assert result.structured_content["errors"]

    asyncio.run(scenario())
