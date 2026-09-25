# Test Task 1

from src.task1 import hello

def test_hello(capsys):
    """test the hello function"""
    hello()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"