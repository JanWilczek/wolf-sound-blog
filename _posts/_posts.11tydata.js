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

            const htmlContent = parts[2];
            const markdownContent = stripHtml(htmlContent);
            const firstLine = truncateToFirstLine(markdownContent);

            // the recommended length of a meta description
            const MAX_CHARACTERS = 160;
            const truncatedCharacters = firstLine.length > MAX_CHARACTERS;
            if (truncatedCharacters) {
                firstLine.length = MAX_CHARACTERS;
            }
            let excerpt = firstLine;
            if (truncatedCharacters) {
                // replace the last 3 characters with ellipsis
                excerpt = excerpt.substring(0, MAX_CHARACTERS - 3) + "...";
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

function stripHtml(string) {
    return string.replace(/<\/?[^>]+(>|$)/g, "");
}
