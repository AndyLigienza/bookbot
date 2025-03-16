import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
        if len(sys.argv) != 2:
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)
        else:
            filepath = sys.argv[1]  # This will be "books/frankenstein.txt" if they run "python3 main.py books/frankenstein.txt"   
            text = get_book_text(filepath)
            num_words = len(count_words(text))
            #print(f"{num_words} words found in the document")
            text_letters = count_letters(text)
            character_count = (dict_sort(text_letters))
            print("============ BOOKBOT ============")
            print("Analyzing book found at books/textenstein.txt...")
            print("----------- Word Count ----------")
            print(f"Found {num_words} total words")
            print("--------- Character Count -------")
            for character in character_count:
                if character["character"].isalpha():
                    print(f"{character['character']}: {character['count']}")
            print("============= END ===============")


from stats import count_words, count_letters, dict_sort

main()