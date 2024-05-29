import allure
import pyautogui
import time


class DesktopApp:
    def __init__(self):
        pass

    @allure.step
    def perform_click(self, kwargs):
        print(f"**** Clicking on {kwargs['imagepath']} ****")
        pyautogui.click(x=kwargs['imagepath'])

    @allure.step
    def perform_write(self, kwargs):
        print(f"**** Writing Text {kwargs['text']} ****")
        pyautogui.write(message=kwargs['text'])

    @allure.step
    def verify_image_displayed(self, kwargs):
        condition = True
        counter = 0
        while condition:
            print("Counter :", counter)
            time.sleep(kwargs['delay_in_sec'])
            if pyautogui.locateOnScreen(kwargs['imagepath']):
                print("**** Image Verified ****")
                return True
            elif counter == kwargs['terminate_counter']:
                print(f"**** Waited for more than {kwargs['terminate_counter']} Hence Terminated ****")
                condition = False
                return condition
            counter += 1

    @allure.step
    def locate_all_button(self, kwargs):
        data = pyautogui.locateAllOnScreen(kwargs['imagepath'])
        print("List of Save buttons:", list(data))
        return list(data)
