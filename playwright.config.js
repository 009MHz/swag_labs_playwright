const BrowserConfig = require('./utils/browserConfig');
const fs = require('fs');
const path = require('path');

const config = {
    retries: 1,
    use: {
        baseURL: 'https://www.saucedemo.com/',
        viewport: { width: 1920, height: 1080 },
        headless: process.env.HEADLESS === 'true',
        trace: 'on-first-retry', // Example trace configuration
        video: 'retain-on-failure', // Example video recording configuration
        screenshot: 'only-on-failure', // Example screenshot configuration
    },
    projects: [
        {
            name: 'chromium',
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
    globalSetup: './global-setup.js',
    globalTeardown: './global-teardown.js',
    outputDir: './reports',
    testDir: './tests',
    reporter: [
        ['dot'], // You can add other reporters if necessary
        ['allure-playwright', { outputFolder: './reports' }],
        ['html', { open: 'never' }], // Example additional reporter
    ],
};

module.exports = config;
