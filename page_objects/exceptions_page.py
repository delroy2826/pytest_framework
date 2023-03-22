from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.db_base_page import DButils
from page_objects.base_page import BasePage


class ExceptionPage(BasePage, DButils):
    __url = "https://practicetestautomation.com/practice-test-exceptions/"
    __add_btn = (By.XPATH, "//button[text()='Add']")
    __save_btn_row2 = (By.XPATH, "//div[@id='row2']//button[text()='Save']")
    __save_btn_row1 = (By.XPATH, "//div[@id='row1']//button[text()='Save']")
    __edit_btn_row1 = (By.XPATH, "//div[@id='row1']//button[text()='Edit']")
    __row2_input_field = (By.XPATH, "//label[text()='Row 2']//following-sibling::input")
    __row2_saved_succ_msg = (By.XPATH, "//div[text()='Row 2 was saved']")
    __row1_input_field = (By.XPATH, "//label[text()='Row 1']//following-sibling::input")
    __row1_saved_succ_msg = (By.XPATH, "//div[text()='Row 1 was saved']")
    __txt_instruction_msg = (By.XPATH, "//p[@id='instructions']")

    def __init__(self, driver: WebDriver, db_name: str = None):
        super().__init__(driver)
        self.db = DButils(database=db_name)

    def open(self):
        super()._open_url(self.__url)

    def click_on_add_btn(self):
        super()._click(self.__add_btn)

    def click_on_save_btn_row2(self):
        super()._click(self.__save_btn_row2)

    def click_on_save_btn_row1(self):
        super()._click(self.__save_btn_row1)

    def click_on_edit_btn_row1(self):
        super()._click(self.__edit_btn_row1)

    def is_row2_field_displayed(self, time: int = 10) -> bool:
        super()._wait_until_element_is_visible(self.__row2_input_field, time)
        return super()._is_displayed(self.__row2_input_field)

    def add_text_row2(self, text: str):
        super()._type(self.__row2_input_field, text)

    def add_text_row1(self, text: str):
        super()._type(self.__row1_input_field, text)

    def is_row2_saved_succ_msg_displayed(self) -> bool:
        super()._wait_until_element_is_visible(self.__row2_saved_succ_msg)
        return super()._is_displayed(self.__row2_saved_succ_msg)

    def verify_row2_succ_msg(self, expectedtext: str) -> bool:
        actualtxtmsg = super()._get_text(self.__row2_saved_succ_msg)
        if actualtxtmsg == expectedtext:
            return True
        return False

    def is_row1_saved_succ_msg_displayed(self) -> bool:
        super()._wait_until_element_is_visible(self.__row1_saved_succ_msg)
        return super()._is_displayed(self.__row1_saved_succ_msg)

    def verify_row1_succ_msg(self, expectedtext: str) -> bool:
        actualtxtmsg = super()._get_text(self.__row1_saved_succ_msg)
        if actualtxtmsg == expectedtext:
            return True
        return False

    def clear_row1_field(self):
        super()._clear(self.__row1_input_field)

    def is_instruction_msg_displayed(self) -> bool:
        super()._wait_until_element_is_visible(self.__txt_instruction_msg)
        return super()._is_displayed(self.__txt_instruction_msg)

    def verify_instruction_txt_msg(self, expectedtext: str) -> bool:
        actualtxtmsg = super()._get_text(self.__txt_instruction_msg)
        if actualtxtmsg == expectedtext:
            return True
        return False
