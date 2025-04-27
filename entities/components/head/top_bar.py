from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from playwright.sync_api import Page

from entities.components.base_component import BaseComponent
from entities.components.head.auth_dropdown import AuthDropDownComponent
from entities.elements.link import LinkElement


class TopBarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.personal_account_link = LinkElement(
            page.locator('a.head-bar__link[data-bs-toggle="dropdown"]').last,
            "Личный кабинет",
        )
        self.auth_dropdown_component = AuthDropDownComponent(page)
