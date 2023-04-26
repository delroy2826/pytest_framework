import pytest
from page_objects.postdata_api import PostDataApi


class TestPostDataApi:

    @pytest.mark.post_data_api
    @pytest.mark.parametrize(("endpoint_url", "parameters", "expected_status_code"),
                             [("/post", {"limit": 50}, 200)])
    def test_TC_1_API(self, endpoint_url, parameters, expected_status_code):
        """ Get List of post text and likes """
        post_data_api_page = PostDataApi()
        resp_tuple_data = post_data_api_page.get_all_post(endpoint_url, parameters)
        assert expected_status_code == resp_tuple_data[1], f"Status code not matched " \
                                                           f"{expected_status_code} != {resp_tuple_data[1]}"
        counter = 1
        for dict_data in resp_tuple_data[0]:
            print(f"{counter}) Text: {dict_data['text']} Likes: {dict_data['likes']}")
            counter += 1

    @pytest.mark.post_data_api
    @pytest.mark.parametrize(("endpoint_url", "user_id_post", "expected_status_code"),
                             [("/user/{0}/post", "60d0fe4f5311236168a109ca", 200)])
    def test_TC_2_API(self, endpoint_url, user_id_post, expected_status_code):
        """ Get List of post by user id "60d0fe4f5311236168a109ca" """
        post_data_api_page = PostDataApi()
        endpoint_url = endpoint_url.format(user_id_post)
        resp_tuple_data = post_data_api_page.get_all_user_post(endpoint_url)
        assert expected_status_code == resp_tuple_data[1], f"Status code not matched " \
                                                           f"{expected_status_code} != {resp_tuple_data[1]}"
        counter = 1
        for dict_data in resp_tuple_data[0]:
            if dict_data['owner']['id'] == user_id_post:
                print(f"{counter}) Text: {dict_data['text']} Likes: {dict_data['likes']} - Verified")
            else:
                print(f"{counter}) Text: {dict_data['text']} Likes: {dict_data['likes']} - Not Verified")
            counter += 1

    @pytest.mark.post_data_api
    @pytest.mark.parametrize(("endpoint_url", "post_id", "expected_status_code"),
                             [("/post/{0}", "60d21b4667d0d8992e610c85", 200)])
    def test_TC_3_API(self, endpoint_url, post_id, expected_status_code):
        """ Get post by post id "60d21b4667d0d8992e610c85" """
        post_data_api_page = PostDataApi()
        endpoint_url = endpoint_url.format(post_id)
        resp_tuple_data = post_data_api_page.get_post_by_id(endpoint_url)
        assert expected_status_code == resp_tuple_data[1], f"Status code not matched " \
                                                           f"{expected_status_code} != {resp_tuple_data[1]}"
        if resp_tuple_data[0]['id'] == post_id:
            print(f"FirstName: {resp_tuple_data[0]['owner']['firstName']}\n"
                  f"LastName: {resp_tuple_data[0]['owner']['lastName']}\n"
                  f"Text: {resp_tuple_data[0]['text']}\n"
                  f"Likes: {resp_tuple_data[0]['likes']}\n"
                  f"Likes: {resp_tuple_data[0]['tags']} - Verified")
        else:
            print(f"Text: {resp_tuple_data[0]['text']} Likes: {resp_tuple_data[0]['likes']} - Not Verified")

    @pytest.mark.post_data_api
    @pytest.mark.parametrize(("endpnt_url_create", "new_post_payload_data", "user_id", "expected_status_code",
                              "update_post_payload_data", "endpnt_url_post"),
                             [("/post/create", ["New Post Created", "https://images.pexels.com/a.jpeg", 50,
                                                ["Flower", "Blue Flower", "Butterfly"]], "643fbe62ea551e4225736c32",
                               200,
                               {'text': "Life of Butterfly", "likes": 5}, "/post/{0}")])
    def test_TC_4_API(self, endpnt_url_create, new_post_payload_data, user_id, expected_status_code,
                      update_post_payload_data, endpnt_url_post):
        post_data_api_page = PostDataApi()
        resp_tuple_data_1 = post_data_api_page.create_post_by_user_id(endpnt_url_create, new_post_payload_data, user_id)
        assert expected_status_code == resp_tuple_data_1[1], f"Status code not matched " \
                                                             f"{expected_status_code} != {resp_tuple_data_1[1]}"
        assert resp_tuple_data_1[0]['text'] == new_post_payload_data[0], "Expected New Post Data is not posted"
        assert resp_tuple_data_1[0]['owner']['id'] == user_id, "Expected User id is not updated"
        assert resp_tuple_data_1[0]['likes'] == new_post_payload_data[2], "Expected likes not is not posted"
        new_post_id = resp_tuple_data_1[0]['id']

        endpnt_url_post = endpnt_url_post.format(new_post_id)
        resp_tuple_data_2 = post_data_api_page.update_post_data(endpnt_url_post, update_post_payload_data)
        assert expected_status_code == resp_tuple_data_2[1], f"Status code not matched " \
                                                             f"{expected_status_code} != {resp_tuple_data_2[1]}"
        assert resp_tuple_data_2[0]['text'] == update_post_payload_data['text'], "Expected New Post Data is not posted"
        assert resp_tuple_data_2[0]['likes'] == update_post_payload_data['likes'], "Expected likes not is not posted"
        assert resp_tuple_data_2[0]['owner']['id'] == user_id, "Expected User id is not updated"

        resp_tuple_data_3 = post_data_api_page.get_post_by_id(endpnt_url_post)
        assert expected_status_code == resp_tuple_data_3[1], f"Status code not matched " \
                                                             f"{expected_status_code} != {resp_tuple_data_3[1]}"

        assert resp_tuple_data_3[0]['text'] == update_post_payload_data['text'], "Expected New Post Data is not posted"
        assert resp_tuple_data_3[0]['likes'] == update_post_payload_data['likes'], "Expected likes not is not posted"
        assert resp_tuple_data_3[0]['owner']['id'] == user_id, "Expected User id is not updated"
        assert resp_tuple_data_1[0]['id'] == new_post_id, "Expected Post Id is not shown"

        resp_tuple_data_4 = post_data_api_page.delete_post_by_id(endpnt_url_post)
        assert expected_status_code == resp_tuple_data_4[1], f"Status code not matched " \
                                                             f"{expected_status_code} != {resp_tuple_data_4[1]}"
        assert resp_tuple_data_4[0]['id'] == new_post_id, "Expected Post Id is not shown"
