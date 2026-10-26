
import nltk

nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

text = input("Enter a sentence: ")

words = nltk.word_tokenize(text)
tags = nltk.pos_tag(words)

print("POS Tags:")
print(tags)
