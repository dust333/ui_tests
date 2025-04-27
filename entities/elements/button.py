from playwright.sync_api import expect

from entities.elements.base_element import BaseElement


class ButtonElement(BaseElement):
    @property
    def type(self) -> str:
        return "Button"

    def check_enabled(self, **kwargs) -> None:
        expect(self.locator).to_be_enabled(**kwargs)

    def check_disabled(self, **kwargs) -> None:
        expect(self.locator).to_be_disabled(**kwargs)
