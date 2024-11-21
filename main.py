def count_words(book):
    words = book.split()
    return len(words)

def count_characters(book):
    chars = {}
    for char in book:
        if char.isalpha():
            char = char.lower()
            if char in chars:
                chars[char] = chars[char]+1
            else:
                chars[char] = 1
    return chars


def sort_on(dict):
    return dict["count"]

def generate_book_report(book):
    report_list = []
    total_words = count_words(book)
    report_list.append(f"{total_words} words found in the document")
    
    character_count = count_characters(book)
    char_list = []
    for char, count in character_count.items():
        char_list.append({"char": char, "count": count})
    char_list.sort(reverse=True, key=sort_on)

    for dict in char_list:
        report_list.append(f"The '{dict["char"]}' character was found {dict["count"]} times")
        
    return "\n".join(report_list)



with open("books/frankenstein.txt") as f:
    book = f.read()
    print("--- Begin report of books/frankenstein.txt ---")
    print(generate_book_report(book))
    print("--- End report ---")
