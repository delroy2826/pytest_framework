import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage


class ShopPageEcommerce(BasePage):
    _lnk_checkout = (By.XPATH, "//a[contains(text(),'Checkout')]")
    _btn_product_add = (By.XPATH, '//a[text()="{0}"]//ancestor::div[contains(@class,"card")]//div['
                                  '@class="card-footer"]//button')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def url_validation(self, expected_url: str):
        time.sleep(5)
        actual_url = super().current_url
        assert expected_url == actual_url, f"Actual URL {actual_url} is not same as Expected URL {expected_url}"

    def validate_checkout_link(self):
        assert super()._is_displayed(self._lnk_checkout) is True, "Checkout link is not displayed"

    def add_product_to_cart(self, prod_list):
        for prod_name in prod_list:
            super()._click(super()._positional_arg_locator(self._btn_product_add, prod_name))

    def navigate_to_checkout_page(self):
        super()._click(self._lnk_checkout)
