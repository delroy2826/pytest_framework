import pytest
import allure
from page_objects.allure_casestest import Calculator


class TestAllure:

    @pytest.mark.testallure
    @pytest.mark.parametrize(("num1", "num2", "answer"), ([1, 2, 3], [5, 5, 10]))
    def test_add_values1(self, num1, num2, answer):
        c1 = Calculator()
        assert c1.addition_two_num(num1, num2) == answer, "Failed"

    @pytest.mark.testallure
    @pytest.mark.parametrize(("num1", "num2", "num3", "result"), ([1, 2, 3, 6], [5, 5, 5, 15]))
    def test_add_values2(self, num1, num2, num3, result):
        c2 = Calculator()
        assert c2.addition_three_num(num1, num2, num3) == result, "Failed"
