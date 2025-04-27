from playwright.sync_api import Page

from entities.components.cart.cart_item import CartItemComponent
from entities.elements.text import TextElement
from entities.pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, default_endpoint="/checkout/")
        self.empty_cart_text = TextElement(
            page.locator("div.text-center h2", has_text="Корзина пуста"),
            "Корзина пуста",
        )
        self._items: None | list[CartItemComponent] = None

    @property
    def items(self) -> list[CartItemComponent]:
        if not self._items:
            self._logger.info("Getting CartItemComponents")
            self.page.wait_for_selector(".cart-checkout-item.rs-cart-item")
            self._items = [
                CartItemComponent(self.page, item.get_attribute("data-id"))
                for item in self.page.locator(".cart-checkout-item[data-id]").all()
            ]
        return self._items
