import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

words = ["running", "better", "children", "studies"]

print("=" * 60)
print("         MORPHOLOGICAL ANALYSIS USING NLTK")
print("=" * 60)

print("\n{:<20}{}".format("Original Word", "Morphological Form"))
print("-" * 40)

for word in words:
    print("{:<20}{}".format(word, lemmatizer.lemmatize(word)))

print("\nMorphological Analysis Completed Successfully.")
print("=" * 60)