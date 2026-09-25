# Task 6: File Handling

def count_words(filename):
    """count the words in a file"""
    with open(filename, 'r') as file:
        text = file.read()
    words_list = text.split()

    return len(words_list)

def main():
    print(f"Word Count: {count_words('task6_read_me.txt')}")

if __name__ == "__main__":
    main()