import pytest
from page_objects.exceptions_page import ExceptionPage


class TestException:

    @pytest.mark.wait_test
    @pytest.mark.parametrize(("inputted", "expectedtext"), [("Delroy", "Row 2 was saved")])
    def test_wait_time_2(self, driver, inputted, expectedtext):
        exception_page = ExceptionPage(driver)
        exception_page.open()
        exception_page.click_on_add_btn()
        assert exception_page.is_row2_field_displayed(), "Row 2 should be displayed"
        exception_page.add_text_row2(inputted)
        exception_page.click_on_save_btn_row2()
        assert exception_page.is_row2_saved_succ_msg_displayed(), "Row 2 saved message should be displayed"
        assert exception_page.verify_row2_succ_msg(expectedtext), "Row 2 saved success message should be displayed"

    @pytest.mark.wait_test
    @pytest.mark.parametrize(("inputted", "expectedtext"), [("Jelly", "Row 1 was saved")])
    def test_wait_time_3(self, driver, inputted, expectedtext):
        exception_page = ExceptionPage(driver)
        exception_page.open()
        exception_page.click_on_edit_btn_row1()
        exception_page.clear_row1_field()
        exception_page.add_text_row1(inputted)
        exception_page.click_on_save_btn_row1()
        assert exception_page.is_row1_saved_succ_msg_displayed(), "Row1 saved success msg should be displayed"
        assert exception_page.verify_row1_succ_msg(expectedtext), "Row 1 saved message should be displayed"

    @pytest.mark.wait_test
    @pytest.mark.parametrize(("inputted", "expectedtext", "expectedinstructionmsg"), [("Delroy", "Row 2 was saved",
                                                                                       'Push “Add” button to add '
                                                                                       'another row')])
    def test_wait_time_4(self, driver, inputted, expectedtext, expectedinstructionmsg):
        exception_page = ExceptionPage(driver)
        exception_page.open()
        assert exception_page.is_instruction_msg_displayed(), "Instruction should be displayed"
        assert exception_page.verify_instruction_txt_msg(expectedinstructionmsg), "Instruction msg should be displayed"
        exception_page.click_on_add_btn()
        assert exception_page.is_row2_field_displayed(), "Row 2 should be displayed"
        exception_page.add_text_row2(inputted)
        exception_page.click_on_save_btn_row2()
        assert exception_page.is_row2_saved_succ_msg_displayed(), "Row 2 saved message should be displayed"
        assert exception_page.verify_row2_succ_msg(expectedtext), "Row 2 saved success message should be displayed"
        assert not exception_page.is_instruction_msg_displayed(), "Instruction should not be displayed"

    @pytest.mark.wait_test
    def test_wait_time_5(self, driver):
        exception_page = ExceptionPage(driver)
        exception_page.open()
        exception_page.click_on_add_btn()
        assert not exception_page.is_row2_field_displayed(2), "Element takes more time to load"
