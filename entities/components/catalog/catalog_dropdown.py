from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from playwright.sync_api import Page

from entities.components.base_component import BaseComponent
from entities.elements.link import LinkElement


class CatalogDropdownComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.personal_account_link = LinkElement(
            page.locator('a.head-bar__link[data-bs-toggle="dropdown"]').last,
            "Личный кабинет",
        )
        self.category_link = lambda category_name: LinkElement(
            page.locator("a.head-dropdown-catalog__category", has_text=category_name),
            category_name,
        )
        self.subcategory_link = lambda category_name: LinkElement(
            page.locator(
                "a.head-dropdown-catalog__subcat-list-item", has_text=category_name
            ),
            category_name,
        )
        self.subcategory_brand_link = lambda brand_name: LinkElement(
            page.locator(
                "#dropdown-subsubcat-2-2 .head-catalog-subcategories a",
                has_text=brand_name,
            ),
            brand_name,
        )
