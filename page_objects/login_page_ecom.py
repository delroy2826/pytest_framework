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
    _lnk_blinking_text = (By.XPATH, '//a[@class="blinkingText"]')
    _txt_header_page_title = (By.XPATH, "//section[@class='page-title']//h1")
    _btn_dialog_login_page = (By.XPATH, '//div[contains(@class,"modal-confirm")]//button[@id="okayBtn"]')
    _input_username_or_pw = (By.XPATH, '//input[@name="{0}"]')

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

    def verify_drop_down_values(self, expected_options: list):
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

    def enter_login_details(self, username: str, password: str, round_btn: str = None,
                            drp_down: str = None, submit: bool = False) -> None:
        super()._type(self._txt_username, username)
        super()._type(self._txt_password, password)

        if round_btn == "User":
            super()._clickJS(self._radio_lbl_user)
            super()._click(self._btn_dialog_login_page)

        if round_btn == "Admin":
            super()._clickJS(self._radio_lbl_admin)

        if drp_down:
            super()._drp_dwn_slt_by_value(self._drp_down_options, drp_down)

        if submit:
            super()._click(self._btn_sign_in)

    def validate_login_error_msg_displayed(self):
        assert super()._is_displayed(self._lbl_alert_err_msg), "Login Error message not displayed"

    def click_on_blinking_text(self):
        super()._clickJS(self._lnk_blinking_text)

    def get_window_addresses(self) -> list:
        return super()._get_all_window_addresses()

    def change_window(self, window_address: str):
        super()._switch_to_window(window_address)

    def verify_new_tab_page_title(self, page_title: str):
        extracted_text = super()._get_text(self._txt_header_page_title)
        assert extracted_text == page_title, "Title is not same"

    def url_validation(self, expected_url: str):
        actual_url = super().current_url
        assert expected_url == actual_url, f"Actual URL {actual_url} is not same as Expected URL {expected_url}"

    def enterlogindetails(self, uname: str, pword: str):
        super()._type(super()._positional_arg_locator(self._input_username_or_pw, "username"), uname)
        super()._type(super()._positional_arg_locator(self._input_username_or_pw, "password"), pword)
        super()._click(self._btn_sign_in)
