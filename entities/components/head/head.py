from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from playwright.sync_api import Page

from entities.components.base_component import BaseComponent
from entities.components.head.main_bar import MainBarComponent
from entities.components.head.top_bar import TopBarComponent


class HeadComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.top_bar = TopBarComponent(page)
        self.main_bar = MainBarComponent(page)
