from __future__ import annotations

from typing import TYPE_CHECKING

from entities.components.base_component import BaseComponent
from entities.components.cart.cart_popup_item import CartPopupItemComponent

if TYPE_CHECKING:
    from playwright.sync_api import Page


class CartPopupComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self._items: None | CartPopupItemComponent = None

    @property
    def items(self) -> list[CartPopupItemComponent]:
        if not self._items:
            self._logger.info("Getting CartPopupItems")
            self.page.wait_for_selector(".modal-cart-item.rs-cart-item")
            self._items = [
                CartPopupItemComponent(self.page, cart_item.get_attribute("data-id"))
                for cart_item in self.page.locator(
                    ".modal-cart-item.rs-cart-item"
                ).all()
            ]
        return self._items
