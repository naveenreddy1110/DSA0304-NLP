
# Information Retrieval using TF-IDF

import re
import math
from collections import Counter

# Sample document collection
documents = {
    "Doc1": "Python is a popular programming language used for artificial intelligence and machine learning",
    "Doc2": "Machine learning is a branch of artificial intelligence",
    "Doc3": "Information retrieval finds relevant documents using search engines",
    "Doc4": "Python programming is useful for data science and web development"
}


# Convert text into lowercase words
def tokenize(text):
    return re.findall(r"[a-z]+", text.lower())


# Tokenize all documents
doc_words = {
    name: tokenize(text)
    for name, text in documents.items()
}

N = len(documents)

# Calculate document frequency for each word
df = {}

for words in doc_words.values():
    for word in set(words):
        df[word] = df.get(word, 0) + 1


# Calculate TF-IDF vector
def tfidf(words):
    counts = Counter(words)
    total = len(words)

    vector = {}

    for word, count in counts.items():
        tf = count / total
        idf = math.log(
            (N + 1) / (df.get(word, 0) + 1)
        ) + 1

        vector[word] = tf * idf

    return vector


# Create TF-IDF vectors for documents
doc_vectors = {
    name: tfidf(words)
    for name, words in doc_words.items()
}


# Calculate cosine similarity
def cosine_similarity(vector1, vector2):
    common_words = set(vector1) | set(vector2)

    dot_product = sum(
        vector1.get(word, 0) * vector2.get(word, 0)
        for word in common_words
    )

    norm1 = math.sqrt(
        sum(value ** 2 for value in vector1.values())
    )

    norm2 = math.sqrt(
        sum(value ** 2 for value in vector2.values())
    )

    if norm1 == 0 or norm2 == 0:
        return 0.0

    return dot_product / (norm1 * norm2)


# Search for documents repeatedly
while True:
    query = input(
        "\nEnter search query (or 'exit' to stop): "
    ).strip()

    if query.lower() == "exit":
        print("Program terminated.")
        break

    query_words = tokenize(query)

    if not query_words:
        print("Please enter a valid search query.")
        continue

    query_vector = tfidf(query_words)

    # Rank documents by similarity
    results = []

    for name, vector in doc_vectors.items():
        score = cosine_similarity(
            query_vector, vector
        )
        if score > 0:
            results.append((name, score))

    results.sort(key=lambda item: item[1], reverse=True)

    print("\nSearch Results:")

    if not results:
        print("No relevant documents found.")
    else:
        for rank, (name, score) in enumerate(results, 1):
            print(
                rank, ".", name,
                "| Relevance Score:", round(score, 4)
            )
            print("Document:", documents[name])
