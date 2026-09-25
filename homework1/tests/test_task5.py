# Test Task 5

import pytest
from src.task5 import favorite_books, student_database

def test_favorite_books():
    assert len(favorite_books) == 5

@pytest.mark.parametrize("index, expected_book", [
    (0, ("Matched", "Ally Condie")),
    (1, ("Legend", "Marie Lu")),
    (2, ("The Giver", "Lois Lowry")),
    (3, ("Life of Pi", "Yann Martel")),
    (4, ("The Book Thief", "Markus Zusak")),
])

def test_first_three_books(index, expected_book):
    """test that the books are correct"""
    assert favorite_books[index] == expected_book

@pytest.mark.parametrize("student, student_id", [
    ("Braelynn", "26591"),
    ("Tyler", "46512"),
    ("Victoria", "16512"),
    ("Naomi", "98415"),
])

def test_student_database(student, student_id):
    """test that the students are correct"""
    assert student_database[student] == student_id