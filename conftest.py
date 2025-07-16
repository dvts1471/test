import pytest

from utils.driver_manager import DriverManager


@pytest.fixture(autouse=True, scope="function")
def teardown():
    yield
    if DriverManager.is_driver_initiated():
        DriverManager.close_driver()