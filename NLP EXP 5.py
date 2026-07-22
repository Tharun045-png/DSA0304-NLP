import nltk
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = ["playing", "studies", "running", "happily", "books"]

print("=" * 55)
print("        PORTER STEMMING ALGORITHM")
print("=" * 55)

print("\n{:<20}{}".format("Original Word", "Stemmed Word"))
print("-" * 35)

for word in words:
    print("{:<20}{}".format(word, stemmer.stem(word)))

print("\nWord Stemming Completed Successfully.")
print("=" * 55)