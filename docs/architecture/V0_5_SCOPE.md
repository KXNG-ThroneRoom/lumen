# Lumen v0.5 Scope Lock

Version: v0.5-launch-hygiene

## Purpose

v0.5 is launch hygiene and public-readiness for the controlled local demo. It does not add a new intelligence layer, new data source, new scoring authority, or new production infrastructure.

The goal is to make the current local deterministic fixture demo clear enough for public announcement: a simplified claim story that shows contested evidence without pretending to settle the claim.

Doctrine remains unchanged:

- Methods over conclusions.
- More informed humans, not a new oracle.
- Lumen exposes claims, evidence, contradictions, uncertainty, confidence reasons, and audit trails.
- Lumen does not determine truth.

## v0.5 commitments

v0.5 is in scope only when it improves public clarity, auditability, or launch honesty for the existing controlled fixture demo.

Commitments:

1. Public UI is the simplified black/white tabbed claim story.
2. Public claim is "When does the regulation start?"
3. Public explanation says a news report gives June 1, an official filing gives July 1, and Lumen marks the claim contested instead of guessing.
4. Public tabs are Story, Evidence, Why uncertain, and Audit.
5. Visual language uses yellow/uncertain for contested, blue/supporting for stronger support, and red/conflict for disagreement.
6. Public UI avoids raw hashes, audit IDs, `.md` references, underscores/machine labels, visible provenance strings, and dense technical dashboard wording.
7. Old detailed component names are labeled legacy/internal if mentioned.
8. Local API, fixtures, and verification remain available for inspection.
9. Launch docs explain deferrals explicitly instead of implying hidden capability.
10. Verification commands and blocker labels are documented.

## Demo-ready in v0.5

- Controlled local start-date contradiction fixture.
- Four-tab public story UI.
- Plain-language evidence explanation.
- Visible contested/no-final-verdict language.
- Audit tab that explains checks without exposing confusing internals.
- Aggregate local verification gate.
- Roadmap and deferred-work docs that prevent launch scope creep.

## Not in v0.5

- Live ingestion, crawling, RSS polling, current-event monitoring, or URL fetching.
- Paid APIs, proprietary hosted dependencies, telemetry, secrets, accounts, authentication, or personalization.
- LLM calls in the default local demo path.
- Production claim extraction or broad semantic contradiction detection.
- Production source-independence inference from ownership, funding, geography, affiliation, or source reputation.
- Graph database, vector search, object storage, or durable database complexity.
- Automated final truth determination, article-level truth labels, or claims of real-world verification completeness.
- Blockchain anchoring or tamper-proof audit claims.
- UI redesign beyond preserving the current simplified interface and removing stale references to old public surfaces.

## Scope-creep rejection rules

Reject or defer any proposed v0.5 work if it primarily adds:

- live data breadth instead of better fixture transparency;
- hidden scoring or opaque model judgment;
- UI polish that hides uncertainty, limitations, or auditability;
- production infrastructure not needed for local deterministic demo review;
- new product claims that the current implementation cannot prove;
- analytical categories not already represented by the controlled fixture.

A v0.5 change is acceptable only if it improves at least one of these:

- public copy clarity;
- demo repeatability;
- visible limitations;
- fixture-backed UI honesty;
- auditability;
- confidence reason transparency;
- source-dependency transparency;
- launch verification.

## Relationship to v0.4

v0.4 stabilized demo polish around the detailed backend/frontend contract and legacy/internal honesty components. v0.5 does not discard that substrate. It reframes the public surface around the simplified four-tab story and treats detailed component names as internal or legacy unless a later scope explicitly restores them to public UX.

## v0.5 exit criteria

v0.5 may be called ready for public controlled-demo announcement only when:

- `LAUNCH_READINESS.md` gates pass or clearly record blockers;
- `DEMO_FLOW.md` matches the actual runnable simplified UI;
- `docs/demo/LOCAL_DEMO_WALKTHROUGH.md` exists and matches the current public tabs;
- `ROADMAP_TO_V1.md` separates future phases from current capability;
- `DEFERRED_WORK.md` lists out-of-scope capabilities plainly;
- no owned architecture doc claims live coverage, final authority, hidden scoring, or production intelligence reliability;
- no architecture doc describes the old dense seven-component dashboard as the public v0.5 UI;
- current git state is recorded in handoff and no unowned files were modified by this lane.
