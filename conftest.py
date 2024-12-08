import pytest
import os
import asyncio
import allure
from utils.browser_config import Config
from playwright.async_api import async_playwright

runner = Config()


def pytest_addoption(parser):
    parser.addoption('--env', action='store', default='test', help='Specify the test environment')
    parser.addoption('--mode', help='Specify the execution mode: local, grid, pipeline', default='local')
    parser.addoption('--headless', action='store_true', default=False, help='Run tests in headless mode')


def pytest_configure(config):
    os.environ["env"] = config.getoption('env')
    os.environ["mode"] = config.getoption('mode') or 'local'
    os.environ["headless"] = str(config.getoption('headless'))
    os.environ["screenshot"] = os.environ.get("screenshot", "off").lower()


@pytest.fixture()
async def playwright():
    async with async_playwright() as playwright:
        yield playwright


@pytest.fixture()
async def browser(playwright):
    await runner.setup_browser(playwright)
    yield runner.browser
    await runner.browser.close()


@pytest.fixture()
async def page(browser):
    page_instance = await runner.setup_page()
    yield page_instance
    await runner.capture_handler()
    await page_instance.close()


@pytest.fixture()
async def user_auth(browser):
    page_instance = await runner.user_mode("standard")
    yield page_instance
    await runner.capture_handler()
    await page_instance.close()


@pytest.fixture()
async def admin_auth(browser):
    page_instance = await runner.user_mode("admin")
    yield page_instance
    await runner.capture_handler()
    await page_instance.close()


@pytest.fixture()
async def super_auth(browser):
    page_instance = await runner.user_mode("super_admin")
    yield page_instance
    await runner.capture_handler()
    await page_instance.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed: # config on fail only | if rep.when == "call":
        screenshot_path = os.path.join("reports/screenshots", f"{item.name}.png")
        os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)

        try:
            page = item.funcargs.get('page') or item.funcargs.get('auth_page')
            if page:
                loop = asyncio.get_event_loop()
                loop.run_until_complete(page.screenshot(path=screenshot_path, full_page=True))
                with open(screenshot_path, "rb") as image_file:
                    allure.attach(
                        image_file.read(),
                        name="screenshot",
                        attachment_type=allure.attachment_type.PNG
                    )
        except Exception as e:
            print(f"Failed to take screenshot: {e}")
