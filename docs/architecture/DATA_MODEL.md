# Lumen Data Model

## Modeling principles

- Articles and documents are source containers, not facts.
- Claims are the unit of analysis.
- Evidence can support, contradict, contextualize, remain unclear, or be missing.
- Source independence is modeled separately from source count.
- Confidence is an explainable derived object, not a hidden scalar.
- Every meaningful transformation produces an audit event.
- Unknown, unresolved, contested, unsupported, and contradicted are valid states.
- Narrative analysis is labeled as analysis, not fact.
- Raw evidence is immutable; derived objects reference raw IDs and hashes.

## Required object contract for v0.2

The backend lane should implement these concepts as Pydantic models in `apps/api/app/models.py`. Field names may be adapted only if the API response preserves the same meaning and tests enforce the uncertainty/audit contract.

## Core entities

### RawSourceDocument

Immutable record of collected or fixture-provided source material.

Fields:

- `id`: stable document identifier.
- `source_url`: source URL when available.
- `source_name`: outlet, institution, person, repository, or fixture name.
- `author`: author or null.
- `published_at`: source publication timestamp or null.
- `collected_at`: local collection timestamp.
- `ingestion_method`: `sample_json`, `manual_text`, `manual_url`, `rss`, or future method.
- `raw_text`: original text when available.
- `raw_payload`: original structured payload when available.
- `content_hash`: SHA-256 over canonical raw content.
- `archive_reference`: local/archive pointer.
- `language`: BCP-47 code when known.
- `version`: immutable version number.
- `limitations`: source/document-level limitations.

Rules:

- Never overwrite raw records.
- A changed source becomes a new document version.
- Derived objects reference raw source IDs and hashes.

### Source

Entity describing who or what published, originated, funded, or amplified information.

Fields:

- `id`
- `name`
- `source_type`: `media`, `government`, `ngo`, `company`, `academic`, `individual`, `wire`, `social`, `repository`, `unknown`.
- `country`
- `language`
- `owner`
- `funding_notes`
- `affiliation_notes`
- `correction_history_notes`
- `reliability_notes`
- `metadata_confidence`: `known`, `partial`, `unknown`.
- `limitations`

Rules:

- Metadata gaps must be represented as unknown, not inferred silently.
- Authority may affect context; it does not replace evidence.

### SourceDependencyEdge

Relationship showing that sources/documents may not be independent.

Fields:

- `id`
- `from_source_id`
- `to_source_id`
- `from_document_id`
- `to_document_id`
- `dependency_type`: `wire_dependency`, `citation_dependency`, `shared_owner`, `press_release`, `syndication`, `language_reuse`, `shared_author`, `unknown_possible_dependency`.
- `wire_dependency`: boolean.
- `citation_dependency`: boolean.
- `evidence_ref`
- `confidence`: `confirmed`, `probable`, `possible`, `unknown`.
- `independence_notes`
- `audit_event_id`

Rules:

- Ten articles repeating one wire report count as one evidence stream.
- Source count and evidence-stream count must not be conflated.

### Claim

Atomic assertion extracted from a document or fixture.

Fields:

- `id`
- `source_document_id`
- `raw_claim_text`
- `normalized_claim`
- `claim_type`: `factual`, `causal`, `legal`, `statistical`, `attribution`, `quote`, `prediction`, `speculation`, `moral_framing`, `media_authenticity`, `anonymous_source`, `expert_interpretation`.
- `actors`: list of entities.
- `actions`: list of actions/events.
- `targets`: list of entities.
- `location`
- `time_range`
- `evidence_refs`: evidence IDs.
- `contradiction_refs`: contradiction IDs.
- `confidence_id`: derived confidence object ID.
- `status`: controlled status vocabulary.
- `status_reason`: visible reason for the status.
- `created_at`
- `extraction_method`: `fixture`, `deterministic_placeholder`, `human`, `model_assisted_future`.
- `limitations`
- `audit_event_id`

Rules:

- A claim records that an assertion was made; it does not assert truth by itself.
- A claim without `status` is invalid.
- A claim without `status_reason` is invalid for API/UI output.
- Blanket article-level truth labels are out of scope.

### EvidenceItem

Object that may support, contradict, contextualize, fail to resolve, or indicate missing evidence for a claim.

Fields:

- `id`
- `evidence_type`: `primary_document`, `official_dataset`, `court_filing`, `full_transcript`, `raw_video`, `raw_image`, `geolocation`, `named_on_record_source`, `local_direct_reporting`, `wire_report`, `anonymous_source`, `expert_interpretation`, `social_media_post`, `opinion_commentary`, `missing_expected_evidence`.
- `source_document_id`
- `source_id`
- `claim_ids`
- `relationship`: `supports`, `contradicts`, `contextualizes`, `missing`, `unclear`.
- `quote_or_excerpt`
- `locator`: page, timestamp, URL fragment, or local path.
- `proximity_score`
- `provenance_score`
- `independence_score`
- `specificity_score`
- `verifiability_score`
- `timestamp_quality`
- `chain_of_custody_notes`
- `limitations`
- `audit_event_id`

Rules:

- Evidence relationship must be explicit.
- Missing expected evidence is represented as data, not hidden.

### Contradiction

Explicit conflict between claims or evidence items.

Fields:

