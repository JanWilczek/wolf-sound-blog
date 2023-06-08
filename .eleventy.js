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

    eleventyConfig.addCollection("posts", function(collectionApi) {
        return collectionApi.getFilteredByGlob("_posts/**/*.md");
    });

    // Categories collections
    eleventyConfig.addCollection("ccpp", function(collectionApi) {
        return collectionApi.getFilteredByGlob("_posts/c-c++/*.md");
    });
    eleventyConfig.addCollection("audio_fx", function(collectionApi) {
        return collectionApi.getFilteredByGlob("_posts/fx/*.md");
    });
    eleventyConfig.addCollection("dsp", function(collectionApi) {
        return collectionApi.getFilteredByGlob("_posts/dsp/*.md");
    });
    eleventyConfig.addCollection("programming_in_general", function(collectionApi) {
        return collectionApi.getFilteredByGlob("_posts/programming-in-general/*.md");
    });
    eleventyConfig.addCollection("synthesis", function(collectionApi) {
        return collectionApi.getFilteredByGlob("_posts/synthesis/*.md");
    });
    eleventyConfig.addCollection("podcast", function(collectionApi) {
        return collectionApi.getFilteredByGlob("_posts/podcast/*.md");
    });
    eleventyConfig.addCollection("python", function(collectionApi) {
        return collectionApi.getFilteredByGlob("_posts/**/*.md").filter(item => {
            return "python" in item.data.categories;
        });
    })
    eleventyConfig.addCollection("sound_in_general", function(collectionApi) {
        return collectionApi.getFilteredByGlob("_posts/**/*.md").filter(item => {
            return "Sound in general" in item.data.categories;
        });
    })

    return {
        dir: {
            layouts: "_layouts"
        }
    }
};
