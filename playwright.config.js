const { defineConfig } = require('@playwright/test');

module.exports = defineConfig({
    timeout: 30000,
    retries: 2,
    testDir: 'tests',
    fullyParallel: true,

    use: {
        headless: true,
        viewport: process.env.HEADLESS === 'true' ? { width: 1920, height: 1080 } : null,
        screenshot: {
            mode: 'on',
            fullPage: true,
        },
        video: 'retain-on-failure',
        launchOptions: {
            args: process.env.HEADLESS === 'true' ? [] : ['--start-maximized'],
        },
    },
    projects: [
        {
            name: 'chrome',
            use: { browserName: 'chromium' },
        },
        {
            name: 'firefox',
            use: { browserName: 'firefox' },
        },
        {
            name: 'webkit',
            use: { browserName: 'webkit' },
        },
    ],
    reporter: process.env.SKIP_REPORT
        ? [['list']]
        : [
              ['list'],
              ['allure-playwright', { resultsDir: 'reports', clean: true }],
          ],
});
