import pyautogui
import pytest
from page_objects.desktop_poc_app import DesktopApp
from page_objects.sqlite_db_lite import DesktopPocDB
import os
import time
import shutil
from datetime import datetime
import allure


class TestDesktop:
    CR_WRK_DIR = os.getcwd()
    UBUNTU_WSL_PATH = r"\\wsl.localhost\Ubuntu-22.04\\"
    pyautogui.PAUSE = 0.5

    @staticmethod
    def get_imagefld_path():
        list_path = TestDesktop.CR_WRK_DIR.split("\\")
        UPDATED_PATH = list_path
        return "\\".join(UPDATED_PATH) + r"\images" + "\\"

    @staticmethod
    def copy_file_from_project():
        src_path = TestDesktop.UBUNTU_WSL_PATH + r"home\delroy\fox-core-engine-poc\fox-core-engine-poc\Fox-gRPC" \
                                                 r"-service\steps.db"
        dst_path = TestDesktop.CR_WRK_DIR
        shutil.copy(src_path, dst_path)
        print('Steps File Copied')

    # @pytest.mark.desktop_poc
    # @pytest.mark.parametrize(("num_steps", "img_dtl_dict", "db_name", "expected_data_in_db"),
    #                          [(10, {'start_btn': "startbtn.png", 'max_btn': "maxbtn.png", 'miz_btn': 'minimize.png',
    #                                 'reset_time_ctn': "resettimecounter.png", 'reset_stp_btn': "resetstepsbtn.png",
    #                                 'dur_txt_bx': "durationtxtbx.png", 'dur_txt_input': "1",
    #                                 'desc_txt_bx': "descriptiontxtbx.png", 'desc_txt_input': "Text {0}",
    #                                 'add_one_stp_btn': "add1stepbtn.png", 'send_btn': "sendbtn.png",
    #                                 'expected_result_img': "resultforstep1.png", "back_btn": "backbtn.png"},
    #                            'steps.db', {"description": 'Text ', 'status': 'DONE',
    #                                         'timestamp': datetime.now().strftime("%m/%d/%Y")})])
    # def test_add_10_steps_scenario1(self, num_steps, img_dtl_dict, db_name, expected_data_in_db):
    #     time.sleep(10)
    #     self.desktop_poc = DesktopApp()
    #     path = self.get_imagefld_path()
    #
    #     self.desktop_poc.perform_click({'imagepath': path + img_dtl_dict['start_btn']})
    #     # self.desktop_poc.perform_click({'imagepath': path + img_dtl_dict['max_btn']})
    #     self.desktop_poc.perform_click({'imagepath': path + img_dtl_dict['reset_time_ctn']})
    #     self.desktop_poc.perform_click({'imagepath': path + img_dtl_dict['reset_stp_btn']})
    #
    #     for i in range(1, num_steps + 1):
    #         self.desktop_poc.perform_click({'imagepath': path + img_dtl_dict['dur_txt_bx']})
    #         self.desktop_poc.perform_write({'text': img_dtl_dict['dur_txt_input']})
    #         self.desktop_poc.perform_click({'imagepath': path + img_dtl_dict['desc_txt_bx']})
    #         self.desktop_poc.perform_write({'text': img_dtl_dict['desc_txt_input'].format(i)})
    #         self.desktop_poc.perform_click({'imagepath': path + img_dtl_dict['add_one_stp_btn']})
    #         time.sleep(0.5)
    #
    #     self.desktop_poc.perform_click({'imagepath': path + img_dtl_dict['send_btn']})
    #     time.sleep(15)
    #     # status = self.desktop_poc.verify_image_displayed({'imagepath': path + img_dtl_dict['expected_result_img'],
    #     #                                                   "delay_in_sec": 1, 'terminate_counter': 20})
    #     # assert status is True, "Image Validation Failed"
    #     # self.desktop_poc.perform_click({'imagepath': path + img_dtl_dict['minimize.png']})
    #     self.desktop_poc.perform_click({'imagepath': path + img_dtl_dict['back_btn']})
    #     pyautogui.alert("Front End Completed")
    #     self.copy_file_from_project()
    #     self.db_verification = DesktopPocDB(TestDesktop.CR_WRK_DIR + '\\' + db_name)
    #     actual_list_data = self.db_verification.extract_values_desc_with_limit(num_steps)
    #     status = self.db_verification.verify_data_in_database(expected_data_in_db, actual_list_data, num_steps)
    #     self.db_verification.close_db()
    #     assert status is True, "Database Validation Failed"
    #     pyautogui.alert("Database Verification Completed")

    @pytest.mark.desktop_poc
    @pytest.mark.parametrize(("num_steps", "img_dtl_dict", "db_name", "expected_data_in_db"),
                             [(10, {'start_btn': "startbtn.png", 'max_btn': "maxbtn.png",
                                    'reset_time_ctn': "resettimecounter.png", 'reset_stp_btn': "resetstepsbtn.png",
                                    'dur_txt_bx': "mini_duration.png", 'dur_txt_input': "1",
                                    'desc_txt_bx': "mini_description.png", 'desc_txt_input': "Text {0}",
                                    'add_one_stp_btn': "add1stepbtn.png", 'send_btn': "sendbtn.png",
                                    'expected_result_img': "resultforstep1.png", "back_btn": "backbtn.png",
                                    "min_savebtn": "min_savebtn.png"},
                               'steps.db', {"description": 'Text ', 'status': 'DONE',
                                            'timestamp': datetime.now().strftime("%m/%d/%Y")})])
    def test_add_10_steps_scenario2(self, num_steps, img_dtl_dict, db_name, expected_data_in_db):
        time.sleep(5)
        self.desktop_poc = DesktopApp()
        path = self.get_imagefld_path()

        self.desktop_poc.perform_click({'imagepath': path + img_dtl_dict['start_btn']})
        self.desktop_poc.perform_click({'imagepath': path + img_dtl_dict['max_btn']})
        self.desktop_poc.perform_click({'imagepath': path + img_dtl_dict['reset_time_ctn']})
        self.desktop_poc.perform_click({'imagepath': path + img_dtl_dict['reset_stp_btn']})

        for i in range(1, num_steps + 1):
            self.desktop_poc.perform_click({'imagepath': path + img_dtl_dict['dur_txt_bx']})
            self.desktop_poc.perform_write({'text': img_dtl_dict['dur_txt_input']})
            self.desktop_poc.perform_click({'imagepath': path + img_dtl_dict['desc_txt_bx']})
            self.desktop_poc.perform_write({'text': img_dtl_dict['desc_txt_input'].format(i)})
            self.desktop_poc.perform_click({'imagepath': path + img_dtl_dict['add_one_stp_btn']})
            time.sleep(0.5)
        time.sleep(3)
        self.desktop_poc.locate_all_button({'imagepath': path + img_dtl_dict['min_savebtn']})
        time.sleep(3)
        self.desktop_poc.perform_click({'imagepath': path + img_dtl_dict['send_btn']})
        time.sleep(num_steps+5)
        # status = self.desktop_poc.verify_image_displayed({'imagepath': path + img_dtl_dict['expected_result_img'],
        #                                                   "delay_in_sec": 1, 'terminate_counter': 20})
        # assert status is True, "Image Validation Failed"
        # self.desktop_poc.perform_click({'imagepath': path + img_dtl_dict['max_btn']})
        self.desktop_poc.perform_click({'imagepath': path + img_dtl_dict['back_btn']})
        self.copy_file_from_project()
        self.db_verification = DesktopPocDB(TestDesktop.CR_WRK_DIR + '\\' + db_name)
        actual_list_data = self.db_verification.extract_values_desc_with_limit(num_steps)
        status = self.db_verification.verify_data_in_database(expected_data_in_db, actual_list_data, num_steps)
        self.db_verification.close_db()
        assert status is True, "Database Validation Failed"

    # @pytest.mark.desktop_poc
    # @pytest.mark.parametrize(("num_steps", "img_dtl_dict", "db_name", "expected_data_in_db"),
    #                          [(10, {'start_btn': "startbtn.png", 'max_btn': "maxbtn.png",
    #                                 'reset_time_ctn': "resettimecounter.png", 'reset_stp_btn': "resetstepsbtn.png",
    #                                 'dur_txt_bx': "durationtxtbx.png", 'dur_txt_input': "1",
    #                                 'desc_txt_bx': "descriptiontxtbx.png", 'desc_txt_input': "Text {0}",
    #                                 'add_one_stp_btn': "add1stepbtn.png", 'send_btn': "sendbtn.png",
    #                                 'expected_result_img': "resultforstep1.png", "back_btn": "backbtn.png"},
    #                            'steps.db', {"description": 'Text ', 'status': 'DONE',
    #                                         'timestamp': datetime.now().strftime("%m/%d/%Y")})])
    # def test_add_10_steps_scenario3(self, num_steps, img_dtl_dict, db_name, expected_data_in_db):
    #     time.sleep(5)
    #     self.desktop_poc = DesktopApp()
    #     path = self.get_imagefld_path()
    #
    #     self.desktop_poc.perform_click({'imagepath': path + img_dtl_dict['start_btn']})
    #     self.desktop_poc.perform_click({'imagepath': path + img_dtl_dict['max_btn']})
    #     self.desktop_poc.perform_click({'imagepath': path + img_dtl_dict['reset_time_ctn']})
    #     self.desktop_poc.perform_click({'imagepath': path + img_dtl_dict['reset_stp_btn']})
    #
    #     for i in range(1, num_steps + 1):
    #         self.desktop_poc.perform_click({'imagepath': path + img_dtl_dict['dur_txt_bx']})
    #         self.desktop_poc.perform_write({'text': img_dtl_dict['dur_txt_input']})
    #         self.desktop_poc.perform_click({'imagepath': path + img_dtl_dict['desc_txt_bx']})
    #         self.desktop_poc.perform_write({'text': img_dtl_dict['desc_txt_input'].format(i)})
    #         self.desktop_poc.perform_click({'imagepath': path + img_dtl_dict['add_one_stp_btn']})
    #         time.sleep(0.2)
    #
    #     self.desktop_poc.perform_click({'imagepath': path + img_dtl_dict['send_btn']})
    #     status = self.desktop_poc.verify_image_displayed({'imagepath': path + img_dtl_dict['expected_result_img'],
    #                                                       "delay_in_sec": 1, 'terminate_counter': 20})
    #     assert status is True, "Image Validation Failed"
    #     self.desktop_poc.perform_click({'imagepath': path + img_dtl_dict['max_btn']})
    #     self.desktop_poc.perform_click({'imagepath': path + img_dtl_dict['back_btn']})
    #     self.copy_file_from_project()
    #     self.db_verification = DesktopPocDB(TestDesktop.CR_WRK_DIR + '\\' + db_name)
    #     actual_list_data = self.db_verification.extract_values_desc_with_limit(num_steps)
    #     status = self.db_verification.verify_data_in_database(expected_data_in_db, actual_list_data, num_steps)
    #     self.db_verification.close_db()
    #     assert status is True, "Database Validation Failed"
