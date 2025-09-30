from stats import get_num_words
from stats import get_char_count
from stats import sort_characters

def get_book_text(filename):
    with open(filename) as f:
        contents = f.read()
    return contents

def main():
    book = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(book)
    char_count = get_char_count(book)
    print(f"Found {num_words} total words")
    print(char_count)
    print(sort_characters(char_count))

main()