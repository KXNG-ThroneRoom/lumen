# Lumen v0.6 Scope Lock

Version: v0.6-controlled-manual-input

## Scope stance

v0.6 is a controlled manual/local input layer. It is not live ingestion.

The purpose of v0.6 is to make human-supplied local text explicit, auditable, and limited before any later ingestion work is considered. A manually supplied article, excerpt, or paste is an assertion container. It is evidence that the user supplied text for inspection; it is not evidence that the text is true.

v0.6 must preserve the Lumen doctrine:

- methods over conclusions;
- more informed humans, not a new oracle;
- articles are containers of claims, not facts;
- unknown, unresolved, and contested are valid outputs;
- confidence is a method signal, not a truth verdict;
- audit traces explain transformations, not real-world correctness.

## In scope

v0.6 may add or document only these capability boundaries:

- controlled manual text submission;
- controlled manual text submission only; file parsing remains deferred unless a later scope explicitly adds it;
- explicit source labels supplied by the user;
- deterministic normalization from submitted payload into a RawDocument record;
- deterministic derivation of a SourceDocument record used by analysis routes;
- audit events for submission, normalization, extraction, scoring, contradiction exposure, briefing, and verification;
- visible limitations stating that manual input is an assertion container;
- API documentation for `POST /ingest/manual` as the controlled manual/local input boundary;
- compatibility mapping from existing `POST /analyze` local-text behavior to the v0.6 document lifecycle.

## Out of scope

v0.6 must not include:

- URL fetching;
- URL crawling;
- RSS polling;
- live feeds;
- scraping;
- automated source discovery;
- network retrieval from submitted links;
- paid APIs;
- LLM extraction or hosted model calls;
- telemetry or analytics;
- accounts, authentication, personalization, or user profiles;
- database persistence, object storage, vector stores, queues, background jobs, or storage complexity beyond local in-memory/local deterministic demo state;
- production source coverage;
- final truth/oracle/verdict claims;
- automatic settlement of contradictions;
- treating article text, source labels, or user metadata as facts.

If a submitted manual payload contains a URL-looking string, v0.6 treats it as text metadata only. It must not fetch it, follow it, validate it over the network, enrich it, or imply the content at that URL was inspected.

## Manual input truth boundary

Manual input is an assertion container.

Allowed claims about manual input:

- the user supplied this text for inspection;
- Lumen transformed the supplied payload into inspectable local objects;
- Lumen extracted placeholder/local claims under documented limitations;
- Lumen attached confidence reasons, uncertainty, limitations, and audit references to the resulting objects.

Forbidden claims about manual input:

- the supplied article is true;
- the source label is authoritative;
- a URL in the text was inspected;
- the source exists or was contacted;
- the content is complete, current, or representative;
- Lumen has verified real-world correctness.

## Required user-visible limitations

Any v0.6 output derived from manual input must disclose:

- controlled manual/local input only;
- no live retrieval, crawling, scraping, RSS, or network enrichment;
- submitted text/articles are containers of claims, not facts;
- source labels are user assertions unless backed by supplied evidence;
- placeholder extraction is not production-grade semantic extraction;
- confidence values are method signals and remain contestable;
- audit references trace local transformations and do not prove the underlying claim.

## Route boundary

`POST /ingest/manual` is the v0.6 boundary for turning controlled local input into document records. It should produce a document-lifecycle response, not a final claim verdict.

`POST /analyze` may remain as the legacy/local analysis shortcut while v0.6 is introduced, but architecture docs must distinguish:

- ingestion/manual submission: create/normalize local document containers;
- analysis: inspect claims derived from those local containers;
- audit verification: check local method-trace consistency.

The route must be deterministic and local. It must not open network sockets, require secrets, call models, or persist to a production database in the default path.

## Acceptance gate

v0.6 architecture is acceptable only when:

- `V0_6_SCOPE.md` clearly says v0.6 is controlled manual/local input only;
- `CONTROLLED_INPUT_LAYER.md` defines RawDocument and SourceDocument lifecycle states;
- `API_CONTRACT.md` documents `POST /ingest/manual` without implying live ingestion;
- `MVP_PHASES.md`, `ROADMAP_TO_V1.md`, and `DEFERRED_WORK.md` keep URL/RSS/live ingestion deferred;
- docs preserve uncertainty and no-final-verdict wording;
- verification can run locally without secrets, network, paid services, telemetry, accounts, or LLM calls.
