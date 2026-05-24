from __future__ import annotations

from app.models import Source
from app.source_graph import build_source_graph


def _dump(obj):
    if hasattr(obj, "model_dump"):
        return obj.model_dump(mode="json")
    return obj


def test_source_dependency_warning_counts_wire_repetition_as_one_stream():
    sources = [
        Source(
            id="outlet-a",
            name="Outlet A",
            source_type="publisher",
            wire_dependency="wire-dispatch-1",
            citation_dependency=[],
            independence_notes=["near-identical wire language"],
        ),
        Source(
            id="outlet-b",
            name="Outlet B",
            source_type="publisher",
            wire_dependency="wire-dispatch-1",
            citation_dependency=[],
            independence_notes=["near-identical wire language"],
        ),
    ]

    graph = _dump(build_source_graph(sources))

    assert graph["independent_evidence_streams"] == 1
    warnings = " ".join(graph["warnings"]).lower()
    assert "wire" in warnings
    assert "article volume" in warnings or "not proof" in warnings
    for src in graph["sources"]:
        assert "wire_dependency" in src
        assert "citation_dependency" in src
        assert "independence_notes" in src
