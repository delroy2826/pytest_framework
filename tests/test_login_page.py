# Open Browser
import pytest
from page_objects.logged_in_successfully import LoggedInSuccessfullyPage
from page_objects.login_page import LoginPage


class TestPositiveScenario:

    @pytest.mark.login
    @pytest.mark.positive
    @pytest.mark.parametrize(("username", "password", "expected_msg"),
                             [("student", "Password123", "Logged In Successfully")])
    def test_positive_login(self, driver, username, password, expected_msg):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login(username, password)

        logged_in = LoggedInSuccessfullyPage(driver)
        assert logged_in.expected_url == logged_in.current_url, "Actual URL is not same as Expected URL"

        assert logged_in.header == expected_msg, "Header is not as expected"
        assert logged_in.is_logout_button_displayed(), "Log out button should be visible"
        logged_in.logout()
        assert login_page.verify_login_page_title(), "Should be navigated to login page"
