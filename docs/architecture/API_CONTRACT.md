# Lumen API Contract

Version: v0.6-controlled-manual-input

## Purpose

This document defines the stable local API contract for the Lumen controlled demo path and the v0.6 controlled manual/local input layer.

The contract exists to keep backend, frontend, evaluation, and audit work aligned without expanding scope. It is a deterministic, fixture-backed/manual-local contract for local MVP demonstration only. It is not a live URL/RSS/crawl ingestion contract, not a production intelligence API, and not a claim that Lumen can determine final truth.

Lumen exposes methods, evidence, claims, uncertainty, source context, and audit references so humans can reason with more context. v0.6 adds a document lifecycle for controlled manual/local input only; it does not introduce live ingestion or a new intelligence layer.

## v0.6 scope note

The implemented analysis response schema remains `lumen.analysis.v0.3` unless the backend, frontend, tests, and docs intentionally move together. v0.6 is a controlled manual/local input scope, not a live-ingestion or production-intelligence release.

For v0.6:

- `/sample` remains the canonical controlled fixture path.
- `/analyze` remains the existing manual local-text analysis shortcut.
- `POST /ingest/manual` is the controlled document-container boundary for manual/local input.
- Manual input is an assertion container, not truth. Articles are containers of claims, not facts.
- Submitted URLs are inert strings unless a future scope explicitly authorizes retrieval.
- The default path must not use URL fetching, RSS, crawling, scraping, live feeds, paid APIs, LLM calls, telemetry, accounts, hidden scoring, production databases, or external network dependencies.
- Audit verification demonstrates method-trace consistency, not real-world correctness.
- Confidence values and statuses are claim-level method signals, not truth verdicts.

## Runtime guarantees

The v0.3 demo API must remain:

- local-first;
- deterministic for controlled fixtures and local text;
- open-source and inspectable;
- free of paid API dependencies;
- free of LLM calls in the default path;
- free of telemetry and hidden network calls;
- limited to controlled fixture/demo data or manually submitted local text. File parsing remains deferred unless a later scope explicitly adds it.
- unable to fetch or enrich submitted URL strings in v0.6.

## Required routes

### GET /health

Returns service status and method-boundary metadata.

Current response fields:

```json
{
  "status": "ok",
  "service": "lumen-api",
  "version": "0.4.0",
  "deterministic": true,
  "doctrine": "methods over conclusions; more informed humans, not a new oracle",
  "limitations": ["..."]
}
```

Rules:

- `version` reports the backend service/demo release line and must match the implemented `/health` response for the v0.4 demo path.
- `version` is intentionally separate from the analysis response `schema_version`; `lumen.analysis.v0.3` may remain valid while the response envelope is unchanged.
- `deterministic` must be true for the local demo path.
- Health output must not include production-readiness, live coverage, or final-authority claims.
- Limitations must remain visible even on health/status endpoints.

### GET /sample

Returns the canonical fixture-backed demo analysis.

Use this route for frontend static fixtures, screenshots, dashboard verification, and contract tests.

Required behavior:

- no request body;
- no external network calls;
- no LLM calls;
- returns the same `AnalysisResponse` schema as `POST /analyze`;
- uses `mode: "fixture_demo"`;
- returns controlled fixture data only;
- includes claims, evidence, sources, source graph, contradictions, briefing, audit trail, audit verification, limitations, confidence reasons, and fixture/deferred labels where applicable.

### POST /analyze

Returns deterministic local analysis over manually supplied text.

Request body (`AnalysisRequest`):

```json
{
  "text": "A local text snippet to inspect.",
  "topic": "Optional topic label",
  "source_name": "Optional source label"
}
```

Allowed request fields for v0.3:

| Field | Type | Required | Notes |
| --- | --- | --- | --- |
| `text` | string | yes | Local text only. No URL fetching in v0.3. |
| `topic` | string | no | Display label, not an analytical conclusion. Defaults to `User supplied text`. |
| `source_name` | string | no | User-provided source label; must not be treated as evidence by itself. Defaults to `user_supplied`. |

Required behavior:

- no live URL ingestion;
- no external network calls;
- no LLM calls;
- placeholder/deterministic extraction must disclose its limitation;
- returns the same `AnalysisResponse` envelope as `/sample`;
- uses `mode: "local_input"`;
- every displayed analytical object must link to status/reason/evidence/audit/limitations as applicable.

