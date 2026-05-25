# Lumen Web

Static Next.js mock interface for the first Lumen scaffold.

The UI is intentionally local, deterministic, and sample-data driven. It demonstrates the product direction without claiming live ingestion, real-world verification, or automated truth determination.

## Panels

- BriefingPanel: structured uncertainty-first briefing; refuses to render a briefing without limitation and audit references.
- ClaimMatrix: atomic claims, statuses, confidence logic, evidence references, and guard rails that withhold claim/confidence display when status or reasons are missing.
- EvidenceTrail: source provenance, source proximity, evidence limitations reference, and evidence audit reference.
- SourceSpread: explicit fixture-backed/deferred panel that groups visible fixture sources without inferring ownership, geography, affiliation, or independence.
- NarrativeMap: framing analysis explicitly labeled as analysis, not fact, with a visible audit reference.
- ContradictionBoard: unresolved disputes and evidence gaps, with a visible audit reference.
- AuditTrail: hash-chain style transformation log.

## Uncertainty rendering rules

The static UI keeps uncertainty visible instead of filling gaps:

- no claim text is rendered when status is missing;
- no confidence value is rendered when confidence reasons are missing;
- no briefing is rendered without a limitation reference and audit reference;
- no evidence item is rendered without a limitations reference and audit reference;
- narrative, source-spread, and contradiction panels require an audit reference and explicit fixture/deferred labels;
- source independence is not inferred from article volume or fixture count.

## Run

```bash
cd apps/web
npm install
npm run dev
```

## Local scaffold verification

```bash
npm run verify:static
npm run typecheck
```
