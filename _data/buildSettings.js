const process = require('node:process');

module.exports = function() {
    return {
        environment: process.env.WOLFSOUND_ENVIRONMENT || "development"
    };
};
