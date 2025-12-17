


def get_book_text(filepath):
    return open(filepath).read()


def main():
    book_text = get_book_text('/home/warden/workspace/github.com/lupben/bookbot/books/frankenstein.txt')
    word_count=num_of_words(book_text)
    print(f"Found {word_count} total words")

def num_of_words(text):
    words = text.split()
    return len(words)


main()








