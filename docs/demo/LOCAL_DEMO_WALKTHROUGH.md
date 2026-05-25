# Lumen Local Demo Walkthrough

Version: v0.6-ui-alignment

## Purpose

This walkthrough is for the current controlled local/manual demo. It matches the simplified public UI: one contested claim, four tabs, and plain-language uncertainty.

Small visible version note: v0.6 local/manual only. Manual input is an assertion container, not a fact, and the public UI should not add a manual-input workflow to this demo page.

Core public sentence: Two sources disagree; Lumen marks the claim contested instead of guessing.

Older internal component screens are not the current public launch UX.

It is not a production deployment path. It does not demonstrate live ingestion, URL fetching, broad extraction, broad verification, persistence, accounts, telemetry, model-backed analysis, paid-source access, or final truth determination.

## Preflight

From repo root:

```text
bash scripts/verify_lumen.sh
```

Proceed only if the verifier passes or if failures are recorded as launch blockers.

## Start the demo

Backend:

```text
uvicorn apps.api.app.main:app --reload
```

Frontend:

```text
npm run dev --prefix apps/web
```

Open the local Next.js URL printed by the dev server, usually `http://localhost:3000`.

## What the audience should see

The page should show:

- "Lumen local demo";
- "v0.6 local/manual only";
- "Methods over conclusions";
- main claim: "When does the regulation start?";
- summary: a news report says June 1, an official filing says July 1, and Lumen marks the claim contested instead of guessing;
- status cards for contested answer, official-record support, and date conflict;
- tabs: Story, Evidence, Why uncertain, Audit;
- footer note: controlled local demo only; local/manual inputs are assertions, not facts; no live news; no replacement for human judgment.

The page should not show raw internal fingerprints, internal audit keys, source file names, underscores/machine labels, internal method labels, or dense technical language.

## Talk track

Opening:

```text
This is a controlled local fixture demo. Lumen does not decide what is true. It shows why a claim is contested and what evidence would help a human inspect it.
```

Story tab:

```text
The public claim says one date. The official record says another. Lumen keeps both visible instead of smoothing over the disagreement.
```

Evidence tab:

```text
The official record is stronger support, but the conflicting report still matters. More coverage is not automatically more proof.
```

Why uncertain tab:

```text
The honest answer is contested. We know the two dates conflict. We do not know whether the report was wrong, outdated, or missing context.
```

Audit tab:

```text
The system records checks and method signals for inspection. That tracking does not prove the underlying claim; it helps reviewers understand the path.
```

Close:

```text
Lumen is for methods over conclusions: more informed humans, not a new oracle.
```

## Manual/local input boundary

v0.6 manual/local input is a controlled submission boundary. A pasted article, excerpt, local file, source label, or URL-looking string should be introduced as user-supplied material for inspection, not as evidence that the article is true, current, complete, or fetched from the network.

If a walkthrough mentions manual input, say plainly:

```text
Manual input is an assertion container. Lumen can show how the supplied text was transformed and inspected, but that audit path does not prove the underlying claim.
```

The public demo page remains the four-tab claim story. Do not turn this walkthrough into a live-ingestion, URL-fetching, or broad-analysis demo.

## Optional API inspection

For developer or reviewer audiences, show the local API after the public UI:

```text
GET http://localhost:8000/health
GET http://localhost:8000/sample
GET http://localhost:8000/audit/verify
```

Explain that API fields are internal/developer inspection surfaces. They are not meant to crowd the public four-tab story.

## Stop conditions

Stop the demo and record a blocker if:

- the page does not show the simplified four-tab claim story;
- the page implies the date dispute is settled;
- controlled-local-demo language is missing;
- the demo requires network access, URL fetching, paid services, credentials, telemetry, accounts, persistence services, or LLM calls;
- older internal component copy appears as the public UI;
- developer-only identifiers appear in the public page.

## Screenshot checklist

Capture only after preflight passes:

1. full page with main claim and status cards;
2. Story tab;
3. Evidence tab;
4. Why uncertain tab;
5. Audit tab;
6. footer or note showing controlled-local-demo boundary.

Do not crop away uncertainty or limitation language.
