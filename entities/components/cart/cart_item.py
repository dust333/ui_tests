from __future__ import annotations

from typing import TYPE_CHECKING

from entities.components.base_item_component import BaseItemComponent
from entities.elements.button import ButtonElement
from entities.elements.text import TextElement

if TYPE_CHECKING:
    from playwright.sync_api import Page


class CartItemComponent(BaseItemComponent):
    """Класс описывает товар со страницы корзины"""

    def __init__(self, page: Page, data_id: str):
        super().__init__(page)
        self.price_text = TextElement(
            page.locator(
                f'[data-id="{data_id}"] .cart-checkout-item__bar span.fw-bold'
            ),
            "Цена",
        )
        self.delete_from_cart_button = ButtonElement(
            page.locator(f'[data-id="{data_id}"] .cart-checkout-item__del.rs-remove'),
            "Удалить из корзины",
        )
        self.name_text = TextElement(
            page.locator(f'[data-id="{data_id}"] .cart-checkout-item__title'),
            "Название позиции",
        )

    def check_visible(self) -> None:
        self._logger.info("Checking visibility of all elements")
        self.price_text.check_visible()
        self.name_text.check_visible()
        self.delete_from_cart_button.check_visible()
