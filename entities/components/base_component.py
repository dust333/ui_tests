from __future__ import annotations

from typing import TYPE_CHECKING

import allure

if TYPE_CHECKING:
    from playwright.sync_api import Page

from playwright.sync_api import expect

from utils.logger import LoggerClass


class BaseComponent:
    def __init__(self, page: Page):
        self.page = page
        self._logger = LoggerClass(self.__class__.__name__)

    def verify_url(self, expected_path: str) -> None:
        step = f"Checking that page have url {expected_path}"
        with allure.step(self):
            self._logger.info(step)
            expect(self.page).to_have_url(expected_path)
