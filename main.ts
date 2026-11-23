// News-image entry for make.fun competition news-image-20261123
// (Node 22, standard library only): its image is the entry.png beside
// this file, drawn by draw.py in this repository from the verified
// world headlines of Monday 23 November 2026 (COP31 collapse, Democrats'
// 258-seat House majority, Hormuz tanker strikes, sea drones hitting a
// Russian warship in Libya, Russian strikes on the Kyiv region, and
// BepiColombo entering orbit around Mercury). The program copies it to
// /output/entry.png, the location the grader reads.
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
// /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
//
// No network, no clock, no randomness: the copy is byte-for-byte, so
// repeated runs write identical bytes.

import { createHash } from 'node:crypto';
import { copyFileSync, readFileSync } from 'node:fs';
import { join } from 'node:path';

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const src = new URL('./entry.png', import.meta.url);
const dest = join(outDir, 'entry.png');

copyFileSync(src, dest);
const bytes = readFileSync(dest);
const sha256 = createHash('sha256').update(bytes).digest('hex');
console.log(`wrote ${dest} (${bytes.length} bytes, sha256 ${sha256})`);
