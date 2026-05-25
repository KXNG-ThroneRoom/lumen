# Lumen Confidence Scoring Methodology

Version: v0.6-controlled-manual-input

## Purpose

Confidence scoring in Lumen is an explanation mechanism, not a verdict mechanism. It helps users understand why the system assigned a method-state to a claim.

Lumen does not determine what users must believe. It exposes the rule path, evidence quality, uncertainty, and provenance behind a confidence band.

Confidence language must remain methodological in all API responses, public UI copy, screenshots, and demos. A band describes how documented rules handled available inputs; it must not be phrased as proof, final truth, certainty, or completion of real-world verification.

Public docs and contributor onboarding must link this methodology when they mention confidence. Users and contributors may challenge confidence reasons, cap application, or score wording through `../../ADVERSARIAL_REVIEW.md`.

For v0.6 controlled manual input, confidence bands can only describe the documented rule path over supplied local material and attached fixture evidence. A submitted source label, `source_url`, URL-looking string, or article excerpt is metadata or user-supplied content unless explicitly supported by separately supplied evidence. It must not raise confidence merely by looking authoritative.

## Required Fields

Every scored claim must include:

- status;
- confidence_band;
- confidence_reason;
- applied_rules;
- evidence_refs;
- source_refs;
- limitation_refs;
- audit_ref.

A claim missing status or confidence_reason is invalid for display.

A public surface that displays confidence without a nearby limitation reference is also invalid for v0.6 demo purposes.

## Confidence Bands

- high: strong primary or near-primary evidence, strong provenance, independent corroboration, and no material unresolved contradiction.
- medium: meaningful support exists, but some dependency, indirectness, provenance gap, or missing context remains.
- low: weak, indirect, dependent, anonymous, stale, or incomplete evidence dominates.
- capped: a governance cap prevents elevation.
- unknown: confidence cannot be assigned honestly from available inputs.

High confidence still preserves uncertainty. Low, capped, unknown, unresolved, unsupported, and contested states must be displayed as valid analytical outcomes rather than failures. The current public fixture demonstrates contested output rather than a final verdict.

## Deterministic MVP Rule Order

MVP scoring applies rules in this order:

1. Start at unknown.
2. If no inspectable evidence exists, set unsupported or unresolved with low/unknown confidence.
3. If the item is framing, speculation, or interpretation rather than an inspectable factual claim, mark that limitation plainly and do not inflate confidence.
4. Treat manually submitted text, source labels, `source_url`, and URL-looking strings as assertions/metadata until evidence supports them.
5. Add support for primary or near-primary evidence with adequate provenance.
6. Add support for independent evidence streams.
7. Reduce or cap confidence for anonymous sourcing.
8. Reduce or cap confidence for wire/citation/source dependency.
9. Reduce or cap confidence for material contradiction.
10. Reduce confidence for missing timestamp, missing origin, stale source, or unclear chain of custody.
11. Emit visible reasons and audit references.

## Anonymous-Source Caps

Default cap rules:

| Source condition | Maximum band without stronger evidence | Required reason |
| --- | --- | --- |
| Unsupported anonymous assertion | low | Anonymous assertion has no inspectable support. |
| Anonymous official / unnamed institutional source | low | Identity and incentives cannot be independently inspected. |
| Anonymous eyewitness | low | Witness cannot be independently assessed. |
| Anonymous expert interpretation | low | Expert basis is not inspectable. |
| Leaked document with weak provenance | capped | Document chain of custody is uncertain. |

Independent primary evidence can raise confidence above the cap, but the reason must explain why.

## Source-Independence Effects

Independent evidence streams can raise confidence. Dependent repetition cannot.

Dependency indicators include:

- same wire origin;
- citation loop;
- repeated language;
- common press release;
- same anonymous briefing;
- unclear origin;
- shared ownership/funding materially relevant to the claim.

When dependency exists, confidence_reason must say that article count was not treated as independent support.

## Primary Evidence Effects

Primary evidence may increase confidence when it is relevant and has adequate provenance.

Primary evidence is not automatically decisive. It can be incomplete, forged, selectively edited, stale, miscaptioned, mistranslated, or context-dependent.

Scoring must distinguish:

- evidence existence;
- evidence authenticity;
- evidence relevance;
- evidence completeness;
- evidence chain of custody.

## Contradiction Effects

Material contradictions usually produce contested or capped status.

Contradiction reasons must identify:

- the conflict type;
- the conflicting source or evidence;
- whether the conflict is direct or indirect;
- why uncertainty remains.

## Unknown / Unresolved Handling

Unknown and unresolved are not failures. They are honest outputs when evidence is inadequate.

Use unknown when the system cannot classify.
Use unresolved when a claim is clear but evidence is insufficient or incomplete.
Use contested when competing evidence or claims materially conflict.

## Anti-Bias Requirements

Confidence must never use hidden ideology, partisan identity, popularity, institution type, or source prestige as a substitute for evidence.

Official, mainstream, alternative, anonymous, activist, corporate, government, and independent sources all remain claim sources requiring context.

## Audit Coupling

Every score assignment must produce or reference an audit event containing:

- rule_version;
- input_hash;
- output_hash;
- applied_rules;
- confidence_reason;
- limitations;
- previous_event_hash;
- event_hash.

Audit coupling explains how the score was produced. It does not prove that the underlying claim is correct.
