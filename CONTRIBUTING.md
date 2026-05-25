# Contributing to Lumen

Lumen welcomes contributions that make claim inspection, evidence visibility, uncertainty handling, provenance, governance, and auditability clearer.

The project doctrine is mandatory:

- Methods over conclusions.
- More informed humans, not a new oracle.
- Lumen does not determine truth.
- Unknown, unresolved, unsupported, contradicted, and contested are valid outcomes.
- Confidence is a documented method signal, not a command to believe.

## Before you contribute

Read these first:

- `CONSTITUTION.md`
- `LIMITATIONS.md`
- `README.md`
- `docs/architecture/MVP_SCOPE.md`
- `docs/architecture/API_CONTRACT.md`
- `docs/architecture/DEMO_FLOW.md`
- `docs/governance/GOVERNANCE_RULES.md`
- `docs/governance/CONFIDENCE_SCORING.md`
- `ADVERSARIAL_REVIEW.md`

If your change affects a public output, confidence scoring, limitation disclosure, audit trail, source-dependency logic, or demo wording, treat it as a governance-relevant change.

## Current scope boundary

The current v0.5 demo is local, deterministic, fixture-backed, and limited. The public UI is a simplified claim story with Story, Evidence, Why uncertain, and Audit tabs.

Do not add or imply:

- live ingestion, crawling, RSS polling, or URL fetching;
- paid APIs, secrets, telemetry, or hidden network calls;
- LLM calls in the default local demo path;
- production claim extraction, live retrieval, or global source coverage;
- article-level truth labels or final authority language;
- propaganda-detection, deception-proof, or perfect-neutrality claims;
- blockchain anchoring, accounts, personalization, or database complexity unless explicitly scoped later.

Use controlled fixtures and explicit limitation labels. If a capability is partial, fixture-backed, stubbed, or deferred, say so close to the output. Do not describe legacy internal components as the current public UI.

## Public wording rules

Allowed framing:

- "Lumen exposes claims, evidence, uncertainty, provenance, and audit trails."
- "Confidence explains the documented rule path for available inputs."
- "The demo uses controlled fixtures."
- "Audit trails record method traceability."
- "Contradictions are exposed, not automatically resolved."

Avoid or explicitly prohibit:

- "Lumen proves..."
- "Lumen settles..."
- "truth score" or "truth engine"
- "production intelligence"
- "global coverage"
- "propaganda detector"
- "deception proof"
- any language that tells users what to believe.

## Development setup

Backend:

```bash
cd apps/api
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[test]"
uvicorn app.main:app --reload
```

Frontend:

```bash
cd apps/web
npm install
npm run dev
```

Optional local Compose path:

```bash
docker compose --profile dev up
```

If the Compose path drifts from package metadata, prefer the explicit backend/frontend commands and update Compose in a scoped infrastructure change.

## Verification expectations

Run the checks relevant to your change. For full local demo verification from the repo root:

```bash
bash scripts/verify_lumen.sh
```

The aggregate gate prefers `.venv/bin/python` when present, so contributors do
not accidentally treat a host Python without pytest as a product regression.

For docs or UI wording changes, also scan for overclaiming language and inspect matches manually:

```bash
git grep -nE 'truth machine|truth score|truth engine|oracle|proves|settles|final verdict|production intelligence|global coverage|propaganda detector|propaganda detection|deception proof'
```

A match is acceptable only when it appears as a prohibition, limitation disclosure, or governance warning.

## Pull request checklist

A contribution is not ready for review unless it answers:

- What claim-inspection, evidence-visibility, uncertainty, provenance, or audit problem does this improve?
- Which files and public surfaces changed?
- Which limitations remain visible to users?
- Which governance/scoring/audit rules are affected?
- Which tests or verification commands were run?
- Does the change preserve controlled-fixture boundaries?
- Does the change avoid hidden scoring, hidden weighting, telemetry, secrets, paid APIs, and fake capability claims?
- Does the change avoid overwriting, deleting, or mutating original evidence without explicit review?

## Challenge and review path

Use `ADVERSARIAL_REVIEW.md` to challenge a rule, output, score, limitation disclosure, audit trail, or wording choice.

Accepted or partially accepted challenges should update the relevant docs, tests/evals, and audit notes. Governance changes must be public, versioned, and reviewable; silent scoring or disclosure changes are prohibited.
