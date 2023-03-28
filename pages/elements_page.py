from locators.elements_locators import CheckBoxLocators

from pages.base_page import BasePage


class CheckBoxPage(BasePage):
    """CheckBoxPage."""

    locators = CheckBoxLocators()

    def click_check_box(self):
        """Click_check_box."""
        self.element_is_visible(self.locators.BUTTON_ELEMENTS).click()
        self.element_is_visible(self.locators.BUTTON_CHECK_BOX).click()
        self.element_is_visible(self.locators.CHECK_BOX_HOME).click()
        self.element_is_visible(self.locators.CHECK_BOX_DOWNLOADS).click()
        self.element_is_visible(self.locators.CHECK_BOX_WORD).click()

    def check_text(self) -> tuple:
        """Check_text."""
        default_text = self.element_is_visible(self.locators.DEFAULT_TEXT).text
        text_selected = self.element_is_visible(self.locators.TEXT_SELECTED).text
        return default_text, text_selected
