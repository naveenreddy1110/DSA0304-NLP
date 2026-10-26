
import re

text = input("Enter a sentence: ")
words = text.split()

print("POS Tags:")

for word in words:
    word = word.lower()

    if re.match(r"^(the|a|an)$", word):
        tag = "DT"
    elif re.match(r".*ly$", word):
        tag = "RB"
    elif re.match(r".*ing$", word):
        tag = "VBG"
    elif re.match(r".*ed$", word):
        tag = "VBD"
    elif re.match(r"^(is|am|are|was|were|run|runs)$", word):
        tag = "VB"
    else:
        tag = "NN"

    print(word, "->", tag)
