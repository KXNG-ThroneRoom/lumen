# Lumen v0.4 Verification Checklist

Purpose: provide a repeatable local gate for v0.4 demo polish and launch-readiness work without hidden scoring, secrets, network calls, or fake production claims.

## Environment expectations

- Run from the repo root: `/Users/amirtbz/lumen`.
- Prefer the project Python environment when present:
  - `source .venv/bin/activate`
- `python3` must be available and include the dependencies needed by `apps/api/tests`.
- `apps/web/node_modules` must exist before web verification gates run:
  - `cd apps/web && npm install`
- No API keys or external credentials are required for the aggregate verification path.
- Verification should not delete, reset, clean, or commit uncommitted work.

## Aggregate command

```bash
scripts/verify_lumen.sh
```

The aggregate gate runs these checks where the corresponding project areas are present:

1. institutional-memory index strict check with the script-selected Python interpreter
2. API pytest with the script-selected Python interpreter
3. API compileall with the script-selected Python interpreter
4. `npm run verify:static --prefix apps/web`
5. `npm run typecheck --prefix apps/web`

The script prefers `.venv/bin/python` when it exists, then falls back to `python3` from `PATH`. The script exits non-zero if any required available gate fails. Web gates are treated as unavailable/failing if `apps/web/package.json` exists but `apps/web/node_modules` is missing, because static verification and typecheck cannot be trusted without installed dependencies.

## Release-blocking audit criteria

- [ ] Aggregate verification script exists at `scripts/verify_lumen.sh` and is executable.
- [ ] Institutional-memory indexes are current under strict check mode.
- [ ] API tests pass without external credentials.
- [ ] API modules compile.
- [ ] Static web dashboard verification passes and covers the expected dashboard panels.
- [ ] Web TypeScript typecheck passes.
- [ ] Golden cases remain valid JSON and continue to prohibit final-truth claims, hidden confidence scoring, and authority-as-proof shortcuts.
- [ ] No launch/demo copy claims production readiness beyond verified local behavior.
- [ ] No secrets, tokens, or private credentials appear in the verification artifacts.

## Handoff format for verifier cards

Record the exact command and exit status, for example:

```text
command: scripts/verify_lumen.sh
exit_status: 0
result: PASS
notes: ran from /Users/amirtbz/lumen with .venv activated; apps/web/node_modules present
```

If the command fails, include the failing gate name and the final `RESULT FAIL` line from the script output.
