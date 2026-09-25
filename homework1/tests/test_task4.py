# Test Task 4

import pytest
from src.task4 import calculate_discount

@pytest.mark.parametrize("price, discount, expected", [
    (100, 20, 80),       # all ints
    (67.99, 5.5, 64.25), # all floats
    (10, 55.3, 4.47), # int price float discount
    (99.89, 40, 59.93),     # float price int dicount
])

def test_calculate_discount(price, discount, expected):
    assert calculate_discount(price, discount) == pytest.approx(expected)