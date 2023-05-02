import pytest
from page_objects.commentdata_api import CommentDataApi


class TestCommentDataApi:

    @pytest.mark.comment_data_api
    @pytest.mark.parametrize(("endpoint_url", "expected_status_code", "param_data"), [("/comment", 200, {"limit": 50})])
    def test_TC_1_API(self, endpoint_url, expected_status_code, param_data):
        """ Get List of Comments """
        comment_data_api = CommentDataApi()
        resp_tuple_data = comment_data_api.get_comment_lists(endpoint_url, param_data)
        assert expected_status_code == resp_tuple_data[1], f"Status code not matched " \
                                                           f"{expected_status_code} != {resp_tuple_data[1]}"
        for cmt_dt in resp_tuple_data[0]['data']:
            title = cmt_dt['owner']['title'].capitalize()
            firstName = cmt_dt['owner']['firstName'].capitalize()
            lastName = cmt_dt['owner']['lastName'].capitalize()
            comment = cmt_dt['message'].capitalize()
            print(f"{title} {firstName} {lastName} -> {comment}")

    @pytest.mark.comment_data_api
    @pytest.mark.parametrize(("endpoint_url", "expected_status_code", "post_comment_id"),
                             [("/post/{0}/comment", 200, "60d21b7967d0d8992e610d1b")])
    def test_TC_2_API(self, endpoint_url, expected_status_code, post_comment_id):
        """ Get Comments for Post by POST ID """
        comment_data_api = CommentDataApi()
        endpoint_url = endpoint_url.format(post_comment_id)
        resp_tuple_data = comment_data_api.get_comment_lists(endpoint_url)
        assert expected_status_code == resp_tuple_data[1], f"Status code not matched " \
                                                           f"{expected_status_code} != {resp_tuple_data[1]}"
        for cmt_dt in resp_tuple_data[0]['data']:
            if cmt_dt['post'] == post_comment_id:
                title = cmt_dt['owner']['title'].capitalize()
                firstName = cmt_dt['owner']['firstName'].capitalize()
                lastName = cmt_dt['owner']['lastName'].capitalize()
                comment = cmt_dt['message'].capitalize()
                print(f"{title} {firstName} {lastName} -> {comment} -> Verified")

    @pytest.mark.comment_data_api
    @pytest.mark.parametrize(("endpoint_url", "expected_status_code", "user_id"),
                             [("/user/{0}/comment", 200, "60d0fe4f5311236168a109ca")])
    def test_TC_3_API(self, endpoint_url, expected_status_code, user_id):
        """ Get Comments for Post by user ID """
        comment_data_api = CommentDataApi()
        endpoint_url = endpoint_url.format(user_id)
        resp_tuple_data = comment_data_api.get_comment_lists(endpoint_url)
        assert expected_status_code == resp_tuple_data[1], f"Status code not matched " \
                                                           f"{expected_status_code} != {resp_tuple_data[1]}"
        for cmt_dt in resp_tuple_data[0]['data']:
            if cmt_dt['owner']['id'] == user_id:
                title = cmt_dt['owner']['title'].capitalize()
                firstName = cmt_dt['owner']['firstName'].capitalize()
                lastName = cmt_dt['owner']['lastName'].capitalize()
                comment = cmt_dt['message'].capitalize()
                print(f"{title} {firstName} {lastName} -> {comment} -> Verified")

    @pytest.mark.comment_data_api
    @pytest.mark.parametrize(("end_point_cmt_url", "end_point_del_url", "user_id_post",
                              "post_comment_id", "expected_status_code"),
                             [("/comment/create", "/comment/{0}", "60d0fe4f5311236168a109ca",
                               "60d21b7967d0d8992e610d1b", 200)])
    def test_TC_4_API(self, end_point_cmt_url, end_point_del_url, user_id_post, post_comment_id, expected_status_code):
        """ Create Comment , Verify the comment for the post, delete the comment """
        comment_data_api = CommentDataApi()
        comment_msg = "Nice Picture"
        resp_tuple_data_1 = comment_data_api.create_comment(end_point_cmt_url, comment_msg,
                                                            user_id_post, post_comment_id)
        assert expected_status_code == resp_tuple_data_1[1], f"Status code not matched " \
                                                             f"{expected_status_code} != {resp_tuple_data_1[1]}"
        assert resp_tuple_data_1[0]['message'] == comment_msg, "Expected message is not displayed"
        new_comment_id = resp_tuple_data_1[0]['id']
        endpoint_url = end_point_del_url.format(new_comment_id)
        resp_tuple_data_2 = comment_data_api.delete_comment(endpoint_url)
        assert expected_status_code == resp_tuple_data_2[1], f"Status code not matched " \
                                                             f"{expected_status_code} != {resp_tuple_data_2[1]}"
        assert resp_tuple_data_2[0]['id'] == new_comment_id, "Expected ID is not displayed"
