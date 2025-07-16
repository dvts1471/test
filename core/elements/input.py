from core.elements import BaseElement


class Input(BaseElement):
    def fill(self, text):
        self.logger.debug(f'Fill {self.__class__.__name__}({self.locator}) "{text}"')
        self.element.send_keys(text)

    def clear(self):
        self.logger.debug(f"Clear {self.__class__.__name__}({self.locator})")
        self.element.clear()
