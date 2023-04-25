from tests.tests_dummy_api_tc import PayloadFile
from page_objects.api_base_page import APIUtils


class UserDataApi(APIUtils):

    def __init__(self, base_url: str | None = None, headers: dict | None = None):
        super().__init__(base_url, headers)

    def get_total_count(self, endpoint_url: str):
        resp_data = super()._get(endpoint_url)
        return resp_data[0]['total'], resp_data[1]

    def get_list_of_users(self, endpoint_url: str, params_data: dict):
        resp_data = super()._get(endpoint_url, params_data)
        return resp_data[0]['data'], resp_data[1]

    def update_user_data(self, endpoint_url: str, payload_data: dict):
        resp_data = super()._put(endpoint_url, payload_data)
        return resp_data[0]['lastName'], resp_data[1]

    def get_user_data_by_id(self, endpoint_url: str):
        resp_data = super()._get(endpoint_url)
        return resp_data[0], resp_data[1]

    def create_new_user(self, endpoint_url_create, payload_data_list):
        payload = PayloadFile.create_user_payload
        payload['firstName'] = payload_data_list[0]
        payload['lastName'] = payload_data_list[1]
        payload['email'] = payload_data_list[2]
        resp_data = super()._post(endpoint_url_create, payload)
        return resp_data[0]['id'], resp_data[1]

    def delete_user(self, endpoint_url_delete):
        resp_data = super()._delete(endpoint_url_delete)
        return resp_data[0]['id'], resp_data[1]





