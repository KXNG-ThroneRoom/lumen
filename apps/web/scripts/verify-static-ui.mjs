import { execFileSync } from 'node:child_process';
import { existsSync, readFileSync } from 'node:fs';
import { join } from 'node:path';

const root = process.cwd();
const requiredFiles = [
  'package.json',
  'src/app/page.tsx',
  'src/app/layout.tsx',
  'src/app/globals.css',
  'src/lib/api-contract.ts',
  'src/data/demo-response.json',
  'src/components/BriefingPanel.tsx',
  'src/components/ClaimMatrix.tsx',
  'src/components/EvidenceTrail.tsx',
  'src/components/NarrativeMap.tsx',
  'src/components/SourceSpread.tsx',
  'src/components/ContradictionBoard.tsx',
  'src/components/AuditTrail.tsx',
];

const requiredPhrases = [
  'When does the regulation start?',
  'Two sources disagree',
  'Lumen marks this as contested',
  'Story',
  'Evidence',
  'Why uncertain',
  'Audit',
  'No final verdict',
  'Controlled local demo only',
  'Methods over conclusions',
  'v0.6 local/manual only',
  'Manual input area',
  'Local assertion container',
  'not a verified fact',
  'does not submit',
];

const requiredImplementationSignals = [
  "'use client'",
  'useState<ViewId>',
  "useState<ViewId>('story')",
  'onClick={() => setActiveView(view.id)}',
  '<details>',
  '<summary>',
  'maxLength={1200}',
  'text stays hidden',
];

const demoDocFiles = [
  '../../docs/demo/README.md',
  '../../docs/demo/LOCAL_DEMO_WALKTHROUGH.md',
  'README.md',
];

const requiredDemoDocPhrases = [
  'simplified',
  'controlled local demo',
  'When does the regulation start?',
  'Two sources disagree',
  'Story',
  'Evidence',
  'Why uncertain',
  'Audit',
  'not the current public launch UX',
];

const requiredOwnedDemoDocPhrases = new Map([
  ['../../docs/demo/LOCAL_DEMO_WALKTHROUGH.md', ['v0.6 local/manual only', 'Manual input is an assertion container, not a fact']],
  ['README.md', ['v0.6 local/manual only', 'manual input is an assertion container, not a fact']],
]);

const retiredDashboardPhrases = [
  'public intelligence terminal',
  'Claim-level analysis scaffold',
  'Visible method chain',
  'Confidence method signal',
  'hash-chain',
  'source proximity',
  'provenance',
];

const publicDocRetiredPhrases = [
  'Static Next.js mock interface for the first Lumen scaffold',
  'public intelligence terminal',
  'seven-panel dashboard',
  'dense dashboard',
  'technical dashboard',
  'provenance-heavy',
  'raw audit identifiers',
  'raw hashes',
  'audit IDs',
  '.md evidence references',
  'provenance strings',
  '## Panels',
  'BriefingPanel:',
  'ClaimMatrix:',
  'EvidenceTrail:',
  'SourceSpread:',
  'NarrativeMap:',
  'ContradictionBoard:',
  'AuditTrail:',
  'hash-chain style transformation log',
];

const missing = requiredFiles.filter((file) => !existsSync(join(root, file)));
if (missing.length > 0) {
  throw new Error(`Missing UI scaffold files: ${missing.join(', ')}`);
}

const packageJson = JSON.parse(readFileSync(join(root, 'package.json'), 'utf8'));
const packageDescription = packageJson.description ?? '';
if (!packageDescription.includes('Controlled local Lumen demo UI')) {
  throw new Error('package.json description must describe the simplified controlled local demo UI');
}
for (const phrase of ['intelligence-dashboard', 'dashboard mock UI', 'narrative, contradiction, briefing, and audit panels']) {
  if (packageDescription.includes(phrase)) {
    throw new Error(`package.json still contains retired public-interface wording: ${phrase}`);
  }
}

const page = readFileSync(join(root, 'src/app/page.tsx'), 'utf8');
for (const phrase of requiredPhrases) {
  if (!page.includes(phrase)) {
    throw new Error(`page.tsx missing simplified UI phrase: ${phrase}`);
  }
}
for (const signal of requiredImplementationSignals) {
  if (!page.includes(signal)) {
    throw new Error(`page.tsx missing simplified UI implementation signal: ${signal}`);
  }
}
for (const phrase of retiredDashboardPhrases) {
  if (page.includes(phrase)) {
    throw new Error(`page.tsx still contains retired dashboard wording: ${phrase}`);
  }
}

