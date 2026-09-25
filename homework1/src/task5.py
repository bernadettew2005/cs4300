# Task 5: Lists and Dictionaries

favorite_books = [
    ("Matched", "Ally Condie"),
    ("Legend", "Marie Lu"),
    ("The Giver", "Lois Lowry"),
    ("Life of Pi", "Yann Martel"),
    ("The Book Thief", "Markus Zusak"),
]

student_database = {
    "Braelynn": "26591",
    "Tyler": "46512",
    "Victoria": "16512",
    "Naomi": "98415",
}

def main():
    print("First 3 books in list:")
    print(favorite_books[0:3])
    print("-------------------")
    print("Students:")
    print(student_database)

if __name__ == "__main__":
    main()