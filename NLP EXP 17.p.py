import nltk
from nltk.corpus import wordnet as wn

nltk.download('wordnet')

word = input("Enter a word: ")

synsets = wn.synsets(word)

print("=" * 60)
print("             WORDNET EXPLORATION")
print("=" * 60)

print("\nWord :", word)

for synset in synsets:
    print("\nSynset     :", synset.name())
    print("Definition :", synset.definition())

    examples = synset.examples()

    if examples:
        print("Example    :", examples[0])

print("\nWordNet Exploration Completed Successfully.")
print("=" * 60)