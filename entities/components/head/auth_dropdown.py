from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from playwright.sync_api import Page

from entities.components.base_component import BaseComponent
from entities.elements.button import ButtonElement


class AuthDropDownComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.login_button = ButtonElement(
            page.locator("a.dropdown-item.rs-in-dialog", has_text="Вход"),
            "Вход",
        )
