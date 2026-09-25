# Test Task 6

import pytest
from src.task6 import count_words

@pytest.mark.parametrize("filename, expected", [
    ("task6_read_me.txt", 104),
])
def test_count_words(filename, expected):
    assert count_words(filename) == expected