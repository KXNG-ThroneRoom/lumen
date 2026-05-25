# Lumen Web

Static Next.js interface for the current Lumen controlled local demo.

The public UI is intentionally simple: a black-and-white tabbed claim story that helps a reader understand one controlled fixture dispute without pretending to decide reality. It uses local sample data only. It does not read live news, call paid APIs, call LLMs, produce final verdicts, or replace human judgment.

## Current public demo surface

The current public surface presents one fixture claim in four tabs:

- Story: shows the disagreement in sequence.
- Evidence: compares the news report, the official record, and source-independence warning.
- Why uncertain: explains why the answer remains contested.
- Audit: explains that local checks exist while keeping raw internal fingerprints and machine labels out of the main reader view.

Canonical public copy that should remain visible:

- Main claim: "When does the regulation start?"
- Explanation: "Two sources disagree. A news report says June 1. An official filing says July 1. Lumen marks this as contested instead of guessing."
- Boundary note: "Controlled local demo only. It does not read live news, declare truth, or replace human judgment."

Visual language:

- yellow / middle: contested or uncertain;
- blue / good: stronger support;
- red / bad: conflict or weaker/conflicting support.

## Legacy/internal component note

Older component files still exist under `src/components/` as legacy/internal honesty components and contract fixtures. They are useful for regression checks, but they are not the current public launch UX and should not be described as the primary public interface.

Do not promise public display of raw internal fingerprints, internal audit keys, source file names, underscore machine labels, or dense technical language in the simplified demo.

## Run

```bash
cd apps/web
npm install
npm run dev
```

Open the local Next.js URL printed by the dev server, usually `http://localhost:3000`.

## Local verification

```bash
npm run verify:static
npm run typecheck
```

`npm run verify:static` checks that the simplified tabbed page still contains the controlled claim story, required tabs, no retired interface wording in the page, backend fixture parity, and demo-doc wording that matches this public surface.
