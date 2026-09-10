from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class OntologyEntity:
    entity_id: str
    entity_type: str
    attributes: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class OntologyRelationship:
    relationship_type: str
    source_id: str
    target_id: str
    attributes: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class OntologyEvent:
    event_type: str
    subject_id: str
    observed_at: str | None = None
    attributes: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class OntologyAction:
    action_id: str
    subject_id: str
    action_type: str
    human_approval_required: bool = True
    constraints: tuple[str, ...] = ()


class OperationalOntology:
    """Small, domain-neutral graph of operational objects, relations, events and actions."""

    def __init__(self) -> None:
        self._entities: dict[str, OntologyEntity] = {}
        self._relationships: list[OntologyRelationship] = []
        self._events: list[OntologyEvent] = []
        self._actions: list[OntologyAction] = []

    def add_entity(self, entity: OntologyEntity) -> None:
        if entity.entity_id in self._entities:
            raise ValueError(f"Duplicate ontology entity: {entity.entity_id}")
        self._entities[entity.entity_id] = entity

    def add_relationship(self, relationship: OntologyRelationship) -> None:
        missing = [
            entity_id
            for entity_id in (relationship.source_id, relationship.target_id)
            if entity_id not in self._entities
        ]
        if missing:
            raise ValueError(f"Relationship references unknown entities: {', '.join(missing)}")
        self._relationships.append(relationship)

    def add_event(self, event: OntologyEvent) -> None:
        if event.subject_id not in self._entities:
            raise ValueError(f"Event references unknown entity: {event.subject_id}")
        self._events.append(event)

    def add_action(self, action: OntologyAction) -> None:
        if action.subject_id not in self._entities:
            raise ValueError(f"Action references unknown entity: {action.subject_id}")
        self._actions.append(action)

    def entity(self, entity_id: str) -> OntologyEntity | None:
        return self._entities.get(entity_id)

    def neighbors(self, entity_id: str) -> tuple[OntologyEntity, ...]:
        ids: list[str] = []
        for relationship in self._relationships:
            if relationship.source_id == entity_id:
                ids.append(relationship.target_id)
            elif relationship.target_id == entity_id:
                ids.append(relationship.source_id)
        return tuple(self._entities[item] for item in ids)

    @property
    def entities(self) -> tuple[OntologyEntity, ...]:
        return tuple(self._entities.values())

    @property
    def relationships(self) -> tuple[OntologyRelationship, ...]:
        return tuple(self._relationships)
