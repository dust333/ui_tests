from playwright.sync_api import Page

from entities.components.catalog.item_card import ItemCardComponent
from entities.pages.base_page import BasePage


class CatalogPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, default_endpoint="/catalog/*/")
        self._items: None | list[ItemCardComponent] = None

    @property
    def items(self) -> list[ItemCardComponent]:
        if not self._items:
            self._logger.info("Getting ItemCardComponents")
            self.page.wait_for_selector(".item-card.rs-product-item")
            self._items = [
                ItemCardComponent(self.page, item.get_attribute("data-id"))
                for item in self.page.locator(".item-card.rs-product-item").all()
            ]
        return self._items

    def check_items_visible(self) -> None:
        for item in self.items:
            item.check_visible()