for (const file of demoDocFiles) {
  const absolute = join(root, file);
  if (!existsSync(absolute)) {
    throw new Error(`missing simplified public demo doc: ${file}`);
  }
  const body = readFileSync(absolute, 'utf8');
  for (const phrase of requiredDemoDocPhrases) {
    if (!body.includes(phrase)) {
      throw new Error(`${file} missing simplified public demo phrase: ${phrase}`);
    }
  }
  for (const phrase of publicDocRetiredPhrases) {
    if (body.includes(phrase)) {
      throw new Error(`${file} still contains retired public-interface wording: ${phrase}`);
    }
  }

  for (const phrase of requiredOwnedDemoDocPhrases.get(file) ?? []) {
    if (!body.includes(phrase)) {
      throw new Error(`${file} missing v0.6 local/manual-only boundary phrase: ${phrase}`);
    }
  }
}

const styles = readFileSync(join(root, 'src/app/globals.css'), 'utf8');
for (const colorToken of ['--bg: #000000', '--text: #f7f7f7', '--good:', '--bad:', '--middle:', '.tone-good', '.tone-bad', '.tone-middle']) {
  if (!styles.includes(colorToken)) {
    throw new Error(`globals.css missing simplified color token: ${colorToken}`);
  }
}
for (const retiredStyle of ['--cyan', 'radial-gradient', 'ui-monospace']) {
  if (styles.includes(retiredStyle)) {
    throw new Error(`globals.css still contains retired terminal styling: ${retiredStyle}`);
  }
}

const contract = readFileSync(join(root, 'src/lib/api-contract.ts'), 'utf8');
for (const invariant of ['missing status', 'missing confidence reason', 'missing evidence reference', 'missing audit reference']) {
  if (!contract.includes(invariant)) {
    throw new Error(`api-contract.ts missing render invariant: ${invariant}`);
  }
}

const demo = JSON.parse(readFileSync(join(root, 'src/data/demo-response.json'), 'utf8'));

const VOLATILE_AUDIT_FIELDS = new Set([
  'audit_reference',
  'created_at',
  'event_hash',
  'generated_at',
  'genesis_event_hash',
  'input_hash',
  'latest_event_hash',
  'output_hash',
  'previous_event_hash',
  'timestamp',
]);

function normalizeBackendParity(value) {
  if (Array.isArray(value)) {
    return value.map(normalizeBackendParity);
  }
  if (value && typeof value === 'object') {
    return Object.fromEntries(
      Object.entries(value)
        .filter(([key]) => !VOLATILE_AUDIT_FIELDS.has(key))
        .map(([key, child]) => [key, normalizeBackendParity(child)]),
    );
  }
  return value;
}

function summarizeMismatch(left, right, path = '$') {
  if (typeof left !== typeof right) {
    return `${path}: type ${typeof left} !== ${typeof right}`;
  }
  if (Array.isArray(left) || Array.isArray(right)) {
    if (!Array.isArray(left) || !Array.isArray(right)) {
      return `${path}: array/non-array mismatch`;
    }
    if (left.length !== right.length) {
      return `${path}: array length ${left.length} !== ${right.length}`;
    }
    for (let index = 0; index < left.length; index += 1) {
      const mismatch = summarizeMismatch(left[index], right[index], `${path}[${index}]`);
      if (mismatch) return mismatch;
    }
    return null;
  }
  if (left && right && typeof left === 'object') {
    const leftKeys = Object.keys(left).sort();
    const rightKeys = Object.keys(right).sort();
    if (leftKeys.join('\u0000') !== rightKeys.join('\u0000')) {
      return `${path}: keys ${leftKeys.join(',')} !== ${rightKeys.join(',')}`;
    }
    for (const key of leftKeys) {
      const mismatch = summarizeMismatch(left[key], right[key], `${path}.${key}`);
      if (mismatch) return mismatch;
    }
    return null;
  }
  if (left !== right) {
    return `${path}: ${JSON.stringify(left)} !== ${JSON.stringify(right)}`;
  }
  return null;
}

function loadBackendSampleIfAvailable() {
  try {
    const repoRoot = join(root, '..', '..');
    const pythonBin = existsSync(join(repoRoot, '.venv/bin/python')) ? join(repoRoot, '.venv/bin/python') : 'python3';
    const output = execFileSync(
      pythonBin,
      [
        '-c',
        [
          'import json',
          'from apps.api.app.main import build_sample_analysis',
          'print(json.dumps(build_sample_analysis().model_dump(mode="json"), sort_keys=True))',
        ].join('; '),
      ],
      { cwd: repoRoot, encoding: 'utf8', stdio: ['ignore', 'pipe', 'pipe'] },
    );
    return JSON.parse(output);
  } catch (error) {
    throw new Error(`unable to load backend sample for fixture parity: ${error.message}`);
  }
}