### POST /ingest/manual

Creates controlled local document containers from manually supplied input. This route is the v0.6 boundary for RawDocument and SourceDocument lifecycle creation. It is not a URL-fetching or live-ingestion route.

Request body (`ManualIngestRequest`, conceptual v0.6 contract):

```json
{
  "input_method": "manual_text",
  "raw_text": "A local article, excerpt, note, or claim container supplied by the user.",
  "title": "Optional topic label",
  "source_name": "Optional user-supplied source label",
  "source_url": "https://example.invalid/user-supplied-string-only"
}
```

Allowed request fields for v0.6:

| Field | Type | Required | Notes |
| --- | --- | --- | --- |
| `title` | string | no | Display/context label, not an analytical conclusion. Defaults to `Manual input`. |
| `source_name` | string | no | User-provided source label; assertion only. |
| `author` | string/null | no | User-provided metadata only; not verified. |
| `published_at` | string/null | no | User-provided metadata only; not verified. |
| `source_url` | string/null | no | Optional user-supplied string. Must not be fetched, validated over the network, or treated as inspected content. |
| `raw_text` | string | yes | Local supplied content only. It must not be fetched from the network by Lumen. |
| `input_method` | string | no | Canonical value is `manual_text`. URL, RSS, crawl, and file-input modes are unsupported in v0.6. |

No request aliases are accepted in v0.6. Legacy field names are intentionally rejected so the contract hardens around one vocabulary before external clients exist.

Response body (`ManualIngestResponse`, conceptual v0.6 contract):

```json
{
  "schema_version": "lumen.ingest.manual.v0.6",
  "mode": "manual_input",
  "raw_document": {
    "raw_document_id": "raw-local-001",
    "input_method": "manual_text",
    "state": "normalized",
    "content_hash": "sha256:...",
    "user_source_label": "user supplied",
    "user_topic_label": "optional topic",
    "source_url": null,
    "source_url_fetched": false,
    "limitations": ["Manual input is an assertion container, not proof of truth."],
    "audit_reference": "sha256:..."
  },
  "source_document": {
    "source_document_id": "doc-local-001",
    "raw_document_id": "raw-local-001",
    "state": "ready_for_local_analysis",
    "source_assertion_type": "user_supplied",
    "analysis_allowed": true,
    "limitations": ["Source labels are user assertions unless backed by supplied evidence."],
    "audit_reference": "sha256:..."
  },
  "limitations": ["No URL fetching, RSS polling, crawling, scraping, LLM calls, paid APIs, telemetry, or production storage."],
  "limitations_ref": "LIMITATIONS.md"
}
```

Required behavior:

- create a RawDocument as the preserved local submission envelope;
- create a SourceDocument as the normalized local analysis container;
- record audit references for receipt and normalization;
- reject empty or unsupported input with visible limitations;
- never fetch `source_url` or any URL-looking string in `raw_text`;
- never call external networks, paid APIs, LLMs, telemetry, accounts, queues, or production databases in the default path;
- never present document creation as source verification or claim truth.

Compatibility note: current `POST /analyze` behavior may be understood as a shortcut that receives manual text and immediately runs local analysis. v0.6 separates the conceptual document lifecycle from analysis so future code can add the boundary without implying live ingestion.

### GET /audit/verify

Returns audit-chain verification for the current sample/demo ledger.

Current response shape is `AuditVerification`:

```json
{
  "valid": true,
  "event_count": 0,
  "errors": [],
  "genesis_event_hash": "sha256:...",
  "latest_event_hash": "sha256:..."
}
```

Rules:

- Verification proves transformation trace consistency, not real-world correctness.
- If verification fails, frontend must display an audit warning and must not present affected analysis as dependable.

## Shared response envelope

`GET /sample` and `POST /analyze` return the same top-level `AnalysisResponse` object shape.

Required top-level fields:

```json
{
  "schema_version": "lumen.analysis.v0.3",
  "mode": "fixture_demo",
  "topic": "Fixture: regulation start-date contradiction",
  "claims": [],
  "evidence": [],
  "sources": [],
  "source_graph": {},
  "contradictions": [],
  "briefing": {},
  "audit_trail": [],
  "audit_events": [],
  "audit_verification": {},
  "limitations": [],
  "limitations_ref": "LIMITATIONS.md"
}
```

