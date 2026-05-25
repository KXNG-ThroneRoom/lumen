# Lumen v0.5 Verification Checklist

Purpose: provide a repeatable local gate for v0.5 public-MVP announcement hygiene while keeping the demo bounded to verified, deterministic, controlled local behavior.

## Scope boundary

v0.5 verification is launch-hygiene verification for the controlled local demo. It is not a production-readiness certification and it does not verify live reality.

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
- `scripts/verify_lumen.sh` will select `.venv/bin/python` when it exists, then fall back to `python3` from `PATH`.
- If pytest is not installed globally, `.venv` or an equivalent Python environment with API test dependencies is required.
- `apps/web/node_modules` must exist before web verification gates run:
  - `cd apps/web && npm install`
- No API keys or external credentials are required for the aggregate verification path.
- Verification should not delete, reset, clean, discard, overwrite committed work, or commit uncommitted work.

## Preferred aggregate command

```bash
bash scripts/verify_lumen.sh
```

The aggregate gate is the preferred verifier for v0.5 run-path hygiene. It runs these checks where the corresponding project areas are present:

1. institutional-memory index strict check with the script-selected Python interpreter;
2. project-contamination scan for forbidden foreign-project references;
3. secret literal scan over public docs, verifier scripts, and launch-hygiene artifacts;
4. API pytest with the script-selected Python interpreter;
5. API compileall with the script-selected Python interpreter;
6. `npm run verify:static --prefix apps/web`;
7. `npm run typecheck --prefix apps/web`.

The script exits non-zero if any required available gate fails. Web gates are treated as unavailable/failing if `apps/web/package.json` exists but `apps/web/node_modules` is missing, because static verification and typecheck cannot be trusted without installed dependencies.

## Stale public reference scan

Run the scan before public announcement and review all hits in context:

```bash
git grep -nE 'truth engine|truth machine|oracle|final verdict|production intelligence|live geopolitical|current-events|global source coverage|paid API|telemetry|blockchain|user accounts|database|LLM calls|live ingestion|real-time ingestion|seven-panel|dense dashboard|public intelligence terminal|hash-chain|raw hashes|audit ID|provenance strings' -- '*.md'
```

Allowed hits are limitation disclosures, explicit prohibitions, historical institutional-memory artifacts, or internal architecture notes. Block release if current public copy presents stale dense-dashboard UX, live analysis, final verdicts, hidden scoring, or production capability as the current demo.

## Backend API verification checks

- [ ] `apps/api/README.md` describes the API as a deterministic controlled demo API, not a production analysis service.
- [ ] `GET /sample` is described as fixture-backed/sample flow only.
- [ ] `POST /analyze` is described as local input analysis that treats supplied text as supplied evidence, not proof of truth.
- [ ] `GET /audit/verify` is described as checking local sample audit-chain consistency only.
- [ ] Audit/scoring primitives are documented as method traceability and deterministic scoring signals, not final verdicts.
- [ ] API docs explicitly say there is no live ingestion, no LLM calls, no paid APIs, no hidden network behavior, and no telemetry in the local demo path.
- [ ] Any mention of backend version `0.4.0` or schema `lumen.analysis.v0.3` is framed as current API contract stability, not a v0.5 schema expansion.

## Public demo verification checks

- [ ] Public launch/readme/checklist copy says controlled local demo or local deterministic demo.
- [ ] Public copy does not claim production readiness, live current-event coverage, global source coverage, a truth engine, final verdicts, or hidden scoring.
- [ ] Current public UI expectation remains the simplified tabbed claim story:
  - claim: “When does the regulation start?”
  - tabs: Story, Evidence, Why uncertain, Audit
  - explanation: two sources disagree; Lumen marks the claim contested instead of guessing
- [ ] The simplified UI does not expose raw hashes, audit IDs, `.md` references, underscores/machine labels, provenance strings, or dense internal dashboard language in the public view.
- [ ] Legacy/internal component files, if present, are not treated as the current public UX.

## Release-blocking audit criteria

- [ ] Aggregate verification script exists at `scripts/verify_lumen.sh` and is executable.
- [ ] `bash scripts/verify_lumen.sh` passes from the repo root, or every failure has an explicit waiver/remediation card.
- [ ] Institutional-memory indexes are current under strict check mode.
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
