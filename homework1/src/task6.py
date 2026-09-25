# Task 6: File Handling

# count the words in a file
def count_words(filename):
    with open(filename, 'r') as file:
        text = file.read()
    words_list = text.split()

    return len(words_list)

def main():
    print(f"Word Count: {count_words('task6_read_me.txt')}")

if __name__ == "__main__":
    main()