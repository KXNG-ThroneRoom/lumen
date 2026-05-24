# Lumen API

Local deterministic backend core for the Lumen v0.2 MVP.

This service exposes claim-level primitives only. It does not perform real-time ingestion, call LLMs, use paid APIs, or present conclusions as final truth.

Routes:

- `GET /health` — service and doctrine status.
- `GET /sample` — fixture-backed structured analysis.
- `POST /analyze` — deterministic local placeholder analysis for supplied text.
- `GET /audit/verify` — verifies the in-memory sample audit hash chain.

Local run after installing dependencies:

```bash
cd apps/api
python3 -m pip install -e '.[test]'
uvicorn app.main:app --reload
```

Verification from repo root:

```bash
python3 -m pytest apps/api/tests -q
python3 -m compileall apps/api/app
```

Limitations:

- Claim extraction is a transparent placeholder and returns limitation metadata.
- Contradiction detection is fixture/rule based only.
- Confidence scores are deterministic method signals, not truth verdicts.
- Audit storage is local/in-memory for the MVP route path; durable append-only storage is deferred.
