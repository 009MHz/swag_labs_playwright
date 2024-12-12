from pages.__base import BasePage
from elements.__inventory import *
from playwright.async_api import Page, expect
import random as rand


class InventPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    # Page Interaction
    """Item Purchase"""
    async def _item_pick(self, locator, index):
        add_chart_locator = f"({locator})[{index}]"
        await self._click(add_chart_locator)

    async def click_ordered_add_to_chart(self, attempt: int):
        for i in range(1, attempt + 1):
            await self._item_pick(Products.add_btn, i)
            print(f"Clicking index{i}")

    async def click_random_add_to_chart(self, attempt: int):
        total_items = await self._find(Products.container).count()
        indices = list(range(1, total_items))

        for i in range(min(attempt, total_items)):
            index = rand.choice(indices)
            indices.remove(index)
            await self._item_pick(Products.add_btn, index)

    async def click_chart_icon(self):
        await self._click(Header.item_cart)
        await expect(self.page).to_have_url(YourCart.url)

    """Your Cart"""
    async def cart_remove_random_item(self):
        collected_items = await self._find(YourCart.item_remove).count()
        choice = rand.randint(1, collected_items)
        remove_locators = f"({YourCart.item_remove})[{choice}]"
        await self._click(remove_locators)
        assert await self._find(YourCart.item_remove).count() < collected_items, "The Item is not removed"

    async def cart_checkout_click(self):
        await self._click(YourCart.checkout_btn)
        await expect(self.page).to_have_url(BuyInfo.url)

    """Checkout Info"""
    async def buy_info_insert_first_name(self, first_name: str):
        await expect(self._find(BuyInfo.first_name)).to_be_empty()
        await expect(self._find(BuyInfo.first_name)).to_have_attribute("placeholder", "First Name")
        await self._type(BuyInfo.first_name, first_name)
        await expect(self._find(BuyInfo.first_name)).not_to_be_empty()

    async def buy_info_insert_last_name(self, last_name: str):
        await expect(self._find(BuyInfo.last_name)).to_be_empty()
        await expect(self._find(BuyInfo.last_name)).to_have_attribute("placeholder", "Last Name")
        await self._type(BuyInfo.last_name, last_name)
        await expect(self._find(BuyInfo.last_name)).not_to_be_empty()

    async def buy_info_insert_postal_code(self, postal_code: str):
        await expect(self._find(BuyInfo.postal)).to_be_empty()
        await expect(self._find(BuyInfo.postal)).to_have_attribute("placeholder", "Zip/Postal Code")
        await self._type(BuyInfo.postal, postal_code)
        await expect(self._find(BuyInfo.postal)).not_to_be_empty()

    async def buy_info_continue(self):
        await self._click(BuyInfo.continue_btn)
        await expect(self.page).to_have_url(BuyPreview.url)

    """Checkout Overview"""
    async def buy_preview_click_finish(self):
        await self._click(BuyPreview.finish_btn)
        await expect(self.page).to_have_url(BuyComplete.url)

    # Page Validation
    """Inventory Header"""
    async def cart_empty_presence(self):
        await self._look(Header.item_cart)
        await expect(self._find(Header.item_chart_count)).not_to_be_visible()

    async def cart_item_added_presence(self):
        await self._look(Header.item_cart)
        await expect(self._find(Header.item_chart_count)).to_be_visible()

    async def cart_item_counter(self, attempt: int):
        await self._look(Header.item_chart_count)
        counter = await self._find(Header.item_chart_count).text_content()
        assert counter == str(attempt), "Item counter doesn't match"

    """Your Cart"""
    async def cart_page_section_presence(self):
        await self._look(YourCart.section_title)
        await expect(self._find(YourCart.section_title)).to_have_text("Your Cart")

    async def cart_item_presence(self):
        collected_items = await self._find(YourCart.item_holder).count()

        for index in range(1, collected_items + 1):
            name_locators = f"({YourCart.item_name})[{index}]"
            info_locators = f"({YourCart.item_info})[{index}]"
            price_locators = f"({YourCart.item_price})[{index}]"
            remove_locators = f"({YourCart.item_remove})[{index}]"

            await self._look(name_locators)
            await expect(self._find(name_locators)).not_to_have_text("")

            await self._look(info_locators)
            await expect(self._find(info_locators)).not_to_have_text("")

            await self._look(price_locators)
            await expect(self._find(price_locators)).to_contain_text("$")

            await self._touch(remove_locators)
            await expect(self._find(remove_locators)).to_have_text("Remove")

    """Checkout Info"""
    async def buy_info_page_section_presence(self):
        await self._look(BuyInfo.section_title)
        await expect(self._find(BuyInfo.section_title)).to_have_text("Checkout: Your Information")

        await expect(self._find(BuyInfo.main_form)).to_be_visible()

        await expect(self._find(BuyInfo.cancel_btn)).to_be_enabled()
        await expect(self._find(BuyInfo.cancel_btn)).to_have_text("Cancel")

        await expect(self._find(BuyInfo.continue_btn)).to_be_enabled()
        await expect(self._find(BuyInfo.continue_btn)).to_have_text("Continue")

    """Checkout Overview"""
    async def buy_preview_page_section_presence(self):
        await self._look(BuyPreview.section_title)
        await expect(self._find(BuyPreview.section_title)).to_have_text("Checkout: Overview")

        await expect(self._find(BuyPreview.summary_info)).to_be_visible()

        await expect(self._find(BuyPreview.cancel_btn)).to_be_enabled()
        await expect(self._find(BuyPreview.cancel_btn)).to_have_text("Cancel")

        await expect(self._find(BuyPreview.finish_btn)).to_be_enabled()
        await expect(self._find(BuyPreview.finish_btn)).to_have_text("Finish")

    # Todo 1: Item calculator before checkout
    async def single_checkout_calculation(self):
        total_price = 0.0
        total_goods = await self._find(YourCart.item_price).count()
        for item_order in range(1, total_goods+1):
            mod_locators = f"({YourCart.item_price})[{item_order}]"

            # Todo 1a: Retrieve Price Text from the carousel
            current_price = await self._find(mod_locators).text_content()
            print(f"Collected raw price: {current_price}")

            # Todo 1b: Trim the text and collect the number only
            formatted_price = current_price.split('$')[-1].strip()
            print(f"Formatted price: {formatted_price}")

            # Todo 1c: Add the number into current calculation
            total_price += float(formatted_price)

        # Todo 1e: Add the '$' sign and return the result
        print(f"Returned current calculation ${total_price:.2f}")
        return f"${total_price:.2f}"

    # Todo 2: Price total retriever
    async def all_item_total_retriever(self):
        # Todo 2a: Collect the Item total under Price Total section
        raw_price = await self._find(BuyPreview.item_total).text_content()
        print(f"Retrieved value: \n'{raw_price}'")

        # Todo 2b: Trim the content
        formatted_price = raw_price.split(':')[-1].strip()
        print(f"Collected value: {formatted_price}")

        # Todo 2c: Collect the result with same format with previous returned data type
        return formatted_price

    # Todo 3: Total price vs item calculator verification
    async def checkout_price_validator(self):
        # Todo 3a: Collect the result from 2f
        single_item_calculation = await self.single_checkout_calculation()

        # Todo 3b: Compare the result with 3c
        total_price = await self.all_item_total_retriever()

        # Todo 3c: Create the assertion for the price should be matched
        print(f"Single item: {single_item_calculation}\nTotal Price: {total_price}")
        assert total_price == single_item_calculation, f"The single item price calculation doesn't match with the total price"

    """Checkout Complete"""
    async def complete_page_section_presence(self):
        await self._look(BuyComplete.section_title)
        await expect(self._find(BuyComplete.section_title)).to_have_text("Checkout: Complete!")

        await expect(self._find(BuyComplete.main_display)).to_be_visible()
        await expect(self._find(BuyComplete.header)).to_have_text("Thank you for your order!")
        await expect(self._find(BuyComplete.info)).to_contain_text("as fast as the pony")

        await expect(self._find(BuyComplete.back_home_btn)).to_be_enabled()
        await expect(self._find(BuyComplete.back_home_btn)).to_have_text("Back Home")
