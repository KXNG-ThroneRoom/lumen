import type { EvidenceItem } from '../data/lumenSample';

export function EvidenceTrail({ evidence }: { evidence: EvidenceItem[] }) {
  return (
    <section className="panel" aria-labelledby="evidence-heading">
      <div className="panel-kicker">Evidence trail</div>
      <h2 id="evidence-heading">Provenance and source independence</h2>
      <div className="evidence-grid">
        {evidence.map((item) => (
          <article className={`evidence-card ${item.quality}`} key={item.id}>
            <div className="evidence-meta">
              <span>{item.id}</span>
              <span>{item.sourceType}</span>
            </div>
            <h3>{item.label}</h3>
            <blockquote>{item.quote}</blockquote>
            <dl>
              <div>
                <dt>Provenance</dt>
                <dd>{item.provenance}</dd>
              </div>
              <div>
                <dt>Independence</dt>
                <dd>{item.independence}</dd>
              </div>
            </dl>
          </article>
        ))}
      </div>
    </section>
  );
}
