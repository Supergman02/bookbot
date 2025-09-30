from stats import get_num_words
from stats import get_char_count
from stats import sort_characters
import sys

def get_book_text(filename):
    with open(filename) as f:
        contents = f.read()
    return contents

def print_report(num_words, char_list, book_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in char_list:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = get_book_text(f"{sys.argv[1]}")
    num_words = get_num_words(book)
    char_count = get_char_count(book)
    sorted_char_count = sort_characters(char_count)
    print_report(num_words, sorted_char_count, sys.argv[1])

main()