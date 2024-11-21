def count_words(book):
    words = book.split()
    return len(words)

def count_characters(book):
    chars = {}
    for char in book:
        char = char.lower()
        if char in chars:
            chars[char] = chars[char]+1
        else:
            chars[char] = 1
    return chars

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    print(count_words(file_contents))
    print(count_characters(file_contents))
