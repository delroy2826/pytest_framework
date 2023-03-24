import mysql.connector as connector
from tabulate import tabulate
import config


class DButils:
    GlobalConnection = None

    def __init__(self, host=config.host, database=config.database, user=config.user,
                 password=config.password):
        self.host, self.database, self.user, self.password = (host, database, user, password)
        try:
            self.connection = connector.connect(host=self.host, database=self.database, user=self.user,
                                                password=self.password)
            DButils.GlobalConnection = self.connection
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
        :param tb_name: table name in the database
        :param tb_columns_structure: structure of the table:
        Example: (customer_id INT,name VARCHAR(100),address VARCHAR(255),
                        email VARCHAR(100),phone VARCHAR(10),PRIMARY KEY (customer_id))
        """
        cursor = self.connection.cursor(buffered=True)
        cursor.execute(f"CREATE TABLE {tb_name} {tb_columns_structure}")
        cursor.close()

    def _update_records_in_the_table(self, tb_name: str, set_condition: str, where_condition: str) -> None:
        """
        Updates values in the table
        :param tb_name: table name in the database
        :param set_condition: command should be passed in this format "fullname='BB',email='BBB'"
        :param where_condition: command should be passed in this format "username='B'"
        """
        cursor = self.connection.cursor(buffered=True)
        cursor.execute(f"UPDATE {tb_name} SET {set_condition} WHERE {where_condition}")
        self.connection.commit()
        cursor.close()

    def _add_columns_in_the_table(self, tb_name: str, add_columns: list[str]) -> None:
        """
        Alter table columns in the existing table by adding new columns
        :param tb_name: table name in the database
        :param add_columns: adding columns list of string.
            -EXAMPLE: ["address_1 VARCHAR(5) NOT NULL", "address_2 VARCHAR(10)","nick_name VARCHAR(10)"]
        """
        cursor = self.connection.cursor(buffered=True)
        add_col = ",".join(["ADD {0}".format(i) for i in add_columns])
        cursor.execute(f"ALTER TABLE {tb_name} {add_col}")

    def _modify_columns_in_the_table(self, tb_name: str, modify_columns: list[str]) -> None:
        """
        Alter table columns by modifying existing columns data type
        :param tb_name: table name in the database
        :param modify_columns: modifying columns list of string.
            -EXAMPLE: ["address_1 VARCHAR(5)", "address_2 VARCHAR(10)"]
        """
        cursor = self.connection.cursor(buffered=True)
        modify_col = ",".join(["MODIFY COLUMN {0}".format(i) for i in modify_columns])
        cursor.execute(f"ALTER TABLE {tb_name} {modify_col}")

    def _rename_columns_in_the_table(self, tb_name: str, rename_columns: list[str]) -> None:
        """
        Alter table columns by renaming existing columns to new column name
        :param tb_name: table name in the database
        :param rename_columns: renaming columns list of string.
            -EXAMPLE: ["ADDRESS_1 TO address_1", "ADDRESS_2 TO address_2"]
        """
        cursor = self.connection.cursor(buffered=True)
        rename_col = ",".join(["RENAME COLUMN {0}".format(i) for i in rename_columns])
        cursor.execute(f"ALTER TABLE {tb_name} {rename_col}")

    def _drop_columns_in_the_table(self, tb_name: str, drop_columns: list[str]) -> None:
        """
        Alter table columns by drop/deleting existing columns from the table
        :param tb_name: table name in the database
        :param drop_columns: drop columns list of string.
            -EXAMPLE: ["address_1", "address_2"]
        """
        cursor = self.connection.cursor(buffered=True)
        drop_col = ",".join(["DROP COLUMN {0}".format(i) for i in drop_columns])
        cursor.execute(f"ALTER TABLE {tb_name} {drop_col}")

    def _complete_query_function(self, db_query: str, print_output: bool = False,
                                 tablefmt: str = 'simple') -> list[dict] | None:
        """
        Global Method where complete query should be passed
        :param db_query: Database Query
        :param print_output: print the out if 'True' is passed as arguement
        :param tablefmt: Various plain-text table formats (`tablefmt`) are supported:
        'plain', 'simple', 'grid', 'pipe', 'orgtbl', 'rst', 'mediawiki','latex', 'latex_raw', 'latex_booktabs',
        'latex_longtable' and tsv
        :return: Return list of dictionary or None
        """
        cursor = self.connection.cursor(buffered=True)
        if ("show" in db_query.lower()) or ('select' in db_query.lower()):
            cursor.execute(db_query)
            fetch_all = cursor.fetchall()
            desc = cursor.description
            column_names = [col[0] for col in desc]
            dict_data = [dict(zip(column_names, row))
                         for row in fetch_all]
            result_data = tabulate(fetch_all, headers=cursor.column_names, tablefmt=tablefmt)
            cursor.close()
            print(result_data, "\n\n", dict_data) if print_output else "Nothing"
            return dict_data
        elif ("insert" in db_query.lower()) or ("delete" in db_query.lower()) or ("truncate" in db_query.lower()) or \
                ("drop" in db_query.lower()) or ("update" in db_query.lower()):
            cursor.execute(db_query)
            self.connection.commit()
        elif ("create" in db_query.lower()) or ("use" in db_query.lower()) or ("alter" in db_query.lower()):
            cursor.execute(db_query)
        cursor.close()

    @staticmethod
    def close_connection() -> None:
        """ Close Connection of database """
        DButils.GlobalConnection.close()
        print("Connection Closed")
