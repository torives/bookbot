def count_words(text: str):
    words = text.split()
    return len(words)

# Returns a dict containing all letter characters present in `book` and their count.
# This function is case-insensitive.
def count_characters(text: str):
    chars = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in chars:
                chars[char] = chars[char]+1
            else:
                chars[char] = 1
    return chars

def generate_book_report(book):
    report_list = []
    total_words = count_words(book)
    report_list.append(f"{total_words} words found in the document")
    
    character_count = count_characters(book)
    sorted_chars = sorted(character_count.items(), key=lambda item: item[1], reverse=True)

    for tuple in sorted_chars:
        report_list.append(f"The '{tuple[0]}' character was found {tuple[1]} times")
        
    return "\n".join(report_list)

with open("books/frankenstein.txt") as f:
    book = f.read()
    report = generate_book_report(book)
    print("--- Begin report of books/frankenstein.txt ---")
    print(report)
    print("--- End report ---")
