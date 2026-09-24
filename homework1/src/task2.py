# Task 2: Variables and Data Types

def get_int():
    return 5

def get_float():
    return 3.14

def get_string():
    return "this is a string"

def get_bool():
    return True

def main():
    my_int = get_int()
    my_float = get_float()
    my_string = get_string()
    my_bool = get_bool()

    print(f"int: {my_int}")
    print(f"float: {my_float}")
    print(f"string: {my_string}")
    print(f"bool: {my_bool}")

if __name__ == "__main__":
    main()