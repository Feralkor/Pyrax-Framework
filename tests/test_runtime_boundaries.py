from pyrax.runtime import EventCollector, OperationalMemory, RuntimeEvent


def test_runtime_events_are_filterable_by_run() -> None:
    collector = EventCollector()
    collector.emit(RuntimeEvent("SOURCE_FETCH", "run-1", "2026-09-10T12:00:00Z", "source", "PASS"))
    collector.emit(RuntimeEvent("SOURCE_FETCH", "run-2", "2026-09-10T12:01:00Z", "source", "PASS"))
    assert len(collector.by_run("run-1")) == 1
    assert collector.by_run("run-1")[0].run_id == "run-1"


def test_operational_memory_preserves_decision_outcomes() -> None:
    memory = OperationalMemory()
    memory.append({"decision_id": "review-capacity", "outcome": "accepted"})
    memory.append({"decision_id": "other", "outcome": "rejected"})
    assert memory.by_decision("review-capacity") == [
        {"decision_id": "review-capacity", "outcome": "accepted"}
    ]
