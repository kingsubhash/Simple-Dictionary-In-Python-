import json

from difflib import get_close_matches

data= json.load(open("dictionary_compact.json"))

def translate(word):
    word=word.lower()
    if word in data:
       return data[word]
    elif len(get_close_matches(word,data.keys()))>0:
       user=input('Did you mean %s instead? \n Enter Y if Yes N if No: '%get_close_matches(word,data.keys())[0])
       if user=='Y'or'y':
           return data[get_close_matches(word,data.keys())[0]]
       elif user=='N':
           print ( "Sorry there is not such word. Please double check it")
           #return "sorry"
       else:
           print ( "Sorry we didnot understand what you mean")
           #return"Sorr cant understand"



    else:
        return"Plese enter a valid word"

word=input("Enter a word: ")
output=translate(word)
if type(output)==list:
    for item in output:
        print (item)
else:
    print(output)
