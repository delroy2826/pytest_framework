from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage
from page_objects.db_base_page import DButils


class LoginPage(BasePage, DButils):
    __url = "https://practicetestautomation.com/practice-test-login/"
    __username_field = (By.XPATH, '//input[@id="username"]')
    __password_field = (By.XPATH, '//input[@id="password"]')
    __submit_btn = (By.XPATH, "//button[text()='Submit']")
    __title_login_page = (By.XPATH, '//section[@id="login"]//h2[text()="Test login"]')
    __txt_username_error_msg = (By.XPATH, f"//div[text()='Your username is invalid!']")
    __txt_password_error_msg = (By.XPATH, f"//div[text()='Your password is invalid!']")
    __txt_login_error_msg = (By.ID, 'error')

    def __init__(self, driver: WebDriver, db_name: str = None):
        super().__init__(driver)
        self.db = DButils(database=db_name)

    def open(self):
        super()._open_url(self.__url)

    def execute_login(self, username: str, password: str):
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

    def display_query_results(self, query):
        print(self.db._display_query_result(query))

    def database_output_in_dictionary_format(self, query):
        print(self.db._db_select_data_output(query))

    def get_row_record_using_id(self, sqlquery, find_with_row_id):
        print(self.db._get_row_record_data(sqlquery, find_with_row_id))

    def verify_expected_data_in_row_record(self, sqlquery,   find_with_row_id, expected_data):
        print(self.db._verify_value_in_row_record(sqlquery, find_with_row_id, expected_data))

    def get_tables_from_database(self):
        print(self.db._display_tables_in_database())

    def get_tables_in_database_in_dictionary(self):
        print(self.db._get_tables_in_database())

    def display_columns_of_the_table(self, tb_name):
        print(self.db._display_columns_from_table(tb_name))

    def get_columns_of_the_table(self, tb_name):
        print(self.db._get_columns_name_from_table(tb_name))

    def insert_values_into_table(self, tb_name, lst_of_tupledata):
        self.db._insert_data_into_table(tb_name, lst_of_tupledata)
        print(self.db._display_all_table_data(tb_name))

    def delete_record_from_table_by_id(self, tb_name, condition):
        print(self.db._delete_record_from_table(tb_name, condition))
        print(self.db._display_all_table_data(tb_name))

    def delete_complete_records_from_the_database(self, tb_name):
        self.db._delete_complete_records_from_table(tb_name)

    def truncate_complete_records_from_the_database(self, tb_name):
        self.db._truncate_table_records(tb_name)

    def display_all_databases_server(self, tablefmt):
        print(self.db._display_database(tablefmt))

    def get_all_databases_server(self):
        print(self.db._get_database())

    def change_database(self, db_name):
        self.db._use_database(db_name)
        print(self.db._get_tables_in_database())

    def create_database_and_drop(self, tb_name, tb_columns_structure):
        self.db._create_table_in_database(tb_name, tb_columns_structure)
        print(self.db._display_columns_from_table(tb_name))
        print(self.db._get_tables_in_database())
        self.db._drop_table_from_database(tb_name)
        print(self.db._get_tables_in_database())
