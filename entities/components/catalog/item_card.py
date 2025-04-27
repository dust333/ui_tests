from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from playwright.sync_api import Page

from entities.components.base_item_component import BaseItemComponent
from entities.elements.button import ButtonElement
from entities.elements.text import TextElement


class ItemCardComponent(BaseItemComponent):
    """Класс описывает товар со страниц каталога или со страницы избранного"""

    def __init__(self, page: Page, data_id: str):
        super().__init__(page)
        self.price_text = TextElement(
            page.locator(
                f'[data-id="{data_id}"] .item-product-price__new-price .rs-price-new'
            ),
            "Цена",
        )
        self.add_to_cart_button = ButtonElement(
            page.locator(f'[data-id="{data_id}"] .item-product-cart-action button'),
            "Добавить в корзину",
        )
        self.add_to_favorite_button = ButtonElement(
            page.locator(f'[data-id="{data_id}"] .fav.rs-favorite'),
            "Добавить в избранное",
        )
        self.name_text = TextElement(
            page.locator(f'[data-id="{data_id}"] .item-card__title'), "Название позиции"
        )

    def check_visible(
        self,
    ) -> None:
        self._logger.info("Checking visibility of all elements")
        self.price_text.check_visible()
        self.name_text.check_visible()
        self.add_to_cart_button.check_visible()
        self.add_to_favorite_button.check_visible()
