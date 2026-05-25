import { auditReferenceCanRender, fixturePanelLabel } from '../lib/api-contract';

export function NarrativeMap({ frames, auditReference }: { frames: string[]; auditReference: string }) {
  const hasAuditReference = auditReferenceCanRender(auditReference);

  if (!hasAuditReference) {
    return (
      <section className="panel" aria-labelledby="narrative-heading">
        <div className="panel-kicker">Narrative map</div>
        <h2 id="narrative-heading">Narrative analysis withheld</h2>
        <p>Audit reference is required before narrative analysis can be rendered.</p>
      </section>
    );
  }

  return (
    <section className="panel" aria-labelledby="narrative-heading">
      <div className="panel-kicker">Narrative map</div>
      <h2 id="narrative-heading">Narrative analysis, not fact</h2>
      <p>
        Explicit {fixturePanelLabel(frames.length > 0, hasAuditReference)} panel. Audit reference: {auditReference}. Narrative roles are analysis
        labels, not findings of truth.
      </p>
      <div className="narrative-map">
        {frames.map((frame) => (
          <article className="narrative-node" key={frame}>
            <span className="node-role">Deferred fixture label</span>
            <h3>{frame}</h3>
            <p>No intent, deception, or coordination is inferred from this stub.</p>
            <small>Future narrative outputs must remain marked as analysis, not fact.</small>
          </article>
        ))}
      </div>
    </section>
  );
}
