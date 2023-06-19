const fs = require('fs');

module.exports = {
    eleventyComputed: {
        excerpt: async data => {
            if (data.description) {
                return data.description;
            }

            const filePath = data.page.inputPath.replace("./_posts", __dirname);
            const fileContent = await fs.readFileSync(filePath, 'utf8');

            // omit front matter
            const parts = fileContent.split('---');

            if (parts.length < 2) {
                // Not a post?
                return "";
            }

            // get the article and strip html tags
            const markdownContent = parts[2].replace(/<\/?[^>]+(>|$)/g, "");
            
            const firstLine = truncateToFirstLine(markdownContent);
            let firstLineWords = firstLine.split(' ');
            const MAX_WORDS = 15;
            const truncatedWords = firstLineWords.length > MAX_WORDS;
            if (truncatedWords) {
                firstLineWords.length = MAX_WORDS;
            }
            let excerpt = firstLineWords.join(' ');
            if (truncatedWords) {
                excerpt += "...";
            }
            return excerpt;
        }
    }

}

function truncateToFirstLine(string) {
    const lines = string.split('\n');
    for (const line of lines) {
        if (line.trim().length > 0) {
            return line.trim();
        }
    }
    return "";
}
