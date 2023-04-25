import pytest
from page_objects.userdata_api import UserDataApi


class TestUserDataApi:
    @pytest.mark.user_data_api
    @pytest.mark.parametrize(("endpoint_url", "expected_tc", "expected_status_code"), [("/user", 102, 200)])
    def test_TC_1_API(self, endpoint_url, expected_tc, expected_status_code):
        """ Verify Total count and status code. """
        user_data_api_page = UserDataApi()
        resp_tuple_data = user_data_api_page.get_total_count(endpoint_url)
        assert expected_status_code == resp_tuple_data[1], f"Status code not matched " \
                                                           f"{expected_status_code} != {resp_tuple_data[1]}"
        assert expected_tc == resp_tuple_data[0], f"Total Count History is not matching Expected Count " \
                                                  f"{expected_tc} != {resp_tuple_data[0]}"

    @pytest.mark.user_data_api
    @pytest.mark.parametrize(("endpoint_url", "params_data", "expected_status_code"), [("/user", {'limit': 50}, 200)])
    def test_TC_2_API(self, endpoint_url, params_data, expected_status_code):
        """ Get List of Users with page limit as 50 and print 'firstName' """
        user_data_api_page = UserDataApi()
        resp_tuple_data = user_data_api_page.get_list_of_users(endpoint_url, params_data)
        assert expected_status_code == resp_tuple_data[1], f"Status code not matched " \
                                                           f"{expected_status_code} != {resp_tuple_data[1]}"
        count = 1
        for firstname in resp_tuple_data[0]:
            print(count, " ", firstname['firstName'])
            count += 1

    @pytest.mark.user_data_api
    @pytest.mark.parametrize(("endpoint_url", "user_id", "payload_data", "expected_status_code"),
                             [("/user/{0}", "643fbe62ea551e4225736c32",
                               {"lastName": "oliveira"}, 200)])
    def test_TC_3_API(self, endpoint_url, user_id, payload_data, expected_status_code):
        """ Update lastName of user id "643fbe62ea551e4225736c32" and verify 'lastName' is updated """
        user_data_api_page = UserDataApi()
        endpoint_url = endpoint_url.format(user_id)
        resp_tuple_data = user_data_api_page.update_user_data(endpoint_url, payload_data)
        assert expected_status_code == resp_tuple_data[1], f"Status code not matched " \
                                                           f"{expected_status_code} != {resp_tuple_data[1]}"
        assert payload_data['lastName'] == resp_tuple_data[0], f"User Data update failed " \
                                                               f"{payload_data['lastName']} != {resp_tuple_data[0]}"

    @pytest.mark.user_data_api
    @pytest.mark.parametrize(("endpoint_url", "user_id", "expected_status_code"),
                             [("/user/{0}", "643fbe62ea551e4225736c32", 200)])
    def test_TC_4_API(self, endpoint_url, user_id, expected_status_code):
        """ Get user detail by user id "643fbe62ea551e4225736c32" """
        user_data_api_page = UserDataApi()
        endpoint_url = endpoint_url.format(user_id)
        resp_tuple_data = user_data_api_page.get_user_data_by_id(endpoint_url)
        assert expected_status_code == resp_tuple_data[1], f"Status code not matched " \
                                                           f"{expected_status_code} != {resp_tuple_data[1]}"
        print(resp_tuple_data[0])

    @pytest.mark.user_data_api
    @pytest.mark.parametrize(
        ("endpoint_url_create", "endpoint_url_delete", "payload_data_list", "expected_status_code"),
        [("/user/create", "/user/{0}", ["Delroy", "Olive", "DelroyOlive@gmail.com"], 200)])
    def test_TC_5_API(self, endpoint_url_create, endpoint_url_delete, payload_data_list, expected_status_code):
        """ Create User and Delete the created user """
        user_data_api_page = UserDataApi()
        resp_tuple_data_1 = user_data_api_page.create_new_user(endpoint_url_create, payload_data_list)
        assert expected_status_code == resp_tuple_data_1[1], f"Status code not matched " \
                                                             f"{expected_status_code} != {resp_tuple_data_1[1]}"
        endpoint_url = endpoint_url_delete.format(resp_tuple_data_1[0])
        resp_tuple_data_2 = user_data_api_page.delete_user(endpoint_url)
        assert expected_status_code == resp_tuple_data_2[1], f"Status code not matched " \
                                                             f"{expected_status_code} != {resp_tuple_data_2[1]}"
        assert resp_tuple_data_2[0] == resp_tuple_data_1[0], f"Expected User ID is not deleted"
