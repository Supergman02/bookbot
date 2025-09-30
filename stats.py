def get_num_words(text):
    word_list = text.split()
    count = len(word_list)
    return count

def get_char_count(text):
    lower_text = text.lower()
    characters={}
    for c in lower_text:
        if c not in characters:
            characters[c] = 1
        else:
            characters[c] += 1
    return characters

def sort_on(items):
    return items["num"]

def sort_characters(char_dic):
    characters = []
    for i in char_dic:
        characters.append({"char": i, "num": char_dic[i]})
    characters.sort(reverse=True, key=sort_on)
    return characters