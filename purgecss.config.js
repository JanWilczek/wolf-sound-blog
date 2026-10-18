// Removes CSS rules (mostly unused Bootstrap) that match nothing in the built site.
// Runs after the Eleventy build via _js/purge-css.js (`npm run build:purgecss`).
module.exports = {
  content: [
    "_site/**/*.html",
    "_site/assets/scripts.js",
    "_site/assets/js/**/*.js",
  ],
  css: ["_site/assets/css/main.css"],
  safelist: {
    // Classes toggled at runtime by assets/scripts.js and the smart navbar
    standard: ["show", "collapse", "collapsing", "collapsed", "is-fixed", "is-visible"],
    // Color modes are switched at runtime via the data-bs-theme attribute
    greedy: [/data-bs-theme/],
  },
};
