from pages.home_page.home_page import HomePage
from playwright.async_api import Page
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class LoginInit(HomePage):
    def __init__(self, page: Page):
        super().__init__(page)

    async def create_session(self, username: str, password: str):
        logger.info("Opening Login Page")
        await self.open_page()
        logger.info(f"Providing username type: {username}")
        await self.insert_user_name(username)
        logger.info("Providing Valid Password")
        await self.insert_password(password)
        await self.click_login_button()
