# Lumen Web

Static Next.js mock interface for the first Lumen scaffold.

The UI is intentionally local, deterministic, and sample-data driven. It demonstrates the product direction without claiming live ingestion, real-world verification, or automated truth determination.

## Panels

- BriefingPanel: structured uncertainty-first briefing; refuses to render a briefing without limitation and audit references.
- ClaimMatrix: atomic claims, statuses, confidence logic, evidence references, and guard rails that withhold claim/confidence display when status or reasons are missing.
- EvidenceTrail: source provenance, source independence, and evidence quality.
- SourceSpread: explicit deferred/stub panel that groups visible fixture sources without inferring ownership, geography, affiliation, or independence.
- NarrativeMap: framing analysis explicitly labeled as analysis, not fact, with a visible audit reference.
- ContradictionBoard: unresolved disputes and evidence gaps, with a visible audit reference.
- AuditTrail: hash-chain style transformation log.

## Uncertainty rendering rules

The static UI keeps uncertainty visible instead of filling gaps:

- no claim text is rendered when status is missing;
- no confidence value is rendered when confidence reasons are missing;
- no briefing is rendered without a limitation reference;
- narrative and contradiction analysis require an audit reference;
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
