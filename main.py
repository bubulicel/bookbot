#IMPORT STUFF
from stats import get_num_characters
from stats import get_num_words
from stats import sort_char_count
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:    
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {get_num_words(sys.argv[1])} total words")
        print("--------- Character Count -------")
        num_chars = get_num_characters(sys.argv[1])
        sorted_list = sort_char_count(num_chars)
        for d in sorted_list:
            if d["char"].isalpha():
                print(f"{d["char"]}: {d["count"]}")



main()