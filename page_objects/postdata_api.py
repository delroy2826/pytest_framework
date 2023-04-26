from tests.tests_dummy_api_tc import PayloadFile
from page_objects.api_base_page import APIUtils


class PostDataApi(APIUtils):

    def __init__(self, base_url: str | None = None, headers: dict | None = None):
        super().__init__(base_url, headers)

    def get_all_post(self, endpoint_url: str, params: dict):
        resp_data = super()._get(endpoint_url, params)
        return resp_data[0]['data'], resp_data[1]

    def get_all_user_post(self, endpoint_url: str):
        resp_data = super()._get(endpoint_url)
        return resp_data[0]['data'], resp_data[1]

    def get_post_by_id(self, endpoint_url: str):
        resp_data = super()._get(endpoint_url)
        return resp_data[0], resp_data[1]

    def create_post_by_user_id(self, endpoint_url_create, new_post_payload_data, user_id):
        payload = PayloadFile.create_post_payload
        payload['text'] = new_post_payload_data[0]
        payload['image'] = new_post_payload_data[1]
        payload['likes'] = new_post_payload_data[2]
        payload['tags'] = new_post_payload_data[3]
        payload['owner'] = user_id
        resp_data = super()._post(endpoint_url_create, payload)
        return resp_data[0], resp_data[1]

    def update_post_data(self, endpnt_url_post, update_post_payload_data):
        payload = update_post_payload_data
        resp_data = super()._put(endpnt_url_post, payload)
        return resp_data[0], resp_data[1]

    def delete_post_by_id(self, endpoint_url: str):
        resp_data = super()._delete(endpoint_url)
        return resp_data[0], resp_data[1]
