// Removes unused CSS from the built site according to purgecss.config.js.
// The PurgeCSS CLI does not resolve the globs from the config file, so the API is used instead.
const fs = require("node:fs");
const { PurgeCSS } = require("purgecss");
const config = require("../purgecss.config.js");

(async () => {
  const results = await new PurgeCSS().purge(config);
  if (results.length === 0) {
    console.error("purge-css: no CSS files matched", config.css);
    process.exit(1);
  }
  for (const { file, css } of results) {
    const before = fs.statSync(file).size;
    fs.writeFileSync(file, css);
    console.log(`purge-css: ${file} ${before} -> ${css.length} bytes`);
  }
})();
