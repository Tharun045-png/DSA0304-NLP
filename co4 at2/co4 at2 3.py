from nltk import CFG
from nltk.parse import EarleyChartParser
from nltk.featstruct import FeatStruct

grammar = CFG.fromstring("""
S -> NP VP

NP -> Det N
NP -> Det N REL
NP -> NP PP

REL -> RelPro VP
VP -> V NP
VP -> V GERUND NP
VP -> V NP CONJ VP
VP -> V PP

PP -> P NP

Det -> "The" | "the" | "a"
N -> "doctor" | "patient" | "medication" | "visit" | "week" | "Chennai"
V -> "reviewed" | "recommends" | "starting" | "scheduling"
RelPro -> "who"
P -> "last" | "in"
GERUND -> "starting"
CONJ -> "and"
""")

sentence = (
    "The doctor who reviewed the patient last week "
    "recommends starting medication and scheduling "
    "a follow-up visit in Chennai"
)

words = sentence.split()

parser = EarleyChartParser(grammar)

print("Medical Report:")
print(sentence)

print("\nParsing Result:")

try:
    count = 0

    for tree in parser.parse(words):
        count += 1
        print("\nParse", count)
        print(tree)

    print("\nTotal Parses:", count)

except ValueError as e:
    print("Parsing Error:", e)


print("\nSemantic Representation")
print("----------------------")

semantic_data = {
    "Agent": "Doctor",
    "Action": "Recommends",
    "Treatment": "Medication",
    "Follow-up Action": "Scheduling a follow-up visit",
    "Location": "Chennai",
    "Time": "Last week"
}

for role, value in semantic_data.items():
    print(role, ":", value)


print("\nFeature Structure")
print("-----------------")

features = FeatStruct(
    SUBJECT="Doctor",
    NUMBER="singular",
    ACTION="recommends",
    TREATMENT="medication",
    FOLLOW_UP="visit",
    LOCATION="Chennai"
)

print(features)