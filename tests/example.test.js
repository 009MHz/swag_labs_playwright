const { test, expect } = require('@playwright/test');

test.describe('Playwright Test Suite', () => {

    test('should have the correct title', async ({ page }) => {
        await page.goto('https://playwright.dev/');
        // Expect a title "to contain" a substring.
        await expect(page).toHaveTitle(/Playwright/);
    });

    test('should navigate to the Get Started link', async ({ page }) => {
        await page.goto('https://playwright.dev/');
        // Click the get started link.
        await page.getByRole('link', { name: 'Get started' }).click();
        // Expects page to have a heading with the name of Installation.
        await expect(page.getByRole('heading', { name: 'Installation' })).toBeVisible();
    });

});
