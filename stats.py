def get_num_words(text):
    words = text.split()
    return len(words)

def num_characters(text):
    characters = text.lower()
    alphabet = {}
    for char in characters:
        if char in alphabet:
            alphabet[char] +=1
        else:
            alphabet[char] = 1
    return alphabet

def sort_characters(alphabet):
    character_list = []
    for k,v in alphabet.items():
        separate = {"char" : k, "num": v}
        character_list.append(separate)  
    character_list.sort(reverse=True, key=sort_on)
    return character_list

def sort_on(separate):
    return separate["num"]
    

