const { test, expect } = require("@playwright/test");
const HomePage = require("../../pages/home_page/homePage");

/** Test Fixtures */
test.describe("Home Page", () => {
    let homePage;

    test.beforeEach(async ({ page }) => {
        homePage = new HomePage(page);
        await test.step("Navigate to the saucedemo home page", async () => {
            await homePage.openPage();
        });
    });

    test("The Page Header should be equal with 'Swag Labs'", async () => {
        await test.step("Verify the Header Existence", async () => {
            await homePage.pageTitlePresence();
        });
    });

    test("The Login Form should exist and be accessible", async () => {
        await test.step("1. Check the username input", async () => {
            await homePage.userNameInputPresence();
        });

        await test.step("2. Check the password input", async () => {
            await homePage.passwordInputPresence();
        });

        await test.step("3. Check the Login button", async () => {
            await homePage.loginButtonPresence();
        });
    });

    test("User must be able to interact with the input form", async () => {
        await test.step("1. Insert a valid text in the username input", async () => {
            await homePage.insertUserName("qa_test01@gmail.com");
        });

        await test.step("2. Insert a valid password in the password input", async () => {
            await homePage.insertPassword("qa123456");
        });

        await test.step("3. Click on the login button", async () => {
            await homePage.clickLoginButton();
        });
    });
});