Top-level fields are intentionally limited to the implemented Pydantic model. The v0.3 envelope does not include `analysis_id`, `rule_version`, `input_document_ids`, `source_dependency_edges`, `narrative_frames`, or `confidence_assessments` as top-level fields.

Field rules:

- `schema_version` must change when breaking response changes are introduced.
- `mode` must be one of `fixture_demo` or `local_input` for v0.3.
- `limitations_ref` is required even when `limitations` contains inline strings.
- `audit_trail` and `audit_events` currently both expose the deterministic audit ledger for compatibility with UI/audit consumers.
- Claims, evidence, and briefing must carry direct audit references so the UI can render traceability without inferring it from the ledger.
- If a module is stubbed/deferred, return a labeled object or empty array plus visible limitation; do not imply completed capability.

## Object contracts

### RawDocument

Conceptual v0.6 fields for the controlled input boundary:

```json
{
  "raw_document_id": "raw-local-001",
  "input_method": "manual_text",
  "state": "normalized",
  "submitted_text": "User supplied local text...",
  "user_source_label": "Optional source label",
  "user_topic_label": "Optional topic label",
  "source_url": null,
  "source_url_fetched": false,
  "received_at": "2026-01-01T00:00:00Z",
  "content_hash": "sha256:...",
  "limitations": ["Manual input is an assertion container, not truth."],
  "audit_reference": "sha256:..."
}
```

Allowed states for v0.6: `received`, `normalized`, `rejected`, `superseded`.

RawDocument records what was supplied locally. It must not claim the source exists, the article is accurate, or any URL was inspected.

### SourceDocument

Conceptual v0.6 fields for the normalized analysis container:

```json
{
  "source_document_id": "doc-local-001",
  "raw_document_id": "raw-local-001",
  "source_id": "src-user-input",
  "state": "ready_for_local_analysis",
  "display_name": "user supplied",
  "topic": "User supplied text",
  "text_for_analysis": "Normalized local text...",
  "source_assertion_type": "user_supplied",
  "analysis_allowed": true,
  "limitations": ["Source labels are user assertions unless backed by supplied evidence."],
  "audit_reference": "sha256:..."
}
```

Allowed states for v0.6: `derived`, `ready_for_local_analysis`, `analysis_completed`, `analysis_failed`, `discarded`.

SourceDocument is a local analysis container derived from RawDocument. It may feed placeholder extraction. It must not certify source truthfulness or publication authenticity.

### Source

Implemented `Source` fields:

```json
{
  "id": "src-demo-wire",
  "name": "Demo Wire Fixture",
  "source_type": "wire_report",
  "url": null,
  "author": null,
  "publisher": "Lumen fixtures",
  "owner": null,
  "country": null,
  "language": "en",
  "funding": null,
  "wire_dependency": null,
  "citation_dependency": [],
  "independence_notes": ["Fixture source; independence is controlled for demo."],
  "reliability_notes": [],
  "anonymous": false,
  "interested_party": false
}
```

Source metadata gaps must remain explicit. Authority, outlet type, or popularity must never substitute for evidence.

### Source graph

Implemented `SourceGraph` fields:

```json
{
  "sources": [],
  "independent_evidence_streams": 1,
  "wire_dependencies": {},
  "citation_dependencies": {},
  "independence_notes": [],
  "warnings": []
}
```

The source graph records dependency and independence signals. It does not certify source truthfulness.

### Claim

Implemented `Claim` fields:

```json
{
  "id": "claim-demo-001",
  "raw_claim_text": "The rule starts on 1 June.",
  "normalized_claim": "rule starts on 2024-06-01",
  "claim_type": "factual_claim",
  "source_document_id": "doc-demo-001",
  "actors": ["Regulator"],
  "targets": ["Rule"],
  "location": null,
  "time_range": "2024-06-01",
  "evidence_refs": ["ev-demo-001"],
  "contradiction_refs": ["contradiction-demo-001"],
  "confidence_score": 0.42,
  "confidence_reason": ["Material fixture contradiction remains unresolved."],
  "status": "contested",
  "limitations": ["Fixture claim; not live analysis."],
  "limitations_ref": "LIMITATIONS.md",
  "audit_reference": "sha256:...",
  "created_at": "2026-01-01T00:00:00Z"
}
```

Display invariants:

