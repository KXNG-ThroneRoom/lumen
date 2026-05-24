# Lumen

Lumen is free, open-source epistemic infrastructure for public-interest information analysis.

It does not tell users what is true. It exposes methods: claims, evidence, contradictions, uncertainty, source provenance, source dependency, narrative framing, confidence logic, and audit trails so humans can form better judgments.

## Doctrine

- Methods over conclusions.
- More informed humans, not a new oracle.
- Articles are containers of claims, not facts.
- The claim is the unit of analysis.
- Unknown, unresolved, and contested are valid outputs.
- Confidence must be explainable and linked to evidence.
- Every meaningful transformation must be auditable.
- Governance rules must be visible and versioned.

## MVP shape

The first scaffold is intentionally narrow:

- FastAPI backend for local deterministic primitives.
- Next.js static intelligence-dashboard UI.
- Sample JSON inputs and outputs.
- Deterministic confidence scoring rules.
- Local append-only hash-chained audit ledger primitive.
- Evaluation golden cases focused on method quality.

The MVP does not include real-time production ingestion, paid APIs, user accounts, blockchain, production-scale search, or any claim of complete real-world verification.

## Repository map

```text
apps/api/                  FastAPI scaffold and deterministic primitives
apps/web/                  Next.js static UI scaffold
packages/governance/       Versioned governance method package boundary
packages/scoring/          Transparent confidence scoring boundary
packages/audit_ledger/     Append-only audit ledger boundary
packages/claim_extractor/  Claim extraction boundary
packages/ingestors/        Input preservation and ingestion boundary
packages/source_graph/     Source dependency and provenance boundary
packages/briefing/         Briefing generation boundary
docs/architecture/         System design, MVP boundaries, data model
docs/governance/           Public rules and scoring doctrine
docs/audits/               Scaffold audit artifacts
examples/                  Deterministic sample data
evals/                     Evaluation plan and golden cases
```

## Local development

The scaffold is designed to run locally with open-source infrastructure only. Until backend and frontend workers finish their domains, treat the commands below as the intended local interface rather than a production promise.

```bash
# backend, after apps/api is present
cd apps/api
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest

# frontend, after apps/web is present
cd apps/web
npm install
npm run dev
```

Docker Compose is included as a local-development entry point and may require the backend/frontend scaffolds to be present before all services start.

## Trust model

Lumen earns trust by being inspectable, not authoritative. Outputs must preserve uncertainty and expose the reasons behind confidence assignments. Narrative analysis is analysis, not fact. Audit logs are tamper-evident design primitives, not a blockchain implementation.
