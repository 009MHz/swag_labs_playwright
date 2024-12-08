const { defineConfig } = require('@playwright/test');
const {PageScreenshotOptions} = require("playwright-core");

module.exports = defineConfig({
    timeout: 30000,
    retries: 1,
    testDir: './tests',
    use: {
        browserName: 'chromium',
        headless: true,
        viewport: { width: 1280, height: 720 },
        screenshot: {
            mode: "on",
            fullPage: true
        },
        video: 'retain-on-failure',
    },
    reporter: [
        ['list'],
        ['allure-playwright',
            {resultsDir: 'reports', clean: true,}],
    ],
});
