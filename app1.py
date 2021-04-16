import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]

    elif word.upper() in data:
        return data[word.upper()]

    elif len(get_close_matches(word, data.keys())) > 0:
        y_n =  input("Did you mean %s instead? (Y/N)" % get_close_matches(word, data.keys())[0])

        if y_n == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        else:
            return "The word doesn't exist in the dictionary. Please enter a valid word"
    else:
        return "Please enter a valid input"

word = input("Enter the word: ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)