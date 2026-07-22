def plural(word):
    if word.endswith("y"):
        return word[:-1] + "ies"
    elif word.endswith(("s", "x", "z", "ch", "sh")):
        return word + "es"
    else:
        return word + "s"

print("=" * 50)
print("     MORPHOLOGICAL PARSING")
print("=" * 50)

word = input("\nEnter a Noun : ")

print("\nGenerated Plural Form :", plural(word))

print("\nParsing Completed Successfully.")
print("=" * 50)