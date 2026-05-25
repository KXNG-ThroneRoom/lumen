# Lumen

Lumen is free, open-source infrastructure for inspecting public-interest claims.

It does not tell users what is true. It exposes methods, evidence, claims, contradictions, uncertainty, source provenance, source dependency, narrative framing, confidence logic, limitations, and audit trails so humans can form better judgments.

## What Lumen is

- A local-first method demonstration for claim-level analysis.
- A way to inspect how evidence, source dependency, contradictions, and uncertainty affect confidence explanations.
- A governance-first project where scoring rules, limitation disclosures, and audit requirements are public.
- A demo surface for controlled fixtures and manually supplied local text.

## What Lumen is not

- Not an oracle, truth machine, or automated final authority.
- Not a production intelligence system.
- Not live geopolitical or current-events analysis.
- Not global source coverage, broad web search, or production ingestion.
- Not propaganda detection, deception proof, or proof of intent.
- Not a paid-API, telemetry, account, blockchain, or hidden-hosted-service product.

## Doctrine

- Methods over conclusions.
- More informed humans, not a new oracle.
- Articles are containers of claims, not facts.
- The claim is the unit of analysis.
- Unknown, unresolved, unsupported, contradicted, and contested are valid outputs.
- Confidence must be explainable and linked to evidence and limitations.
- Every meaningful transformation must be auditable.
- Governance rules must be visible and versioned.

## Current demo boundary

The current MVP is intentionally narrow: local, deterministic, fixture-backed, and limited. It demonstrates the method and interface contract; it does not demonstrate complete real-world verification.

Current demo commitments:

- FastAPI backend for local deterministic primitives.
- Next.js dashboard UI for claim, evidence, contradiction, source, narrative, briefing, and audit panels.
- Controlled fixture data and manually supplied local text only.
- Deterministic confidence scoring rules with visible reasons.
- Local hash-chained audit ledger primitive.
- Evaluation/golden cases focused on method quality.
- Visible limitations close to outputs.

Current demo limits:

- No real-time ingestion, crawling, RSS polling, or URL fetching.
- No paid APIs, secrets, telemetry, or hidden network calls.
- No LLM calls in the default local demo path.
- No production-scale retrieval or global source coverage.
- No user accounts or personalization.
- No blockchain anchoring.
- No article-level truth labels or final reality determination.

See `LIMITATIONS.md` for the public limitation disclosure and `ADVERSARIAL_REVIEW.md` for the public challenge path.

## Repository map

```text
apps/api/                  FastAPI scaffold and deterministic primitives
apps/web/                  Next.js dashboard UI scaffold
packages/governance/       Versioned governance method package boundary
packages/scoring/          Transparent confidence scoring boundary
packages/audit_ledger/     Append-only audit ledger boundary
packages/claim_extractor/  Claim extraction boundary
packages/ingestors/        Input preservation and ingestion boundary
packages/source_graph/     Source dependency and provenance boundary
packages/briefing/         Briefing generation boundary
docs/architecture/         System design, MVP boundaries, API contract, demo flow
docs/governance/           Public rules and scoring doctrine
docs/audits/               Scaffold and release-readiness audit artifacts
examples/                  Deterministic sample data
evals/                     Evaluation plan and golden cases
```

## Run locally

These commands are for local development and inspection. They are not a production deployment path.

### Backend API

```bash
cd apps/api
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[test]"
uvicorn app.main:app --reload
```

Useful local endpoints:

```text
GET  http://localhost:8000/health
GET  http://localhost:8000/sample
POST http://localhost:8000/analyze
GET  http://localhost:8000/audit/verify
```

The expected response contract is documented in `docs/architecture/API_CONTRACT.md`.

### Frontend dashboard

```bash
cd apps/web
npm install
npm run dev
```

Open the local Next.js URL printed by the dev server, usually `http://localhost:3000`.

### Optional Docker Compose development path

```bash
docker compose --profile dev up
```

The Compose path is a convenience for local development. If dependency metadata changes, prefer the explicit backend and frontend commands above until Compose is updated.

## Verify the demo boundary

From the repo root, use the aggregate local gate:

```bash
bash scripts/verify_lumen.sh
```

The aggregate gate prefers `.venv/bin/python` when present and then runs API
tests, API compile checks, static UI verification, web typecheck, and
institutional-memory index validation.

Before claiming launch-readiness, also inspect docs and UI copy for overclaims:

```bash
git grep -nE 'truth machine|oracle|proves|settles|production intelligence|global coverage|propaganda detection|deception proof'
```

Allowed occurrences should be explicit prohibitions or limitation disclosures, not product promises.

## Governance and public challenge path

Start with these documents:

- `CONSTITUTION.md` — project doctrine and non-oracle requirements.
- `LIMITATIONS.md` — current MVP limitations and demo disclosure requirements.
- `docs/governance/GOVERNANCE_RULES.md` — required output, limitation, audit, and UI rules.
- `docs/governance/CONFIDENCE_SCORING.md` — confidence methodology and caps.
- `docs/architecture/MVP_SCOPE.md` — current in-scope and out-of-scope boundaries.
- `docs/architecture/API_CONTRACT.md` — local API response contract.
- `docs/architecture/DEMO_FLOW.md` — safe demo sequence and failure states.
- `ADVERSARIAL_REVIEW.md` — how to challenge outputs, rules, limitations, audit completeness, or wording.
- `CONTRIBUTING.md` — contributor onboarding and review expectations.

## Trust model

Lumen earns trust by being inspectable, not authoritative. Outputs must preserve uncertainty and expose the reasons behind confidence assignments. Narrative analysis is analysis, not fact. Audit logs are tamper-evident design primitives that record method traceability; they do not prove that an underlying claim is correct.
