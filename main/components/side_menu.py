from core.components import BaseComponent
from core.elements.button import Button
from core.elements.input import Input


class SideMenu(BaseComponent):
    locator = '//*[@aria-label="Sidepanel"]'
    search_input = Input(f'{locator}//*[contains(@placeholder, "Search")]')
    dashboard_item = Button(f'{locator}//*[contains(@placeholder, "Dashboard")]')

    def __init__(self):
        super().__init__(self.locator)
