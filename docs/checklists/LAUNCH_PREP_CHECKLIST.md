# Lumen Launch Prep Checklist

Purpose: keep Lumen launch/demo readiness honest, auditable, and bounded to verified behavior.

## Before launch/demo

- [ ] Run `scripts/verify_lumen.sh` from the repo root and capture the exact exit status.
- [ ] Confirm `.venv` or equivalent Python environment is active when API dependencies are not globally installed.
- [ ] Confirm `apps/web/node_modules` is installed before relying on web static verification or typecheck.
- [ ] Review `docs/checklists/V0_4_VERIFICATION_CHECKLIST.md` for the full gate list.
- [ ] Confirm uncommitted work is intentional and owned by the active swarm lanes.
- [ ] Confirm no release notes, README copy, or UI text claims final truth, production extraction quality, or hidden scoring.

## Auditability blockers

Launch/demo should block if any of these are true:

- [ ] Aggregate verification fails and no explicit waiver is recorded.
- [ ] Any confidence score is displayed without a visible reason/rule reference.
- [ ] Article-level final truth verdicts appear in API responses, golden cases, docs, or UI copy.
- [ ] Anonymous-source caps are hidden or bypassed without stronger evidence.
- [ ] Source repetition is counted as independent confirmation without dependency disclosure.
- [ ] Audit events are missing for extraction, scoring, briefing, or demo transformations.
- [ ] Secrets, tokens, or private credentials are required for the local demo path.
- [ ] Placeholder extractors are represented as production-grade extraction.

## Demo operator notes

- Say "local deterministic demo" unless production deployment has been separately verified.
- Say "method-first claim/evidence/audit scaffold" rather than truth engine.
- If a verifier reports missing dependencies, install dependencies in the appropriate environment and rerun the aggregate gate; do not mark the gate as passed from partial output.
- Preserve failure output as evidence for remediation cards.
