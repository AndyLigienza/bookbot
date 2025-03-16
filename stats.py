def count_words(text):
    words = text.split()
    return words

def count_letters(text):
    text = text.lower()
    letters = {}
    for letter in text:
        if letter not in letters:
            letters[letter] = 1
        else:
            letters[letter] +=1
    
    return letters

def sort_on(dict):
    return dict["count"]

def dict_sort(stat_dict):
    unsorted_list = []
    for key in stat_dict:
        unsorted_list.append({"character": key, "count": stat_dict[key]})
    
    unsorted_list.sort(reverse=True, key=sort_on)
    return unsorted_list