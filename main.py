import sys
from stats import get_book_text
from stats import get_num_words
from stats import get_character_count

def main():
    header1 = "============ BOOKBOT ============"
    header2 = "----------- Word Count ----------"
    header3 = "--------- Character Count -------"
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    path_to_file = sys.argv[1]
    analyze_msg = f"{header1}\nAnalyzing book found at {path_to_file}"
    contents = get_book_text(path_to_file)
    num_words = get_num_words(contents)
    print(f"{header2}\nFound {num_words} total words found in the document")
    char_count = get_character_count(contents)
    print(header3)
    for k, v in char_count.items():
        if k.isalpha():
            print(f"{k}: {v}")
    print("============= END ===============")

main()
