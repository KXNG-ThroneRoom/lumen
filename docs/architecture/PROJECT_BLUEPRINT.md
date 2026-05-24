

# Lumen — Project Blueprint

## 1. Mission

Lumen is free, open-source epistemic infrastructure for public-interest information analysis.

Lumen does not tell users what is true.

Lumen helps users form more informed conclusions by exposing:

- claims
- evidence
- contradictions
- uncertainty
- source provenance
- source dependency
- incentive structures
- narrative framing
- missing context
- confidence logic
- audit trails

The purpose of Lumen is to democratize analytical methods normally available to intelligence analysts, investigators, journalists, researchers, policy professionals, institutions, and highly trained operators.

Lumen exists for humans.

It is not a replacement for human judgment. It is a system for improving the quality of human judgment.

---

## 2. Core Philosophy

Lumen is built on one central distinction:

> We do not sell conclusions. We expose methods.

Lumen does not claim to produce objective truth.

Instead, Lumen structures public information into inspectable analytical objects so users can understand:

- what is being claimed
- who is claiming it
- what evidence exists
- what evidence is missing
- what claims contradict each other
- what narratives are being constructed
- what incentives may be present
- how confidence was assigned
- why uncertainty remains

Lumen is not anti-media, anti-government, anti-institution, or anti-establishment.

Lumen is:

- pro-transparency
- pro-evidence
- pro-auditability
- pro-methodology
- pro-uncertainty
- pro-human judgment

---

## 3. Product Category

Lumen is not a traditional news app.

It is best understood as:

- open-source intelligence analysis infrastructure
- transparent claim and evidence analysis
- narrative and contradiction mapping
- provenance-aware public information tooling
- uncertainty-first briefing infrastructure

Comparable inspirations:

- OSINT workflows
- investigative journalism workflows
- intelligence briefings
- Ground News-style source comparison
- Wikipedia-style public knowledge contribution
- Git-style public versioning
- cryptographic audit trails
- evidence-based legal reasoning
- scientific reproducibility

---

## 4. Non-Goals

Lumen will not:

- declare final truth
- enforce political ideology
- secretly weight sources
- hide scoring logic
- hide prompts
- hide model versions
- sell access to conclusions
- optimize for outrage
- optimize for engagement loops
- become a partisan fact-checker
- claim certainty where evidence is insufficient
- treat article volume as proof
- treat institutional consensus as automatic truth
- treat anti-institutional narratives as automatic truth

---

## 5. Core User Experience

For any major story, Lumen should answer:

