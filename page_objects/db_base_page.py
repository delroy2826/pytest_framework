import mysql.connector as connector
from tabulate import tabulate


class DButils:

    def __init__(self, host="localhost", database=None, user='root',
                 password='S01titude#'):
        self.host, self.database, self.user, self.password = (host, database, user, password)
        try:
            self.connection = connector.connect(host=self.host, database=self.database, user=self.user,
                                                password=self.password)
            if self.connection.is_connected():
                db_info = self.connection.get_server_info()
                print("Connected to MySql Server : ", db_info)
            else:
                print("Failed")
        except Exception as error:
            print("Error ", error)

    def _display_query_result(self, sql_query: str, tablefmt: str = 'simple') -> str:
        """
        This function displays the result in Readable form using tabulate library
        :param sql_query: SELECT column1, column2, ... FROM table_name;
        :param tablefmt: Various plain-text table formats (`tablefmt`) are supported:
        'plain', 'simple', 'grid', 'pipe', 'orgtbl', 'rst', 'mediawiki',
        'latex', 'latex_raw', 'latex_booktabs', 'latex_longtable' and tsv
        :return: Returns string of data in table format form
        """
        cursor = self.connection.cursor(buffered=True)
        cursor.execute(sql_query)
        result_data = tabulate(cursor.fetchall(), headers=cursor.column_names, tablefmt=tablefmt)
        cursor.close()
        return result_data

    def _display_all_table_data(self, tb_name: str, tablefmt: str = 'simple') -> str:
        """
        This function displays the result in Readable form using tabulate library
        :param tb_name: table name in the database
        :param tablefmt: Various plain-text table formats (`tablefmt`) are supported:
        'plain', 'simple', 'grid', 'pipe', 'orgtbl', 'rst', 'mediawiki',
        'latex', 'latex_raw', 'latex_booktabs', 'latex_longtable' and tsv
        :return: Returns string of data in table format form
            """
        cursor = self.connection.cursor(buffered=True)
        cursor.execute(f"SELECT * FROM {tb_name}")
        result_data = tabulate(cursor.fetchall(), headers=cursor.column_names, tablefmt=tablefmt)
        cursor.close()
        return result_data

    def _db_select_data_output(self, sql_query: str) -> list[dict]:
        """
        Converts result into Dictionary format and returns the data
        :param sql_query: SELECT column1, column2, ... FROM table_name;
        :return:  returns list of dictionary with table data
        """
        cursor = self.connection.cursor(buffered=True)
        cursor.execute(sql_query)
        desc = cursor.description
        column_names = [col[0] for col in desc]
        dict_data = [dict(zip(column_names, row))
                     for row in cursor.fetchall()]
        cursor.close()
        return dict_data

    def _get_row_record_data(self, sqlquery: str, find_with_row_id: str | int) -> dict | None:
        """
        Return row record from the given row id
        :param sqlquery: Select sql query.
        :param find_with_row_id: Identification row id data of the record.
        :return: Returns single data record.
        """
        list_dict_data = self._db_select_data_output(sqlquery)
        for dict_data_single in list_dict_data:
            for key, value in dict_data_single.items():
                if value == find_with_row_id:
                    return dict_data_single
        return None

    def _verify_value_in_row_record(self, sqlquery: str, find_with_row_id: str | int, expected_data: str | int) -> \
            bool | None:
        """
        Return if the expected_data/value is present in the row record
        :param sqlquery: select sql query
        :param find_with_row_id: Identification row id data of the record
        :param expected_data: Expected data to be present in the row record
        :return: Returns True if the expected data is found else returns False
        """
        row_record = self._get_row_record_data(sqlquery, find_with_row_id)
        if expected_data in row_record.values():
            return True
        return False

    def _display_tables_in_database(self, tablefmt: str = 'simple') -> str:
        """
        Display all tables present in the database
        :param tablefmt: Various plain-text table formats (`tablefmt`) are supported:
        'plain', 'simple', 'grid', 'pipe', 'orgtbl', 'rst', 'mediawiki',
        'latex', 'latex_raw', 'latex_booktabs', 'latex_longtable' and tsv
        :return: Returns table data with format form
        """
        cursor = self.connection.cursor(buffered=True)
        cursor.execute("SHOW TABLES")
        result_data = tabulate(cursor.fetchall(), headers=cursor.column_names, tablefmt=tablefmt)
        cursor.close()
        return result_data

    def _get_tables_in_database(self) -> list[dict]:
        """
        Converts result into Dictionary format and returns the data
        :return: Return list of dictionary with table data
        """
        cursor = self.connection.cursor(buffered=True)
        cursor.execute("SHOW TABLES")
        desc = cursor.description
        column_names = [col[0] for col in desc]
        dict_data = [dict(zip(column_names, row))
                     for row in cursor.fetchall()]
        cursor.close()
        return dict_data

    def _display_columns_from_table(self, tb_name: str, tablefmt: str = 'simple') -> str:
        """
        Displays table information
        :param tb_name: table name in the database
        :param tablefmt: Various plain-text table formats (`tablefmt`) are supported:
            'plain', 'simple', 'grid', 'pipe', 'orgtbl', 'rst', 'mediawiki',
            'latex', 'latex_raw', 'latex_booktabs', 'latex_longtable' and tsv
        :return : returns string data with column names
        """
        cursor = self.connection.cursor(buffered=True)
        cursor.execute(f"SHOW COLUMNS FROM {tb_name}")
        result_data = tabulate(cursor.fetchall(), headers=cursor.column_names, tablefmt=tablefmt)
        cursor.close()
        return result_data

    def _get_columns_name_from_table(self, tb_name: str) -> tuple[str]:
        """
        Column names information
        :param tb_name: table name in the database
        :return: Returns only column names in tuple
        """
        cursor = self.connection.cursor(buffered=True)
        cursor.execute(f"SELECT * FROM {tb_name} LIMIT 0")
        column_data = cursor.column_names
        cursor.close()
        return column_data

    def _insert_data_into_table(self, tb_name: str, lst_of_tupledata: list[tuple]) -> None:
        """
        Inserts data into table
        :param tb_name: table name in the database
        :param lst_of_tupledata: list of tuples with values that is required to be inserted in to the table
                                example : [('A','AA','AAA'),('B','BB','BBB')]
        """
        cursor = self.connection.cursor(buffered=True)
        for tuple_data in lst_of_tupledata:
            cursor.execute(f"INSERT INTO {tb_name}({','.join(self._get_columns_name_from_table(tb_name))}) \
            VALUES {tuple_data}")
        self.connection.commit()
        cursor.close()

    def _delete_record_from_table(self, tb_name: str, condition: str) -> None:
        """
        Deletes record from the table as per given condition
        :param tb_name: table name in the database
        :param condition: where condition to be passed
        """
        cursor = self.connection.cursor(buffered=True)
        cursor.execute(f"DELETE FROM {tb_name} WHERE {condition}")
        self.connection.commit()
        cursor.close()

    def _delete_complete_records_from_table(self, tb_name: str) -> None:
        """
        Deletes complete records from the table
        :param tb_name: table name in the database
        """
        cursor = self.connection.cursor(buffered=True)
        cursor.execute(f"DELETE FROM {tb_name}")
        self.connection.commit()
        cursor.close()

    def _truncate_table_records(self, tb_name: str) -> None:
        """
        Deletes complete records from the table similar to DELETE FROM {table_name} command.
        :param tb_name: table name in the database
        """
        cursor = self.connection.cursor(buffered=True)
        cursor.execute(f"TRUNCATE TABLE {tb_name}")
        self.connection.commit()
        cursor.close()

    def _drop_table_from_database(self, tb_name: str) -> None:
        """
        Deletes table from the database
        :param tb_name: table name in the database
        """
        cursor = self.connection.cursor(buffered=True)
        cursor.execute(f"DROP TABLE {tb_name}")
        self.connection.commit()
        cursor.close()

    def _drop_database(self, db_name: str) -> None:
        """
        Deletes database
        :param db_name: database name
        """
        cursor = self.connection.cursor(buffered=True)
        cursor.execute(f"DROP DATABASE {db_name}")
        self.connection.commit()
        cursor.close()

    def _create_database(self, db_name: str) -> None:
        """
        Creates Database
        :param db_name: Database Name
        """
        cursor = self.connection.cursor(buffered=True)
        cursor.execute(f"CREATE DATABASE {db_name}")
        cursor.close()

    def _display_database(self, tablefmt: str = 'simple') -> str:
        """
        Display all database present
        :param tablefmt: Various plain-text table formats (`tablefmt`) are supported:
        'plain', 'simple', 'grid', 'pipe', 'orgtbl', 'rst', 'mediawiki','latex', 'latex_raw', 'latex_booktabs',
        'latex_longtable' and tsv
        :return: str : table data in design format
        """
        cursor = self.connection.cursor(buffered=True)
        cursor.execute("SHOW DATABASES")
        result_data = tabulate(cursor.fetchall(), headers=cursor.column_names, tablefmt=tablefmt)
        cursor.close()
        return result_data

    def _get_database(self) -> list[dict]:
        """
        Converts result into Dictionary format and returns the data,
        :return: list[dict] : list of dictionary with database names
        """
        cursor = self.connection.cursor(buffered=True)
        cursor.execute("SHOW DATABASES")
        desc = cursor.description
        column_names = [col[0] for col in desc]
        dict_data = [dict(zip(column_names, row))
                     for row in cursor.fetchall()]
        cursor.close()
        return dict_data

    def _use_database(self, db_name: str) -> None:
        """
        Selects the database to be utilized for operation
        :param db_name: database name
        """
        cursor = self.connection.cursor(buffered=True)
        cursor.execute(f"USE {db_name}")
        cursor.close()

    def _create_table_in_database(self, tb_name: str, tb_columns_structure: str) -> None:
        """
        Creates table structure,
        :param tb_name: table name,
        :param tb_columns_structure: structure of the table:
        Example: (customer_id INT,name VARCHAR(100),address VARCHAR(255),
                        email VARCHAR(100),phone VARCHAR(10),PRIMARY KEY (customer_id))
        """
        cursor = self.connection.cursor(buffered=True)
        cursor.execute(f"CREATE TABLE {tb_name} {tb_columns_structure}")
        cursor.close()

    def _close_connection(self) -> None:
        """ Close Connection of database """
        self.connection.close()

