
# Access WordNet using NLTK

import nltk

from nltk.corpus import wordnet as wn

while True:
    word = input(
        "\nEnter a word (or 'exit' to stop): "
    ).strip().lower()

    if word == "exit":
        print("Program terminated.")
        break

    if not word:
        print("Please enter a word.")
        continue

    synsets = wn.synsets(word)

    if not synsets:
        print("No meanings found for this word.")
        continue

    print("\nWord:", word)
    print("Number of meanings:", len(synsets))

    for i, syn in enumerate(synsets[:5], 1):
        print("\nMeaning", i)
        print("Synset:", syn.name())
        print("Definition:", syn.definition())

        synonyms = sorted(set(
            lemma.name().replace("_", " ")
            for lemma in syn.lemmas()
        ))

        print("Synonyms:", ", ".join(synonyms))

        examples = syn.examples()

        if examples:
            print("Example:", examples[0])
