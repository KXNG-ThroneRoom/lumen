# Lumen Governance Rules

Version: v0.2-local-deterministic
Scope: MVP governance, scoring, audit, and public-facing disclosure rules.

## 1. Governing Doctrine

Lumen exposes methods, evidence, claims, uncertainty, and provenance. It does not decide what users must believe.

All outputs must preserve the distinction between:

- what was claimed;
- who or what made the claim;
- what evidence was linked;
- what evidence is missing;
- what contradictions were found;
- what rules were applied;
- what remains unknown, unresolved, or contested.

## 2. Mandatory Output Rules

Every displayed claim must include:

- status;
- confidence band;
- confidence reason;
- evidence references or explicit missing-evidence notes;
- source/provenance reference;
- audit reference.

Every briefing must include:

- limitations reference;
- unresolved questions;
- audit reference;
- confidence explanation;
- explicit statement when fixture or placeholder data is used.

Every narrative analysis panel must say it is analysis, not fact.

## 3. Valid Claim Statuses

Lumen may use these MVP statuses:

- supported: evidence currently attached supports the claim under documented rules.
- strongly_corroborated: multiple independent evidence streams support the claim, with strong provenance.
- plausible: evidence is partial, indirect, or not independently confirmed.
- unresolved: evidence is insufficient to support or reject the claim.
- contested: credible attached evidence or claims conflict.
- contradicted: attached evidence directly conflicts with the claim.
- unsupported: no adequate supporting evidence is attached.
- narrative_only: the item is framing, interpretation, or rhetoric rather than a factual claim.
- unknown: the system cannot classify the claim honestly with available inputs.

Status labels describe method-state, not final reality.

## 4. Confidence Bands

MVP confidence bands:

- high: strong provenance, primary or near-primary evidence, and independent support with no material unresolved contradiction.
- medium: meaningful support exists, but some dependency, missing context, or indirect evidence remains.
- low: weak, indirect, dependent, anonymous, or incomplete evidence dominates.
- capped: a rule cap prevents a higher band, usually due to anonymity, dependency, missing provenance, or unresolved contradiction.
- unknown: confidence cannot be assigned honestly.

A confidence band without a visible reason is invalid.

## 5. Anonymous-Source Caps

Anonymous-source claims are capped unless stronger evidence is attached.

Default caps:

- unsupported anonymous assertion: capped at low;
- anonymous official or unnamed institutional source: capped at low unless independently supported;
- anonymous eyewitness: capped at low unless corroborated by primary or independent evidence;
- anonymous expert interpretation: narrative_only or low unless tied to inspectable evidence;
- leaked document: score the document provenance separately; anonymity of leaker does not make the document self-validating.

No number of dependent anonymous repeats should raise confidence by itself.

## 6. Source-Independence Rules

Article volume is not evidence volume.

Sources are not independent when they share:

- the same wire-service origin;
- circular citation;
- a common press release;
- the same anonymous briefing;
- replicated wording without separate reporting;
- same ownership/funding where relevant to the claim;
- synchronized publication without disclosed independent evidence.

Dependent sources may show spread or amplification. They must not be counted as independent corroboration.

## 7. Primary-Evidence Rule

Primary evidence can raise confidence when provenance and relevance are adequate.

Primary evidence includes original documents, full transcripts, official datasets, court filings, direct video, direct images, geolocation material, timestamped records, raw source material, and archived originals.

Primary evidence does not remove uncertainty. It must still be assessed for authenticity, completeness, context, chain of custody, timestamp quality, and relevance.

## 8. Contradiction Handling

Contradictions must be exposed, not forced into premature resolution.

When material contradictions exist, the claim should usually be contested or capped unless governance rules document why the contradiction is not material.

Contradiction outputs must identify:

- conflicting claim or evidence;
- contradiction type;
- source references;
- uncertainty note;
- audit reference.

## 9. Limitation Disclosure Policy

Limitations must appear close to the output they qualify.

Required disclosures include:

- fixture/demo data;
- placeholder extraction;
- incomplete source coverage;
- missing primary evidence;
- source dependency;
- anonymous-source caps;
- unresolved contradiction;
- stale or uncertain timestamps;
- narrative analysis limitations.

Limitations must be written plainly and must not be buried in footnotes alone.

## 10. Audit Requirements

Every meaningful transformation must create or reference an audit event.

MVP audit events should cover:

- sample loaded;
- claim extracted or placeholder-generated;
- evidence attached;
- score assigned;
- source dependency evaluated;
- contradiction checked;
- briefing generated;
- governance rule applied.

Audit events must include rule version, operation, reason, input hash, output hash, previous hash, and event hash where available.

## 11. User Interface Governance

The interface must not create certainty theater.

UI must avoid:

- single unexplained aggregate scores;
- green/red verdict framing without method context;
- hidden uncertainty;
- unsupported badges of authority;
- overconfident summaries;
- suppressing unresolved questions.

UI must show:

- status;
- confidence reason;
- evidence quality;
- source dependency;
- limitations;
- audit reference.

## 12. Governance Change Process

Any change to these rules must be documented with:

- changed rule;
- reason;
- expected effect;
- risk of misuse;
- test/eval impact;
- reviewer or challenge notes when available.

Silent governance changes are prohibited.
