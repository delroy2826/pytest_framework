from tests.tests_dummy_api_tc import PayloadFile
from page_objects.api_base_page import APIUtils


class CommentDataApi(APIUtils):

    def __init__(self, base_url: str | None = None, headers: dict | None = None):
        super().__init__(base_url, headers)

    def get_comment_lists(self, endpoint_url, param_data=None):
        resp_data = super()._get(endpoint_url, param_data)
        return resp_data[0], resp_data[1]

    def create_comment(self, end_point_cmt_url, comment_msg, user_id_post, post_comment_id):
        payload = PayloadFile.create_comment_payload
        payload["message"] = comment_msg
        payload["owner"] = user_id_post
        payload["post"] = post_comment_id
        resp_data = super()._post(end_point_cmt_url, payload)
        return resp_data[0], resp_data[1]

    def delete_comment(self, end_point_del_url):
        resp_data = super()._delete(end_point_del_url)
        return resp_data[0], resp_data[1]
