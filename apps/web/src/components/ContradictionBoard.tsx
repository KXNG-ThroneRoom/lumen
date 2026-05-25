import type { Contradiction } from '../lib/api-contract';
import { auditReferenceCanRender, fixturePanelLabel } from '../lib/api-contract';

export function ContradictionBoard({ contradictions, auditReference }: { contradictions: Contradiction[]; auditReference: string }) {
  const hasAuditReference = auditReferenceCanRender(auditReference);

  if (!hasAuditReference) {
    return (
      <section className="panel" aria-labelledby="contradictions-heading">
        <div className="panel-kicker">Contradiction board</div>
        <h2 id="contradictions-heading">Contradiction analysis withheld</h2>
        <p>Audit reference is required before contradiction analysis can be rendered.</p>
      </section>
    );
  }

  return (
    <section className="panel" aria-labelledby="contradictions-heading">
      <div className="panel-kicker">Contradiction board</div>
      <h2 id="contradictions-heading">Conflicts stay visible until resolved</h2>
      <p>
        Explicit {fixturePanelLabel(contradictions.length > 0, hasAuditReference)} panel. Audit reference: {auditReference}. Contradictions expose
        unresolved disputes; they do not settle them.
      </p>
      <div className="contradiction-list">
        {contradictions.map((item) => (
          <article className="contradiction-card" key={item.id}>
            <div className="contradiction-topline">
              <span>{item.id}</span>
              <strong>{item.status.replaceAll('_', ' ')}</strong>
            </div>
            <div className="claim-links">Type: {item.contradiction_type.replaceAll('_', ' ')}</div>
            <h3>{item.summary}</h3>
            <p>{item.limitations.join(' ') || 'Fixture contradiction lacks a limitation note; treat as deferred.'}</p>
            <div className="claim-links">Linked claims: {item.claim_ids.join(', ')}</div>
          </article>
        ))}
      </div>
    </section>
  );
}
