# Lumen MVP Scope

## Scope lock

This document is the architecture lane scope lock for Lumen v0.2. It is intentionally narrow.

Lumen v0.2 is a local, deterministic demonstration of Lumen's method-first workflow over fixture-backed inputs. It is not a live intelligence system, a production ingestion platform, a global search product, or an automated authority on reality.

The MVP must make users more informed by exposing claims, evidence, uncertainty, source dependency, confidence reasons, limitations, and audit references. It must not ask users to trust hidden machinery.

## MVP goal

Create an honest local baseline that proves the repository shape, governance method, deterministic backend primitives, eval harness, and uncertainty-first UI contract.

The v0.2 baseline should answer:

- What claim was made?
- Which source or document contains it?
- What evidence is linked to it?
- What source dependencies weaken independence?
- What contradictions or unresolved questions remain?
- Which transparent rules affected confidence?
- Which audit event records each meaningful transformation?
- Which limitations must the user see before interpreting the output?

## In scope for v0.2

### Inputs

- Local fixture JSON and manually provided text sent to the local API.
- Structured source metadata fields when available.
- Seeded evidence, contradiction, source-dependency, narrative, and audit examples.
- Placeholder claim extraction that clearly discloses its limitations.

### Backend primitives

- FastAPI application importable locally.
- Pydantic models for claim, evidence, source, audit event, confidence assessment, and briefing objects.
- Deterministic scoring rules with visible reasons.
- Anonymous-source confidence caps.
- Primary-evidence boost rules.
- Source graph primitive with wire dependency, citation dependency, and independence notes.
- Fixture-based contradiction detector that exposes conflicts without resolving them.
- Hash-chained audit ledger with genesis event and verification function.
- Deterministic briefing generator that includes limitations and audit references.
- API routes:
  - `GET /health`
  - `GET /sample`
  - `POST /analyze`
  - `GET /audit/verify`

### Frontend contract

The frontend may remain mostly static until the API contract is stable, but any displayed analytical object must follow these rules:

- No claim is displayed without status.
- No confidence is displayed without visible reasons.
- No briefing is displayed without limitations.
- No analysis panel is displayed without an audit reference or explicit deferred/stub label.
- Narrative, source-spread, and contradiction panels may be stubbed if backend data is not ready, but the stubs must say what is deferred.

### Documentation and governance alignment

- Architecture docs define module boundaries and data contracts.
- Governance docs define confidence statuses, anonymous-source caps, source-independence rules, limitation disclosure, adversarial review, and MVP security boundaries.
- Eval docs define golden cases and deterministic tests.
- Audit report lists changed files and verification status.

## Out of scope for v0.2

The following are explicitly excluded from the v0.2 MVP:

- Real-time ingestion.
- Global crawling, streaming news pipelines, or broad web search.
- Paid APIs or credentialed external services.
- LLM calls in the core local path.
- Blockchain or distributed ledger implementation.
- Telemetry, analytics, tracking, or hidden instrumentation.
- User accounts, personalization, or moderation systems.
- Production-scale search, vector search, or graph database operations.
- Hidden source weighting, ideological weighting, or undisclosed scoring.
- Automated final truth determination.
- Claims of propaganda immunity, perfect neutrality, production intelligence reliability, or complete real-world verification.
- Silent mutation, deletion, or replacement of raw evidence.

## Deferred after v0.2

These are valid future candidates, not v0.2 requirements:

- RSS/manual URL ingestion with raw archive preservation.
- SQLite persistence for local claim/evidence/audit objects.
- CLI for local article ingestion and rerun reproducibility.
- Governance rule version registry.
- Broader golden-case library.
- Optional model-assisted extraction behind explicit configuration and audit metadata.
- Postgres, graph database, object storage, vector index, or search engine integrations.
- Public contribution workflows and challenge queues.

## MVP acceptance criteria

Lumen v0.2 is acceptable when:

- Core local backend imports and deterministic tests pass.
- `/health`, `/sample`, `/analyze`, and `/audit/verify` exist.
- Sample analysis is fixture-backed and includes claims, evidence, source dependency notes, confidence reasons, limitations, and audit references.
- Audit verification detects tampering.
- Unknown, unresolved, contested, unsupported, and contradicted are valid statuses.
- Anonymous-source caps and primary-evidence boosts are documented and testable.
- The frontend does not imply certainty beyond backend output.
- Docs disclose MVP limits and no-authority stance.
- No secrets, paid dependencies, telemetry, or fake capability claims are introduced.

## User-facing limitations to preserve

Every demo, briefing, or UI path must preserve these limitations:

- Fixture data is illustrative and local.
- Placeholder extraction is not broad real-world extraction.
- Source metadata may be incomplete and must not be inferred silently.
- Confidence scores are transparent method outputs for inspection, not truth scores.
- Contradiction detection exposes conflicts; it does not settle them.
- Narrative labels identify possible framing patterns; framing is not proof of deception.
- Missing evidence and unresolved status are valid outcomes, not product failures.

## Scope-creep rejection checklist

Reject or defer any proposed feature unless it directly improves one of these v0.2 goals:

- claim clarity
- evidence visibility
- uncertainty handling
- source-dependency transparency
- confidence explainability
- auditability
- local deterministic reproducibility
- honest limitation disclosure
