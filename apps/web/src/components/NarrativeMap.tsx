import type { NarrativeFrame } from '../data/lumenSample';

export function NarrativeMap({ frames, auditReference }: { frames: NarrativeFrame[]; auditReference: string }) {
  if (!auditReference) {
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
      <p>Audit reference: {auditReference}. Narrative roles are fixture labels, not findings of truth.</p>
      <div className="narrative-map">
        {frames.map((frame) => (
          <article className="narrative-node" key={frame.role}>
            <span className="node-role">{frame.role}</span>
            <h3>{frame.observedFrame}</h3>
            <p>{frame.evidence}</p>
            <small>{frame.caution}</small>
          </article>
        ))}
      </div>
    </section>
  );
}