const backendSample = loadBackendSampleIfAvailable();
const parityMismatch = summarizeMismatch(demo, backendSample);
if (parityMismatch) {
  throw new Error(`demo-response.json drifted from canonical backend /sample fixture: ${parityMismatch}`);
}

const requiredTopLevelFields = [
  'schema_version',
  'mode',
  'claims',
  'evidence',
  'sources',
  'source_graph',
  'contradictions',
  'briefing',
  'audit_trail',
  'audit_events',
  'audit_verification',
  'limitations',
  'limitations_ref',
];
for (const field of requiredTopLevelFields) {
  if (!(field in demo)) {
    throw new Error(`demo-response.json missing top-level backend contract field: ${field}`);
  }
}
if (!Array.isArray(demo.audit_trail) || demo.audit_trail.length === 0) {
  throw new Error('demo-response.json must include non-empty audit_trail');
}
if (!Array.isArray(demo.audit_events) || demo.audit_events.length === 0) {
  throw new Error('demo-response.json must include non-empty audit_events');
}
if (!demo.audit_verification || typeof demo.audit_verification.valid !== 'boolean' || !demo.audit_verification.latest_event_hash) {
  throw new Error('demo-response.json must include audit_verification valid state and latest_event_hash');
}
if (!Array.isArray(demo.claims) || demo.claims.length === 0) {
  throw new Error('demo-response.json must include claims');
}
for (const claim of demo.claims) {
  if (!claim.status || !claim.confidence_reason?.length || !claim.evidence_refs?.length || !claim.audit_reference || !claim.limitations_ref) {
    throw new Error(`demo claim ${claim.id ?? '<missing id>'} lacks status, confidence_reason, evidence_refs, audit_reference, or limitations_ref`);
  }
}
for (const evidence of demo.evidence ?? []) {
  if (!evidence.audit_reference || !evidence.limitations_ref) {
    throw new Error(`demo evidence ${evidence.id ?? '<missing id>'} lacks audit_reference or limitations_ref`);
  }
}
for (const contradiction of demo.contradictions ?? []) {
  if (!contradiction.status || !contradiction.contradiction_type || !contradiction.claim_ids?.length || !contradiction.limitations?.length) {
    throw new Error(`demo contradiction ${contradiction.id ?? '<missing id>'} lacks status, type, linked claims, or limitations`);
  }
}
if (!demo.source_graph?.sources?.length || typeof demo.source_graph.independent_evidence_streams !== 'number') {
  throw new Error('demo-response.json must include source_graph sources and independent_evidence_streams');
}
if (!demo.briefing?.audit_reference || !demo.briefing?.limitations_ref || !demo.briefing?.limitations?.length || !demo.limitations?.length || !demo.limitations_ref) {
  throw new Error('demo-response.json must include briefing audit_reference, briefing limitations_ref, response limitations_ref, and limitations');
}

const componentExpectations = new Map([
  ['src/components/BriefingPanel.tsx', ['Missing information', 'Limitations displayed with briefing', 'Audit reference']],
  ['src/components/ClaimMatrix.tsx', ['Claim audit ref', 'Limitations ref', 'Contradiction refs']],
  ['src/components/EvidenceTrail.tsx', ['Audit reference', 'Limitations']],
  ['src/components/SourceSpread.tsx', ['Source quantity is not source independence', 'Independent evidence streams']],
  ['src/components/NarrativeMap.tsx', ['Narrative analysis, not fact', 'roles are analysis']],
  ['src/components/ContradictionBoard.tsx', ['Contradictions expose', 'Type:', 'Linked claims']],
  ['src/components/AuditTrail.tsx', ['does not', 'prove the underlying claim']],
]);

for (const [file, phrases] of componentExpectations) {
  const body = readFileSync(join(root, file), 'utf8');
  for (const phrase of phrases) {
    if (!body.includes(phrase)) {
      throw new Error(`${file} missing required UI invariant phrase: ${phrase}`);
    }
  }
}

const components = requiredFiles.filter((file) => file.startsWith('src/components/'));
for (const file of components) {
  const body = readFileSync(join(root, file), 'utf8');
  const overclaimingFragments = ['truth score', 'verified as true', `verifies ${'reality'}`];
  if (overclaimingFragments.some((fragment) => body.includes(fragment))) {
    throw new Error(`${file} contains overclaiming language`);
  }
}

console.log(`Static UI scaffold verified: ${requiredFiles.length} files, ${components.length} support components, simplified tabbed demo.`);
