const { chromium, firefox, webkit } = require('playwright');
const fs = require('fs');
const path = require('path');
const SessionHandler = require('./sessHandler');
const LoginHandler = require('./loginHandler');

class BrowserConfig {
    constructor() {
        this.browser = null;
        this.page = null;
    }

    isHeadless() {
        return process.env.HEADLESS === 'true';
    }

    async setupBrowser() {
        const browserType = process.env.BROWSER || 'chromium';
const headless = this.isHeadless();
const launchOptions = { headless, args: ['--start-maximized'] };

const mode = process.env.MODE || 'local';  // Default to 'local' if MODE is not set

switch (mode) {
    case 'pipeline':
    case 'local':
        this.browser = await { chromium, firefox, webkit }[browserType].launch(launchOptions);
        break;
    case 'grid':
        const remoteUrl = 'http://remote-playwright-server:4444';
        this.browser = await { chromium, firefox, webkit }[browserType].connect(remoteUrl);
        break;
    default:
        throw new Error(`Unsupported execution type: ${mode}`);
}

    }

    async createPage(storageState = null, userType = 'user') {
        const contextOptions = {
            viewport: { width: 1920, height: 1080 },
        };
        if (storageState) {
            contextOptions.storageState = await this.createSession(userType);
        }
        const context = await this.browser.newContext(contextOptions);
        this.page = await context.newPage();
        return this.page;
    }

    async createSession(userType) {
        if (this.sessionHandler.isSessionExpired()) {
            const context = await this.browser.newContext();
            const page = await context.newPage();
            const login = new LoginHandler(page);
            const { username, password } = this.sessionHandler.getCredentials(userType);

            await login.login(username, password);
            const storageState = await context.storageState();
            this.sessionHandler.saveSession(storageState);
            await context.close();
        }
        return this.sessionHandler.sessionPath;
    }

    isSessionExpired(sessionPath) {
        const session = JSON.parse(fs.readFileSync(sessionPath));
        const currentTime = Date.now() / 1000;

        return session.cookies.some(cookie => cookie.expires <= currentTime);
    }

    getCredentials(userType) {
        const credentialsPath = path.resolve('data/credentials.json');
        if (!fs.existsSync(credentialsPath)) {
            throw new Error(`Credentials file not found: ${credentialsPath}`);
        }

        const credentials = JSON.parse(fs.readFileSync(credentialsPath));
        if (!credentials[userType]) {
            throw new Error(`User type '${userType}' not found in credentials`);
        }

        return credentials[userType];
    }
}

module.exports = BrowserConfig;
