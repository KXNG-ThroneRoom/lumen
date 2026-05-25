"""Controlled manual input normalization for the local Lumen demo boundary."""

from __future__ import annotations

from .audit import append_audit_event, create_genesis_event, hash_payload, verify_audit_chain
from .models import AnalysisResponse, ManualIngestRequest, ManualIngestResponse, RawDocument, SourceDocument

MANUAL_INPUT_LIMITATIONS = [
    "No URL fetching, live ingestion, crawling, scraping, RSS polling, LLM calls, paid APIs, telemetry, or production storage is performed.",
    "Manual input is an assertion container, not evidence that any article, source label, URL, or claim is true.",
    "Source metadata is user supplied and remains unverified unless separately supported by supplied evidence.",
    "The deterministic analysis path exposes claims and uncertainty for inspection; it does not decide what users must believe.",
]

SOURCE_DOCUMENT_LIMITATIONS = [
    "This source document is derived from user supplied manual input and must not be treated as verified.",
    "Analysis is allowed only as deterministic local inspection of the supplied text.",
    "Any submitted source URL is preserved only as an inert user-supplied string and was not fetched.",
]


def normalize_manual_text(raw_text: str) -> str:
    """Trim and normalize CRLF/CR line endings to LF for deterministic hashing."""

    return raw_text.replace("\r\n", "\n").replace("\r", "\n").strip()


def manual_input_metadata(request: ManualIngestRequest) -> dict[str, object]:
    return {
        "title": request.title,
        "source_name": request.source_name,
        "author": request.author,
        "published_at": request.published_at,
        "source_url": request.source_url,
        "source_url_fetched": False,
        "input_method": request.input_method,
        "metadata_role": "user_asserted_metadata_only",
    }


def manual_content_hash(*, normalized_text: str, metadata: dict[str, object]) -> str:
    stable_payload = {
        "normalized_text": normalized_text,
        "metadata": metadata,
        "input_boundary": "manual_text_assertion_container",
    }
    return f"sha256:{hash_payload(stable_payload)}"


def build_manual_ingest_response(
    request: ManualIngestRequest,
    *,
    analysis: AnalysisResponse | None = None,
) -> ManualIngestResponse:
    """Build a deterministic manual-ingest response without persistence or network calls."""

    normalized_text = normalize_manual_text(request.raw_text)
    metadata = manual_input_metadata(request)
    content_hash = manual_content_hash(normalized_text=normalized_text, metadata=metadata)
    short_hash = content_hash.removeprefix("sha256:")[:16]
    raw_document_id = f"manual-raw-{short_hash}"
    source_document_id = f"manual-source-{short_hash}"

    raw_document = RawDocument(
        raw_document_id=raw_document_id,
        input_method=request.input_method,
        state="normalized",
        submitted_text=request.raw_text,
        user_source_label=request.source_name,
        user_topic_label=request.title,
        source_url=request.source_url,
        source_url_fetched=False,
        content_hash=content_hash,
        limitations=MANUAL_INPUT_LIMITATIONS,
        audit_reference="audit-reference-pending",
    )
    source_document = SourceDocument(
        source_document_id=source_document_id,
        raw_document_id=raw_document_id,
        source_id=f"src-user-{short_hash}",
        state="ready_for_local_analysis",
        display_name=request.source_name,
        topic=request.title,
        text_for_analysis=normalized_text,
        limitations=SOURCE_DOCUMENT_LIMITATIONS,
        audit_reference="audit-reference-pending",
    )

    ledger = [
        create_genesis_event(
            metadata={
                "boundary": "manual_input",
                "persistence": "none",
                "network_calls": "none",
            }
        )
    ]
    audit_event = append_audit_event(
        ledger,
        operation="manual_ingested",
        reason="Normalize controlled manual text as a user assertion container without fetching, persistence, LLM calls, or truth adjudication.",
        input_payload={
            "input_method": request.input_method,
            "raw_text_length": len(request.raw_text),
            "metadata": metadata,
        },
        output_payload={
            "raw_document_id": raw_document_id,
            "source_document_id": source_document_id,
            "content_hash": content_hash,
            "normalized_text_length": len(normalized_text),
        },
        metadata={
            "content_hash": content_hash,
            "source_url_fetched": False,
            "llm_calls": False,
            "network_calls": False,
            "database_persistence": False,
        },
    )
    raw_document = raw_document.model_copy(update={"audit_reference": audit_event.event_hash})
    source_document = source_document.model_copy(update={"audit_reference": audit_event.event_hash})
    verification = verify_audit_chain(ledger)

    return ManualIngestResponse(
        raw_document=raw_document,
        source_document=source_document,
        content_hash=content_hash,
        metadata=metadata,
        limitations=MANUAL_INPUT_LIMITATIONS,
        audit_event=audit_event,
        audit_trail=ledger,
        audit_events=ledger,
        audit_verification=verification,
        analysis=analysis,
    )
