from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from playwright.sync_api import Page
    from entities.elements.text import TextElement

from entities.components.base_component import BaseComponent


class BaseItemComponent(BaseComponent):
    """Класс описывает сущность товара(в корзине, каталоге или меню избранного)"""

    def __init__(self, page: Page):
        super().__init__(page)
        self.price_text: TextElement | None = None
        self.name_text: TextElement | None = None

    def __eq__(self, other) -> bool:
        if isinstance(other, BaseItemComponent):
            return (
                self.name == other.name
                and self.price.removesuffix("р.").strip()
                == other.price.removesuffix("р.").strip()
            )
        raise TypeError

    @property
    def price(self) -> str:
        return str(self.price_text)

    @property
    def name(self) -> str:
        return str(self.name_text)
