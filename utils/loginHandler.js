const HomePage = require('../pages/home_page/homePage');

class LoginHandler {
    constructor(page) {
        this.page = page;
        this.homePage = new HomePage(page);
    }

    async login(username, password) {
        await this.homePage.openPage();
        await this.homePage.insertUserName(username);
        await this.homePage.insertPassword(password);
        await this.homePage.clickLoginButton();
    }
}

module.exports = LoginHandler;
