import pytest

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ServiceChrome
from selenium.webdriver.firefox.service import Service as ServiceFF

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def chrome_driver() -> selenium.webdriver:
    """Фикстура chrome-driver."""
    driver_service = ServiceChrome(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def firefox_driver() -> selenium.webdriver:
    """Фикстура firefox-driver."""
    driver_service = ServiceFF(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=driver_service)
    driver.maximize_window()
    yield driver
    driver.quit()
