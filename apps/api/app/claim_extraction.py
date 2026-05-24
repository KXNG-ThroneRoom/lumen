"""Honest placeholder claim extraction.

This module deliberately avoids pretending to perform production-grade semantic
extraction. It produces deterministic local objects and explicit limitation
metadata so downstream UI/API paths can be exercised without LLM calls.
"""

from __future__ import annotations

import re

from .models import Claim, ClaimStatus, ClaimType, Evidence, EvidenceType, ExtractionResult, Source

PLACEHOLDER_LIMITATIONS = [
    "Claim extraction is deterministic placeholder logic, not production-grade semantic extraction.",
    "The extractor does not verify real-world truth, infer missing context, or resolve ambiguity.",
    "Review by a human or a future audited extraction module is required before relying on extracted claims.",
]


def _slug(index: int) -> str:
    return f"claim-{index:03d}"


def classify_claim_type(text: str) -> ClaimType:
    lower = text.lower()
    if "unnamed" in lower or "anonymous" in lower:
        return ClaimType.ANONYMOUS_SOURCE
    if "caused" in lower or "cause" in lower or "because" in lower:
        return ClaimType.CAUSAL
    if "doubled" in lower or "%" in lower or "percent" in lower:
        return ClaimType.STATISTICAL
    if "image" in lower or "photo" in lower or "video" in lower:
        return ClaimType.MEDIA_AUTHENTICITY
    if "official" in lower or "agency" in lower:
        return ClaimType.INTERESTED_PARTY
    return ClaimType.FACTUAL


def extract_claims(text: str, *, source_document_id: str = "user-input") -> ExtractionResult:
    sentences = [part.strip() for part in re.split(r"(?<=[.!?])\s+", text.strip()) if part.strip()]
    if not sentences:
        sentences = [text.strip()]

    claims: list[Claim] = []
    for index, sentence in enumerate(sentences[:5], start=1):
        claim_type = classify_claim_type(sentence)
        reasons = ["placeholder extraction; confidence intentionally limited", "requires human review"]
        claims.append(
            Claim(
                id=_slug(index),
                source_document_id=source_document_id,
                raw_claim_text=sentence,
                normalized_claim=sentence.rstrip(".!?"),
                claim_type=claim_type,
                evidence_refs=[],
                contradiction_refs=[],
                confidence_score=0.2,
                confidence_reason=reasons,
                status=ClaimStatus.UNKNOWN,
                limitations=PLACEHOLDER_LIMITATIONS,
            )
        )

    return ExtractionResult(claims=claims, limitations=PLACEHOLDER_LIMITATIONS)


def sample_sources() -> list[Source]:
    return [
        Source(
            id="src-wire-a",
            name="Metro Wire Service",
            source_type="wire_report",
            wire_dependency="metro-wire-dispatch-001",
            independence_notes=["Wire dispatch is one evidence stream even if republished."],
        ),
        Source(
            id="src-local-a",
            name="Local Court Filing Archive",
            source_type="primary_document_repository",
            independence_notes=["Primary filing is separate from article commentary."],
        ),
    ]


def sample_evidence() -> list[Evidence]:
    return [
        Evidence(
            id="ev-primary-filing",
            source_id="src-local-a",
            evidence_type=EvidenceType.COURT_FILING,
            summary="Official filing states the regulation begins on July 1.",
            provenance="fixture:golden_case_gc003",
            proximity="primary",
            timestamp_quality="dated filing",
            primary=True,
            limitations=["Fixture evidence only; not live verification."],
        ),
        Evidence(
            id="ev-wire-report",
            source_id="src-wire-a",
            evidence_type=EvidenceType.WIRE_REPORT,
            summary="Wire report says an article claimed the regulation starts on June 1.",
            provenance="fixture:golden_case_gc003",
            proximity="secondary",
            timestamp_quality="reported timestamp",
            limitations=["Secondary report; article volume is not proof."],
        ),
    ]


def sample_claims() -> list[Claim]:
    return [
        Claim(
            id="claim-regulation-june",
            source_document_id="fixture-gc003",
            raw_claim_text="The regulation starts on June 1.",
            normalized_claim="regulation start date is June 1",
            claim_type=ClaimType.FACTUAL,
            evidence_refs=["ev-wire-report"],
            contradiction_refs=["contradiction-regulation-start-date"],
            confidence_score=0.45,
            confidence_reason=["fixture claim from article", "primary document conflicts with article"],
            status=ClaimStatus.CONTESTED,
            limitations=["Fixture sample; no live evidence retrieval."],
        ),
        Claim(
            id="claim-regulation-july",
            source_document_id="fixture-gc003",
            raw_claim_text="The official filing states the regulation starts on July 1.",
            normalized_claim="regulation start date is July 1",
            claim_type=ClaimType.FACTUAL,
            evidence_refs=["ev-primary-filing"],
            contradiction_refs=["contradiction-regulation-start-date"],
            confidence_score=0.65,
            confidence_reason=["primary document attached", "conflict remains visible rather than silently resolved"],
            status=ClaimStatus.CONTESTED,
            limitations=["Primary evidence boosts confidence but does not create a final truth verdict."],
        ),
    ]
