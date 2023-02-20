import pytest


def add_two_numbers(a, b):
    return a + b


@pytest.mark.math
@pytest.mark.parametrize(("num1", "num2", "result"),
                         [(1, 2, 3),
                          (2, 2, 4),
                          (3, 4, 7)])
def test_small_number(num1, num2, result):
    assert add_two_numbers(num1, num2) == result, f"The sum {num1} and {num2} should be {result}"


@pytest.mark.math
@pytest.mark.parametrize(("num1", "num2", "result"),
                         [(100, 200, 300),
                          (200, 200, 400)])
def test_large_number(num1, num2, result):
    assert add_two_numbers(num1, num2) == result, f"The sum {num1} and {num2} should be {result}"
