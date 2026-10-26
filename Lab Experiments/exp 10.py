
text = input("Enter a sentence: ")
words = text.split()

print("Transformation-Based POS Tags:")

for word in words:
    tag = "NN"

    if word.lower() in ["the", "a", "an"]:
        tag = "DT"

    # Transformation rules
    if word.lower() in ["is", "am", "are", "was", "were"]:
        tag = "VB"

    if word.lower().endswith("ing"):
        tag = "VBG"

    if word.lower().endswith("ly"):
        tag = "RB"

    print(word, "->", tag)
