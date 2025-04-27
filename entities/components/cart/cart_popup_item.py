from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from playwright.sync_api import Page

from entities.components.base_item_component import BaseItemComponent
from entities.elements.button import ButtonElement
from entities.elements.text import TextElement


class CartPopupItemComponent(BaseItemComponent):
    """Класс описывает товар из Popup корзины"""

    def __init__(self, page: Page, data_id: str):
        super().__init__(page)
        self.price_text = TextElement(
            page.locator(f'[data-id="{data_id}"] .modal-cart-item__price'), "Цена"
        )
        self.delete_from_cart_button = ButtonElement(
            page.locator(f'[data-id="{data_id}"] .modal-cart-item__delete'),
            "Добавить в корзину",
        )
        self.name_text = TextElement(
            page.locator(f'[data-id="{data_id}"] .modal-cart-item__title'),
            "Название позиции",
        )

    def check_visible(self) -> None:
        self._logger.info("Checking visibility of all elements")
        self.price_text.check_visible()
        self.name_text.check_visible()
        self.delete_from_cart_button.check_visible()
