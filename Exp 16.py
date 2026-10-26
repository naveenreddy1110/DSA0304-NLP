
# Named Entity Recognition (NER) using spaCy

import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

while True:
    text = input(
        "\nEnter text (or 'exit' to stop): "
    ).strip()

    if text.lower() == "exit":
        print("Program terminated.")
        break

    if not text:
        print("Please enter some text.")
        continue

    doc = nlp(text)

    print("\nNamed Entities:")

    if not doc.ents:
        print("No named entities found.")
    else:
        for entity in doc.ents:
            meaning = spacy.explain(entity.label_)
            print(
                entity.text, "-->",
                entity.label_, "(" + meaning + ")"
            )
