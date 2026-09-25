# Test Task 7

import pytest
from src.task7 import get_website_status

@pytest.mark.parametrize("url, expected_status", [
    ("https://example.com", 200),
    ("https://www.google.com", 200),
])

def test_get_website_status(url, expected_status):
    """test the get_website_status function"""
    assert get_website_status(url) == expected_status