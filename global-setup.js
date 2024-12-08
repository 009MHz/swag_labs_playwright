require('dotenv').config();
const BrowserConfig = require('./utils/browserConfig');

module.exports = async () => {
    const browserConfig = new BrowserConfig();
    await browserConfig.setupBrowser();
    global.browserConfig = browserConfig;
};
