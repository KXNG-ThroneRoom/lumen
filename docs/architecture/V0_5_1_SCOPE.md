# Lumen v0.5.1 Scope Lock

Version: v0.5.1-stabilization-hygiene

## Purpose

v0.5.1 is a stabilization and hygiene release for the existing v0.5 controlled local fixture demo.

It does not add analytical capability. It does not add live ingestion, model calls, paid services, accounts, telemetry, production storage, or a redesigned public UI. Its job is to make the already-scoped v0.5 demo easier to verify from a fresh clone, easier to explain honestly, and harder to overclaim.

## Current public demo surface

The public demo surface remains:

- one controlled fixture-backed claim story: "When does the regulation start?";
- simplified black/white UI with four tabs: Story, Evidence, Why uncertain, and Audit;
- visible contested/uncertain language instead of final verdict wording;
- red conflict, blue supporting evidence, and yellow uncertainty cues;
- technical details kept behind appropriate developer or expandable inspection surfaces.

The public demo must not expose raw hashes, raw IDs, `.md` references, machine labels, provenance jargon, or dense dashboard language as the main user experience.

## In scope for v0.5.1

v0.5.1 may change documentation, verification guidance, and scope wording when the change improves launch hygiene without expanding capability.

Allowed work:

1. Define v0.5.1 as stabilization/hygiene, not product expansion.
2. Keep roadmap sequencing explicit and disciplined.
3. Make deferred-work boundaries more visible and honest.
4. Document fresh-clone install, verification, and local demo flow.
5. Remove or reframe stale public-facing references to older dashboard surfaces.
6. Clarify known environment assumptions and local-only verification constraints.
7. Preserve the v0.5 controlled fixture demo as the only current public claim story.

## Out of scope for v0.5.1

v0.5.1 must not introduce or imply:

- live ingestion, crawling, RSS polling, URL fetching, or monitoring;
- LLM calls or paid APIs in the default local demo path;
- auth, accounts, personalization, telemetry, or analytics;
- durable databases, graph databases, vector stores, object storage, queues, or hosted production infrastructure;
- new public analytical claim surfaces beyond the controlled start-date fixture;
- broad contradiction detection, source-independence inference, or production claim extraction;
- final truth determination, article-level truth labels, or production/live truth claims;
- blockchain anchoring or tamper-proof audit claims;
- public UI redesign beyond preserving the simplified claim-story interface and removing stale wording.

## Stabilization gates

v0.5.1 is ready only when:

- `docs/architecture/FRESH_CLONE_READINESS.md` explains install, verification, demo flow, and environment assumptions;
- `docs/architecture/ROADMAP_TO_V1.md` shows v0.5.1 as a hygiene step between v0.5 and later phases;
- `docs/architecture/DEFERRED_WORK.md` remains explicit that deferred work is neither promised nor silently implemented;
- public-facing docs do not describe the older dense dashboard as the current public UI;
- verification commands are documented and can be run without secrets, paid services, telemetry, live feeds, accounts, or LLM calls;
- no owned architecture doc expands current capability beyond the controlled local fixture demo.

## Relationship to v0.5

v0.5 established the public-readiness framing for the simplified controlled local demo. v0.5.1 preserves that boundary and tightens the surrounding launch hygiene: fresh-clone readiness, roadmap discipline, and deferred-work clarity.

Any proposal that changes what Lumen analyzes, ingests, stores, calls over the network, or claims publicly belongs in a later scoped phase, not v0.5.1.
