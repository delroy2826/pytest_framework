import allure_pytest
import allure_commons
import allure


class Calculator:

    @allure.step
    def addition_two_num(self, num1, num2):
        total = num1 + num2
        print(total)
        return num1 + num2

    @allure.step
    def addition_three_num(self, num1, num2, num3):
        total = num1 + num2 + num3
        allure.description("Executing addition_three_num")
        print(total)
        return total

