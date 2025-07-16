from constants import URL
from core.elements import BaseElement
from core.elements.button import Button
from core.elements.input import Input
from core.pages import BasePage


class LoginPage(BasePage):
    url = f"{URL}/auth/login"

    login_title = BaseElement('//h5[contains(., "Login")]')

    username_input = Input('//*[@name="username"]')
    username_validation_msg = BaseElement(f'//*[.{username_input.locator}]/span')

    password_input = Input('//*[@name="password"]')
    password_validation_msg = BaseElement(f'//*[.{password_input.locator}]/span')

    login_button = Button('//*[@type="submit"]')

    alert = BaseElement('//*[@role="alert"]')

    def login(self, username, password):
        self.logger.info(f'Login with username: "{username}" password: "{password}"')
        self.username_input.fill(username)
        self.password_input.fill(password)

        self.login_button.click()

    def is_loaded(self, timeout=5):
        return all([
            self.login_title.is_loaded(timeout=timeout)
        ])