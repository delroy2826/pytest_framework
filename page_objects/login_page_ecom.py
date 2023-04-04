from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage


class LoginPageEcommerce(BasePage):
    _lbl_username = (By.XPATH, '//label[@for="username"]')
    _lbl_password = (By.XPATH, '//label[@for="password"]')
    _radio_lbl_admin = (By.XPATH, "//span[@class='radiotextsty' and text()='Admin']")
    _radio_lbl_user = (By.XPATH, "//span[@class='radiotextsty' and text()=' User']")
    _drp_down_options = (By.XPATH, '//select[@class="form-control"]')
    _lbl_term_and_condition = (By.XPATH, '//span[@class="text-white termsText"]')
    _btn_sign_in = (By.XPATH, '//input[@id="signInBtn"]')
    _txt_username = (By.XPATH, '//input[@id="username"]')
    _txt_password = (By.XPATH, '//input[@id="password"]')
    _lbl_alert_err_msg = (By.XPATH, "//div[contains(@class,'alert') and contains(text(),"
                                    "' username/password.')]//strong[text()='Incorrect']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_ecom_url(self, url: str):
        super()._open_url(url)

    def verify_username_displayed(self):
        assert super()._is_displayed(self._lbl_username) is True, "Username Field not Displayed"

    def verify_password_displayed(self):
        assert super()._is_displayed(self._lbl_password) is True, "Password Field not Displayed"

    def verify_radio_admin_displayed(self):
        assert super()._is_displayed(self._radio_lbl_admin) is True, "Radio label Admin not Displayed"

    def verify_radio_user_displayed(self):
        assert super()._is_displayed(self._radio_lbl_user) is True, "Radio label User not Displayed"

    def verify_drop_down_values(self, expected_options):
        actual_option_list = super()._get_drp_dwn_opts(self._drp_down_options, True)
        for expected_value in expected_options:
            if expected_value in actual_option_list:
                continue
            else:
                assert False, f"Expected option {expected_value} not in actual options {actual_option_list}"

    def verify_trm_and_cond_displayed(self):
        assert super()._is_displayed(self._lbl_term_and_condition) is True, "Terms and Condition is not displayed"

    def verify_sign_in_btn_displayed(self):
        assert super()._is_displayed(self._btn_sign_in) is True, "Sign in button is mot displayed"

    def validate_login_form_content(self, expected_options: list) -> bool:
        self.verify_username_displayed()
        self.verify_password_displayed()
        self.verify_radio_admin_displayed()
        self.verify_radio_user_displayed()
        self.verify_drop_down_values(expected_options)
        self.verify_trm_and_cond_displayed()
        self.verify_sign_in_btn_displayed()
        return True

    def enter_login_details(self, username: str, password: str, submit: bool) -> None:
        super()._type(self._txt_username, username)
        super()._type(self._txt_password, password)
        if submit:
            super()._click(self._btn_sign_in)

    def validate_login_error_msg_displayed(self):
        assert super()._is_displayed(self._lbl_alert_err_msg), "Login Error message not displayed"
