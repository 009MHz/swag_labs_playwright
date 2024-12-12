import pytest
import allure
from allure import severity_level as severity
from pages.invent_page import PreCond
from pages.invent_page.inventory_page import InventPage


@pytest.fixture(scope='function')
async def invent(user_auth):
    inventory = InventPage(user_auth)
    pre_cond = PreCond(inventory.page)
    await pre_cond.load_page()
    return inventory


@allure.epic("Complex")
@allure.story("Checkout item processes with removal should be works properly")
@allure.feature("Purchase", "Checkout")
@pytest.mark.positive
@pytest.mark.smoke
class TestPurchasingFlow:
    @allure.feature(
        "Inventory/ Purchase",
        "Your Cart/ Checkout",
        "Checkout/ Customer Info",
        "Checkout/ Overview",
        "Checkout/ Completion"
    )
    @allure.title("User should be able to reach complete checkout screen after purchased item removal")
    @allure.severity(severity.CRITICAL)
    async def test_complex_purchase(self, invent):
        with allure.step("1. Click Add to cart on the random item "):
            await invent.click_ordered_add_to_chart(3)
            await invent.cart_item_counter(3)

        with allure.step("2. Go to Your Chart Page"):
            await invent.click_chart_icon()
            await invent.cart_page_section_presence()
            await invent.cart_item_presence()

        with allure.step("3. Remove a random item"):
            await invent.cart_remove_random_item()

        with allure.step("4. Click on the checkout button"):
            await invent.cart_checkout_click()
            await invent.buy_info_page_section_presence()

        with allure.step("5. Fill in the displayed form"):
            await invent.buy_info_insert_first_name("QA")
            await invent.buy_info_insert_last_name("Test")
            await invent.buy_info_insert_postal_code("123")

        with allure.step("6. Click the 'Continue' button"):
            await invent.buy_info_continue()
            await invent.buy_preview_page_section_presence()

        # Todo : Validate the total result vs single item calculation
        with allure.step("7. Calculate the price before completing the checkout"):
            await invent.checkout_price_validator()

        with allure.step("8. Click the 'Finish' button"):
            await invent.buy_preview_click_finish()
            await invent.complete_page_section_presence()
