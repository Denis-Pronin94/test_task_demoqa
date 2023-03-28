from selenium.webdriver.common.by import By


class CheckBoxLocators:
    """Локаторы для теста TestElements."""

    BUTTON_ELEMENTS = (By.XPATH, '//div[@class="card mt-4 top-card"][1]')
    BUTTON_CHECK_BOX = (By.XPATH, '//span[text()="Check Box"]')
    CHECK_BOX_HOME = (
        By.XPATH,
        '//span[text()="Home"]/../..//button[@class="rct-collapse rct-collapse-btn"]',
    )
    CHECK_BOX_DOWNLOADS = (
        By.XPATH,
        '//span[text()="Downloads"]/../..//button[@class="rct-collapse rct-collapse-btn"]',
    )
    CHECK_BOX_WORD = (By.XPATH, '//span[text()="Word File.doc"]')
    DEFAULT_TEXT = (By.XPATH, '//span[text()="You have selected :"]')
    TEXT_SELECTED = (By.XPATH, '//span[text()="wordFile"]')
