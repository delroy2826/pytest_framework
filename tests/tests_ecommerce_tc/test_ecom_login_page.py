import pytest
import config
from page_objects.login_page_ecom import LoginPageEcommerce
from page_objects.shop_page_ecom import ShopPageEcommerce
from page_objects.checkout_page_ecom import CheckoutPageEcommerce


class TestLoginPageEcom:
    @pytest.mark.All
    @pytest.mark.content_validation
    @pytest.mark.parametrize(("url", "expected_options"), [(config.url, ['Student', 'Teacher', 'Consultant'])])
    def test_TC_1(self, driver, url, expected_options):
        """ Verify all fields are displayed in login form. """
        login_page_ecom = LoginPageEcommerce(driver)
        login_page_ecom.open_ecom_url(url)
        assert login_page_ecom.validate_login_form_content(expected_options)

    @pytest.mark.All
    @pytest.mark.ecom_login
    @pytest.mark.parametrize(("url", "uname", "pword", "submit_form", "expected_url"),
                             [(config.url, "rahulshettyacademy", "learning",
                               True, "https://rahulshettyacademy.com/angularpractice/shop")])
    def test_TC_2(self, driver, url, uname, pword, submit_form, expected_url):
        """ Validate successfull login """
        login_page_ecom = LoginPageEcommerce(driver)
        login_page_ecom.open_ecom_url(url)
        login_page_ecom.enter_login_details(uname, pword, submit=submit_form)
        shop_page_ecom = ShopPageEcommerce(driver)
        shop_page_ecom.url_validation(expected_url)
        shop_page_ecom.validate_checkout_link()

    @pytest.mark.All
    @pytest.mark.invalid_login
    @pytest.mark.parametrize(("url", "uname", "pword", "submit_form"),
                             [(config.url, "invalid_uname", "invalid_pword", True)])
    def test_TC_3(self, driver, url, uname, pword, submit_form):
        """ Validate Unsuccessfull login """
        login_page_ecom = LoginPageEcommerce(driver)
        login_page_ecom.open_ecom_url(url)
        login_page_ecom.enter_login_details(uname, pword, submit=submit_form)
        login_page_ecom.validate_login_error_msg_displayed()

    @pytest.mark.All
    @pytest.mark.content_validation
    @pytest.mark.parametrize(("url", "uname", "pword", "page_title", "expected_url_1", "submit_form", "expected_url_2"),
                             [(config.url, "rahulshettyacademy", "learning", "DOCUMENTS REQUEST",
                               "https://rahulshettyacademy.com/documents-request", True,
                               "https://rahulshettyacademy.com/angularpractice/shop")])
    def test_TC_4(self, driver, url, uname, pword, page_title, expected_url_1, submit_form, expected_url_2):
        """ Validate New tab is opened and verify Document Request title, url. """
        login_page_ecom = LoginPageEcommerce(driver)
        login_page_ecom.open_ecom_url(url)
        login_page_ecom.click_on_blinking_text()
        window_addresses_list = login_page_ecom.get_window_addresses()
        login_page_ecom.change_window(window_addresses_list[1])
        login_page_ecom.verify_new_tab_page_title(page_title)
        login_page_ecom.url_validation(expected_url_1)
        login_page_ecom.change_window(window_addresses_list[0])
        login_page_ecom.enter_login_details(uname, pword, submit=submit_form)
        shop_page_ecom = ShopPageEcommerce(driver)
        shop_page_ecom.url_validation(expected_url_2)
        shop_page_ecom.validate_checkout_link()

    @pytest.mark.All
    @pytest.mark.ecom_login
    @pytest.mark.parametrize(("url", "uname", "pword", "round_btn", "drp_down", "expected_url"),
                             [(config.url, "rahulshettyacademy", "learning", "User", "stud",
                               "https://rahulshettyacademy.com/angularpractice/shop"),
                              (config.url, "rahulshettyacademy", "learning", "User", "consult",
                               "https://rahulshettyacademy.com/angularpractice/shop"),
                              (config.url, "rahulshettyacademy", "learning", "User", "teach",
                               "https://rahulshettyacademy.com/angularpractice/shop")])
    def test_TC_5(self, driver, url, uname, pword, round_btn, drp_down, expected_url):
        """ Validate user can log in as user type and Student as Drop down value. """
        login_page_ecom = LoginPageEcommerce(driver)
        login_page_ecom.open_ecom_url(url)
        login_page_ecom.enter_login_details(uname, pword, round_btn, drp_down, submit=True)
        shop_page_ecom = ShopPageEcommerce(driver)
        shop_page_ecom.url_validation(expected_url)
        shop_page_ecom.validate_checkout_link()

    @pytest.mark.All
    @pytest.mark.ecom_login
    @pytest.mark.parametrize(("url", "uname", "pword", "round_btn", "drp_down", "expected_url"),
                             [(config.url, "rahulshettyacademy", "learning", "User", "stud",
                               "https://rahulshettyacademy.com/angularpractice/shop")])
    def test_TC_6(self, driver, url, uname, pword, round_btn, drp_down, expected_url):
        """ Validate user can log in as user type and Student as Drop down value. """
        login_page_ecom = LoginPageEcommerce(driver)
        login_page_ecom.open_ecom_url(url)
        login_page_ecom.enter_login_details(uname, pword, round_btn, drp_down, submit=True)
        shop_page_ecom = ShopPageEcommerce(driver)
        shop_page_ecom.url_validation(expected_url)
        shop_page_ecom.validate_checkout_link()

    @pytest.mark.All
    @pytest.mark.ecom_login
    @pytest.mark.parametrize(("url", "uname", "pword", "round_btn", "drp_down", "expected_url"),
                             [(config.url, "rahulshettyacademy", "learning", "User", "teach",
                               "https://rahulshettyacademy.com/angularpractice/shop")])
    def test_TC_7(self, driver, url, uname, pword, round_btn, drp_down, expected_url):
        """ Validate user can log in as user type and Teacher as Drop down value. """
        login_page_ecom = LoginPageEcommerce(driver)
        login_page_ecom.open_ecom_url(url)
        login_page_ecom.enter_login_details(uname, pword, round_btn, drp_down, submit=True)
        shop_page_ecom = ShopPageEcommerce(driver)
        shop_page_ecom.url_validation(expected_url)
        shop_page_ecom.validate_checkout_link()

    @pytest.mark.All
    @pytest.mark.ecom_login
    @pytest.mark.parametrize(("url", "uname", "pword", "round_btn", "drp_down", "expected_url"),
                             [(config.url, "rahulshettyacademy", "learning", "User", "consult",
                               "https://rahulshettyacademy.com/angularpractice/shop")])
    def test_TC_8(self, driver, url, uname, pword, round_btn, drp_down, expected_url):
        """ Validate user can log in as user type and Consultant as Drop down value. """
        login_page_ecom = LoginPageEcommerce(driver)
        login_page_ecom.open_ecom_url(url)
        login_page_ecom.enter_login_details(uname, pword, round_btn, drp_down, submit=True)
        shop_page_ecom = ShopPageEcommerce(driver)
        shop_page_ecom.url_validation(expected_url)
        shop_page_ecom.validate_checkout_link()

    @pytest.mark.All
    @pytest.mark.ecom_login
    @pytest.mark.parametrize(("url", "uname", "pword"), [(config.url, "rahulshettyacademy", "learning")])
    def test_TC_9(self, driver, url, uname, pword):
        """ Basic Positional argument login. """
        login_page_ecom = LoginPageEcommerce(driver)
        login_page_ecom.open_ecom_url(url)
        login_page_ecom.enterlogindetails(uname, pword)
        shop_page_ecom = ShopPageEcommerce(driver)
        shop_page_ecom.validate_checkout_link()

    @pytest.mark.All
    @pytest.mark.order_placement
    @pytest.mark.parametrize(("url", "uname", "pword", "submit_form", "expected_url", "prod_list", "delivery_loc"),
                             [(config.url, "rahulshettyacademy", "learning",
                               True, "https://rahulshettyacademy.com/angularpractice/shop",
                               ['iphone X', 'Blackberry'], "India")])
    def test_TC_10(self, driver, url, uname, pword, submit_form, expected_url, prod_list, delivery_loc):
        """ Place order for multiple smartphone and verify if order is placed successfully. """
        login_page_ecom = LoginPageEcommerce(driver)
        login_page_ecom.open_ecom_url(url)
        login_page_ecom.enter_login_details(uname, pword, submit=submit_form)
        shop_page_ecom = ShopPageEcommerce(driver)
        shop_page_ecom.url_validation(expected_url)
        shop_page_ecom.validate_checkout_link()
        shop_page_ecom.add_product_to_cart(prod_list)
        shop_page_ecom.navigate_to_checkout_page()
        checkout_page_ecom = CheckoutPageEcommerce(driver)
        for prod_name in prod_list:
            checkout_page_ecom.verify_product_displayed(prod_name)
        checkout_page_ecom.click_on_checkout_btn()
        checkout_page_ecom.select_delivery_location(delivery_loc)
        checkout_page_ecom.select_terms_and_condition()
        checkout_page_ecom.purchase_and_verify_success_msg()
