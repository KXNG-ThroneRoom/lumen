# Lumen Launch Prep Checklist

Purpose: keep Lumen launch/demo readiness honest, auditable, and bounded to verified behavior.

## Before launch/demo

- [ ] Run `bash scripts/verify_lumen.sh` from the repo root and capture the exact exit status plus final RESULT line.
- [ ] Confirm `.venv` or equivalent Python environment is active when API dependencies are not globally installed.
- [ ] Confirm `apps/web/node_modules` is installed before relying on web static verification or typecheck.
- [ ] Review `docs/checklists/V0_5_VERIFICATION_CHECKLIST.md` for the current gate list.
- [ ] Review `docs/checklists/PUBLIC_ANNOUNCEMENT_CHECKLIST.md` before publishing announcement copy, screenshots, demo scripts, or release notes.
- [ ] Confirm uncommitted work is intentional and owned by active swarm lanes.
- [ ] Confirm no release notes, README copy, or UI text claims final truth, production extraction quality, live coverage, or hidden scoring.
- [ ] Confirm the current public UI is described as the simplified Story / Evidence / Why uncertain / Audit claim story, not the old dense dashboard.

## Auditability blockers

Launch/demo should block if any of these are true:

- [ ] Aggregate verification fails and no explicit waiver is recorded.
- [ ] Institutional-memory indexes are stale after new swarm or postmortem artifacts.
- [ ] Current public copy describes stale dense-dashboard UX as the public launch surface.
- [ ] Any confidence score is displayed without a visible reason/rule reference.
- [ ] Article-level final truth verdicts appear in API responses, golden cases, docs, or UI copy.
- [ ] Anonymous-source caps are hidden or bypassed without stronger evidence.
- [ ] Source repetition is counted as independent confirmation without dependency disclosure.
- [ ] Audit events are missing for extraction, scoring, briefing, or demo transformations.
- [ ] Secrets, tokens, private credentials, telemetry, paid APIs, or hidden network calls are required for the local demo path.
- [ ] Placeholder extractors are represented as production-grade extraction.

## Public announcement checks

- [ ] Announcement says Lumen is method-first and supports human judgment.
- [ ] Announcement says v0.5 is a controlled local demo, not production readiness.
- [ ] Announcement names the demo claim only as a fixture-backed example.
- [ ] Announcement avoids truth-engine, final-verdict, propaganda-detection, live-geopolitical-analysis, and global-coverage claims.
- [ ] Announcement includes or links the limitation disclosure.

## Demo operator notes

- Say "local deterministic demo" unless production deployment has been separately verified.
- Say "method-first claim/evidence/audit scaffold" rather than truth engine.
- Say "contested instead of guessed" when explaining the regulation-start fixture.
- If a verifier reports missing dependencies, install dependencies in the appropriate environment and rerun the aggregate gate; do not mark the gate as passed from partial output.
- Preserve failure output as evidence for remediation cards.
