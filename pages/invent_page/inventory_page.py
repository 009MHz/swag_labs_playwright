import time

from pages.__base import BasePage
from elements.__inventory import *
from playwright.async_api import Page, expect
import random as rand


class InventPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    """Inventory Header Validation"""
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

    """Item Purchase Interaction"""
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
            print(f"{i + 1}. Picking item {index}")
            indices.remove(index)
            await self._item_pick(Products.add_btn, index)
            print(f"Item {index} selected")