from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from utils.driver_manager import DriverManager

from selenium.webdriver.support import expected_conditions as EC

from utils.logger import Logger


class BaseElement:
    logger = Logger(__name__)

    def __init__(self, locator):
        self.locator = locator

    def get_text(self):
        return self.element.text

    @property
    def driver(self):
        return DriverManager().driver

    @property
    def element(self):
        return self.wait_element()

    def wait_element(self, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, self.locator))
        )

    def is_loaded(self, timeout=5):
        try:
            self.wait_element(timeout=timeout)
            return True
        except:
            return False

    def click(self):
        self.logger.debug(f"Click on {self.__class__.__name__}({self.locator})")
        self.wait_element().click()