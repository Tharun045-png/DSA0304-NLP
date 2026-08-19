import nltk
from nltk import CFG
from nltk.parse import EarleyChartParser

grammar = CFG.fromstring("""
S -> VP
VP -> V NP
NP -> Det N
NP -> Det N PP
NP -> N PP
NP -> N PP PP
PP -> P NP
NP -> Adj N
NP -> Det Adj N

V -> "show"
Det -> "the"
Adj -> "last"
N -> "transactions" | "card" | "month"
P -> "with" | "from"
""")

sentence = "show the transactions with the card from last month"

parser = EarleyChartParser(grammar)

print("Input:", sentence)
print("\nParse Trees:")

count = 0

for tree in parser.parse(sentence.split()):
    count += 1
    print("\nParse", count)
    print(tree)

print("\nTotal Number of Parses:", count)