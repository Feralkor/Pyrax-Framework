from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class DecisionNode:
    node_id: str
    node_type: str
    label: str


@dataclass(frozen=True)
class DecisionEdge:
    source: str
    target: str
    relation: str


class DecisionGraph:
    """Directed graph for tracing how facts/signals/decisions/outcomes depend on one another."""

    def __init__(self) -> None:
        self._nodes: dict[str, DecisionNode] = {}
        self._edges: list[DecisionEdge] = []

    def add_node(self, node: DecisionNode) -> None:
        if node.node_id in self._nodes:
            raise ValueError(f"Duplicate decision node: {node.node_id}")
        self._nodes[node.node_id] = node

    def add_edge(self, edge: DecisionEdge) -> None:
        if edge.source not in self._nodes or edge.target not in self._nodes:
            raise ValueError("Decision edge must reference existing nodes")
        if edge.source == edge.target:
            raise ValueError("Decision graph self-loops are not allowed")
        self._edges.append(edge)
        if self._has_cycle():
            self._edges.pop()
            raise ValueError("Decision graph cycle detected")

    def downstream(self, node_id: str) -> tuple[DecisionNode, ...]:
        visited: set[str] = set()
        queue = [node_id]
        ordered: list[DecisionNode] = []
        while queue:
            current = queue.pop(0)
            for edge in self._edges:
                if edge.source == current and edge.target not in visited:
                    visited.add(edge.target)
                    ordered.append(self._nodes[edge.target])
                    queue.append(edge.target)
        return tuple(ordered)

    def _has_cycle(self) -> bool:
        adjacency: dict[str, list[str]] = {node_id: [] for node_id in self._nodes}
        for edge in self._edges:
            adjacency[edge.source].append(edge.target)
        visiting: set[str] = set()
        visited: set[str] = set()

        def visit(node_id: str) -> bool:
            if node_id in visiting:
                return True
            if node_id in visited:
                return False
            visiting.add(node_id)
            for target in adjacency[node_id]:
                if visit(target):
                    return True
            visiting.remove(node_id)
            visited.add(node_id)
            return False

        return any(visit(node_id) for node_id in self._nodes)
