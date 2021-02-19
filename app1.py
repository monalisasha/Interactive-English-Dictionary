import json

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        return "Please enter a valid input"

word = input("Enterr the word: ")
print(translate(word))