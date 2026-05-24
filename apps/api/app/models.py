"""Pydantic models for Lumen's deterministic MVP backend.

The models intentionally keep uncertainty and confidence reasons mandatory on
claim objects. A claim without a status and visible confidence reasoning is not a
valid Lumen analysis object.
"""

from __future__ import annotations

from datetime import datetime, timezone
from enum import Enum
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator


def utc_now() -> datetime:
    """Return a timezone-aware UTC timestamp."""

    return datetime.now(timezone.utc)


class ClaimStatus(str, Enum):
    CONFIRMED = "confirmed"
    STRONGLY_CORROBORATED = "strongly_corroborated"
    PROBABLE = "probable"
    PLAUSIBLE = "plausible"
    CONTESTED = "contested"
    UNSUPPORTED = "unsupported"
    CONTRADICTED = "contradicted"
    NARRATIVE_ONLY = "narrative_only"
    UNKNOWN = "unknown"
    UNRESOLVED = "unresolved"


class ClaimType(str, Enum):
    FACTUAL = "factual_claim"
    CAUSAL = "causal_claim"
    LEGAL = "legal_claim"
    STATISTICAL = "statistical_claim"
    ATTRIBUTION = "attribution_claim"
    QUOTE = "quote_claim"
    PREDICTION = "prediction"
    SPECULATION = "speculation"
    MORAL_FRAMING = "moral_framing"
    MEDIA_AUTHENTICITY = "image_video_authenticity_claim"
    ANONYMOUS_SOURCE = "anonymous_source_claim"
    EXPERT_INTERPRETATION = "expert_interpretation"
    INTERESTED_PARTY = "interested_party_claim"


class EvidenceType(str, Enum):
    PRIMARY_DOCUMENT = "primary_document"
    OFFICIAL_DATASET = "official_dataset"
    COURT_FILING = "court_filing"
    FULL_TRANSCRIPT = "full_transcript"
    RAW_VIDEO = "raw_video"
    RAW_IMAGE = "raw_image"
    GEOLOCATION = "geolocation_evidence"
    NAMED_SOURCE = "named_on_record_source"
    LOCAL_REPORTING = "local_direct_reporting"
    WIRE_REPORT = "wire_report"
    ANONYMOUS_SOURCE = "anonymous_source"
    EXPERT_INTERPRETATION = "expert_interpretation"
    SOCIAL_MEDIA = "social_media_post"
    COMMENTARY = "opinion_commentary"


class Source(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: str
    name: str
    source_type: str
    url: str | None = None
    author: str | None = None
    publisher: str | None = None
    owner: str | None = None
    country: str | None = None
    language: str | None = None
    funding: str | None = None
    wire_dependency: str | None = None
    citation_dependency: list[str] = Field(default_factory=list)
    independence_notes: list[str] = Field(default_factory=list)
    reliability_notes: list[str] = Field(default_factory=list)
    anonymous: bool = False
    interested_party: bool = False


class Evidence(BaseModel):
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def accept_legacy_text(cls, data: Any) -> Any:
        if isinstance(data, dict) and "text" in data and "summary" not in data:
            data = dict(data)
            data["summary"] = data.pop("text")
        return data

    id: str
    claim_id: str | None = None
    source_id: str | None = None
    evidence_type: EvidenceType
    summary: str
    url: str | None = None
    quote: str | None = None
    provenance: str = "fixture"
    proximity: str = "unknown"
    timestamp_quality: str = "unknown"
    primary: bool = False
    anonymous: bool = False
    limitations: list[str] = Field(default_factory=list)


class ConfidenceBreakdown(BaseModel):
    model_config = ConfigDict(extra="forbid")

    score: float = Field(ge=0.0, le=1.0)
    status: ClaimStatus
    reasons: list[str] = Field(min_length=1)
    rule_references: list[str] = Field(default_factory=list)
    caps_applied: list[str] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)


