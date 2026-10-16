/*
 * Adds a line-number gutter to highlighted Markdown code blocks at build time.
 *
 * The gutter follows the markup of Prism's line-numbers plugin: an aria-hidden
 * <span class="line-numbers-rows"> holding one empty <span> per line, numbered
 * with CSS counters. The highlighted code itself is left untouched, so tokens
 * spanning several lines (e.g., block comments) stay intact and the numbers
 * are never copied together with the code.
 */

// Languages whose snippets are typically copied verbatim into a terminal
const LANGUAGES_WITHOUT_LINE_NUMBERS = new Set([
  "bash",
  "console",
  "powershell",
  "ps1",
  "sh",
  "shell",
  "text",
  "zsh",
]);

function countLines(code) {
  // Mirrors the plugin, which drops a trailing empty line
  return code.replace(/\n$/, "").split("\n").length;
}

function addLineNumbers(html, code) {
  const gutter =
    '<span aria-hidden="true" class="line-numbers-rows">' +
    "<span></span>".repeat(countLines(code)) +
    "</span>";
  return html
    .replace(/^<pre class="([^"]*)"/, '<pre class="$1 line-numbers"')
    .replace(/<\/code><\/pre>$/, `${gutter}</code></pre>`);
}

function withLineNumbers(highlight) {
  return function (code, languageSpec) {
    const html = highlight(code, languageSpec);
    // Empty string: no language given, markdown-it renders the block itself
    if (!html) {
      return html;
    }
    const language = (languageSpec || "").split("/")[0];
    if (LANGUAGES_WITHOUT_LINE_NUMBERS.has(language)) {
      return html;
    }
    return addLineNumbers(html, code);
  };
}

/*
 * Eleventy plugin; must be added after @11ty/eleventy-plugin-syntaxhighlight
 * because it wraps the Markdown highlighter that plugin registers.
 */
function lineNumbersPlugin(eleventyConfig) {
  const highlight = eleventyConfig.markdownHighlighter;
  if (typeof highlight !== "function") {
    throw new Error(
      "prism-line-numbers: no Markdown highlighter registered; add the syntax highlight plugin first."
    );
  }
  eleventyConfig.addMarkdownHighlighter(withLineNumbers(highlight));
}

module.exports = { lineNumbersPlugin, withLineNumbers };