# db_1 = DButils(database='testdb')
# print(db_1._display_database())
# table_name = "test1"
# tb_structure = """(
#     customer_id INT,
#     name VARCHAR(100),
#     address VARCHAR(255),
#     email VARCHAR(100),
#     phone VARCHAR(10),
#     PRIMARY KEY (customer_id)
# )"""
# db_1._create_table_in_database(table_name, tb_structure)
# print(db_1._display_columns_from_table('test1'))
# db_1._close_connection()


# db_1 = DButils(database='football_club')
# DB_NAME = "testDB12;"
# db_1._drop_database(DB_NAME)
# print(db_1._display_database())
# print(db_1._get_database())
# print(db_1._drop_database(DB_NAME))
# db_1._close_connection()

# db = DButils(database='automobile')
# db_query = "SELECT * FROM owner"
# print(db._db_select_data_output(db_query))
# column_names = db._get_columns_name_from_table('owner')
# values_for_data = [('Ow07', 'Norbert', '170, Jamica')]
# db._insert_data_into_table('owner', column_names, values_for_data)
# print(db._display_query_result(db_query))
# print(db._display_query_result(db_query))
# print(db._db_select_data_output(db_query))
# print(db._get_row_record_data(db_query, "Ow02"))
# print(db._get_row_record_data(db_query, "Ow05"))
# print(db._verify_value_in_row_record(db_query, 'Ow01', 'Amjad Omer'))
# print(db._display_tables_in_database())
# print(db._get_tables_in_database())
# print(db._display_columns_from_table('owner'))
# print(db_2._get_tables_in_database())
# db._delete_record_from_table("owner", "ownerID = 'Ow05'")
# print(db._display_query_result(db_query))
# db._close_connection()
# print(db_2._get_tables_in_database())
# db_1 = DButils(database='football_club')
# db_query = "SELECT * FROM games"
# print(db_1._display_query_result(db_query))
# db_1._delete_complete_records_form_table("games")
# from datetime import datetime
# now = datetime.now()
# formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
# db_1._insert_data_into_table('games', [(1130, formatted_date, 4), (1134, formatted_date, 5)])
# db_1._tuncate_table_records('games')
# print(db_1._display_query_result(db_query))
# db_1._close_connection()