```text
What is being claimed?
Who is claiming it?
What is the original source?
What evidence supports it?
What evidence contradicts it?
What evidence is missing?
What narrative frame is being used?
Who benefits from this framing?
How independent are the sources?
How confident should we be?
What remains unresolved?
The UI should be an intelligence dashboard, not a news feed.
Core screens:
1. Briefing Panel
    * short structured summary
    * confidence rating
    * unresolved questions
    * watch indicators
2. Claim Matrix
    * atomic claims
    * claim type
    * supporting evidence
    * contradicting evidence
    * confidence
    * status
3. Evidence Trail
    * raw sources
    * primary evidence
    * quotes
    * documents
    * datasets
    * archived links
4. Narrative Map
    * hero
    * villain
    * victim
    * threat
    * proposed solution
    * omitted context
    * emotional language
5. Source Spread
    * source geography
    * ownership
    * political leaning where available
    * state/private affiliation
    * local/global distinction
    * source independence
6. Contradiction Board
    * conflicting claims
    * unresolved disputes
    * source disagreement
    * evidence gaps
7. Audit Trail
    * every transformation
    * every scoring decision
    * every rule applied
    * model/prompt/version metadata
    * hash-chain verification

⸻

6. System Architecture
Ingestion Layer
  ↓
Raw Evidence Archive
  ↓
Article / Document Parser
  ↓
Atomic Claim Extractor
  ↓
Claim Normalizer
  ↓
Source Graph
  ↓
Evidence Matcher
  ↓
Contradiction Detector
  ↓
Narrative Analyzer
  ↓
Governance + Confidence Scoring
  ↓
Audit Ledger
  ↓
Briefing Engine
  ↓
User Interface / API / CLI

⸻

7. Core Modules
7.1 Ingestion Layer
Purpose:
* ingest public information sources
* preserve raw input
* record collection metadata
* avoid mutating originals
Initial sources:
* RSS feeds
* manually provided URLs
* static example JSON
* future: GDELT
* future: Media Cloud
* future: ClaimReview-compatible fact-check data
* future: public primary-source repositories
Initial MVP should not require paid APIs.

⸻

7.2 Raw Evidence Archive
Purpose:
* preserve raw source material
* maintain original text
* store metadata
* support auditability
Every raw object should include:
id
source_url
source_name
author
published_at
collected_at
raw_text
content_hash
archive_reference
ingestion_method
Raw records are immutable.
If source material changes, create a new version.

⸻

7.3 Claim Extraction
Purpose:
Break articles and documents into atomic claims.
A claim is not an article.
A claim is a specific assertion that can be inspected, supported, contradicted, or left unresolved.
Example:
Bad:
"Article says Iran escalated tensions."

Good:
"On DATE, SOURCE claimed that ACTOR performed ACTION against TARGET at LOCATION."
Claim fields:
id
source_document_id
raw_claim_text
normalized_claim
claim_type
actors
targets
location
time_range
evidence_refs
contradiction_refs
confidence_score
status
created_at
Claim types:
* factual claim
* causal claim
* legal claim
* statistical claim
* attribution claim
* quote claim
* prediction
* speculation
* moral framing
* image/video authenticity claim
* anonymous-source claim
* expert interpretation

⸻

7.4 Source Graph
Purpose:
Track whether multiple reports are actually independent.
Source graph should model:
source
author
publisher
owner
country
language
source_type
funding
wire_dependency
citation_dependency
political/ideological metadata when available
correction history
reliability notes
Important rule:
Ten articles repeating one wire report count as one evidence stream, not ten.

⸻

7.5 Evidence Layer
Purpose:
Link claims to evidence.
Evidence types:
primary_document
official_dataset
court_filing
full_transcript
raw_video
raw_image
satellite/geolocation evidence
named_on_record_source
local_direct_reporting
wire_report
anonymous_source
expert_interpretation
social_media_post
opinion/commentary
Evidence is scored by:
* proximity
* provenance
* independence
* specificity
* verifiability
* timestamp quality
* chain of custody
* contradiction status

⸻

7.6 Contradiction Detection
Purpose:
Detect when claims conflict.
Contradiction types:
actor contradiction
time contradiction
location contradiction
causal contradiction
numerical contradiction
legal interpretation contradiction
source attribution contradiction
media authenticity contradiction
omission contradiction
The system should not automatically resolve contradictions.
It should expose them.

⸻

7.7 Narrative Analysis
Purpose:
Detect framing patterns.
Narrative fields:
hero
villain
victim
threat
solution
moral frame
emotional language
omitted context
beneficiary
amplifiers
repeated phrases
Narrative analysis should be clearly labeled as analysis, not fact.

⸻

7.8 Governance + Scoring
Purpose:
Apply transparent rules to confidence and status.
Statuses:
confirmed
strongly_corroborated
probable
plausible
contested
unsupported
contradicted
narrative_only
unknown
Core scoring principles:
* primary evidence outranks commentary
* source independence matters
* anonymous claims are capped
* official statements are interested-party claims
* article volume is not proof
* hostile-source agreement increases confidence
* missing primary evidence lowers confidence
* contradiction lowers confidence
* uncertainty must remain visible
Every score must be explainable.

⸻

7.9 Audit Ledger
Purpose:
Create append-only traceability.
Every transformation must produce an audit event:
raw input collected
article parsed
claim extracted
claim normalized
evidence attached
contradiction detected
score assigned
narrative frame generated
briefing generated
human edit made
governance rule changed
Each audit event should include:
event_id
timestamp
actor_type
actor_id
input_hash
output_hash
previous_event_hash
event_hash
operation
reason
rule_version
model_version
prompt_hash
code_version
The audit ledger should be hash-chained.
Blockchain is optional later.
The MVP should implement local tamper-evident append-only logs first.

⸻

7.10 Briefing Engine
Purpose:
Generate concise, structured intelligence-style briefings.
Briefing format:
Topic:
Bottom line:
Confidence:
What changed:
Key claims:
Evidence:
Contradictions:
Missing information:
Narrative frames:
Incentives:
Watch indicators:
Unresolved questions:
Audit reference:
Briefings must never hide uncertainty.

⸻

8. MVP Scope
The first MVP should support:
Input:
- one article URL or sample article JSON
- optional topic cluster JSON

Output:
- extracted claim matrix
- source metadata
- basic evidence trail
- simple narrative map
- deterministic confidence scoring
- audit log
- static briefing panel
MVP should include:
* FastAPI backend
* Next.js frontend
* sample JSON data
* deterministic scoring rules
* append-only audit ledger
* basic tests
* Docker Compose
* clear docs
* visible limitations
MVP should not include:
* real-time global ingestion
* blockchain
* paid API dependencies
* production-scale search
* user accounts
* complex moderation
* claims of real-world verification
* automatic final truth determination

⸻

9. Suggested Tech Stack
Backend:
Python
FastAPI
Pydantic
SQLite for MVP
Postgres later
pytest
Frontend:
Next.js
TypeScript
Tailwind
React components
Static mock data first
Data / Retrieval later:
Postgres
pgvector
Neo4j or graph layer
OpenSearch
Object storage
Audit:
JSONL append-only event log
SHA-256 hash chain
signed release artifacts later
Deployment:
Docker Compose for local
Vercel frontend optional
Railway/Fly/Render backend optional
Self-hosting preferred

⸻

10. Open Source Packaging
Lumen should be easy to run locally:
git clone <repo>
cd lumen
docker compose up
Developer path:
cd apps/api
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest

cd ../web
npm install
npm run dev
Repository structure:
lumen/
  apps/
    api/
    web/
  packages/
    ingestors/
    claim_extractor/
    governance/
    scoring/
    audit_ledger/
    briefing/
    source_graph/
  docs/
    architecture/
    governance/
    audits/
  evals/
  examples/
  scripts/
  data/

⸻

11. Evaluation Strategy
Lumen must be evaluated on methods, not vibes.
Initial eval categories:
claim_extraction_accuracy
claim_type_accuracy
source_dependency_detection
anonymous_source_cap_enforcement
contradiction_detection
primary_evidence_boost
unsupported_claim_detection
unknown_status_correctness
narrative_frame_detection
audit_chain_integrity
Golden cases should test:
* anonymous single-source claim
* many articles from same wire source
* primary document contradiction
* headline stronger than article body
* official statement with incentive conflict
* hostile sources agreeing on one fact
* missing denominator in statistical claim
* old image presented as new
* unresolved claim with insufficient evidence

⸻

12. Design Direction
Aesthetic:
dark
raw
intelligence-dashboard
minimal
sharp
monospace accents
not glossy
not cartoon SaaS
Emotional tone:
calm
serious
transparent
precise
non-partisan
anti-oracle
The UI should feel like a public intelligence terminal.

⸻

13. First Build Sprint
Goal:
Create the Lumen scaffold.
Deliverables:
README.md
CONSTITUTION.md
PROJECT_BLUEPRINT.md
GOVERNANCE_RULES.md
CONFIDENCE_SCORING.md
AUDIT_TRAIL_SPEC.md
BIAS_RESISTANCE.md

FastAPI scaffold
Next.js scaffold
sample JSON files
audit ledger primitive
scoring primitive
claim matrix component
briefing panel component
tests
scaffold audit report
Acceptance criteria:
* project runs locally or has clear run instructions
* no legacy project references
* no fake capability claims
* no hidden scoring
* no secrets
* no paid API dependency
* audit trail design is present
* method-first philosophy is clear
* unknown/unresolved status exists
* UI shows the product direction
---
