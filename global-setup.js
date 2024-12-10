const { chromium, firefox, webkit } = require('@playwright/test');

async function globalSetup(config) {
    const browsers = {
        chromium: chromium,
        firefox: firefox,
        webkit: webkit,
    };

    for (const project of config.projects) {
        const browserType = browsers[project.use.browserName];
        if (browserType) {
            const browser = await browserType.launch({
                headless: project.use.headless,
                args: project.use.browserName === 'chromium' ? ['--start-maximized'] : [],
            });
            const context = await browser.newContext();
            const page = await context.newPage();

            // Set screen size manually for Firefox and WebKit
            if (project.use.browserName !== 'chromium') {
                const screenSize = await page.evaluate(() => ({
                    width: window.screen.availWidth,
                    height: window.screen.availHeight,
                }));
                await page.setViewportSize(screenSize);
            }

            await context.close();
            await browser.close();
        }
    }
}

module.exports = globalSetup;
