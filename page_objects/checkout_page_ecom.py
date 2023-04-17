from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage


class CheckoutPageEcommerce(BasePage):

    _txt_prod_name = (By.XPATH, "//div[@class='media-body']//a[text()='{0}']")
    _btn_checkout = (By.XPATH, "//button[contains(text(),'Checkout')]")
    _txt_field_country = (By.XPATH, '//input[@id="country"]')
    _lnk_country_txt = (By.XPATH, '//div[@class="suggestions"]//a[text()="{0}"]')
    _chk_bx_terms_and_condition = (By.XPATH, "//label[@for='checkbox2' and contains(text(),'I agree with the')]")
    _btn_purchase = (By.XPATH, '//input[@value="Purchase"]')
    _txt_success_alert = (By.XPATH, "//strong[text()='Success!']//parent::div[contains(@class,'alert-success ')]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def verify_product_displayed(self, prod_name):
        assert super()._is_displayed(super()._positional_arg_locator(self._txt_prod_name, prod_name)) is True, \
            f"{prod_name} Product not found in checkout page"

    def click_on_checkout_btn(self):
        super()._click(self._btn_checkout)

    def select_delivery_location(self, delivery_loc):
        super()._type(self._txt_field_country, delivery_loc)
        super()._click(super()._positional_arg_locator(self._lnk_country_txt, delivery_loc))

    def select_terms_and_condition(self):
        super()._clickJS(self._chk_bx_terms_and_condition)

    def purchase_and_verify_success_msg(self):
        super()._click(self._btn_purchase)
        assert super()._is_displayed(self._txt_success_alert) is True, "Order Placed success message not displayed"
