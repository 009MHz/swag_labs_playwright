import allure
from playwright.async_api import Page, expect
from elements.__inventory import PageInfo
from pages.__base import BasePage


class PreCond(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    async def load_page(self):
        with allure.step("▸ Navigate to Inventory page"):
            await self.page.goto(PageInfo.url)
            await expect(self._find(PageInfo.main_display)).to_be_visible()
