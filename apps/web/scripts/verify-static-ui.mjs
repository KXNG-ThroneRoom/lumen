import { existsSync, readFileSync } from 'node:fs';
import { join } from 'node:path';

const root = process.cwd();
const requiredFiles = [
  'package.json',
  'src/app/page.tsx',
  'src/app/layout.tsx',
  'src/app/globals.css',
  'src/components/BriefingPanel.tsx',
  'src/components/ClaimMatrix.tsx',
  'src/components/EvidenceTrail.tsx',
  'src/components/NarrativeMap.tsx',
  'src/components/ContradictionBoard.tsx',
  'src/components/AuditTrail.tsx',
  'src/data/lumenSample.ts',
];

const requiredPhrases = [
  'Methods over conclusions',
  'More informed humans, not a new oracle',
  'Narrative analysis, not fact',
  'Unknown / unresolved / contested remain valid outputs',
  'hash-chain',
  'source independence',
];

const missing = requiredFiles.filter((file) => !existsSync(join(root, file)));
if (missing.length > 0) {
  throw new Error(`Missing UI scaffold files: ${missing.join(', ')}`);
}

const page = readFileSync(join(root, 'src/app/page.tsx'), 'utf8');
for (const phrase of requiredPhrases) {
  if (!page.includes(phrase)) {
    throw new Error(`page.tsx missing doctrine phrase: ${phrase}`);
  }
}

const components = requiredFiles.filter((file) => file.startsWith('src/components/'));
for (const file of components) {
  const body = readFileSync(join(root, file), 'utf8');
  if (body.includes('truth score') || body.includes('verified as true')) {
    throw new Error(`${file} contains overclaiming language`);
  }
}

console.log(`Static UI scaffold verified: ${requiredFiles.length} files, ${components.length} components.`);
