# Lumen v0.5.1 Verification Checklist

Purpose: provide a repeatable local gate for v0.5.1 verification reliability and environment hygiene while keeping the demo bounded to verified, deterministic, controlled local behavior.

## Scope boundary

v0.5.1 verification is launch-hygiene verification for the controlled local demo. It is not a production-readiness certification and it does not verify live reality.

The verified demo path must remain:

- local and deterministic;
- fixture-backed or manually supplied local text only;
- free of paid APIs, secrets, telemetry, LLM calls, live ingestion, crawling, accounts, blockchain, and database/storage expansion;
- explicit that confidence scores are method signals, not truth verdicts;
- explicit that audit references verify transformation trace consistency, not the underlying claim.

## Environment expectations

- Run from the repo root: `/Users/amirtbz/lumen`.
- Prefer the project Python environment when present:
  - `source .venv/bin/activate`
- `scripts/verify_lumen.sh` selects `.venv/bin/python` when it exists, then falls back to `python3` from `PATH`.
- The selected Python interpreter must be runnable and must have the API test dependencies installed.
- `apps/web/node_modules` must exist before web verification gates run:
  - `cd apps/web && npm install`
- If `apps/web/node_modules` exists, `npm` must also be available on `PATH`.
- No API keys or external credentials are required for the aggregate verification path.
- Verification should not delete, reset, clean, discard, overwrite committed work, or commit uncommitted work.

## Preferred aggregate command

```bash
bash scripts/verify_lumen.sh
```

The aggregate gate is the preferred verifier for v0.5.1 run-path hygiene. It runs these checks where the corresponding project areas are present:

1. selected Python interpreter discovery and runnability check;
2. institutional-memory index strict check with the selected Python interpreter;
3. project-contamination scan for forbidden foreign-project references;
4. secret literal scan over public docs, verifier scripts, and launch-hygiene artifacts;
5. API pytest with the selected Python interpreter;
6. API compileall with the selected Python interpreter;
7. `npm run verify:static --prefix apps/web` when web dependencies are installed;
8. `npm run typecheck --prefix apps/web` when web dependencies are installed.

The script exits non-zero if any required available gate fails. Web gates are treated as unavailable/failing if `apps/web/package.json` exists but `apps/web/node_modules` is missing, because static verification and typecheck cannot be trusted without installed dependencies. If web dependencies are installed but `npm` is missing, the verifier reports a concise npm discovery failure.

## Backend API verification checks

- [ ] `apps/api/README.md` describes the API as a deterministic controlled demo API, not a production analysis service.
- [ ] Local run commands consistently prefer `.venv` activation and `python -m ...` from that environment.
- [ ] `GET /sample` is described as fixture-backed/sample flow only.
- [ ] `POST /analyze` is described as local input analysis that treats supplied text as supplied evidence, not proof of truth.
- [ ] `GET /audit/verify` is described as checking local sample audit-chain consistency only.
- [ ] Audit/scoring primitives are documented as method traceability and deterministic scoring signals, not final verdicts.
- [ ] API docs explicitly say there is no live ingestion, no LLM calls, no paid APIs, no hidden network behavior, and no telemetry in the local demo path.
- [ ] Any mention of backend version `0.4.0` or schema `lumen.analysis.v0.3` is framed as current API contract stability, not a v0.5/v0.5.1 schema expansion.

## Verifier reliability checks

- [ ] `scripts/verify_lumen.sh` is executable and has valid shell syntax.
- [ ] The verifier can be run from repo root or from a directory inside the repo.
- [ ] The verifier does not install dependencies, mutate source files, call networks, require secrets, or commit work.
- [ ] Missing Python is reported as a Python interpreter discovery/check failure.
- [ ] Missing web dependencies are reported as skipped web gates plus a failing aggregate result.
- [ ] Missing `npm` with installed web dependencies is reported as an npm discovery failure.
- [ ] Scan read errors fail the relevant scan instead of silently passing.
- [ ] Output remains concise: start/pass/fail/skip lines, gate output, aggregate gate count, and final `RESULT PASS` or `RESULT FAIL`.

## Release-blocking audit criteria

- [ ] `bash -n scripts/verify_lumen.sh` passes.
- [ ] `bash scripts/verify_lumen.sh` passes from the repo root, or every failure has an explicit waiver/remediation card.
- [ ] Project-contamination scan reports no forbidden foreign-project references.
- [ ] Secret literal scan reports no credentials, private keys, API key names, or token assignments in scanned public/verifier paths.
- [ ] API tests pass without external credentials.
- [ ] API modules compile.
- [ ] Static web UI verification passes against the simplified tabbed public UI.
- [ ] Web TypeScript typecheck passes.
- [ ] No launch/demo copy claims production readiness beyond verified local behavior.
- [ ] No secrets, tokens, or private credentials appear in verification artifacts.

## Handoff format for verifier cards

Record the exact command and exit status, for example:

```text
command: bash scripts/verify_lumen.sh
exit_status: 0
result: PASS
notes: ran from /Users/amirtbz/lumen; script selected .venv/bin/python; apps/web/node_modules present; contamination and secret scans passed
```

If the command fails, include the failing gate name and the final `RESULT FAIL` line from the script output.
