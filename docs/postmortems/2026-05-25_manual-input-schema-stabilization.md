---
schema_version: 1
doc_type: implementation_postmortem
project: Lumen
phase: v0.6.1
sprint: manual-input-schema-stabilization
date: 2026-05-25
detected_at: 2026-05-25
introduced_at: 2026-05-25
resolved_at: 2026-05-25
detection_method: human_review
repo_path: /Users/amirtbz/lumen
repo_commit_before: 0a0a7edd33a8e13708dd8d8f0fc67a965104926f
repo_commit_after: uncommitted-local-after-lumen-v0-6-1-manual-input-schema-stabilization
branch: main
status: resolved
severity: medium
prevention_status: verified
failure_classes:
  - schema_drift
  - architecture_drift
affected_modules:
  - manual_input
  - api_contract
  - document_models
affected_files:
  - apps/api/app/models.py
  - apps/api/app/manual_input.py
  - apps/api/app/main.py
  - apps/api/tests/test_manual_input.py
  - apps/api/tests/test_api_contract.py
related_tasks:
  - t_5d47167c
  - t_aef1565a
related_swarms:
  - docs/swarms/2026-05-25_lumen-v0-6-controlled-manual-input-layer.md
related_postmortems: []
constitution_articles_at_risk:
  - V
  - XI
  - XII
supersedes: ""
tags:
  - v0.6.1
  - manual_input
  - schema_stabilization
retrieval_keywords:
  - manual input schema stabilization
  - RawDocument SourceDocument
  - input_method canonical
  - no live ingestion
related_docs:
  - docs/architecture/API_CONTRACT.md
  - docs/architecture/CONTROLLED_INPUT_LAYER.md
  - docs/architecture/V0_6_SCOPE.md
forensic_log: ""
index_record: docs/postmortems/index.jsonl
line_ceiling_exception: false
line_ceiling_exception_reason: ""
---

## Summary

The v0.6 controlled manual input layer was epistemically sound, but human review found early schema and ontology drift before commit. The contract risk was resolved in v0.6.1 by narrowing the public input vocabulary, removing redundant manual document objects, and keeping the API focused on manual text as an assertion container rather than live ingestion or source verification.

## Symptom

The pre-commit audit found that the manual input contract had grown more surface area than the first durable API needed. `ManualDocument` overlapped with `RawDocument`, `ManualSourceDocument` was unused, `input_method` and `input_mode` duplicated the same concept, unsupported file input appeared in the contract vocabulary, and alias compatibility shims existed before there were real external clients to support.

## Root cause

The first v0.6 implementation modeled likely future ingestion concepts too early. That made the manual input boundary look more mature and extensible than it was, even though the actual capability was deliberately limited to controlled `manual_text` submissions with no fetching, persistence, LLM calls, or truth adjudication.

## Causal chain

- v0.6 added `POST /ingest/manual` with correct epistemic boundaries.
- Future-facing document vocabulary entered the schema before future ingestion modes were implemented.
- Redundant objects and duplicate field names increased contract ambiguity.
- Human review caught the ambiguity before the API was committed as durable.
- v0.6.1 narrowed the schema to the implemented capability and reverified the boundary.

## Fix

`ManualDocument` was removed because it duplicated `RawDocument`, and `ManualSourceDocument` was removed because it was unused. `input_method` became the only canonical input concept, while `input_mode` was removed from active app, docs, and eval paths. Unsupported file input was removed from the active contract because v0.6.1 supports `manual_text` only. Broad legacy alias support was removed before external clients depended on it.

The response now uses two explicit object roles: `RawDocument` means the user-submitted assertion container, and `SourceDocument` means the normalized analysis-ready derivative. `source_url` remains inert user-supplied metadata only, with `source_url_fetched` always false. `build_manual_ingest_response` now accepts `AnalysisResponse | None`, matching the response model.

## Prevention

Prevention status: verified. The manual input tests now assert the strict canonical request schema, unsupported input rejection, empty normalized input rejection, stable content hashes, audit event creation, inert source URL metadata, and absence of duplicate `input_method`/`input_mode` exposure. Verification passed with 32 backend tests and the aggregate verifier reported 8 gates and 0 failures.

No fetching, scraping, RSS polling, LLM calls, external API calls, telemetry, auth/accounts, database persistence, or truth-verdict behavior was introduced.

## What we learned

For early API contracts, future vocabulary is still product surface area. The safest stabilization point is before commit, while redundant ontology and compatibility shims can still be removed without migration cost.
