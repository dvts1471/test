import threading

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class DriverManager:
    _thread_local = threading.local()


    @property
    def driver(self):
        if not self.__get_driver():
            self.__create_driver()
        return self.__get_driver()

    @classmethod
    def __create_driver(cls):
        driver_path = ChromeDriverManager().install()
        service = webdriver.ChromeService(driver_path)
        cls._thread_local._driver = webdriver.Chrome(service=service)

    @classmethod
    def __get_driver(cls):
        return getattr(cls._thread_local, '_driver', None)

    @classmethod
    def is_driver_initiated(cls):
        return True if cls.__get_driver() else False

    @classmethod
    def close_driver(cls):
        if cls.__get_driver():
            cls.__get_driver().close()
            cls._thread_local._driver = None

