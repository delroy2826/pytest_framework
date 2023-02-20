from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.base_page import BasePage


class LoggedInSuccessfullyPage(BasePage):
    __url = "https://practicetestautomation.com/logged-in-successfully/"
    __actual_success_msg_txt_area = (By.XPATH, "//h1[text()='Logged In Successfully']")
    __logout_btn = (By.XPATH, "//a[text()='Log out']")
    __header_locator = (By.CLASS_NAME, "post-title")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url(self) -> str:
        return self.__url

    @property
    def header(self) -> str:
        super()._wait_until_element_is_visible(self.__header_locator)
        return super()._get_text(self.__header_locator)

    def is_logout_button_displayed(self) -> bool:
        return super()._is_displayed(self.__logout_btn)

    def verify_welcome_msg(self, expected_msg: str):
        actualtxtmsg = super()._get_text(self.__actual_success_msg_txt_area)
        if actualtxtmsg == expected_msg:
            return True
        return False

    def logout(self):
        super()._click(self.__logout_btn)
