from entities.elements.base_element import BaseElement


class InputElement(BaseElement):
    @property
    def type(self) -> str:
        return "Input"

    def clear(self, **kwargs) -> None:
        self.locator.clear(**kwargs)

    def fill(self, value: str, **kwargs) -> None:
        self.locator.fill(value, **kwargs)
