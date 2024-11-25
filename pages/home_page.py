from pages.__base import BasePage
from elements.__home import *
from playwright.async_api import Page, expect


class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    async def open_page(self):
        await self.page.goto(PageInfo.url)

    """Login Action"""
    async def insert_user_name(self, username: str):
        await self._type(MainForm.user_name, username)
        await expect(self._find(MainForm.user_name)).not_to_be_empty()

    async def insert_password(self, password: str):
        await self._type(MainForm.password, password)
        await expect(self._find(MainForm.password)).not_to_be_empty()

    async def click_login_button(self):
        await self._click(MainForm.login_btn)

    """Page Header Validation"""
    async def page_title_presence(self):
        await self._look(PageInfo.title)
        await expect(self._find(PageInfo.title)).to_be_visible()
        await expect(self._find(PageInfo.title)).to_have_text("Swag Labs")

    """Login Form Validation"""
    async def login_form_presence(self):
        await self._look(PageInfo.main_form)
        await expect(self._find(PageInfo.title)).to_be_visible()

    async def user_input_presence(self):
        await self._touch(MainForm.user_name)
        await expect(self._find(MainForm.user_name)).to_be_empty()
        await expect(self._find(MainForm.user_name)).to_have_attribute("placeholder", "Username")

    async def pass_input_presence(self):
        await self._touch(MainForm.password)
        await expect(self._find(MainForm.password)).to_be_empty()
        await expect(self._find(MainForm.password)).to_have_attribute("placeholder", "Password")

    async def login_button_presence(self):
        await self._look(MainForm.login_btn)
        await expect(self._find(MainForm.login_btn)).to_be_enabled()
        await expect(self._find(MainForm.login_btn)).to_have_attribute("value", "Login")

    """Login Information Validation"""
    async def allowed_user_form_presence(self):
        await self._look(FormInfo.user_form)
        await expect(self._find(FormInfo.user_form)).not_to_have_text("")

    async def allowed_user_title_presence(self):
        await self._look(FormInfo.user_header)
        await expect(self._find(FormInfo.user_header)).to_have_text("Accepted usernames are:")

    async def allowed_user_content_presence(self):
        await self._look(FormInfo.user_form)
        await expect(self._find(FormInfo.user_form)).to_contain_text("standard_user")
        await expect(self._find(FormInfo.user_form)).to_contain_text("locked_out_user")
        await expect(self._find(FormInfo.user_form)).to_contain_text("problem_user")
        await expect(self._find(FormInfo.user_form)).to_contain_text("performance_glitch_user")
        await expect(self._find(FormInfo.user_form)).to_contain_text("error_user")
        await expect(self._find(FormInfo.user_form)).to_contain_text("visual_user")
        
    async def allowed_pass_title_presence(self):
        await self._look(FormInfo.pass_header)
        await expect(self._find(FormInfo.pass_header)).to_have_text("Password for all users:")

    async def allowed_pass_content_presence(self):
        await self._look(FormInfo.pass_form)
        await expect(self._find(FormInfo.pass_form)).to_contain_text("secret_sauce")


    # async def sort_control_presence(self):
    #     await self._look(JobSort.control)
    #     await expect(self._find(JobSort.control)).to_be_visible()
    #
    # async def email_presence(self):
    #     await self._look(DataDiri.Initial.email_label)
    #     await expect(self._find(DataDiri.Initial.email_label)).to_have_text("Email")
    #
    #     await self._touch(DataDiri.Initial.email_input)
    #     await expect(self._find(DataDiri.Initial.email_input)).to_be_empty()
    #     await expect(self._find(DataDiri.Initial.email_input)).to_have_attribute("placeholder", "johndoe@gmail.com")
    #
    #
    # async def sort_item_presence(self):
    #     for item in JobSort.options:
    #         await self._look(JobSort.control_expanded)
    #         await expect(self._find(JobSort.control_expanded)).to_be_visible()
    #
    #         await self._look(JobSort.options[item])
    #         await expect(self._find(JobSort.options[item])).to_be_visible()
    #         await self._click(JobSort.options[item])
    #         await self.sort_control_click()