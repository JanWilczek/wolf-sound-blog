const markdownIt = require("markdown-it");
const markdownItAnchor = require("markdown-it-anchor");
const markdownItFootnote = require("markdown-it-footnote");
const markdownItAttrs = require("markdown-it-attrs");
const markdownItTexmath = require("markdown-it-texmath");
const syntaxHighlight = require("@11ty/eleventy-plugin-syntaxhighlight");
const katex = require("katex");
const site = require("./_data/site.json");
const { wordCount } = require("eleventy-plugin-wordcount");
const pluginRss = require("@11ty/eleventy-plugin-rss");
const { minify } = require("terser");

module.exports = function (eleventyConfig) {
  // Add header anchor and footnotes plugin to Markdown renderer
  const markdownLib = markdownIt({ html: true, typographer: true });
  markdownLib
    .use(markdownItFootnote)
    .use(markdownItAnchor)
    .use(markdownItAttrs, {
      leftDelimiter: "{:",
      rightDelimiter: "}",
      allowedAttributes: [],
    })
    .use(markdownItTexmath, {
      engine: katex,
      delimiters: ["dollars", "beg_end"],
      katexOptions: {
        throwOnError: true,
        strict: false,
      },
    });
  eleventyConfig.setLibrary("md", markdownLib);

  // Watch CSS files for changes
  eleventyConfig.setBrowserSyncConfig({
    files: "./_site/assets/**/*.css",
  });

  // Enable syntax highlighting
  eleventyConfig.addPlugin(syntaxHighlight);

  // For counting words
  eleventyConfig.addPlugin(wordCount);

  // Copy the assets folder to the _site folder
  eleventyConfig.addPassthroughCopy("assets");
  eleventyConfig.addPassthroughCopy("wp-content");
  eleventyConfig.addPassthroughCopy("favicon.png");
  eleventyConfig.addPassthroughCopy("ads.txt");
  eleventyConfig.addPassthroughCopy("robots.txt");
  eleventyConfig.addPassthroughCopy(".htaccess");

  eleventyConfig.addCollection("posts", function (collectionApi) {
    return collectionApi.getFilteredByGlob("_posts/**/*.md");
  });

  // Categories collections
  eleventyConfig.addCollection("ccpp", function (collectionApi) {
    return getPostsForCategory(collectionApi, "c/c++");
  });
  eleventyConfig.addCollection("audio_fx", function (collectionApi) {
    return getPostsForCategory(collectionApi, "audio fx");
  });
  eleventyConfig.addCollection("dsp", function (collectionApi) {
    return getPostsForCategory(collectionApi, "digital signal processing");
  });
  eleventyConfig.addCollection(
    "programming_in_general",
    function (collectionApi) {
      return getPostsForCategory(collectionApi, "programming in general");
    }
  );
  eleventyConfig.addCollection("synthesis", function (collectionApi) {
    return getPostsForCategory(collectionApi, "sound synthesis");
  });
  eleventyConfig.addCollection("podcast", function (collectionApi) {
    return getPostsForCategory(collectionApi, "podcast");
  });
  eleventyConfig.addCollection("python_category", function (collectionApi) {
    return getPostsForCategory(collectionApi, "python");
  });
  eleventyConfig.addCollection("sound_in_general", function (collectionApi) {
    return getPostsForCategory(collectionApi, "sound in general");
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

      const found = collection.find((p) =>
        p.inputPath.includes(relativePostPath)
      );
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
  eleventyConfig.addFilter("absolute_url", function (allContent, url) {
    return eleventyConfig.getFilter("url")(url);
  });

  // Fix for Jekyll's for the relative_url filter.
  eleventyConfig.addFilter("relative_url", function (url) {
    return site.baseurl + url;
  });

  eleventyConfig.addShortcode("link", (collection, relativeFilePath) => {
    try {
      if (collection.length < 1) {
        throw "Collection appears to be empty";
      }
      if (!Array.isArray(collection)) {
        throw "Collection is an invalid type - it must be an array!";
      }
      if (typeof relativeFilePath !== "string") {
        throw "Relative file path is an invalid type - it must be a string!";
      }

      const found = collection.find((p) =>
        p.inputPath.includes(relativeFilePath)
      );
      if (found === 0 || found === undefined) {
        throw `${relativeFilePath} not found in specified collection.`;
      } else {
        return found.url;
      }
    } catch (e) {
      console.error(
        `An error occured while searching for the url to ${relativeFilePath}. Details:`,
        e
      );
    }
  });

  eleventyConfig.addFilter("normalize_whitespace", (string) => {
    if (typeof string !== "string") {
      throw "normalize_whitespace: argument must be a string!";
    }

    return string.replace(/\s\s+/g, " ");
  });

  eleventyConfig.addLiquidFilter("truncate_to_first_newline", (string) => {
    return string.split("\n")[0];
  });

  eleventyConfig.addPlugin(pluginRss);

  // Return all the tags used in a collection
  eleventyConfig.addFilter("getAllTags", (collection) => {
    let tagSet = new Set();
    for (let item of collection) {
      (item.data.tags || []).forEach((tag) => tagSet.add(tag));
    }
    return Array.from(tagSet);
  });

  eleventyConfig.addLiquidFilter("jsmin", async function (code) {
    try {
      const minified = await minify(code);
      return minified.code;
    } catch (err) {
      console.error("Terser error: ", err);
      // Fail gracefully.
      return code;
    }
  });

  return {
    dir: {
      layouts: "_layouts",
    },
  };
};

function getPostsForCategory(collectionApi, category) {
  return collectionApi.getFilteredByGlob("_posts/**/*.md").filter((item) => {
    return item.data.categories
      .map((categoryName) => {
        return categoryName.toLowerCase();
      })
      .includes(category);
  });
}
