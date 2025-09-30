def get_book_text(filename):
    with open(filename) as f:
        contents = f.read()
    return contents

def count_words(text):
    word_list = text.split()
    count = len(word_list)
    return count

def main():
    book = get_book_text("books/frankenstein.txt")
    num_words = count_words(book)
    print(f"Found {num_words} total words")

main()