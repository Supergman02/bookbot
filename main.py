def get_book_text(filename):
    with open(filename) as f:
        contents = f.read()
    return contents

def main():
    st = get_book_text("books/frankenstein.txt")
    print(st)

main()