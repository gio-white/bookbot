import sys
from stats import get_num_words, get_char_count, sort_char_numb

def get_book_text(filepath):
    with open(filepath) as f:
        filecontent = f.read()
    return filecontent


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>U")
        sys.exit(1)
    path = sys.argv[1]
    book = get_book_text(path)
    # print(frankenstein)
    num_words = get_num_words(book)
    print(f"Found {num_words} total words")
    char_count = get_char_count(book)

    sorted_list = sort_char_numb(char_count)
    for item in sorted_list:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")

main()