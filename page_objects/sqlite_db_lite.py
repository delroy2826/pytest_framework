import sqlite3
import allure


class DesktopPocDB:

    def __init__(self, db_path):
        self.sqliteConnection = sqlite3.connect(db_path)
        print("Connected to SQLite")

    @allure.step
    def extract_values_desc_with_limit(self, limit):
        sql_query = f"SELECT * FROM (SELECT * FROM steps ORDER BY ID DESC LIMIT {limit}) ORDER BY ID;"

        cursor = self.sqliteConnection.cursor()
        print(cursor.execute(sql_query))
        data_list = cursor.fetchall()
        print(f"List of tables\n {data_list}")
        return data_list

    @allure.step
    def verify_data_in_database(self, expected_data, example_db_op, num_steps):
        for i in range(1, num_steps + 1):
            actual = example_db_op[i - 1]
            # print(actual[-1],i-1)
            # print(actual[-3],expected_data['status'])
            # print(actual[-7], expected_data['description'])
            # print(actual[-2] == expected_data['timestamp'])
            if (actual[-1] == i - 1) and actual[-3] == expected_data['status'] and actual[-7] == expected_data[
                'description'] + str(i) and actual[-2] == expected_data['timestamp']:
                print(f'STEPNUMBER Actual {actual[-1]} Expected {i - 1} : ', actual[-1] == i - 1)
                print(f'STATUS Actual {actual[-3]} Expected {expected_data["status"]} : ',
                      actual[-3] == expected_data['status'])
                print(f'DESCRIPTION {actual[-7]} Expected {expected_data["description"] + str(i)} : ',
                      actual[-7] == expected_data['description'] + str(i))
                print(f'TIMESTAMP {actual[-2]} Expected {expected_data["timestamp"]} : ',
                      actual[-2] == expected_data['timestamp'])
            else:
                print('Failed Verification Row ID:', actual[0])
                print(f'STEPNUMBER Actual {actual[-1]} Expected {i - 1} : ', actual[-1] == i - 1)
                print(f'STATUS Actual {actual[-3]} Expected {expected_data["status"]} : ',
                      actual[-3] == expected_data['status'])
                print(f'DESCRIPTION {actual[-7]} Expected {expected_data["description"] + str(i)} : ',
                      actual[-7] == expected_data['description'] + str(i))
                print(f'TIMESTAMP {actual[-2]} Expected {expected_data["timestamp"]} : ',
                      actual[-2] == expected_data['timestamp'])
                return False
        return True

    @allure.step
    def close_db(self):
        self.sqliteConnection.close()
        print("Database closed")
