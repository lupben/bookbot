from stats import num_of_words, count_char, sorted_list_dic
import sys


def get_book_text(filepath):
    return open(filepath).read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    book_text = get_book_text(sys.argv[1])



    filepath = sys.argv[1]
    word_count = num_of_words(book_text)
    char_count = count_char(book_text)
    sorted_chars = sorted_list_dic(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for item in sorted_chars:
        ch = item["char"]
        if ch.isalpha():
            print(f"{ch}: {item['num']}")
        

    print("============= END ===============")
    


main()







