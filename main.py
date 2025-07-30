from stats import get_num_words
from stats import num_characters
from stats import sort_characters
from stats import sort_on
import sys 

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_char = num_characters(text)
    sort_char = sort_characters(num_char)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sort_char:
        current_char_string = char["char"]
        current_char_count =  char["num"]
        if current_char_string.isalpha():
            print(f"{current_char_string}: {current_char_count}") 
    print("============= END ===============")
def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()


main()