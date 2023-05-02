import pytest
from page_objects.tagdata_api import TagDataApi


class TestTagDataApi:

    @pytest.mark.tag_data_api
    @pytest.mark.parametrize(("endpoint_url", "expected_status_code"), [("/tag", 200)])
    def test_TC_1_API(self, endpoint_url, expected_status_code):
        tag_data_api = TagDataApi()
        resp_tuple_data = tag_data_api.get_tag_lists(endpoint_url)
        assert expected_status_code == resp_tuple_data[1], f"Status code not matched " \
                                                           f"{expected_status_code} != {resp_tuple_data[1]}"
        for tagname in resp_tuple_data[0]['data']:
            print(tagname)
