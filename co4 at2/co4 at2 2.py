from nltk import CFG
from nltk.parse import EarleyChartParser

grammar = CFG.fromstring("""
S -> VP

VP -> V NP
VP -> V NP PP

NP -> Det N
NP -> Det N PP
NP -> N
NP -> N PP

PP -> P NP

V -> "book"
Det -> "a"
N -> "flight" | "Delhi" | "seat" | "window"
P -> "to" | "with"
""")

sentence = "book a flight to Delhi with a window seat"

words = sentence.split()

parser = EarleyChartParser(grammar)

print("Voice Command:")
print(sentence)

print("\nEarley Parse Results:")

count = 0

for tree in parser.parse(words):
    count += 1
    print("\nParse", count)
    print(tree)

print("\nTotal Parses:", count)