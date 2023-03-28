from pages.elements_page import CheckBoxPage

import pytest

from pytest_lazyfixture import lazy_fixture

from selenium import webdriver


@pytest.mark.parametrize(
    'driver',
    [
        lazy_fixture('chrome_driver'),
        lazy_fixture('firefox_driver'),
    ],
)
class TestElements:
    """Сюьт - elements test."""

    def test_check_box(self, driver: webdriver):
        """Тест - check_box."""
        check_box_page = CheckBoxPage(driver, 'https://demoqa.com/')
        check_box_page.open()
        check_box_page.click_check_box()
        default_text, text_selected = check_box_page.check_text()
        assert default_text == 'You have selected :'
        assert text_selected == 'wordFile'
