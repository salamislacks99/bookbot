def get_book(book_path):

    with open(book_path, 'r', encoding='utf-8') as f:
        book = f.read() 
        return book
    
def get_word_count(book):
    return len(book.split())

def get_character_count(book):
    book = book.lower()

    chars = {}

    for letter in book:

        if letter in chars:
            chars[letter] += 1
        else:
            chars[letter] = 1

    return chars

def sort_on(items):
    return items["num"]

def sort_dict(book):

    sorted = []

    for char in book:
        sorted.append( {"char": char, "num": book[char] } )
        
    sorted.sort(reverse=True, key=sort_on)
    return sorted