
text = input("Enter words: ").lower().split()

probabilities = {
    "the": ("DT", 0.95),
    "cat": ("NN", 0.90),
    "dog": ("NN", 0.90),
    "runs": ("VB", 0.85),
    "eats": ("VB", 0.85),
    "quickly": ("RB", 0.90),
    "a": ("DT", 0.95),
    "book": ("NN", 0.90)
}

print("Stochastic POS Tags:")

for word in text:
    if word in probabilities:
        tag, probability = probabilities[word]
    else:
        tag, probability = ("NN", 0.50)

    print(word, "->", tag, "Probability:", probability)
