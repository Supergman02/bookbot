from stats import get_num_words
from stats import get_char_count
from stats import sort_characters

def get_book_text(filename):
    with open(filename) as f:
        contents = f.read()
    return contents

def print_report(num_words, char_list):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in char_list:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")

def main():
    book = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(book)
    char_count = get_char_count(book)
    sorted_char_count = sort_characters(char_count)
    print_report(num_words, sorted_char_count)

main()