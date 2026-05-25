# Lumen v0.6 Verification Checklist

Version: v0.6-controlled-manual-input-layer

## Scope lock

v0.6 verifies the controlled manual/local input layer. It is not live ingestion and not a production truth service.

Required boundary statements:

- Manual input is an assertion container, not truth.
- Articles and submitted text are containers of claims, not facts.
- Local/manual analysis must not fetch URLs, crawl, poll RSS, call LLMs, require paid APIs, require secrets, create accounts, send telemetry, or persist production data.
- Confidence is a visible method signal with reasons, not a final verdict.
- Audit traces explain transformations; they do not prove the underlying claim.

## Required local gates

Run from repository root:

```text
bash scripts/verify_lumen.sh
```

The aggregate gate must include:

- institutional-memory strict index validation;
- project-contamination scan;
- redacted secret literal scan;
- explicit backend manual/local input contract pytest gate;
- full backend pytest suite;
- API compile check;
- static UI verifier;
- web typecheck.

## Backend manual/local input checks

The following focused checks are release blockers for this lane:

```text
.venv/bin/python -m pytest \
  apps/api/tests/test_api_contract.py::test_analyze_returns_stable_v03_contract_with_local_input_evidence \
  apps/api/tests/test_api_contract.py::test_analyze_route_returns_local_input_contract_without_external_capability_claims \
  -q
```

Expected behavior:

- `/analyze` returns `mode: local_input`.
- Local input evidence uses `provenance: local_user_input`.
- Claims preserve status, confidence reasons, evidence refs, audit refs, and limitation refs.
- Limitations disclose no LLM calls and no real-time ingestion.
- The response does not claim external retrieval, semantic production extraction, broad verification, or truth determination.

## Public UI checks

The main public UI must remain the simplified four-tab claim story:

- Story
- Evidence
- Why uncertain
- Audit

The public UI must not show raw hashes, IDs, `.md` names, underscores/machine labels, provenance jargon, dense dashboard language, or final-verdict wording.

The public UI may mention local/manual input only as a boundary disclosure. It must not add a manual-input workflow to the public demo page in this lane.

## Eval and backlog checks

- `evals/golden_cases.json` must describe the four-tab public UI verifier and manual/local input contract without stale seven-panel public dashboard requirements.
- `evals/eval_plan.md` must state that manual/local input evals assert containment and auditability, not truth.
- `docs/backlog/PUBLIC_BACKLOG.md` must keep URL fetching, RSS, live monitoring, LLM extraction/calls, paid APIs, telemetry, auth/accounts, database persistence, and production truth/oracle claims deferred.

## Institutional-memory checks

If a v0.6 swarm AAR is created or changed, regenerate and validate indexes:

```text
python3 scripts/regen_indexes.py --check --strict
python3 scripts/regen_indexes.py
python3 scripts/regen_indexes.py --check --strict
```

Postmortem decision rule:

- Write a postmortem only for a qualifying failure, near-miss, schema/architecture drift, verifier failure requiring remediation, or non-obvious fix.
- Do not create a ceremonial postmortem when the lane only updates planned v0.6 verification artifacts and all gates pass.

## Launch blocker language

Block release if any v0.6 artifact implies:

- live ingestion exists;
- URL/RSS/network fetching is active;
- LLM extraction or external model calls are in the default path;
- paid APIs or secrets are required;
- telemetry, accounts, auth, or production database persistence are present;
- an article or manual input can be declared true/false as a final verdict;
- audit records prove the real-world claim rather than the method path.
