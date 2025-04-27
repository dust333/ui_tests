from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from playwright.sync_api import Page

from entities.components.base_component import BaseComponent
from entities.elements.button import ButtonElement
from entities.elements.input import InputElement


class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.login_input = InputElement(
            page.get_by_role("textbox", name="Логин или E-mail"),
            "Логин",
        )
        self.password_input = InputElement(
            page.locator('input[type="password"]'), "Пароль"
        )
        self.login_button = ButtonElement(
            page.locator("button.btn.btn-primary", has_text="Войти"), "Войти"
        )
