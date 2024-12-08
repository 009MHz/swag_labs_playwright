import pytest
from pages.home_page.home_page import HomePage
import allure
from allure import severity_level as severity


@pytest.fixture(scope='function')
async def home_page(page):
    home_page = HomePage(page)
    with allure.step("▸ Navigate to the saucedemo home page"):
        await home_page.open_page()
    return home_page


@allure.epic("Home")
@allure.story("Smoke Testing: Home Page")
@allure.feature("Home")
@pytest.mark.positive
@pytest.mark.smoke
class TestSmokeHomePage:
    @allure.title('The Page Header should be equal with "Swag Labs"')
    @allure.feature("Home/ Header")
    @allure.severity(severity.NORMAL)
    async def test_home_page_header(self, home_page):
        with allure.step("Verify the Header Existence"):
            await home_page.page_title_presence()

    @allure.feature("Home/ Login Form")
    @allure.title("The Login Form should be exist and accessible")
    @allure.severity(severity.CRITICAL)
    async def test_main_login_form(self, home_page):
        with allure.step("1. Validate the username input"):
            await home_page.user_input_presence()
