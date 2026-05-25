# Controlled Input Layer

Version: v0.6-controlled-manual-input

## Purpose

The controlled input layer defines how Lumen accepts user-supplied local material without becoming a live ingestion system.

v0.6 accepts manual/local input as an assertion container. It preserves what the user supplied, records deterministic transformations, and passes bounded SourceDocument objects to the existing claim/evidence/briefing pipeline. It does not fetch, crawl, scrape, enrich, verify, or settle the real-world truth of the submitted material.

## Non-negotiable boundary

Controlled input is not live ingestion.

The layer must not:

- fetch submitted URLs;
- crawl pages;
- poll RSS or feeds;
- scrape websites;
- discover sources automatically;
- call LLMs or paid APIs;
- require secrets, accounts, telemetry, or auth;
- write production databases, object stores, vector stores, or queues;
- treat source labels or article text as verified facts.

If a user submits a URL as part of the text or metadata, Lumen stores it as user-supplied text only. The system must not dereference it in v0.6.

## Core objects

### RawDocument

RawDocument is the preserved local submission envelope. It represents what arrived at the controlled boundary, not what is true.

Required conceptual fields:

| Field | Meaning |
| --- | --- |
| `raw_document_id` | Local deterministic identifier for this submission. |
| `input_method` | Canonical value is `manual_text`; URL, RSS, crawl, and file-input modes are deferred in v0.6. |
| `submitted_text` | User-supplied text content. |
| `user_source_label` | Optional user-supplied source label; assertion only. |
| `user_topic_label` | Optional user-supplied topic label; display/context only. |
| `source_url` | Optional string if the user provided one; never fetched in v0.6. |
| `source_url_fetched` | Always `false` in v0.6. |
| `received_at` | Local receipt timestamp. |
| `content_hash` | Hash of submitted local content for local audit traceability. |
| `limitations` | Required limitations for manual/local input. |
| `audit_reference` | Audit event for receiving/preserving the submission. |

RawDocument lifecycle states:

1. `received` — payload crossed the local manual boundary.
2. `normalized` — deterministic cleanup/preparation completed.
3. `rejected` — payload failed local validation such as empty text.
4. `superseded` — a later manual submission replaced it in a demo flow.

RawDocument must not contain claims of source truth, source reachability, network retrieval, or publication authenticity.

### SourceDocument

SourceDocument is the normalized analysis container derived from a RawDocument. It is what downstream claim extraction and analysis use.

Required conceptual fields:

| Field | Meaning |
| --- | --- |
| `source_document_id` | Local deterministic identifier used by claims. |
| `raw_document_id` | Link back to the preserved RawDocument. |
| `source_id` | Local source object identifier. |
| `display_name` | Human-readable label derived from user input or fallback. |
| `topic` | Topic/context label, not a conclusion. |
| `text_for_analysis` | Deterministically normalized local text. |
| `source_assertion_type` | `user_supplied`; never `verified_source` in v0.6. |
| `analysis_allowed` | Whether placeholder/local extraction may run. |
| `limitations` | Required limitations carried forward. |
| `audit_reference` | Audit event for normalization/derivation. |

SourceDocument lifecycle states:

1. `derived` — created from a valid RawDocument.
2. `ready_for_local_analysis` — eligible for deterministic placeholder extraction.
3. `analysis_completed` — downstream analysis response was produced.
4. `analysis_failed` — local deterministic analysis failed with visible error/limitation.
5. `discarded` — excluded from a demo run without deleting the original RawDocument evidence.

SourceDocument may support claims such as "this text was supplied for inspection". It must not support claims such as "this article is accurate" or "this source was independently verified" unless future scoped evidence explicitly supports that.

## Processing lifecycle

The v0.6 local lifecycle is:

1. User manually submits local text.
2. Lumen validates minimum local shape: non-empty text and the canonical manual input method.
3. Lumen creates a RawDocument and records an audit event.
4. Lumen deterministically normalizes the RawDocument into a SourceDocument.
5. Lumen records a normalization audit event.
6. Placeholder/local extraction may create claim objects from the SourceDocument.
7. Existing scoring, source-graph, contradiction, briefing, and audit verification logic runs with visible limitations.
8. Output remains claim-level and uncertainty-preserving.

No step may call a network, fetch a URL, enrich metadata, call an external model, or persist to production infrastructure in the v0.6 default path.

## API relationship

`POST /ingest/manual` owns steps 1–5. It returns document lifecycle metadata and limitations.

`POST /analyze` may continue to provide a local analysis shortcut, but it should be documented as equivalent to accepting a manual text container and immediately running local analysis. It is not live ingestion.

`GET /sample` remains the canonical fixture-backed demo path.

`GET /audit/verify` verifies local method-trace consistency. It does not verify the real-world truth of a RawDocument, SourceDocument, article, source, or claim.

## Audit requirements

The controlled input layer must record audit events for:

- manual payload received;
- local validation accepted or rejected;
- RawDocument normalized into SourceDocument;
- placeholder claims extracted;
- analysis response assembled;
- briefing generated;
- audit chain verified.

Audit hashes and references are developer/auditor artifacts. The simplified public UI should explain that checks were recorded without showing raw hashes, IDs, machine labels, or dense provenance language.

## Failure and rejection states

A v0.6 implementation should reject or visibly limit:

- empty input;
- unsupported input methods;
- attempts to submit live URL ingestion as if it were in scope;
- binary or file-based content; file parsing remains deferred until separately scoped;
- text that exceeds the local demo limit, if a limit is set;
- malformed metadata.

Rejection should be explicit, local, and non-destructive. Do not delete submitted local artifacts unless separately authorized.

## Future migration guard

Future URL/RSS/live ingestion may reuse the document vocabulary only after a new scope document authorizes it. Until then:

- RawDocument means local manual text submission;
- SourceDocument means local analysis container;
- submitted URL strings are metadata, not fetched resources;
- source labels are assertions, not verified facts;
- documents remain containers of claims, not facts.
