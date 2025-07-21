#IMPORT STUFF
from stats import get_num_characters
from stats import get_num_words
from stats import sort_char_count
import sys

def main(path_to_file):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(path_to_file)} total words")
    print("--------- Character Count -------")
    num_chars = get_num_characters(path_to_file)
    sorted_list = sort_char_count(num_chars)
    for d in sorted_list:
        if d["char"].isalpha():
            print(f"{d["char"]}: {d["count"]}")



main()