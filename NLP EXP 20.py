import nltk
from nltk.corpus import wordnet as wn
import re

nltk.download('wordnet')

sentence = input("Enter sentence: ")
word = input("Enter ambiguous word: ").lower()

context = set(re.findall(r'\w+', sentence.lower()))
synsets = wn.synsets(word)

best_sense = None
max_overlap = 0

for sense in synsets:
    definition = set(re.findall(r'\w+', sense.definition().lower()))
    overlap = len(context & definition)

    if overlap > max_overlap:
        max_overlap = overlap
        best_sense = sense

print("=" * 60)
print("        WORD SENSE DISAMBIGUATION")
print("=" * 60)

if best_sense:
    print("\nWord       :", word)
    print("Best Sense :", best_sense.name())
    print("Definition :", best_sense.definition())
    print("Overlap    :", max_overlap)
else:
    print("\nNo suitable sense found.")

print("\nWSD Completed Successfully.")
print("=" * 60)