- no claim without `status`;
- no claim without `confidence_reason`;
- no claim without at least one `evidence_refs` item or an explicit missing-evidence representation;
- no claim without `audit_reference`;
- no claim without `limitations_ref`;
- claim status is claim-level only and must not be projected onto the whole source/article.

Allowed `claim_type` values for v0.3:

- `factual_claim`
- `causal_claim`
- `legal_claim`
- `statistical_claim`
- `attribution_claim`
- `quote_claim`
- `prediction`
- `speculation`
- `moral_framing`
- `image_video_authenticity_claim`
- `anonymous_source_claim`
- `expert_interpretation`
- `interested_party_claim`

Allowed `status` values for v0.3:

- `confirmed`
- `strongly_corroborated`
- `probable`
- `plausible`
- `contested`
- `unsupported`
- `contradicted`
- `narrative_only`
- `unknown`
- `unresolved`

### Evidence

Implemented `Evidence` fields:

```json
{
  "id": "ev-demo-001",
  "claim_id": "claim-demo-001",
  "source_id": "src-demo-primary",
  "evidence_type": "primary_document",
  "summary": "Fixture primary notice lists a June start date.",
  "url": null,
  "quote": "Effective 1 June...",
  "provenance": "fixture",
  "proximity": "direct",
  "timestamp_quality": "known_fixture_timestamp",
  "primary": true,
  "anonymous": false,
  "limitations": ["Controlled fixture; not a live document."],
  "limitations_ref": "LIMITATIONS.md",
  "audit_reference": "sha256:..."
}
```

Allowed `evidence_type` values for v0.3:

- `primary_document`
- `official_dataset`
- `court_filing`
- `full_transcript`
- `raw_video`
- `raw_image`
- `geolocation_evidence`
- `named_on_record_source`
- `local_direct_reporting`
- `wire_report`
- `anonymous_source`
- `expert_interpretation`
- `social_media_post`
- `opinion_commentary`

Missing expected evidence must remain visible in limitations or missing-information fields; it must not be hidden behind confident language.

### Confidence breakdown

Implemented `ConfidenceBreakdown` fields, nested inside `Briefing.confidence`:

```json
{
  "score": 0.42,
  "status": "contested",
  "reasons": ["Contradictory fixture evidence prevents a higher band."],
  "rule_references": [],
  "caps_applied": [],
  "warnings": []
}
```

Rules:

- Confidence must be explainable, auditable, and contestable.
- Numeric score is for sorting/communication only, not authority.
- Anonymous-source caps and source-dependency warnings must be visible when applied.
- v0.3 does not expose a top-level `confidence_assessments` array; claim-level reasons and briefing confidence carry the implemented confidence contract.

### Contradiction

Implemented `Contradiction` fields:

```json
{
  "id": "contradiction-demo-001",
  "claim_ids": ["claim-demo-001", "claim-demo-002"],
  "contradiction_type": "time",
  "summary": "Fixture sources disagree on whether the start date is June or July.",
  "status": "fixture_detected",
  "limitations": ["Fixture/rule-based contradiction only; no semantic intelligence is claimed."]
}
```

Allowed `status` values:

- `fixture_detected`
- `not_resolved`

Contradictions are exposed, not automatically resolved.

### Briefing

Implemented `Briefing` fields:

```json
{
  "id": "briefing-demo-001",
  "topic": "Fixture: regulation start-date contradiction",
  "bottom_line": "The fixture contains a contested start-date claim; available evidence does not resolve the conflict.",
  "confidence": {},
  "key_claims": [],
  "evidence": [],
  "contradictions": [],
  "missing_information": ["No additional primary notice is present in the fixture."],
  "narrative_frames": ["Fixture-backed narrative analysis is deferred for v0.3."],
  "watch_indicators": ["New primary fixture would change confidence."],
  "unresolved_questions": ["Which fixture date should be treated as operative?"],
  "limitations": ["Controlled fixture only; no live event coverage."],
  "limitations_ref": "LIMITATIONS.md",
  "audit_reference": "sha256:...",
  "generated_at": "2026-01-01T00:00:00Z"
}
```

Display invariants:

- no briefing without `limitations_ref` and `limitations`;
- no briefing without `audit_reference`;
- bottom line must preserve unknown, unresolved, contested, unsupported, and contradicted states where present;
- briefing must not hide limitations behind polish.

### Audit event