class Claim(BaseModel):
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def accept_legacy_claim_fields(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data
        data = dict(data)
        legacy_text = data.pop("text", None)
        if legacy_text is not None:
            data.setdefault("raw_claim_text", legacy_text)
            data.setdefault("normalized_claim", str(legacy_text).rstrip(".!?"))
        if "confidence" in data and "confidence_score" not in data:
            data["confidence_score"] = data.pop("confidence")
        if "confidence_reasons" in data and "confidence_reason" not in data:
            data["confidence_reason"] = data.pop("confidence_reasons")
        return data

    id: str
    raw_claim_text: str
    normalized_claim: str
    claim_type: ClaimType
    source_document_id: str | None = None
    actors: list[str] = Field(default_factory=list)
    targets: list[str] = Field(default_factory=list)
    location: str | None = None
    time_range: str | None = None
    evidence_refs: list[str] = Field(default_factory=list)
    contradiction_refs: list[str] = Field(default_factory=list)
    confidence_score: float = Field(ge=0.0, le=1.0)
    confidence_reason: list[str] = Field(min_length=1)
    status: ClaimStatus
    limitations: list[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=utc_now)


class Contradiction(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: str
    claim_ids: list[str] = Field(min_length=1)
    contradiction_type: str
    summary: str
    status: Literal["fixture_detected", "not_resolved"] = "fixture_detected"
    limitations: list[str] = Field(default_factory=lambda: ["Fixture/rule-based contradiction only; no semantic intelligence is claimed."])


class SourceGraph(BaseModel):
    model_config = ConfigDict(extra="forbid")

    sources: list[Source]
    independent_evidence_streams: int = Field(ge=0)
    wire_dependencies: dict[str, str] = Field(default_factory=dict)
    citation_dependencies: dict[str, list[str]] = Field(default_factory=dict)
    independence_notes: list[str] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)


class AuditEvent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    event_id: str
    timestamp: datetime = Field(default_factory=utc_now)
    actor_type: str = "system"
    actor_id: str = "lumen.local.deterministic"
    operation: str
    reason: str
    input_hash: str
    output_hash: str
    previous_event_hash: str
    event_hash: str
    rule_version: str = "lumen.rules.v0.2"
    model_version: str = "none"
    prompt_hash: str = "none"
    code_version: str = "local"
    metadata: dict[str, Any] = Field(default_factory=dict)


class AuditVerification(BaseModel):
    model_config = ConfigDict(extra="forbid")

    valid: bool
    event_count: int
    errors: list[str] = Field(default_factory=list)
    genesis_event_hash: str | None = None
    latest_event_hash: str | None = None


class Briefing(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: str
    topic: str
    bottom_line: str
    confidence: ConfidenceBreakdown
    key_claims: list[Claim]
    evidence: list[Evidence]
    contradictions: list[Contradiction]
    missing_information: list[str]
    narrative_frames: list[str]
    watch_indicators: list[str]
    unresolved_questions: list[str]
    limitations: list[str] = Field(min_length=1)
    audit_reference: str
    generated_at: datetime = Field(default_factory=utc_now)


class ExtractionResult(BaseModel):
    model_config = ConfigDict(extra="forbid")

    claims: list[Claim]
    limitations: list[str] = Field(min_length=1)
    method: str = "deterministic_placeholder"
    capability_claim: str = "Placeholder extraction only; not production-grade semantic extraction."


class AnalysisRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    text: str = Field(min_length=1)
    topic: str = "User supplied text"
    source_name: str = "user_supplied"


class AnalysisResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    topic: str
    claims: list[Claim]
    evidence: list[Evidence]
    sources: list[Source]
    source_graph: SourceGraph
    contradictions: list[Contradiction]
    briefing: Briefing
    audit_events: list[AuditEvent]
    audit_verification: AuditVerification
    limitations: list[str] = Field(min_length=1)
