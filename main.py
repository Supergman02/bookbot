from stats import get_num_words
def get_book_text(filename):
    with open(filename) as f:
        contents = f.read()
    return contents

def main():
    book = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(book)
    print(f"Found {num_words} total words")

main()