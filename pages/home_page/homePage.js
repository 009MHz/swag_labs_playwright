const BasePage = require("../basePage");
const { PageInfo, MainForm } = require("../../elements/__home");
const { expect } = require("@playwright/test");

class HomePage extends BasePage {
    constructor(page) {
        super(page);
        this.page = page;
    }

    /** Home Page Interaction */
    async openPage() {
        await this.page.goto(PageInfo.url);
    }

    async insertUserName(username) {
        await this.type(MainForm.userName, username);
        await expect(this.find(MainForm.userName)).not.toBeEmpty();
    }

    async insertPassword(password) {
        await this.type(MainForm.password, password);
        await expect(this.find(MainForm.password)).not.toBeEmpty();
    }

    async clickLoginButton() {
        await this.click(MainForm.loginButton);
    }

    /** Home Page Validation */
    async pageTitlePresence() {
        await this.look(PageInfo.title);
        await expect(this.find(PageInfo.title)).toBeVisible();
        await expect(this.find(PageInfo.title)).toHaveText("Swag Labs");
    }

    async userNameInputPresence() {
        await this.touch(MainForm.userName);
        await expect(this.find(MainForm.userName)).toBeEmpty();
        await expect(this.find(MainForm.userName)).toHaveAttribute("placeholder", "Username");
    }

    async passwordInputPresence() {
        await this.touch(MainForm.passwordXPath);
        await expect(this.find(MainForm.passwordXPath)).toBeEmpty();
        await expect(this.find(MainForm.passwordXPath)).toHaveAttribute("placeholder", "Password");
    }

    async loginButtonPresence() {
        await this.look(MainForm.loginButton);
        await expect(this.find(MainForm.loginButton)).toBeEnabled();
        await expect(this.find(MainForm.loginButton)).toHaveAttribute("value", "Login");
    }
}

module.exports = HomePage;