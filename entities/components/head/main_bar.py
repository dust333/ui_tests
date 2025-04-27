from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from playwright.sync_api import Page

from entities.components.base_component import BaseComponent
from entities.components.catalog.catalog_dropdown import \
    CatalogDropdownComponent
from entities.elements.button import ButtonElement


class MainBarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.catalog_button = ButtonElement(
            page.locator("span.ms-2.d-none", has_text="Каталог"),
            "Каталог",
        )
        self.catalog_dropdown = CatalogDropdownComponent(page)
