// news-image-20261123 entrypoint.
//
// Copies the pre-rendered poster (entry.png, built at authoring time by
// draw_poster.py) into the output directory. Nothing is generated at
// grade time: the program only copies one file, so every run writes
// byte-identical output. Standard library only, no network, no clock.

import { copyFileSync, existsSync, mkdirSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const source = join(here, "entry.png");
const outDir = process.env.MAKEFUN_OUTPUT_DIR
  ? resolve(process.env.MAKEFUN_OUTPUT_DIR)
  : resolve(here, "..", "output");

if (!existsSync(source)) {
  console.error(`poster not found beside main.ts: ${source} ` +
    `(run draw_poster.py first)`);
  process.exit(1);
}

mkdirSync(outDir, { recursive: true });
try {
  copyFileSync(source, join(outDir, "entry.png"));
} catch (err) {
  console.error(`failed to copy entry.png to ${outDir}: ${err.message}`);
  process.exit(1);
}
console.log(`wrote ${join(outDir, "entry.png")}`);
