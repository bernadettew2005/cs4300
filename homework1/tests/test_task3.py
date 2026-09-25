# Test Task 3

import pytest
from src.task3 import is_positive, print_primes, print_hundred_sum

@pytest.mark.parametrize("number, expected", [
    (5, "positive"),
    (-5, "negative"),
    (0, "0"),
    (1, "positive"),
    (-1, "negative"),
])

def test_is_positive(number, expected):
    """test the is_positive function"""
    result = is_positive(number)
    assert result == expected

def test_print_primes(capsys):
    """test the print_primes function"""
    print_primes()

    captured = capsys.readouterr()

    assert captured.out == "2\n3\n5\n7\n11\n13\n17\n19\n23\n29\n"

def test_print_hundred_sum(capsys):
    """test the print_hundred_sum function"""
    print_hundred_sum()

    captured = capsys.readouterr()

    assert captured.out == "5050\n"