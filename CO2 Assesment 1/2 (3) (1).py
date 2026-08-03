words = ["unhappy", "happiness", "happily"]

print("{:<12}{:<10}{:<10}{:<10}{:<18}{:<12}".format(
    "Word","Prefix","Base","Suffix","Type","Root"))

for word in words:

    if word.startswith("un"):
        prefix = "un"
        base = "happy"
        suffix = "-"
        typ = "Derivational"

    elif word.endswith("ness"):
        prefix = "-"
        base = "happy"
        suffix = "ness"
        typ = "Derivational"

    elif word.endswith("ly"):
        prefix = "-"
        base = "happy"
        suffix = "ly"
        typ = "Derivational"

    print("{:<12}{:<10}{:<10}{:<10}{:<18}{:<12}".format(
        word,prefix,base,suffix,typ,"happy"))