# Open Browser
import pytest
from page_objects.logged_in_successfully import LoggedInSuccessfullyPage
from page_objects.login_page import LoginPage


class TestPositiveScenario:

    @pytest.mark.All
    @pytest.mark.login
    @pytest.mark.positive
    @pytest.mark.parametrize(("username", "password", "expected_msg"),
                             [("student", "Password123", "Logged In Successfully")])
    def test_positive_login(self, driver, username, password, expected_msg):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login(username, password)

        logged_in = LoggedInSuccessfullyPage(driver)
        assert logged_in.expected_url == logged_in.current_url, "Actual URL is not same as Expected URL"

        assert logged_in.header == expected_msg, "Header is not as expected"
        assert logged_in.is_logout_button_displayed(), "Log out button should be visible"
        logged_in.logout()
        assert login_page.verify_login_page_title(), "Should be navigated to login page"

    # @pytest.mark.All
    # @pytest.mark.db_test
    # @pytest.mark.parametrize(('db_name', 'query'), [('automobile', "SELECT * FROM owner;")])
    # def test_db_1(self, driver, db_name, query):
    #     login_page = LoginPage(driver, db_name=db_name)
    #     login_page.display_query_results(query)
    #
    # @pytest.mark.All
    # @pytest.mark.db_test
    # @pytest.mark.parametrize(('db_name', 'query'), [('automobile', "SELECT * FROM owner;")])
    # def test_db_2(self, driver, db_name, query):
    #     login_page = LoginPage(driver, db_name=db_name)
    #     login_page.database_output_in_dictionary_format(query)
    #
    # @pytest.mark.All
    # @pytest.mark.db_test
    # @pytest.mark.parametrize(('db_name', 'query', 'find_row_id'), [('automobile', "SELECT * FROM owner;", "Ow03")])
    # def test_db_3(self, driver, db_name, query, find_row_id):
    #     login_page = LoginPage(driver, db_name=db_name)
    #     login_page.get_row_record_using_id(query, find_row_id)
    #
    # @pytest.mark.All
    # @pytest.mark.db_test
    # @pytest.mark.parametrize(('db_name', 'query', 'find_row_id', 'expected_data'),
    #                          [('automobile', "SELECT * FROM owner;", "Ow03", "Paulo Galdames")])
    # def test_db_4(self, driver, db_name, query, find_row_id, expected_data):
    #     login_page = LoginPage(driver, db_name=db_name)
    #     login_page.verify_expected_data_in_row_record(query, find_row_id, expected_data)
    #
    # @pytest.mark.All
    # @pytest.mark.db_test
    # @pytest.mark.parametrize('db_name', ['automobile'])
    # def test_db_5(self, driver, db_name):
    #     login_page = LoginPage(driver, db_name=db_name)
    #     login_page.get_tables_from_database()
    #
    # @pytest.mark.All
    # @pytest.mark.db_test
    # @pytest.mark.parametrize('db_name', ['automobile'])
    # def test_db_6(self, driver, db_name):
    #     login_page = LoginPage(driver, db_name=db_name)
    #     login_page.get_tables_in_database_in_dictionary()
    #
    # @pytest.mark.All
    # @pytest.mark.db_test
    # @pytest.mark.parametrize(('db_name', 'table_name'), [('automobile', 'owner')])
    # def test_db_7(self, driver, db_name, table_name):
    #     login_page = LoginPage(driver, db_name=db_name)
    #     login_page.display_columns_of_the_table(table_name)
    #
    # @pytest.mark.All
    # @pytest.mark.db_test
    # @pytest.mark.parametrize(('db_name', 'table_name'), [('automobile', 'owner')])
    # def test_db_8(self, driver, db_name, table_name):
    #     login_page = LoginPage(driver, db_name=db_name)
    #     login_page.get_columns_of_the_table(table_name)
    #
    # @pytest.mark.All
    # @pytest.mark.db_test
    # @pytest.mark.parametrize(('db_name', 'table_name', "list_of_tup_data"),
    #                          [('automobile', 'owner', [('Ow06', "Delroy", "160, JJ")])])
    # def test_db_9(self, driver, db_name, table_name, list_of_tup_data):
    #     login_page = LoginPage(driver, db_name=db_name)
    #     login_page.insert_values_into_table(table_name, list_of_tup_data)
    #
    # @pytest.mark.All
    # @pytest.mark.db_test
    # @pytest.mark.parametrize(('db_name', 'table_name', "list_of_tup_data"),
    #                          [('automobile', 'owner',
    #                            [('Ow07', "Jack", "170, Warsaw"), ('Ow08', "Alen", "180, Wroclaw")])])
    # def test_db_10(self, driver, db_name, table_name, list_of_tup_data):
    #     login_page = LoginPage(driver, db_name=db_name)
    #     login_page.insert_values_into_table(table_name, list_of_tup_data)
    #
    # @pytest.mark.All
    # @pytest.mark.db_test
    # @pytest.mark.parametrize(('db_name', 'table_name', "where_condition"),
    #                          [('automobile', 'owner', 'ownerID="Ow08"')])
    # def test_db_11(self, driver, db_name, table_name, where_condition):
    #     login_page = LoginPage(driver, db_name=db_name)
    #     login_page.delete_record_from_table_by_id(table_name, where_condition)
    #
    # @pytest.mark.All
    # @pytest.mark.db_test
    # @pytest.mark.parametrize(('db_name', 'table_name'),
    #                          [('testdb', 'test1')])
    # def test_db_12(self, driver, db_name, table_name):
    #     login_page = LoginPage(driver, db_name=db_name)
    #     login_page.delete_complete_records_from_the_database(table_name)
    #
    # @pytest.mark.All
    # @pytest.mark.db_test
    # @pytest.mark.parametrize(('db_name', 'table_name'),
    #                          [('testdb', 'test1')])
    # def test_db_13(self, driver, db_name, table_name):
    #     login_page = LoginPage(driver, db_name=db_name)
    #     login_page.truncate_complete_records_from_the_database(table_name)
    #
    # @pytest.mark.All
    # @pytest.mark.db_test
    # @pytest.mark.parametrize(('db_name', 'tableformat'), [(None, 'grid')])
    # def test_db_14(self, driver, db_name, tableformat):
    #     login_page = LoginPage(driver, db_name=db_name)
    #     login_page.display_all_databases_server(tableformat)
    #
    # @pytest.mark.All
    # @pytest.mark.db_test
    # @pytest.mark.parametrize('db_name', [None])
    # def test_db_15(self, driver, db_name):
    #     login_page = LoginPage(driver, db_name=db_name)
    #     login_page.get_all_databases_server()
    #
    # @pytest.mark.All
    # @pytest.mark.db_test
    # @pytest.mark.parametrize(('db_name', 'use_database'), [(None, 'automobile')])
    # def test_db_16(self, driver, db_name, use_database):
    #     login_page = LoginPage(driver, db_name=db_name)
    #     login_page.change_database(use_database)
    #
    # @pytest.mark.All
    # @pytest.mark.db_test
    # @pytest.mark.parametrize(('db_name', 'table_name', 'tb_structure'),
    #                          [("testdb", 'test_tb_3', '''(customer_id INT,name VARCHAR(100),address VARCHAR(255),
    #                     email VARCHAR(100),phone VARCHAR(10),PRIMARY KEY (customer_id))''')])
    # def test_db_17(self, driver, db_name, table_name, tb_structure):
    #     login_page = LoginPage(driver, db_name=db_name)
    #     login_page.create_database_and_drop(table_name, tb_structure)
    #
    # @pytest.mark.All
    # @pytest.mark.db_test
    # @pytest.mark.parametrize(('db_name', 'table_name', 'set_condition', 'where_condition'),
    #                          [("cm_devices", 'customers', "fullname='BB',email='BBB'", "username='B'")])
    # def test_db_18(self, driver, db_name, table_name, set_condition, where_condition):
    #     login_page = LoginPage(driver, db_name=db_name)
    #     login_page.update_records(table_name, set_condition, where_condition)
    #
    # @pytest.mark.All
    # @pytest.mark.db_test
    # @pytest.mark.parametrize(('db_name', 'table_name', 'add_columns'),
    #                          [("college", 'students', ["address_1 VARCHAR(5)", "address_2 VARCHAR(10)"])])
    # def test_db_19(self, driver, db_name, table_name, add_columns):
    #     login_page = LoginPage(driver, db_name=db_name)
    #     login_page.add_columns(table_name, add_columns)
    #
    # @pytest.mark.All
    # @pytest.mark.db_test
    # @pytest.mark.parametrize(('db_name', 'table_name', 'modify_columns'),
    #                          [("college", 'students', ["address_1 VARCHAR(50)", "address_2 VARCHAR(50)"])])
    # def test_db_20(self, driver, db_name, table_name, modify_columns):
    #     login_page = LoginPage(driver, db_name=db_name)
    #     login_page.modify_columns(table_name, modify_columns)
    #
    # @pytest.mark.All
    # @pytest.mark.db_test
    # @pytest.mark.parametrize(('db_name', 'table_name', 'rname_columns'),
    #                          [("college", 'students', ["address_1 TO Address_1", "address_2 TO Address_2"])])
    # def test_db_21(self, driver, db_name, table_name, rname_columns):
    #     login_page = LoginPage(driver, db_name=db_name)
    #     login_page.rename_columns(table_name, rname_columns)
    #
    # @pytest.mark.All
    # @pytest.mark.db_test
    # @pytest.mark.parametrize(('db_name', 'table_name', 'drp_columns'),
    #                          [("college", 'students', ["Address_1", "Address_2"])])
    # def test_db_22(self, driver, db_name, table_name, drp_columns):
    #     login_page = LoginPage(driver, db_name=db_name)
    #     login_page.drop_columns(table_name, drp_columns)
    #
    # @pytest.mark.All
    # @pytest.mark.db_test
    # @pytest.mark.parametrize(('db_name', 'query'),
    #                          [("college", 'SHOW TABLES')])
    # def test_db_23(self, driver, db_name, query):
    #     login_page = LoginPage(driver, db_name=db_name)
    #     login_page.full_query(query)
