import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
nltk.download('omw-1.4')
lemmatizer = WordNetLemmatizer()
word = input("Enter a word: ")
pos = input("Enter POS (n/v/a/r): ")
result = lemmatizer.lemmatize(word, pos=pos)
print("Original word:", word)
print("Root word:", result)
