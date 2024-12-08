class BasePage {
    constructor(page) {
        this.page = page;
    }

    /**
     * Find an element locator.
     * @param {string} locator - The selector of the element.
     * @returns {Locator} - The element locator.
     */
    find(locator) {
        return this.page.locator(locator);
    }

    /**
     * Wait for an element to be visible.
     * @param {string} locator - The selector of the element.
     * @param {number} [timeout=10000] - Timeout in milliseconds.
     */
    async look(locator, timeout = 10000) {
        await this.page.waitForSelector(locator, { state: "visible", timeout });
    }

    /**
     * Wait for an element to be hidden.
     * @param {string} locator - The selector of the element.
     * @param {number} [timeout=7000] - Timeout in milliseconds.
     */
    async conceal(locator, timeout = 7000) {
        await this.page.waitForSelector(locator, { state: "hidden", timeout });
    }

    /**
     * Ensure an element is visible and enabled.
     * @param {string} locator - The selector of the element.
     * @param {number} [timeout=10000] - Timeout in milliseconds.
     */
    async touch(locator, timeout = 10000) {
        await this.look(locator, timeout);
        await this.page.locator(locator).isEnabled({ timeout });
    }

    /**
     * Type text into an input field.
     * @param {string} locator - The selector of the element.
     * @param {string} text - The text to type.
     * @param {number} [timeout=10000] - Timeout in milliseconds.
     */
    async type(locator, text, timeout = 10000) {
        await this.look(locator, timeout);
        await this.page.locator(locator).fill(text);
    }

    /**
     * Click on an element.
     * @param {string} locator - The selector of the element.
     * @param {number} [timeout=10000] - Timeout in milliseconds.
     */
    async click(locator, timeout = 10000) {
        await this.touch(locator, timeout);
        await this.page.locator(locator).click();
    }

    /**
     * Perform a double click on an element.
     * @param {string} locator - The selector of the element.
     * @param {number} [timeout=10000] - Timeout in milliseconds.
     */
    async doubleClick(locator, timeout = 10000) {
        await this.touch(locator, timeout);
        await this.page.locator(locator).dblclick();
    }

    /**
     * Forcefully click on an element with a delay.
     * @param {string} locator - The selector of the element.
     * @param {number} [timeout=10000] - Timeout in milliseconds.
     */
    async force(locator, timeout = 10000) {
        await this.look(locator, timeout);
        await this.page.locator(locator).click({ force: true, delay: 500 });
    }
}

module.exports = BasePage;
