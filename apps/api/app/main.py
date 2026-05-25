"""FastAPI routes for Lumen's deterministic local backend core."""

from __future__ import annotations

from datetime import datetime
from typing import cast

from fastapi import FastAPI

from .audit import append_audit_event, create_genesis_event, verify_audit_chain
from .briefing import generate_briefing
from .claim_extraction import extract_claims
from .contradiction import detect_contradictions
from .demo_fixtures import build_demo_fixture
from .models import AnalysisRequest, AnalysisResponse, Briefing, Claim, Contradiction, Evidence, EvidenceType, Source
from .scoring import apply_scoring
from .source_graph import build_source_graph

app = FastAPI(
    title="Lumen API",
    version="0.4.0",
    description="Deterministic local claim/evidence primitives. Not a final authority on reality.",
)


LIMITATIONS = [
    "Local deterministic MVP only; no real-time ingestion.",
    "No LLM calls, no paid APIs, and no production intelligence reliability claims.",
    "Confidence values expose method signals and uncertainty; they are not truth verdicts.",
]


def _with_audit_timestamp(ledger, timestamp: datetime | None):
    if timestamp is None:
        return ledger
    return [event.model_copy(update={"timestamp": timestamp}) for event in ledger]


def _assemble_analysis(
    *,
    topic: str,
    claims: list[Claim],
    evidence: list[Evidence],
    sources: list[Source],
    mode: str = "fixture_demo",
    fixture_timestamp: datetime | None = None,
) -> AnalysisResponse:
    graph = build_source_graph(sources)
    contradictions = cast(list[Contradiction], detect_contradictions(claims))

    evidence_by_claim: dict[str, list[Evidence]] = {claim.id: [] for claim in claims}
    for item in evidence:
        if item.claim_id and item.claim_id in evidence_by_claim:
            evidence_by_claim[item.claim_id].append(item)
    # If fixture evidence is not claim-bound, keep it available for the sample's contested claims.
    if evidence and not any(item.claim_id for item in evidence):
        for claim in claims:
            evidence_by_claim[claim.id] = evidence

    contradiction_counts = {claim.id: 0 for claim in claims}
    for contradiction in contradictions:
        for claim_id in contradiction.claim_ids:
            contradiction_counts[claim_id] = contradiction_counts.get(claim_id, 0) + 1

    scored_claims = [
        apply_scoring(claim, evidence_by_claim.get(claim.id, []), graph, contradiction_counts.get(claim.id, 0))
        for claim in claims
    ]

    ledger = [create_genesis_event()]
    append_audit_event(
        ledger,
        operation="claim_extracted",
        reason="Represent local input or fixture claims as inspectable claim objects.",
        input_payload={"topic": topic},
        output_payload=[claim.model_dump(mode="json") for claim in scored_claims],
    )
    append_audit_event(
        ledger,
        operation="source_graph_built",
        reason="Track wire/citation dependency and source independence notes.",
        input_payload=[source.model_dump(mode="json") for source in sources],
        output_payload=graph.model_dump(mode="json"),
    )
    append_audit_event(
        ledger,
        operation="contradiction_detected",
        reason="Expose deterministic fixture contradictions without resolving them as final truth.",
        input_payload=[claim.model_dump(mode="json") for claim in scored_claims],
        output_payload=[item.model_dump(mode="json") for item in contradictions],
    )
    score_event = append_audit_event(
        ledger,
        operation="score_assigned",
        reason="Apply documented deterministic confidence rules with visible reasons.",
        input_payload=[claim.id for claim in scored_claims],
        output_payload=[{"id": claim.id, "score": claim.confidence_score, "status": claim.status} for claim in scored_claims],
    )
    scored_claims = [claim.model_copy(update={"audit_reference": score_event.event_hash}) for claim in scored_claims]
    evidence = [item.model_copy(update={"audit_reference": score_event.event_hash}) for item in evidence]

    briefing = cast(
        Briefing,
        generate_briefing(
            topic=topic,
            claims=scored_claims,
            evidence=evidence,
            contradictions=contradictions,
            audit_reference=ledger[-1].event_hash,
        ),
    )
    if fixture_timestamp is not None:
        briefing = briefing.model_copy(update={"generated_at": fixture_timestamp})
    append_audit_event(
        ledger,
        operation="briefing_generated",
        reason="Generate deterministic briefing with limitations and audit reference.",
        input_payload=[claim.model_dump(mode="json") for claim in scored_claims],
        output_payload=briefing.model_dump(mode="json"),
    )

    ledger = _with_audit_timestamp(ledger, fixture_timestamp)
    verification = verify_audit_chain(ledger)
    return AnalysisResponse(
        mode=mode,  # type: ignore[arg-type]
        topic=topic,
        claims=scored_claims,
        evidence=evidence,
        sources=sources,
        source_graph=graph,
        contradictions=contradictions,
        briefing=briefing,
        audit_trail=ledger,
        audit_events=ledger,
        audit_verification=verification,
        limitations=LIMITATIONS,
        limitations_ref="LIMITATIONS.md",
    )


def build_sample_analysis() -> AnalysisResponse:
    fixture = build_demo_fixture()
    return _assemble_analysis(
        topic=fixture.topic,
        claims=fixture.claims,
        evidence=fixture.evidence,
        sources=fixture.sources,
        mode="fixture_demo",
        fixture_timestamp=fixture.fixture_timestamp,
    )


def _evidence_from_local_input(claims: list[Claim], source_id: str) -> tuple[list[Claim], list[Evidence]]:
    enriched_claims: list[Claim] = []
    evidence: list[Evidence] = []
    for claim in claims:
        evidence_id = f"ev-{claim.id}-local-input"
        evidence.append(
            Evidence(
                id=evidence_id,
                claim_id=claim.id,
                source_id=source_id,
                evidence_type=EvidenceType.NAMED_SOURCE,
                summary="User supplied local text containing this claim; no external retrieval or verification was performed.",
                quote=claim.raw_claim_text,
                provenance="local_user_input",
                proximity="source_text",
                timestamp_quality="not_applicable",
                limitations=["Local user input is evidence that the claim was supplied, not evidence that the claim is true."],
            )
        )
        enriched_claims.append(claim.model_copy(update={"evidence_refs": [evidence_id]}))
    return enriched_claims, evidence


@app.get("/health")
def health() -> dict[str, object]:
    return {
        "status": "ok",
        "service": "lumen-api",
        "version": "0.4.0",
        "deterministic": True,
        "doctrine": "methods over conclusions; more informed humans, not a new oracle",
        "limitations": LIMITATIONS,
    }


@app.get("/sample", response_model=AnalysisResponse)
def sample() -> AnalysisResponse:
    return build_sample_analysis()


@app.post("/analyze", response_model=AnalysisResponse)
def analyze(request: AnalysisRequest) -> AnalysisResponse:
    extraction = extract_claims(request.text, source_document_id="user-input")
    source = Source(
        id="src-user-input",
        name=request.source_name,
        source_type="user_supplied_text",
        independence_notes=["User supplied one local text input; independence is not established."],
    )
    claims, evidence = _evidence_from_local_input(extraction.claims, source.id)
    return _assemble_analysis(topic=request.topic, claims=claims, evidence=evidence, sources=[source], mode="local_input")


@app.get("/audit/verify")
def audit_verify() -> dict[str, object]:
    analysis = build_sample_analysis()
    return analysis.audit_verification.model_dump(mode="json")