- `id`
- `claim_ids`
- `evidence_ids`
- `contradiction_type`: `actor`, `time`, `location`, `causal`, `numerical`, `legal_interpretation`, `source_attribution`, `media_authenticity`, `omission`.
- `description`
- `status`: `open`, `partially_resolved`, `resolved_by_new_evidence`, `unresolved`.
- `limitations`
- `audit_event_id`

Rule:

- The system exposes contradictions; it does not force resolution.

### NarrativeFrame

Analysis object describing framing patterns.

Fields:

- `id`
- `document_id`
- `claim_ids`
- `hero`
- `villain`
- `victim`
- `threat`
- `solution`
- `moral_frame`
- `emotional_language`
- `omitted_context`
- `beneficiary`
- `amplifiers`
- `repeated_phrases`
- `analysis_label`: must state that this is analysis, not fact.
- `confidence_notes`
- `limitations`
- `audit_event_id`

Rule:

- Narrative framing is not proof of deception or correctness.

### ConfidenceAssessment

Transparent scoring result for a claim.

Fields:

- `id`
- `claim_id`
- `score`: numeric 0-100 for UI sorting only.
- `status`: controlled status vocabulary.
- `rule_version`
- `reasons`: visible list of rule applications.
- `caps_applied`: e.g. anonymous-source cap.
- `boosts_applied`: e.g. primary evidence boost.
- `penalties_applied`: e.g. contradiction or source-dependency penalty.
- `source_dependency_warnings`
- `uncertainty_notes`
- `missing_evidence_notes`
- `limitations`
- `audit_event_id`

Rules:

- Score without reasons is invalid.
- Anonymous-source claims are capped unless stronger evidence supports them.
- Article volume is not proof.
- The numeric score is a transparent sorting/communication aid, not a final authority.

### AuditEvent

Append-only record of a meaningful transformation.

Fields:

- `event_id`
- `timestamp`
- `actor_type`: `system`, `human`, `model`, `test`.
- `actor_id`
- `operation`: controlled audit operation vocabulary.
- `input_hash`
- `output_hash`
- `previous_event_hash`
- `event_hash`
- `reason`
- `rule_version`
- `model_version`
- `prompt_hash`
- `code_version`
- `object_refs`
- `limitations`

Rules:

- Event hash is computed over canonical event content excluding `event_hash`.
- Genesis events use a null previous hash.
- Verification must detect changed event content, broken previous-hash links, and missing genesis event.
- This is a local tamper-evident ledger design, not a blockchain.

### Briefing

Human-readable structured output that preserves uncertainty.

Fields:

- `id`
- `topic`
- `bottom_line`: concise, uncertainty-aware summary.
- `confidence_summary`
- `what_changed`
- `key_claim_ids`
- `evidence_ids`
- `contradiction_ids`
- `source_dependency_notes`
- `missing_information`
- `narrative_frame_ids`
- `incentive_notes`
- `watch_indicators`
- `unresolved_questions`
- `limitations`
- `audit_event_id`

Rules:

- A briefing without limitations is invalid.
- A briefing without an audit reference is invalid.
- The bottom line must preserve contested, unknown, unsupported, and unresolved status where present.

### AnalysisResult

API-facing aggregate returned by `/sample` and `/analyze`.

Fields:

- `id`
- `input_document_ids`
- `sources`
- `source_dependency_edges`
- `claims`
- `evidence`
- `contradictions`
- `narrative_frames`
- `confidence_assessments`
- `briefing`
- `audit_events`
- `limitations`
- `rule_version`

Rules:

- Analytical output must include limitations.
- Analytical output must include enough audit events or audit refs for the UI to show traceability.

## Controlled vocabularies

### Claim/confidence statuses

- `confirmed`: strongly supported by direct evidence with no known material contradiction in the fixture context.
- `strongly_corroborated`: supported by multiple independent evidence streams or high-quality primary evidence, while still open to revision.
- `probable`: supported by credible evidence but with remaining gaps.
- `plausible`: possible based on available evidence but materially incomplete.
- `contested`: materially disputed by evidence or claims.
- `unsupported`: asserted without sufficient supporting evidence in the analyzed set.
- `contradicted`: materially conflicts with stronger or direct evidence in the analyzed set.
- `narrative_only`: framing/interpretation rather than an independently checkable factual assertion.
- `unknown`: available information is insufficient to assess.
- `unresolved`: conflict or gap remains open after analysis.

### Evidence relationships

- `supports`
- `contradicts`
- `contextualizes`
- `missing`
- `unclear`

### Audit operations

- `genesis`
- `raw_input_collected`
- `document_parsed`
- `claim_extracted`
- `claim_normalized`
- `source_dependency_recorded`
- `evidence_attached`
- `contradiction_detected`
- `score_assigned`
- `narrative_frame_generated`
- `briefing_generated`
- `audit_verified`
- `human_edit_made`
- `governance_rule_changed`

## Suggested v0.2 storage

- JSON fixtures in `examples/` for deterministic demo data.
- Pydantic models in `apps/api/app/models.py`.
- JSONL-style audit records for append-only ledger tests.
- SQLite only if needed later for local persistence.

## Validation rules for backend/tests

- No `Claim` is valid for API/UI output without `status` and `status_reason`.
- No `ConfidenceAssessment` is valid without at least one visible reason.
- No anonymous-source claim may escape documented caps without stronger evidence and a visible reason.
- No briefing is valid without `limitations` and `audit_event_id`.
- No analysis response is valid without top-level `limitations`.
- Source dependency warnings must be visible when dependency edges exist.
- Audit verification must fail on tampered event content or broken hash links.
