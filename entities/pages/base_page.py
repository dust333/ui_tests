import allure
from playwright.sync_api import Page, expect

from utils.logger import LoggerClass


class BasePage:
    def __init__(self, page: Page, default_endpoint: str) -> None:
        self.page = page
        self.default_endpoint = default_endpoint
        self._logger = LoggerClass(self.__class__.__name__)

    def open(self, endpoint: str = "") -> None:
        self.page.goto(endpoint or self.default_endpoint, wait_until="networkidle")

    def verify_url(self, expected_path: str) -> None:
        step = f"Checking that page have url {expected_path}"
        with allure.step(self):
            self._logger.info(step)
            expect(self.page).to_have_url(expected_path)
