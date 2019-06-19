from helpers.web_element import Fixture
import pytest


@pytest.fixture
def browser():
    # Setup driver
    driver = Fixture()
    yield driver
    # Teardown driver
    driver.destroy()
