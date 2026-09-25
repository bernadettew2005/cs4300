# Homework 1

This project contains Python programs and pytest test cases for Homework 1.

## Setup

Before running any programs or tests, activate the virtual environment:

```bash
source venv_hw1/bin/activate
```

## Running a Program

The Python programs are located in the `src` directory.

To run a program, use:

```bash
python3 src/task1.py
```

Replace `task1.py` with the task you want to run. For example:

```bash
python3 src/task4.py
python3 src/task5.py
python3 src/task6.py
python3 src/task7.py
```

## Running Tests

The test files are located in the `tests` directory.

To run a specific test:

```bash
python3 -m pytest tests/test_task1.py
```

For example:

```bash
python3 -m pytest tests/test_task4.py
python3 -m pytest tests/test_task5.py
python3 -m pytest tests/test_task6.py
python3 -m pytest tests/test_task7.py
```

To run **all tests**:

```bash
python3 -m pytest
```