from nltk.stem import PorterStemmer
ps = PorterStemmer()
words = input("Enter words separated by spaces: ").split()
for word in words:
    print(word, "->", ps.stem(word))
