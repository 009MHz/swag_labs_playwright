module.exports = async () => {
    if (global.browserConfig?.browser) {
        await global.browserConfig.browser.close();
    }
};
