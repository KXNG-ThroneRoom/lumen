# Lumen Fresh-Clone Readiness

Version: v0.5.1-stabilization-hygiene

## Purpose

This document describes the expected fresh-clone path for the current controlled local demo. It is an operator and contributor checklist, not a production deployment guide.

The goal is that a new reviewer can install dependencies, run the local verification gate, and start the controlled demo with no secrets, accounts, paid services, telemetry, live ingestion, and no LLM calls.

## Current demo boundary

Fresh-clone readiness applies only to the v0.5/v0.5.1 local deterministic fixture demo:

- one claim story: "When does the regulation start?";
- simplified public UI with Story, Evidence, Why uncertain, and Audit tabs;
- local FastAPI backend primitives;
- local Next.js frontend demo;
- controlled fixture data;
- aggregate local verification via `bash scripts/verify_lumen.sh`.

It does not prove production readiness, live source coverage, broad claim verification, or final truth determination.

## Known environment assumptions

Expected local tools:

- Git.
- Python 3 with `venv` support.
- Node.js and npm compatible with the web app package metadata.
- Bash or a Bash-compatible shell for `scripts/verify_lumen.sh`.
- Localhost ports available for the API and web dev servers, usually 8000 and 3000.

Network expectations:

- Dependency installation may require normal package-registry access.
- Running the demo and verifier after dependencies are installed should not require live news feeds, paid APIs, secrets, telemetry, user accounts, or LLM services.

Repository assumptions:

- Commands below are run from the repository root unless a step explicitly changes directories.
- The default demo path is local and deterministic.
- Existing fixture data is the source of the public demo story.

## Expected install flow

From a fresh clone:

```bash
git clone <lumen-repo-url> lumen
cd lumen
```

Backend setup:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e "./apps/api[test]"
```

Frontend setup:

```bash
npm install --prefix apps/web
```

Notes:

- The aggregate verifier prefers `.venv/bin/python` when present.
- If backend dependency metadata changes, keep this document and `scripts/verify_lumen.sh` aligned.
- If frontend dependency metadata changes, keep this document and `apps/web/README.md` aligned.
- Optional Docker Compose development paths are convenience paths; the explicit backend/frontend setup above is the fresh-clone baseline.

## Verification flow

Run the aggregate gate from the repository root:

```bash
bash scripts/verify_lumen.sh
```

Expected gate coverage:

- institutional-memory index validation when the index script is present;
- project contamination scan;
- secret literal scan;
- API tests;
- API compile check;
- static UI verification;
- web typecheck.

Expected result for a ready local environment:

```text
RESULT PASS
```

If `apps/web/node_modules` is missing, the web gates are expected to skip/fail with an instruction to run `npm install --prefix apps/web`. That is an environment-readiness issue, not an analytical capability issue.

For documentation or public wording changes, also inspect overclaim language manually. Matches are acceptable only when they are prohibitions, limitation disclosures, or governance warnings.

## Local demo flow

Start the backend from the repository root after backend setup:

```bash
source .venv/bin/activate
uvicorn apps.api.app.main:app --reload
```

Start the frontend in a separate shell after frontend setup:

```bash
npm run dev --prefix apps/web
```

Open the local Next.js URL printed by the dev server, usually:

```text
http://localhost:3000
```

The public page should show:

- "Lumen local demo";
- "Methods over conclusions";
- main claim: "When does the regulation start?";
- a contested story where a news report and official filing disagree;
- tabs named Story, Evidence, Why uncertain, and Audit;
- controlled-local-demo and no-final-verdict language.

The public page should not show raw hashes, raw audit IDs, `.md` file references, machine labels, provenance jargon, or old dense dashboard wording as the main user experience.

## Optional API inspection

For developer review after the public UI is running, inspect local endpoints:

```text
GET http://localhost:8000/health
GET http://localhost:8000/sample
POST http://localhost:8000/analyze
GET http://localhost:8000/audit/verify
```

API inspection is a developer surface. It must not be presented as proof that the underlying real-world claim is settled.

## Readiness blockers

Treat fresh-clone readiness as blocked if any of these are true:

- dependency install requires undocumented credentials or paid services;
- verifier requires live feeds, LLM calls, telemetry, accounts, or hidden network services;
- the public UI does not show the simplified four-tab claim story;
- the public UI implies the start-date dispute is settled;
- public docs describe the old dense dashboard as the current user experience;
- verification failures are not documented or are misrepresented as passes;
- setup docs drift from `scripts/verify_lumen.sh` or the app package metadata.

## What this does not certify

Fresh-clone readiness does not certify:

- production deployment safety;
- global source coverage;
- real-time ingestion;
- broad contradiction detection;
- robust claim extraction;
- source-independence inference;
- tamper-proof audit guarantees;
- final truth determination.

Those remain deferred unless a later scope document explicitly brings them into scope with governance, security, tests, limitations, and human approval.
