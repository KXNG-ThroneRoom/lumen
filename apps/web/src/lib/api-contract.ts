export type ClaimStatus =
  | 'confirmed'
  | 'strongly_corroborated'
  | 'probable'
  | 'plausible'
  | 'contested'
  | 'unsupported'
  | 'contradicted'
  | 'narrative_only'
  | 'unknown'
  | 'unresolved';

export type ClaimType =
  | 'factual_claim'
  | 'causal_claim'
  | 'legal_claim'
  | 'statistical_claim'
  | 'attribution_claim'
  | 'quote_claim'
  | 'prediction'
  | 'speculation'
  | 'moral_framing'
  | 'image_video_authenticity_claim'
  | 'anonymous_source_claim'
  | 'expert_interpretation'
  | 'interested_party_claim';

export type EvidenceType =
  | 'primary_document'
  | 'official_dataset'
  | 'court_filing'
  | 'full_transcript'
  | 'raw_video'
  | 'raw_image'
  | 'geolocation_evidence'
  | 'named_on_record_source'
  | 'local_direct_reporting'
  | 'wire_report'
  | 'anonymous_source'
  | 'expert_interpretation'
  | 'social_media_post'
  | 'opinion_commentary';

export type Source = {
  id: string;
  name: string;
  source_type: string;
  url: string | null;
  author: string | null;
  publisher: string | null;
  owner: string | null;
  country: string | null;
  language: string | null;
  funding: string | null;
  wire_dependency: string | null;
  citation_dependency: string[];
  independence_notes: string[];
  reliability_notes: string[];
  anonymous: boolean;
  interested_party: boolean;
};

export type Evidence = {
  id: string;
  claim_id: string | null;
  source_id: string | null;
  evidence_type: EvidenceType;
  summary: string;
  url: string | null;
  quote: string | null;
  provenance: string;
  proximity: string;
  timestamp_quality: string;
  primary: boolean;
  anonymous: boolean;
  limitations: string[];
  limitations_ref: string;
  audit_reference: string;
};

export type Claim = {
  id: string;
  raw_claim_text: string;
  normalized_claim: string;
  claim_type: ClaimType;
  source_document_id: string | null;
  actors: string[];
  targets: string[];
  location: string | null;
  time_range: string | null;
  evidence_refs: string[];
  contradiction_refs: string[];
  confidence_score: number;
  confidence_reason: string[];
  status: ClaimStatus;
  limitations: string[];
  limitations_ref: string;
  audit_reference: string;
  created_at: string;
};

export type ConfidenceBreakdown = {
  score: number;
  status: ClaimStatus;
  reasons: string[];
  rule_references: string[];
  caps_applied: string[];
  warnings: string[];
};

export type Contradiction = {
  id: string;
  claim_ids: string[];
  contradiction_type: string;
  summary: string;
  status: 'fixture_detected' | 'not_resolved';
  limitations: string[];
};

export type FixturePanelLabel = 'fixture-backed' | 'deferred' | 'withheld';

export type SourceGraph = {
  sources: Source[];
  independent_evidence_streams: number;
  wire_dependencies: Record<string, string>;
  citation_dependencies: Record<string, string[]>;
  independence_notes: string[];
  warnings: string[];
};

export type AuditEvent = {
  event_id: string;
  timestamp: string;
  actor_type: string;
  actor_id: string;
  operation: string;
  reason: string;
  input_hash: string;
  output_hash: string;
  previous_event_hash: string;
  event_hash: string;
  rule_version: string;
  model_version: string;
  prompt_hash: string;
  code_version: string;
  metadata: Record<string, unknown>;
};

export type AuditVerification = {
  valid: boolean;
  event_count: number;
  errors: string[];
  genesis_event_hash: string | null;
  latest_event_hash: string | null;
};

export type Briefing = {
  id: string;
  topic: string;
  bottom_line: string;
  confidence: ConfidenceBreakdown;
  key_claims: Claim[];
  evidence: Evidence[];
  contradictions: Contradiction[];
  missing_information: string[];
  narrative_frames: string[];
  watch_indicators: string[];
  unresolved_questions: string[];
  limitations: string[];
  limitations_ref: string;
  audit_reference: string;
  generated_at: string;
};

export type AnalysisResponse = {
  schema_version: string;
  mode: 'fixture_demo' | 'local_input';
  topic: string;
  claims: Claim[];
  evidence: Evidence[];
  sources: Source[];
  source_graph: SourceGraph;
  contradictions: Contradiction[];
  briefing: Briefing;
  audit_trail: AuditEvent[];
  audit_events: AuditEvent[];
  audit_verification: AuditVerification;
  limitations: string[];
  limitations_ref: string;
};

export type ClaimRenderState =
  | { canRender: true; claim: Claim; auditReference: string }
  | { canRender: false; claimId: string; reasons: string[] };

export function claimRenderState(claim: Claim, auditReference: string): ClaimRenderState {
  const reasons: string[] = [];

  if (!claim.status) reasons.push('missing status');
  if (!Array.isArray(claim.confidence_reason) || claim.confidence_reason.length === 0) reasons.push('missing confidence reason');
  if (!Array.isArray(claim.evidence_refs) || claim.evidence_refs.length === 0) reasons.push('missing evidence reference');
  if (!claim.audit_reference || !auditReference) reasons.push('missing audit reference');
  if (!claim.limitations_ref) reasons.push('missing limitations reference');

  if (reasons.length > 0) {
    return { canRender: false, claimId: claim.id || 'claim-without-id', reasons };
  }

  return { canRender: true, claim, auditReference };
}

export function claimAuditReference(claim: Claim, fallbackAuditReference: string): string {
  return claim.audit_reference || fallbackAuditReference;
}

export function evidenceCanRender(evidence: Evidence): boolean {
  return Boolean(evidence.summary && evidence.provenance && evidence.limitations_ref && evidence.audit_reference);
}

export function auditReferenceCanRender(auditReference: string): boolean {
  return Boolean(auditReference && auditReference !== 'audit-reference-pending');
}

export function briefingCanRender(briefing: Briefing, limitationsReference: string): boolean {
  return Boolean(
    briefing.audit_reference &&
      briefing.limitations_ref &&
      limitationsReference &&
      Array.isArray(briefing.limitations) &&
      briefing.limitations.length > 0 &&
      Array.isArray(briefing.confidence.reasons) &&
      briefing.confidence.reasons.length > 0,
  );
}

export function limitationsReferenceFor(response: AnalysisResponse): string {
  const responseLimitations = response.limitations.length > 0 ? response.limitations.join(' | ') : 'response limitations missing';
  const responseLimitationsRef = response.limitations_ref || 'response limitations reference missing';
  const briefingLimitations =
    response.briefing.limitations.length > 0 ? response.briefing.limitations.join(' | ') : 'briefing limitations missing';

  return `${responseLimitationsRef}; response: ${responseLimitations}; briefing: ${briefingLimitations}`;
}

export function fixturePanelLabel(hasData: boolean, hasAuditReference: boolean): FixturePanelLabel {
  if (!hasAuditReference) return 'withheld';
  return hasData ? 'fixture-backed' : 'deferred';
}
