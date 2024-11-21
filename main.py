def count_words(book):
    words = book.split()
    return len(words)

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    print(count_words(file_contents))
