
# Word Sense Disambiguation using the Lesk Algorithm

import re
from nltk.corpus import wordnet as wn

STOPWORDS = {
    "the", "a", "an", "is", "are", "was", "were",
    "to", "in", "on", "at", "of", "and", "or",
    "he", "she", "it", "they", "i", "we", "you",
    "my", "her", "his", "their", "for", "with",
    "from", "into", "this", "that"
}


def tokenize(text):
    return re.findall(r"[a-z]+", text.lower())


def lesk(target_word, sentence):
    target_word = target_word.lower()
    words = tokenize(sentence)

    # Extract context words, excluding the target word
    context = {
        word for word in words
        if word != target_word and word not in STOPWORDS
    }

    synsets = wn.synsets(target_word)

    if not synsets:
        return None, 0, set(), context

    best_synset = None
    best_score = -1
    best_overlap = set()

    for synset in synsets:
        # Build a signature from the definition, examples,
        # and synonyms of each possible meaning
        signature_text = synset.definition()

        signature_text += " " + " ".join(synset.examples())

        signature_text += " " + " ".join(
            lemma.name().replace("_", " ")
            for lemma in synset.lemmas()
        )

        signature = {
            word for word in tokenize(signature_text)
            if word not in STOPWORDS
        }

        overlap = context.intersection(signature)
        score = len(overlap)

        if score > best_score:
            best_score = score
            best_synset = synset
            best_overlap = overlap

    return best_synset, best_score, best_overlap, context


while True:
    word = input(
        "\nEnter the ambiguous word (or 'exit' to stop): "
    ).strip().lower()

    if word == "exit":
        print("Program terminated.")
        break

    if not word or not re.fullmatch(r"[a-z]+", word):
        print("Please enter a single English word.")
        continue

    sentence = input("Enter a sentence containing the word: ").strip()

    if word not in tokenize(sentence):
        print("The sentence must contain the target word.")
        continue

    result, score, overlap, context = lesk(word, sentence)

    if result is None:
        print("No WordNet meanings found for this word.")
    else:
        print("\nTarget word:", word)
        print("Selected meaning:", result.name())
        print("Definition:", result.definition())
        print("Context words:", sorted(context))
        print("Overlapping words:", sorted(overlap))
        print("Overlap score:", score)

        if score == 0:
            print("Note: No context overlap found; "
                  "the first available sense was selected.")
