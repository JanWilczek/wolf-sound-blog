const markdownIt = require("markdown-it");
const markdownItAnchor = require("markdown-it-anchor");
const markdownItFootnote = require("markdown-it-footnote");
const syntaxHighlight = require("@11ty/eleventy-plugin-syntaxhighlight");

module.exports = function(eleventyConfig) {
    // Add header anchor and footnotes 0plugin to Markdown renderer
    const markdownLib = markdownIt({html: true, typographer: true});
    markdownLib.use(markdownItFootnote).use(markdownItAnchor);
    eleventyConfig.setLibrary("md", markdownLib);

    // Enable syntax highlighting
    eleventyConfig.addPlugin(syntaxHighlight);

    // Copy the assets folder to the _site folder
    eleventyConfig.addPassthroughCopy("assets");

    eleventyConfig.addCollection("ccpp", function(collectionApi) {
        return collectionApi.getFilteredByGlob("_posts/c-c++/*.md");
    });

    return {
        dir: {
            layouts: "_layouts"
        }
    }
};
