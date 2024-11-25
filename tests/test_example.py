import re
import pytest
from playwright.async_api import async_playwright, Page, expect


@pytest.fixture()
async def page():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context()
        page = await context.new_page()
        yield page
        await context.close()
        await browser.close()


async def test_has_title(page: Page):
    await page.goto("https://playwright.dev/")
    # Expect a title "to contain" a substring.
    await expect(page).to_have_title(re.compile("Playwright"))


async def test_get_started_link(page: Page):
    await page.goto("https://playwright.dev/")
    # Click the get started link.
    await page.get_by_role("link", name="Get started").click()
    # Expects page to have a heading with the name of Installation.
    await expect(page.get_by_role("heading", name="Installation")).to_be_visible()


async def test_karirlab_title_page(page: Page):
    await page.goto("https://staging.karirlab.co/")
    title = await page.title() # passed test
    # title = page.title()  # Intentional Fail
    assert title == "Awali Cerita Karirmu! | Mulai dari KarirLab | Tips Karir Terlengkap!"
