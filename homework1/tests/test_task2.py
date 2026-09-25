# Test Task 2

import pytest
from src.task2 import get_int, get_float, get_string, get_bool

@pytest.mark.parametrize("function, expected_type", [
    (get_int, int),
    (get_float, float),
    (get_string, str),
    (get_bool, bool),
])

def test_data_types(function, expected_type):
    """test the datatype functions"""
    result = function()
    assert type(result) is expected_type