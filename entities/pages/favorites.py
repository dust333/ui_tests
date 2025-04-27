from playwright.sync_api import Page

from entities.components.cart.cart_popup import CartPopupComponent
from entities.components.catalog.item_card import ItemCardComponent
from entities.components.head.head import HeadComponent
from entities.components.head.login_form import LoginFormComponent
from entities.pages.base_page import BasePage


class FavoritePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, default_endpoint="/favorite/")
        self.head = HeadComponent(page)
        self.login_form = LoginFormComponent(page)
        self.cart_popup = CartPopupComponent(page)
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
