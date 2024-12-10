const { defineConfig } = require('@playwright/test');

module.exports = defineConfig({
    timeout: 30000,
    retries: 2,
    testDir: 'tests',
    fullyParallel: true,

    globalSetup: require.resolve('./global-setup'),
    globalTeardown: require.resolve('./global-teardown'),

    use: {
        screenshot: 'on',
        video: 'retain-on-failure',
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
