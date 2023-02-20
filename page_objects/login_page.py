from typing import Tuple

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.base_page import BasePage


class LoginPage(BasePage):
    __url = "https://practicetestautomation.com/practice-test-login/"
    __username_field = (By.XPATH, '//input[@id="username"]')
    __password_field = (By.XPATH, '//input[@id="password"]')
    __submit_btn = (By.XPATH, "//button[text()='Submit']")
    __title_login_page = (By.XPATH, '//section[@id="login"]//h2[text()="Test login"]')
    __txt_username_error_msg = (By.XPATH, f"//div[text()='Your username is invalid!']")
    __txt_password_error_msg = (By.XPATH, f"//div[text()='Your password is invalid!']")
    __txt_login_error_msg = (By.ID,'error')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def execute_login(self, username: str, password: str):
        # wait = WebDriverWait(self._driver, 10)
        # wait.until(EC.visibility_of_element_located(self.__username_field))
        # self._driver.find_element(self.__username_field).send_keys(username)

        # wait = WebDriverWait(self._driver, 10)
        # wait.until(EC.visibility_of_element_located(self.__password_field))
        # self._driver.find_element(self.__password_field).send_keys(password)
        #
        # wait = WebDriverWait(self._driver, 10)
        # wait.until(EC.visibility_of_element_located(self.__submit_btn))
        # self._driver.find_element(self.__submit_btn).click()

        super()._type(self.__username_field, username)
        super()._type(self.__password_field, password)
        super()._click(self.__submit_btn)

    def verify_login_page_title(self):
        super()._wait_until_element_is_visible(self.__title_login_page)
        return super()._is_displayed(self.__title_login_page)

    def verify_login_error_msg(self, expected_msg: str):
        actualtxtmsg = super()._get_text(self.__txt_login_error_msg)
        if actualtxtmsg == expected_msg:
            return True
        return False

    def is_login_error_msg_displayed(self):
        super()._wait_until_element_is_visible(self.__txt_login_error_msg)
        return super()._is_displayed(self.__txt_login_error_msg)