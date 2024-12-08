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
        with allure.step("1. Check the username input"):
            await home_page.user_name_input_presence()
        with allure.step("2. Check the password input"):
            await home_page.password_input_presence()
        with allure.step("2. Check the Login button"):
            await home_page.login_button_presence()

    @allure.feature("Home/ Login Form")
    @allure.title("User must be able to interact with the input form")
    @allure.severity(severity.CRITICAL)
    async def test_main_login_form(self, home_page):
        with allure.step("1. Insert a valid text on the username input"):
            await home_page.insert_user_name("qa_test01@gmail.com")
        with allure.step("2. Insert a valid password on the password input"):
            await home_page.insert_password("qa123456")
        with allure.step("3. Click on the login button"):
            await home_page.click_login_button()
        # validate the login action result

