import sys
from stats import get_num_words, get_chars_dict, get_sorted_char_list

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = get_sorted_char_list(chars_dict)
    print_report(book_path, num_words, chars_sorted_list)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_info in chars_sorted_list:
        if char_info["char"].isalpha():
            print(f"{char_info['char']}: {char_info['num']}")
    print("============= END ===============")

main()