import pytest

from pyrax.decision_graph import DecisionEdge, DecisionGraph, DecisionNode
from pyrax.maturity import MaturityLevel, assess_maturity
from pyrax.ontology import OntologyEntity, OntologyRelationship, OperationalOntology
from pyrax.scenario import ScenarioEngine


def test_operational_ontology_rejects_unknown_relationship_targets() -> None:
    ontology = OperationalOntology()
    ontology.add_entity(OntologyEntity("order-1", "Order"))
    with pytest.raises(ValueError):
        ontology.add_relationship(OntologyRelationship("belongs_to", "order-1", "customer-1"))


def test_operational_ontology_neighbors() -> None:
    ontology = OperationalOntology()
    ontology.add_entity(OntologyEntity("customer-1", "Customer"))
    ontology.add_entity(OntologyEntity("order-1", "Order"))
    ontology.add_relationship(OntologyRelationship("creates", "customer-1", "order-1"))
    assert tuple(entity.entity_id for entity in ontology.neighbors("customer-1")) == ("order-1",)


def test_decision_graph_traces_downstream_and_rejects_cycles() -> None:
    graph = DecisionGraph()
    graph.add_node(DecisionNode("fact", "FACT", "Observed deficit"))
    graph.add_node(DecisionNode("signal", "SIGNAL", "Risk"))
    graph.add_node(DecisionNode("decision", "DECISION", "Review"))
    graph.add_edge(DecisionEdge("fact", "signal", "informs"))
    graph.add_edge(DecisionEdge("signal", "decision", "triggers"))
    assert [node.node_id for node in graph.downstream("fact")] == ["signal", "decision"]
    with pytest.raises(ValueError):
        graph.add_edge(DecisionEdge("decision", "fact", "feeds"))


def test_scenario_engine_does_not_mutate_baseline() -> None:
    baseline = {"available": 10, "demand": 15}
    result = ScenarioEngine.project(
        "replenish",
        baseline,
        {"add": 8},
        lambda state, assumptions: {**state, "available": state["available"] + assumptions["add"]},
    )
    assert baseline == {"available": 10, "demand": 15}
    assert result.projected["available"] == 18
    assert result.changed_fields == ("available",)


def test_maturity_is_contiguous_and_does_not_skip_missing_gates() -> None:
    assessment = assess_maturity(
        {
            "discovery": True,
            "sources": True,
            "semantics": True,
            "evidence": True,
            "state": True,
            "quality": True,
            "reconciliation": True,
            "signals": True,
            "decisions": True,
            "human_approval": True,
            "anticipation": False,
            "scenarios": True,
            "outcomes": True,
            "operational_memory": True,
            "feedback_loop": True,
        }
    )
    assert assessment.level == MaturityLevel.P3_ASSISTED_INTELLIGENCE
