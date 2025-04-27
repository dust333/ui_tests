from entities.elements.base_element import BaseElement


class TextElement(BaseElement):
    @property
    def type(self) -> str:
        return "Text"

    def __str__(self) -> str:
        self._logger.info(f"Getting text_content for {self.type} {self.name}")
        return self.locator.text_content()

    def __eq__(self, other) -> bool:
        if isinstance(other, TextElement):
            return str(self) == str(other)
        else:
            raise TypeError
