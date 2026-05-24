"""Source graph primitives for source independence accounting."""

from __future__ import annotations

from collections import defaultdict

from .models import Source, SourceGraph


def build_source_graph(sources: list[Source]) -> SourceGraph:
    """Build a deterministic source-dependency summary.

    Sources sharing a wire dependency are counted as one stream. Sources that cite
    one another do not increase independence merely by repetition.
    """

    wire_dependencies = {source.id: source.wire_dependency for source in sources if source.wire_dependency}
    citation_dependencies = {source.id: source.citation_dependency for source in sources if source.citation_dependency}
    warnings: list[str] = []
    notes: list[str] = []

    wire_groups: dict[str, list[str]] = defaultdict(list)
    independent_keys: set[str] = set()

    for source in sources:
        if source.wire_dependency:
            wire_groups[source.wire_dependency].append(source.id)
            independent_keys.add(f"wire:{source.wire_dependency}")
        elif source.citation_dependency:
            independent_keys.add(f"citation-root:{','.join(sorted(source.citation_dependency))}")
        else:
            independent_keys.add(f"source:{source.id}")

        notes.extend(source.independence_notes)

    for wire, members in sorted(wire_groups.items()):
        if len(members) > 1:
            warnings.append(f"wire dependency: {len(members)} sources repeat {wire}; article volume is not proof")
        else:
            warnings.append(f"wire dependency: {members[0]} depends on {wire}")

    for source_id, deps in sorted(citation_dependencies.items()):
        warnings.append(f"citation dependency: {source_id} cites {', '.join(sorted(deps))}")

    if not sources:
        warnings.append("no sources supplied; source independence unknown")

    return SourceGraph(
        sources=sources,
        independent_evidence_streams=len(independent_keys),
        wire_dependencies=wire_dependencies,
        citation_dependencies=citation_dependencies,
        independence_notes=notes or ["Independence counted by dependency roots, not article count."],
        warnings=warnings,
    )


def summarize_independence(graph: SourceGraph) -> list[str]:
    lines = [f"independent_evidence_streams={graph.independent_evidence_streams}"]
    lines.extend(graph.warnings)
    lines.extend(graph.independence_notes)
    return lines
