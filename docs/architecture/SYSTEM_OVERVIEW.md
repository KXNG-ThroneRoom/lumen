# Lumen System Overview

## Mission boundary

Lumen is transparent, open-source infrastructure for public-interest information analysis. It structures information into inspectable analytical objects so humans can reason with more context.

Lumen v0.2 does not decide final truth, rank ideology, provide production intelligence reliability, or sell conclusions. Its invariant is narrower and auditable:

> Every analytical output must expose its input references, applied rules, assumptions, uncertainty, limitations, and audit events.

## v0.2 architecture flow

```text
Local fixture JSON or submitted text
  -> Raw document/source object
  -> Placeholder claim extraction
  -> Claim normalization
  -> Source graph dependency notes
  -> Evidence and contradiction links
  -> Deterministic confidence scoring
  -> Hash-chained audit event(s)
  -> Deterministic briefing
  -> FastAPI response / static UI contract
```

Future architecture may add ingestion, richer parsing, model-assisted extraction, persistence, graph/search stores, and contribution workflows. Those are not v0.2 requirements.

## Runtime boundary

The v0.2 runtime must be local and deterministic:

- No paid APIs.
- No LLM calls in the core path.
- No telemetry or hidden analytics.
- No secrets or credentials required.
- No real-time ingestion.
- No blockchain implementation.
- No mutation of raw source/evidence records.

## Module boundaries

### Input adapter

Accepts local fixture JSON and text submitted to the local API. It canonicalizes inputs for hashing and passes raw content forward without replacing originals.

MVP responsibility:

- Load fixture-backed examples.
- Accept submitted text in `/analyze`.
- Produce stable raw input hashes.

Out of scope:

- live crawling, RSS polling, paywalled sources, streaming pipelines, credentialed ingestion.

### Raw evidence archive

Preserves immutable source/document records with provenance metadata and content hashes.

MVP responsibility:

- Represent raw document/source objects in fixtures and Pydantic models.
- Treat a changed source as a new version, not an overwrite.

Trust rule:

- Derived objects reference raw IDs and hashes; they do not replace raw evidence.

### Placeholder claim extractor

Splits fixture/sample content into claim objects only where deterministic rules or provided fixture fields support it.

MVP responsibility:

- Return explicit limitation metadata.
- Mark extraction method as placeholder/sample/deterministic.
- Avoid implying broad natural-language extraction capability.

Out of scope:

- production claim extraction, model-assisted extraction, multilingual extraction, full document understanding.

### Claim normalizer

Maps extracted or fixture-provided assertions into stable claim objects with type, actors, actions, targets, location, time range, status, evidence refs, contradiction refs, confidence refs, and audit refs.

MVP responsibility:

- Preserve status as required.
- Preserve confidence reason requirement.
- Use controlled vocabularies from `DATA_MODEL.md`.

### Source graph

Tracks whether multiple sources/documents are independent evidence streams or repeated origins.

MVP responsibility:

- Represent `wire_dependency`.
- Represent `citation_dependency`.
- Include `independence_notes`.
- Flag repeated-origin evidence streams.

Rule:

- Article count is not evidence-stream count.

### Evidence linker

Links claims to evidence items that support, contradict, contextualize, remain unclear, or indicate missing expected evidence.

MVP responsibility:

- Deterministic fixture links.
- Relationship vocabulary from `DATA_MODEL.md`.
- Evidence limitations and locator fields.

### Contradiction detector

Exposes seeded conflicts between claims or evidence items without resolving them automatically.

MVP responsibility:

- Fixture-based contradiction detection.
- Contradiction type, description, status, and audit event ID.

Out of scope:

- broad semantic contradiction detection or automated resolution.

### Narrative analyzer

Labels framing patterns such as hero, villain, victim, threat, solution, emotional language, omitted context, beneficiary, and repeated phrases.

MVP responsibility:

- Static or fixture-backed narrative frames.
- Clear `analysis_label` stating that the frame is analysis, not fact.

Out of scope:

- hidden persuasion scoring, author-intent claims, or deception claims based solely on framing.

### Governance and confidence scoring

Applies transparent deterministic rules to generate confidence assessments and statuses.

MVP responsibility:

- Primary-evidence boost.
- Anonymous-source cap.
- Source-dependency penalty/warning.
- Contradiction penalty/warning.
- Missing evidence and unresolved/unknown handling.
- Visible reasons, caps, boosts, penalties, uncertainty notes, and audit references.

Invalid output:

- Confidence without reasons.
- Claim without status.
- Score presented as an authority on reality.

### Audit ledger

Records meaningful transformations as append-only hash-chained audit events.

MVP responsibility:

- Genesis event.
- Event hash computed over canonical event content excluding `event_hash`.
- `previous_event_hash` chain.
- Verification function that detects tampering.
- Event refs from claims, evidence, confidence assessments, contradictions, narrative frames, and briefings.

This is a local tamper-evident ledger design, not a blockchain.

### Briefing engine

Produces concise structured briefings from claims, evidence, source dependencies, contradictions, confidence assessments, limitations, and audit refs.

MVP responsibility:

- Deterministic output.
- Bottom line that preserves uncertainty.
- Confidence summary with reasons.
- Missing information and unresolved questions.
- Limitations reference.
- Audit event ID.

### FastAPI boundary

The local API is the integration seam for backend tests and frontend readiness.

Required v0.2 routes:

- `GET /health`: service health and version/rule metadata.
- `GET /sample`: fixture-backed structured analysis.
- `POST /analyze`: deterministic local analysis over submitted text/fixture-shaped payload.
- `GET /audit/verify`: audit chain verification result.

### Frontend boundary

The frontend may remain static until backend contracts stabilize. Any rendered analytical output must respect the backend schema and uncertainty contract.

UI must not show:

- claim without status
- confidence without reason
- briefing without limitation reference
- analysis without audit reference or explicit deferred/stub label

## Data stores for v0.2

- `examples/` JSON fixtures for deterministic sample data.
- Pydantic models in `apps/api/app/models.py` for runtime validation.
- JSONL-style audit event chain for local tamper-evident verification.
- SQLite only if needed for local scaffold convenience; not required for v0.2 acceptance.

Future stores such as Postgres, graph databases, vector indexes, object storage, and search engines are options, not commitments.

## Trust boundaries

- Raw documents and evidence are immutable.
- Derived objects are auditable interpretations, not replacements for originals.
- Governance rules are documented inputs, not silent code behavior.
- Confidence is explainable and contestable.
- Source authority never replaces evidence.
- Narrative analysis is labeled as analysis.
- UI summaries cannot hide unresolved, unknown, contested, unsupported, or contradicted states.
- Future model-assisted stages must expose model version, prompt hash, rule version, and limitations.

## Open-source infrastructure stance

Lumen v0.2 must be runnable and inspectable without proprietary hosted services. Optional future integrations must be replaceable, documented, and visibly configured.

The default architecture should favor:

- local-first execution
- transparent source code
- deterministic tests
- public governance rules
- inspectable fixtures
- auditable transformations
- forkable methodology
