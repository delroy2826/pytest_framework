import pytest

from page_objects.login_page import LoginPage


class TestNegativeScenario:
    @pytest.mark.All
    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize(("username", "password", "unexpectedness"),
                             [("incorrectUser", "Password123", "Your username is invalid!"),
                              ("student", "incorrectPassword", 'Your password is invalid!')])
    def test_negative_login(self, driver, username, password, unexpectedness):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login(username, password)
        assert login_page.verify_login_error_msg(unexpectedness), "Expected Error message should be correct"
        assert login_page.is_login_error_msg_displayed(), "Expected Error message should be displayed"
