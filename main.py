from stats import num_of_words, count_char, sorted_list_dic


def get_book_text(filepath):
    return open(filepath).read()


def main():
    filepath = "/home/warden/workspace/github.com/lupben/bookbot/books/frankenstein.txt"
    book_text = get_book_text(filepath)

    word_count = num_of_words(book_text)
    char_count = count_char(book_text)
    sorted_chars = sorted_list_dic(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for item in sorted_chars:
        ch = item["char"]
        if ch.isalpha():
            print(f"{ch}: {item['num']}")
        

    print("============= END ===============")


main()







