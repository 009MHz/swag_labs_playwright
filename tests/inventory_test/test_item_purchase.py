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


@allure.epic("Inventory")
@allure.story("User should be able to interact with item list purchase")
@allure.feature("Purchase")
@pytest.mark.positive
@pytest.mark.smoke
class TestCheckoutItemMatch:
    @allure.feature("Inventory/ Purchase")
    @allure.title("The item chart should be equal to '2' when user adding 2 items")
    @allure.severity(severity.NORMAL)
    async def test_2_item_purchase(self, invent, attempt=2):
        with allure.step("1. Verify the item chart presence on default state"):
            await invent.cart_empty_presence()
        with allure.step("2. Click Add to cart button "):
            await invent.click_ordered_add_to_chart(attempt)
        with allure.step("3. Verify the chart state after item added"):
            await invent.cart_item_added_presence()
            await invent.cart_item_counter(attempt)

    @allure.feature("Inventory/ Purchase")
    @allure.title("The item chart should be equal to '3' when user adding 3 items")
    @allure.severity(severity.NORMAL)
    async def test_3_item_purchase(self, invent, attempt=3):
        with allure.step("1. Verify the item chart presence on default state"):
            await invent.cart_empty_presence()
        with allure.step("2. Click Add to cart button "):
            await invent.click_ordered_add_to_chart(attempt)
        with allure.step("3. Verify the chart state after item added"):
            await invent.cart_item_added_presence()
            await invent.cart_item_counter(attempt)

    @allure.feature("Inventory/ Purchase")
    @allure.title("The item chart should be equal to '4' when user adding 4 items")
    @allure.severity(severity.NORMAL)
    async def test_4_item_purchase(self, invent, attempt=4):
        with allure.step("1. Verify the item chart presence on default state"):
            await invent.cart_empty_presence()
        with allure.step("2. Click Add to cart button"):
            await invent.click_ordered_add_to_chart(attempt)
        with allure.step("3. Verify the chart state after item added"):
            await invent.cart_item_added_presence()
            await invent.cart_item_counter(attempt)