import json
from difflib import get_close_matches
data = json.load(open('data.json'))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys())) >0:
        ans= input(" Did you mean %s instead? Enter Y for Yes or N for No " % get_close_matches(word,data.keys())[0])
        if ans =='Y':
            return data[get_close_matches(word,data.keys())[0]]
        elif ans =="N":
            return "The word doesn't exist here!"
        else:
            return "Not Available this time"
    else:
        return "The word doesn't exist, please check!"
word = input("Enter word: ")

output = translate(word)

if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)

