from abc import ABC
from constants import URL
from utils.driver_manager import DriverManager
from utils.logger import Logger


class BasePage(ABC):
    url = URL

    def __init__(self):
        self.logger = Logger(self.__class__.__name__)

    @property
    def driver(self):
        return DriverManager().driver

    def open(self):
        self.logger.info(f"Open {self.__class__.__name__}")
        self.driver.get(url=self.url)
        return self

    def is_loaded(self, timeout=5):
        raise NotImplemented
