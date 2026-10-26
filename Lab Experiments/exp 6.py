
import random

text = input("Enter a sentence: ")

words = text.split()
bigrams = {}

for i in range(len(words) - 1):
    current = words[i]
    next_word = words[i + 1]

    if current not in bigrams:
        bigrams[current] = []

    bigrams[current].append(next_word)

word = random.choice(words[:-1])
generated = [word]

for i in range(5):
    if word in bigrams:
        word = random.choice(bigrams[word])
        generated.append(word)
    else:
        break

print("Generated Text:", " ".join(generated))
