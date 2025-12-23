def num_of_words(text):
    words = text.split()
    return len(words)

def count_char(text):
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sorted_list_dic(char_count):
    result = []
    for i in char_count:
        result.append({"char": i, "num": char_count[i]})
    result.sort(reverse=True, key=sort_on)
    return result

def sort_on(item):
    return item["num"]





