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


@allure.epic("Login")
@allure.story("Smoke Testing: Home Page")
@allure.feature("Login")
class TestLoginAction:
    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.feature("Home/ Login Form")
    @allure.title("User should be navigated to the Inventory page after successful login attempt")
    @allure.severity(severity.CRITICAL)
    async def test_success_login_flow(self, home_page):
        with allure.step("1. Insert the valid username"):
            await home_page.insert_user_name("standard_user")

        with allure.step("2. Insert the valid password"):
            await home_page.insert_password("secret_sauce")

        with allure.step("3. Click on the Login button"):
            await home_page.click_login_button()

        with allure.step("4. Validate the successfully logged in state"):
            await home_page.login_attempt_success()
