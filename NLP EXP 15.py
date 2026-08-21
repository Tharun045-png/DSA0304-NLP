import nltk
from nltk import PCFG
from nltk.parse import ViterbiParser

grammar = PCFG.fromstring("""
S -> NP VP [1.0]
NP -> Det N [0.6] | 'john' [0.4]
VP -> V NP [1.0]
Det -> 'the' [1.0]
N -> 'dog' [0.5] | 'cat' [0.5]
V -> 'sees' [1.0]
""")

sentence = input("Enter sentence: ").lower().split()

parser = ViterbiParser(grammar)
trees = list(parser.parse(sentence))

print("=" * 55)
print("       PROBABILISTIC CFG PARSING")
print("=" * 55)

if trees:
    tree = trees[0]
    print("\nMost Probable Parse Tree:\n")
    print(tree)
    print("\nProbability :", tree.prob())
else:
    print("\nNo valid parse found.")

print("=" * 55)