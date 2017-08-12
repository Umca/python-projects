import json
from difflib import get_close_matches

def translate():
    data = json.load(open('data.json', 'r'))
    word = input('Please, enter the word: ').lower()
    data_keys = data.keys()

    if word in data_keys:
        for definition in data[word]:
            return definition
    elif len(get_close_matches(word.lower(), data_keys, cutoff=0.8)) > 0:
        confirm = input('Did u mean {} ? If yes, enter y, or n if not'.format(get_close_matches(word, data_keys)[0]))
        if confirm == 'y':
            return data[get_close_matches(word, data_keys)[0]]
        else:
            return 'Sorry, try again later...'
    else:
        return 'Sorry, no word matches! :('

print(translate())
