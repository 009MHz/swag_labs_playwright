from pages.__base import BasePage
from elements.__home import *
from playwright.async_api import Page, expect


class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    """Home Page Interaction"""
    async def open_page(self):
        await self.page.goto(PageInfo.url)

    async def insert_user_name(self, username: str):
        await self._type(MainForm.user_name, username)
        await expect(self._find(MainForm.user_name)).not_to_be_empty()

    async def insert_password(self, password: str):
        await self._type(MainForm.password, password)
        await expect(self._find(MainForm.password)).not_to_be_empty()

    async def click_login_button(self):
        await self._click(MainForm.login_btn)

    """Home Page Validation"""
    async def page_title_presence(self):
        await self._look(PageInfo.title)
        await expect(self._find(PageInfo.title)).to_be_visible()
        await expect(self._find(PageInfo.title)).to_have_text("Swag Labs")

    async def user_name_input_presence(self):
        await self._touch(MainForm.user_name)
        await expect(self._find(MainForm.user_name)).to_be_empty()
        await expect(self._find(MainForm.user_name)).to_have_attribute("placeholder", "Username")

    async def password_input_presence(self):
        await self._touch(MainForm.password_xpath)
        await expect(self._find(MainForm.password_xpath)).to_be_empty()
        await expect(self._find(MainForm.password_xpath)).to_have_attribute("placeholder", "Password")

    async def login_button_presence(self):
        await self._look(MainForm.login_btn)
        await expect(self._find(MainForm.login_btn)).to_be_enabled()
        await expect(self._find(MainForm.login_btn)).to_have_attribute("value", "Login")

