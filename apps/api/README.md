# Lumen API

Local deterministic backend core for the Lumen v0.5 controlled demo path.

This service exposes claim-level primitives for a fixture-backed/sample flow. It does not perform real-time ingestion, crawl URLs, call LLMs, use paid APIs, use secrets, or present conclusions as final truth. Its job is to make the method path inspectable: claims, evidence references, uncertainty, scoring reasons, limitations, and audit references.

Routes:

- `GET /health` — service and doctrine status.
- `GET /sample` — deterministic controlled fixture analysis for the local demo.
- `POST /analyze` — deterministic local placeholder analysis for supplied text.
- `POST /ingest/manual` — controlled manual text assertion container with no URL fetching or live ingestion.
- `GET /audit/verify` — verifies the in-memory sample audit hash chain.

Demo-path stability notes:

- `/health` reports backend version `0.4.0` while the analysis envelope remains
  `lumen.analysis.v0.3`; v0.5 launch hygiene does not change the API schema or
  backend product behavior.
- `/sample` returns the controlled fixture topic `Fixture: regulation start-date
  contradiction` using local fixture data only.
- `/analyze` treats user-supplied text as local evidence that a claim was
  supplied, not evidence that the claim is true.
- `/ingest/manual` accepts the canonical `raw_text` + `input_method:
  manual_text` request shape and rejects legacy aliases before external clients
  depend on them.
- Claims expose `status`, `confidence_score`, `confidence_reason`,
  `evidence_refs`, `audit_reference`, and `limitations_ref`.
- Briefings expose uncertainty language, `limitations`, `limitations_ref`, and
  `audit_reference`.
- Confidence scores are deterministic method/scoring signals, not verdicts or
  instructions to believe a claim.
- Audit references and `/audit/verify` describe transformation-trace consistency;
  they do not prove the underlying claim.
- No route performs LLM calls, paid API calls, live ingestion, telemetry, or
  hidden network behavior.

Local run from repo root after installing dependencies in the project environment:

```bash
source .venv/bin/activate
python -m pip install -e 'apps/api[test]'
uvicorn --app-dir apps/api app.main:app --reload
```

Equivalent local run from `apps/api` after activating `.venv`:

```bash
cd apps/api
python -m pip install -e '.[test]'
uvicorn app.main:app --reload
```

Preferred verification from repo root:

```bash
bash scripts/verify_lumen.sh
```

The aggregate verifier selects `.venv/bin/python` when present, then falls back
to `python3` from `PATH`. Activate the project environment for consistent local
commands and dependency resolution:

```bash
source .venv/bin/activate
bash scripts/verify_lumen.sh
```

Focused API verification from repo root after activating `.venv`:

```bash
python -m pytest apps/api/tests -q
python -m compileall apps/api/app
```

Limitations:

- Claim extraction is a transparent placeholder and returns limitation metadata.
- Contradiction detection is fixture/rule based only.
- Confidence scores are deterministic method signals, not truth verdicts.
- Audit storage is local/in-memory for the MVP route path; durable append-only storage is deferred.
