import pytest
from pages.home_page import HomePage
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
@pytest.mark.job_card
class TestSmokeHomePage:
    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title('The Page Header should be equal with "Swag Labs"')
    @allure.feature("Home/ Header")
    @allure.severity(severity.NORMAL)
    async def test_home_page_header(self, home_page):
        with allure.step("Verify the Header Existence"):
            await home_page.page_title_presence()

    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.feature("Home/ Login Form")
    @allure.title("The Login Form should be exist and accessible")
    @allure.severity(severity.CRITICAL)
    async def test_main_login_form(self, home_page):
        with allure.step("1. Validate the username input"):
            await home_page.user_input_presence()
        with allure.step("2. Validate the password input"):
            await home_page.pass_input_presence()
        with allure.step("3. Validate the Login button"):
            await home_page.login_form_presence()

    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.feature("Home/ Login Information")
    @allure.title("The Login Information should be displayed and contains the correct information")
    @allure.severity(severity.NORMAL)
    async def test_allowed_credentials(self, home_page):
        with allure.step("1. Validate the allowed username form"):
            await home_page.allowed_user_form_presence()
        with allure.step("2. Validate the allowed username content"):
            await home_page.allowed_user_title_presence()
            await home_page.allowed_user_content_presence()
        with allure.step("3. Validate the allowed password"):
            await home_page.allowed_pass_title_presence()
            await home_page.allowed_pass_content_presence()
