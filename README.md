# Guides

1. **Set up JavaScript environment:**
   - Install Node.js and npm.
   - Install Playwright using npm.
   - Install Allure Command Line.

2. **Initialize Playwright:**
   - Install necessary browser binaries.

3. **Write test cases:**
   - Use Playwright's API to create and run browser tests.
   - Configure Allure to generate test reports.

4. **Run tests and generate reports:**
   - Use the Playwright Test Runner to execute tests.
   - Use Allure to generate and view reports.

5. **Test Runner Command Line:**
   - Test Runner Configurations.
   - Implementation Example.

---

## 1. Setting Up Your Environment

### Install Node.js
Ensure Node.js and npm are installed on your machine. You can download them from [nodejs.org](https://nodejs.org/).

### Install Playwright
Use npm to install Playwright globally or as a development dependency in your project.

```bash
npm install playwright --save-dev
```

### Install Allure Command Line
Follow the instructions to install Allure Command Line from [the official Allure website](https://docs.qameta.io/allure/#_get_started).

For example, on macOS using Homebrew:

```bash
brew install allure
```

On Windows, download the binary from the [official site](https://docs.qameta.io/allure/#_get_started) and add it to your PATH.

---

## 2. Initialize Playwright

You need to install the necessary browser binaries.

```bash
npx playwright install
```

---

## 3. Write Your First Test

Create a new directory for your tests, e.g., `tests`. Inside this directory, create a file called `test_example.spec.js` with the following content:

```javascript
const { test, expect } = require('@playwright/test');

test.describe('Playwright Test Suite', () => {
    test('should navigate to Playwright page and verify title', async ({ page }) => {
        await page.goto('https://example.com');
        await expect(page).toHaveTitle(/Example Domain/);
    });
});
```

---

## 4. Run Your Tests

Run your tests using the Playwright Test Runner.

```bash
npx playwright test
```

### Generate and Open Allure Report

Generate the Allure report using the following command:

```bash
allure generate <results-folder> --clean
allure open
```

This will generate the report and open it in your default web browser.

---

## 5. Test Runner Command Line

### Test Runner Configurations
- `--headed`: Run tests in a headed mode (default: _headless_).
- `--browser`: Specify the browser to use (chromium, firefox, webkit).
- `--device`: Emulate a specific device.
- `--trace`: Record trace for each test (on, off, retain-on-failure).
- `--video`: Record video for each test (on, off, retain-on-failure).
- `--screenshot`: Capture screenshots automatically (on, off, only-on-failure).
- `--project`: Run tests for a specific project.
- `--workers`: Specify the number of parallel workers (default: based on system capabilities).

---

### Implementation Examples:

*Run tests in all browsers:*
```bash
npx playwright test
```

*Run tests in a specific browser (e.g., Firefox):*
```bash
npx playwright test --browser=firefox
```

*Run a specific test file:*
```bash
npx playwright test tests/test_example.spec.js
```

*Run a specific test with a name or tag:*
```bash
npx playwright test -g "should navigate to Playwright page"
```

*Run tests with video and screenshot capturing for failures:*
```bash
npx playwright test --video=retain-on-failure --screenshot=only-on-failure
```

*Run tests and generate Allure reports:*
```bash
npx playwright test --reporter=line,allure-playwright
allure generate ./allure-results --clean
allure open
```

--- 
