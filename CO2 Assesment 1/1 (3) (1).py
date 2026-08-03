words = ["connected", "connecting", "connection"]

rules = {
    "ed": "Inflectional",
    "ing": "Inflectional",
    "ion": "Derivational"
}

print("{:<15}{:<12}{:<10}{:<15}{:<15}".format(
    "Word","Root","Suffix","Type","Normalized"))

for word in words:
    if word.endswith("ing"):
        root = word[:-3]
        suffix = "ing"

    elif word.endswith("ed"):
        root = word[:-2]
        suffix = "ed"

    elif word.endswith("ion"):
        root = "connect"
        suffix = "ion"

    else:
        root = word
        suffix = "-"

    print("{:<15}{:<12}{:<10}{:<15}{:<15}".format(
        word, root, suffix, rules.get(suffix,"-"), "connect"))