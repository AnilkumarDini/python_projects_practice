# to read the data.json file
import json
from difflib import get_close_matches

data = json.load(open("dictionary\data.json"))

# function to check for the translation or meaning of the word

def translate(word):
    word=word.lower()

    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())):
        print("\nDid you mean %s instead?"%get_close_matches(word, data.keys())[0])
        choice = input("press y for yes or n for no : ")
        if choice =='y':
            return data[get_close_matches(word, data.keys())[0]]
        elif choice =='n':
            return("The word you entered has no meaning !!")
        else:
            return("\nPlease enter y or n\n")

    else:
        print("The word you entered has no meaning !!\n")


word = input("Enter the word : ")
result = translate(word)

if type(result) == list:
    for item in result:
        print(item)
else:
    print(result)


 