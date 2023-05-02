from tests.tests_dummy_api_tc import PayloadFile
from page_objects.api_base_page import APIUtils


class TagDataApi(APIUtils):

    def __init__(self, base_url: str | None = None, headers: dict | None = None):
        super().__init__(base_url, headers)

    def get_tag_lists(self, endpoint_url):
        resp_data = super()._get(endpoint_url)
        return resp_data[0], resp_data[1]
