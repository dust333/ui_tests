from abc import ABC, abstractmethod

import allure
from playwright.sync_api import Locator, expect

from utils.logger import LoggerClass


class BaseElement(ABC):
    def __init__(self, locator: Locator, name: str):
        self.locator = locator
        self.name = name
        self._logger = LoggerClass(self.__class__.__name__)

    @property
    @abstractmethod
    def type(self) -> str:
        pass

    def click(self, **kwargs) -> None:
        step = f'Clicking {self.type} "{self.name}"'

        with allure.step(step):
            self._logger.info(step)
            self.locator.click(**kwargs)

    def check_visible(self, **kwargs) -> None:
        step = f'Checking visibility of {self.type} "{self.name}"'

        with allure.step(step):
            self._logger.info(step)
            expect(self.locator).to_be_visible(**kwargs)

    def check_have_text(self, text: str, **kwargs) -> None:
        step = f'Checking that {self.type} "{self.name}" has text "{text}"'

        with allure.step(step):
            self._logger.info(step)
            expect(self.locator).to_have_text(text, **kwargs)

    def hover(self, **kwargs) -> None:
        self.locator.hover(**kwargs)
