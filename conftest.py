
import pytest
from selenium import webdriver


@pytest.fixture
def setup_browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()