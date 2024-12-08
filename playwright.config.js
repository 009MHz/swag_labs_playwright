const { defineConfig } = require('@playwright/test');

module.exports = defineConfig({
    timeout: 30000,
    retries: 2,
    testDir: './tests',
    use: {
        browserName: 'chromium',
        headless: true,
        viewport: { width: 1280, height: 720 },
        screenshot: 'on',
        video: 'retain-on-failure',
    },
});
