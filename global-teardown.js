module.exports = async () => {
    if (global.__BROWSER_CONTEXT__) {
        await global.__BROWSER_CONTEXT__.close();
    }
    if (global.__BROWSER__) {
        await global.__BROWSER__.close();
    }
};
