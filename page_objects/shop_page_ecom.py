import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage


class ShopPageEcommerce(BasePage):
    _lnk_checkout = (By.XPATH, "//a[contains(text(),'Checkout')]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def url_validation(self, expected_url: str):
        time.sleep(5)
        actual_url = super().current_url
        assert expected_url == actual_url, f"Actual URL {actual_url} is not same as Expected URL {expected_url}"

    def validate_checkout_link(self):
        assert super()._is_displayed(self._lnk_checkout) is True, "Checkout link is not displayed"