Implemented `AuditEvent` fields:

```json
{
  "event_id": "audit-demo-score-001",
  "timestamp": "2026-01-01T00:00:00Z",
  "actor_type": "system",
  "actor_id": "lumen.local.deterministic",
  "operation": "score_assigned",
  "reason": "Applied deterministic confidence rules with visible reasons.",
  "input_hash": "sha256:...",
  "output_hash": "sha256:...",
  "previous_event_hash": "sha256:...",
  "event_hash": "sha256:...",
  "rule_version": "lumen.rules.v0.2",
  "model_version": "none",
  "prompt_hash": "none",
  "code_version": "local",
  "metadata": {}
}
```

Audit events record method traceability. They do not verify real-world correctness.

### Audit verification

Implemented `AuditVerification` fields:

```json
{
  "valid": true,
  "event_count": 6,
  "errors": [],
  "genesis_event_hash": "sha256:...",
  "latest_event_hash": "sha256:..."
}
```

## Frontend compatibility contract

The frontend may consume either:

1. the live local backend response from `/sample`; or
2. a committed static `demo-response.json` that validates as `AnalysisResponse`.

Frontend rendering gates:

- `BriefingPanel` requires briefing `limitations_ref`, `limitations`, and `audit_reference`.
- `ClaimMatrix` rejects or visibly flags any claim missing `status`, `confidence_reason`, `evidence_refs`, `audit_reference`, or `limitations_ref`.
- `EvidenceTrail` shows evidence provenance/proximity, limitations, limitations reference, and audit reference.
- `AuditTrail` shows verification status and latest event hash.
- `NarrativeMap`, `SourceSpread`, and `ContradictionBoard` may render fixture-backed/deferred states only when labeled as such.

### v0.4 panel status contract

| Panel | Contract status | Required behavior |
| --- | --- | --- |
| BriefingPanel | fixture-backed | Render only with briefing limitations, confidence reasons, unresolved questions or missing information, and audit reference. |
| ClaimMatrix | fixture-backed | Render claim-level statuses only; never promote a claim status to article/source truth. |
| EvidenceTrail | fixture-backed | Render evidence provenance, proximity, limitations, and audit reference; do not imply evidence completeness. |
| AuditTrail | fixture-backed | Render verification state and event hashes as method trace consistency only. |
| NarrativeMap | deferred/stub unless richer fixture data exists | Use `briefing.narrative_frames` only with analysis-not-fact and fixture/deferred labels; do not infer intent or deception. |
| SourceSpread | fixture-backed metadata; deferred independence inference | Render `source_graph` and `sources` metadata; do not infer ownership, funding, geography, affiliation, or reliability not present in the fixture. |
| ContradictionBoard | fixture-backed | Render explicit fixture contradictions and unresolved status; do not claim broad semantic contradiction detection. |

## Contract test checklist

Backend/eval tests should verify:

- `/sample` returns the shared `AnalysisResponse` envelope;
- `/analyze` returns the shared `AnalysisResponse` envelope;
- `POST /ingest/manual` documents RawDocument and SourceDocument lifecycle metadata without requiring live retrieval;
- response `mode` is `fixture_demo` for `/sample` and `local_input` for `/analyze`;
- top-level `limitations_ref` and `limitations` exist;
- top-level `audit_trail`, `audit_events`, and `audit_verification` exist;
- briefing includes `limitations_ref`, `limitations`, and `audit_reference`;
- every claim includes `status`, visible confidence reason, evidence reference, limitations reference, and audit reference;
- every evidence item includes limitations reference and audit reference;
- source dependency metadata is present in `source_graph` when dependency exists;
- audit verification returns valid/invalid state with event count, errors, genesis hash, and latest hash;
- no route requires paid APIs, external network calls, telemetry, auth/accounts, production databases, or LLM calls;
- submitted URL strings are not fetched or treated as inspected sources in v0.6.

## Explicit non-goals

The local/v0.6 contract does not include:

- live geopolitical analysis;
- URL crawling, URL fetching, scraping, live feeds, or RSS ingestion;
- global source coverage;
- broad semantic contradiction detection;
- production claim extraction;
- hidden scoring;
- user accounts;
- telemetry;
- proprietary hosted dependencies;
- blockchain anchoring;
- final truth determination;
- treating manual input, article text, source labels, or submitted URL strings as verified facts.
