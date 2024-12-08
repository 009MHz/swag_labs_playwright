const fs = require('fs');
const path = require('path');

class SessionHandler {
    constructor(sessionPath = '.auth/session.json', credentialsPath = 'data/credentials.json') {
        this.sessionPath = sessionPath;
        this.credentialsPath = credentialsPath;
    }

    isSessionExpired() {
        if (!fs.existsSync(this.sessionPath)) return true;

        const session = JSON.parse(fs.readFileSync(this.sessionPath));
        const currentTime = Date.now() / 1000;

        return session.cookies.some(cookie => cookie.expires <= currentTime);
    }

    saveSession(storageState) {
        fs.writeFileSync(this.sessionPath, JSON.stringify(storageState, null, 2));
    }

    getCredentials(userType) {
        if (!fs.existsSync(this.credentialsPath)) {
            throw new Error(`Credentials file not found: ${this.credentialsPath}`);
        }

        const credentials = JSON.parse(fs.readFileSync(this.credentialsPath));
        if (!credentials[userType]) {
            throw new Error(`User type '${userType}' not found in credentials`);
        }

        return credentials[userType];
    }
}

module.exports = SessionHandler;
