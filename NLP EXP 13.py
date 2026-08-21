import nltk
from nltk import CFG
from nltk.parse import ChartParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the'
N -> 'cat' | 'dog'
V -> 'sees' | 'likes'
""")

sentence = input("Enter sentence: ").lower().split()

parser = ChartParser(grammar)
trees = list(parser.parse(sentence))

print("=" * 50)
print("             PARSE TREE")
print("=" * 50)

if trees:
    for tree in trees:
        print()
        tree.pretty_print()
else:
    print("\nNo valid parse tree found.")

print("=" * 50)