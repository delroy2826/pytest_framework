create_user_payload = {
    "firstName": "DummyData",
    "lastName": "DummyData",
    "email": "DummyData@gmail.com"
}

create_post_payload = {
    "text": "Post Message",
    "image": "Post Image URL",
    "likes": 0,
    "tags": [],
    "owner": "user id to create post on behalf"
}

create_comment_payload = {
    "message": "Dummy Message",
    "owner": "{{user_id_post}}",
    "post": "{{post_id_for_comment}}"
}
