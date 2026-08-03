words = ["played", "player", "playing"]

print("{:<12}{:<12}{:<10}{:<18}{:<15}".format(
    "Word","Stem","Affix","Type","Normalized"))

for word in words:

    if word.endswith("ing"):
        stem = word[:-3]
        affix = "ing"
        typ = "Inflectional"

    elif word.endswith("ed"):
        stem = word[:-2]
        affix = "ed"
        typ = "Inflectional"

    elif word.endswith("er"):
        stem = word[:-2]
        affix = "er"
        typ = "Derivational"

    print("{:<12}{:<12}{:<10}{:<18}{:<15}".format(
        word,stem,affix,typ,"play"))