# Lumen Public Announcement Checklist

Purpose: prevent public launch copy from overstating what v0.5 does. Use this checklist before posting a README excerpt, announcement, demo script, screenshot caption, social post, or release note.

## Required framing

- [ ] Describe Lumen as method-first infrastructure for inspecting claims, evidence, uncertainty, limitations, and audit trails.
- [ ] Say "controlled local demo" or "local deterministic demo" when describing v0.5.
- [ ] Say the current demo centers on one fixture-backed claim story: "When does the regulation start?"
- [ ] Say the two-source disagreement is marked contested instead of guessed or resolved by Lumen.
- [ ] State that Lumen supports human judgment; it does not replace it.
- [ ] Link or mention `LIMITATIONS.md` when showing analytical output.

## Current public UI reality

- [ ] Public screenshots or walkthroughs show the simplified black/white tabbed claim story.
- [ ] The visible tabs are Story, Evidence, Why uncertain, and Audit.
- [ ] Visual language stays plain: contested/uncertain, support, and conflict.
- [ ] The public view does not expose raw hashes, audit IDs, `.md` references, underscores/machine labels, provenance strings, or dense internal dashboard language.
- [ ] Legacy/internal component files are not described as the current public UX.

## Prohibited public claims

Block announcement if copy says or implies any of the following as current v0.5 capability:

- [ ] Lumen determines truth, proves claims, settles disputes, or issues final verdicts.
- [ ] Lumen is a production intelligence system or live geopolitical/current-events analysis service.
- [ ] Lumen has global source coverage, broad web search, production ingestion, or real-time monitoring.
- [ ] Lumen calls paid APIs, LLMs, hidden hosted services, or external sources in the default local demo path.
- [ ] Lumen has telemetry, accounts, authentication, personalization, blockchain anchoring, or durable database complexity.
- [ ] Lumen detects propaganda, deception, intent, coordination, or neutrality as a proven fact.
- [ ] Lumen has hidden scoring, secret prompts, undisclosed weights, or unavailable audit rules.

## Verification packet

Before announcement, attach or record:

- [ ] `bash scripts/verify_lumen.sh` command, exit status, and final RESULT line.
- [ ] `python3 scripts/regen_indexes.py --check --strict` result after any institutional-memory artifact changes.
- [ ] Public-reference scan result for stale dense-dashboard/current-UI wording.
- [ ] Project-contamination scan result.
- [ ] Secret literal scan result.
- [ ] Any waiver, limitation, or unresolved risk stated in plain language.

## Safe short copy

Use wording in this shape:

```text
Lumen is a free, open-source, method-first demo for inspecting claims, evidence, uncertainty, limitations, and audit trails. v0.5 is a controlled local demo around one fixture-backed contested claim. It does not determine truth or ingest live events; it shows how a system can expose why a claim is uncertain instead of pretending to know.
```

## Final release-blocker question

If a reader could reasonably walk away believing Lumen is a live truth engine or production verification product, do not publish. Rewrite until the controlled-demo boundary is obvious.
