# Test Task 6

import pytest
from src.task6 import count_words

@pytest.mark.parametrize("filename, expected", [
    ("task6_read_me.txt", 104),
])

def test_count_words(filename, expected):
    """test the count_words function"""
    assert count_words(filename) == expected

def test_empty_file(tmp_path):
    """test an empty file"""
    file = tmp_path / "empty.txt"
    file.write_text("")

    assert count_words(file) == 0

def test_extra_whitespace(tmp_path):
    """test a file with whitespace"""
    file = tmp_path / "whitespace.txt"
    file.write_text("Hello   world\nPython")

    assert count_words(file) == 3

def test_one_word(tmp_path):
    """test a file with one word"""
    file = tmp_path / "one_word.txt"
    file.write_text("Hello")

    assert count_words(file) == 1