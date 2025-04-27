from entities.elements.base_element import BaseElement


class LinkElement(BaseElement):
    @property
    def type(self) -> str:
        return "Link"

    def __str__(self) -> str:
        return self.locator.text_content()
