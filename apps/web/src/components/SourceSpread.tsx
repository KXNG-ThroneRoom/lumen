import type { SourceGraph } from '../lib/api-contract';
import { auditReferenceCanRender, fixturePanelLabel } from '../lib/api-contract';

export function SourceSpread({ sourceGraph, auditReference }: { sourceGraph: SourceGraph; auditReference: string }) {
  const hasAuditReference = auditReferenceCanRender(auditReference);
  const panelLabel = fixturePanelLabel(sourceGraph.sources.length > 0, hasAuditReference);

  return (
    <section className="panel" aria-labelledby="source-spread-heading">
      <div className="panel-kicker">Source spread</div>
      <h2 id="source-spread-heading">Source independence is visible, not assumed</h2>
      <p>
        Explicit {panelLabel} panel. Source quantity is not source independence. Repeated origin streams are counted separately from independent
        corroboration. Audit reference: {hasAuditReference ? auditReference : 'missing — analysis withheld'}.
      </p>
      <p>
        Independent evidence streams recorded in fixture: {sourceGraph.independent_evidence_streams}. The UI renders backend source metadata and
        dependency warnings only; it does not infer ownership, geography, political leaning, or real independence.
      </p>
      <div className="evidence-grid">
        {sourceGraph.sources.map((source) => (
          <article className="evidence-card" key={source.id}>
            <div className="evidence-meta">
              <span>{source.id}</span>
              <span>{source.source_type}</span>
            </div>
            <h3>{source.name}</h3>
            <dl>
              <div>
                <dt>Wire dependency</dt>
                <dd>{source.wire_dependency ?? 'none recorded in fixture'}</dd>
              </div>
              <div>
                <dt>Independence notes</dt>
                <dd>{source.independence_notes.join(' ') || 'No independence note recorded; do not assume independence.'}</dd>
              </div>
              <div>
                <dt>Deferred fields</dt>
                <dd>ownership, geography, affiliation, funding validation, and source graph expansion</dd>
              </div>
            </dl>
          </article>
        ))}
      </div>
      <p>Dependency warnings: {sourceGraph.warnings.length > 0 ? sourceGraph.warnings.join(' | ') : 'none in fixture'}.</p>
    </section>
  );
}
