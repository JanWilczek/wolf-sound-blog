const markdownIt = require("markdown-it");
const markdownItAnchor = require("markdown-it-anchor");
const markdownItFootnote = require("markdown-it-footnote");
const syntaxHighlight = require("@11ty/eleventy-plugin-syntaxhighlight");
const katex = require("katex"); 

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

    // Add katex support from https://benborgers.com/posts/eleventy-katex  
    eleventyConfig.addFilter("latex", (content) => {
        return content.replace(/\$\$(.+?)\$\$/g, (_, equation) => {
            const cleanEquation = equation.replace(/&lt;/g, "<").replace(/&gt;/g, ">");

            return katex.renderToString(cleanEquation, { throwOnError: false });
        });
    });

    // Define a post_url Liquid tag for cross referencing
    // https://rusingh.com/articles/2020/04/24/implement-jekyll-post-url-tag-11ty-shortcode/
    eleventyConfig.addShortcode("post_url", (collection, relativePostPath) => {
        try {
        if (collection.length < 1) {
            throw "Collection appears to be empty";
        }
        if (!Array.isArray(collection)) {
            throw "Collection is an invalid type - it must be an array!";
        }
        if (typeof relativePostPath !== "string") {
            throw "Relative post path is an invalid type - it must be a string!";
        }
    
        const found = collection.find(p => p.inputPath.includes(relativePostPath));
        if (found === 0 || found === undefined) {
            throw `${relativePostPath} not found in specified collection.`;
        } else {
            return found.url;
        }
        } catch (e) {
        console.error(
            `An error occured while searching for the url to ${relativePostPath}. Details:`,
            e
        );
        }
    });

    // Alias for the absolute_url filter.
    eleventyConfig.addFilter("absolute_url", function(allContent, url) {
        return eleventyConfig.getFilter("url")(url);
    });

    eleventyConfig.addShortcode("link", filename => {
        return eleventyConfig.getFilter("url")(filename);
    });

    return {
        dir: {
            layouts: "_layouts"
        }
    }
};
