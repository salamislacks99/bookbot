from stats import *
import sys



def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    book_path = sys.argv[1]

    book = get_book(book_path)
    count = get_word_count(book)
    chars = get_character_count(book)
    chars_sort = sort_dict(get_character_count(book))

    output = f'''============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {count} total words
--------- Character Count -------\n'''
    
    for char in chars_sort:
        if char["char"].isalpha():
            output+=f"{char['char']}: {char['num']}\n"

    output+="============= END ==============="

    print(output)




if __name__ == "__main__": main()