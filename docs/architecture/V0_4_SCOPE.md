# Lumen v0.4 Scope Lock

Version: v0.4-demo-polish

## Purpose

v0.4 is a demo-polish and launch-readiness scope. It does not add a new intelligence layer.

The goal is to make the existing local deterministic fixture demo honest, precise, auditable, and hard to overstate. v0.4 should let a reviewer run the repo, inspect the contract, see every limitation, and understand which panels are real fixture-backed displays versus deferred stubs.

Doctrine remains unchanged:

- Methods over conclusions.
- More informed humans, not a new oracle.
- Lumen exposes claims, evidence, contradictions, uncertainty, provenance, confidence reasons, and audit trails.
- Lumen does not determine truth.

## v0.4 commitments

v0.4 is demo-ready only when the repository can demonstrate these capabilities locally:

1. Local deterministic backend starts without secrets, paid APIs, telemetry, hidden hosted services, external network dependency, or LLM calls.
2. `GET /health`, `GET /sample`, `POST /analyze`, and `GET /audit/verify` are documented and locally inspectable.
3. `/sample` returns a controlled fixture analysis using `schema_version: "lumen.analysis.v0.3"` unless the backend schema is deliberately changed with tests and docs in the same sprint.
4. `/analyze` accepts manually supplied local text only and returns the same analysis envelope while disclosing placeholder extraction limits.
5. The frontend renders the canonical fixture through these panels:
   - BriefingPanel
   - ClaimMatrix
   - EvidenceTrail
   - AuditTrail
   - NarrativeMap
   - SourceSpread
   - ContradictionBoard
6. Every displayed claim includes status, confidence reasons, evidence references, audit reference, and limitations reference.
7. Every briefing includes bottom line, confidence reasons, missing information or unresolved questions, limitations, limitations reference, and audit reference.
8. Source dependency is visible as a method signal; repeated source count is not treated as independent corroboration.
9. Contradictions remain unresolved unless the fixture explicitly includes resolving evidence.
10. Audit verification is displayed as transformation-trace consistency, not proof that a claim is true.

## Panel truth table

| Panel | v0.4 status | Allowed data source | Required label | Deferred boundary |
| --- | --- | --- | --- | --- |
| BriefingPanel | fixture-backed | `/sample` or matching static `demo-response.json` | deterministic fixture/local-input briefing with limitations | no production briefing, no final answer |
| ClaimMatrix | fixture-backed | claims in `AnalysisResponse` | claim-level status and confidence reasons | no article-level verdict |
| EvidenceTrail | fixture-backed | evidence in `AnalysisResponse` | provenance, proximity, limitations, audit reference | no complete source coverage claim |
| AuditTrail | fixture-backed | audit events and verification response | method trace / tamper-evident check | no claim that audit proves reality |
| NarrativeMap | deferred/stub unless richer fixture data is present | `briefing.narrative_frames` strings | analysis-not-fact; fixture-backed/deferred | no intent, deception, or coordination inference |
| SourceSpread | fixture-backed metadata, deferred independence inference | `source_graph` and `sources` | source quantity is not independence | no ownership/funding/affiliation inference unless present in fixture |
| ContradictionBoard | fixture-backed | `contradictions` in `AnalysisResponse` | conflicts exposed, not settled | no broad semantic contradiction detection |

## Demo-ready vs deferred

### Demo-ready in v0.4

- Canonical controlled start-date contradiction fixture.
- Claim cards/rows with status, reasons, evidence refs, limitations refs, and audit refs.
- Evidence trail showing relationship/provenance/limitations/audit refs for fixture evidence.
- Source spread showing explicit wire dependency and source-independence notes when present.
- Contradiction board showing fixture conflict and unresolved/fixture status.
- Narrative map as labeled analysis-not-fact and explicitly deferred/stub unless richer fixture data exists.
- Briefing that preserves contested/unresolved state and visible limitations.
- Audit trail and audit verification display.
- Local verification commands documented in `LAUNCH_READINESS.md`.

### Deferred after v0.4

- Live ingestion, crawling, RSS polling, current-event monitoring, or URL fetching.
- Paid APIs, proprietary hosted dependencies, telemetry, secrets, accounts, auth, or personalization.
- LLM calls in the default local demo path.
- Production claim extraction or broad semantic contradiction detection.
- Production source-independence inference from ownership, funding, geography, affiliation, or source reputation.
- Graph database, vector search, object storage, or durable database complexity.
- Automated final truth determination, article-level truth labels, or claims of real-world verification completeness.
- Blockchain anchoring or tamper-proof audit claims.

## Scope-creep rejection rules

Reject or defer any proposed v0.4 work if it primarily adds:

- live data breadth instead of better fixture transparency;
- hidden scoring or opaque model judgment;
- UI polish that hides uncertainty, limitations, or audit references;
- production infrastructure not needed for local deterministic demo review;
- new product claims that the current implementation cannot prove.

A v0.4 change is acceptable only if it improves at least one of these:

- contract clarity;
- demo repeatability;
- visible limitations;
- fixture-backed panel honesty;
- auditability;
- confidence reason transparency;
- source-dependency transparency;
- launch verification.

## v0.4 exit criteria

v0.4 may be called launch-ready for a controlled demo only when:

- `LAUNCH_READINESS.md` gates pass or clearly record blockers;
- `DEMO_FLOW.md` matches the actual runnable demo path;
- `API_CONTRACT.md` matches backend and static fixture shapes;
- NarrativeMap, SourceSpread, and ContradictionBoard are each visibly fixture-backed, stubbed, or deferred;
- no architecture doc claims live coverage, final authority, hidden scoring, or production intelligence reliability;
- current git state is recorded in the handoff and no unowned files were modified by the architecture lane.
