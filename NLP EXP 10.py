sentence = input("Enter a sentence: ").split()

print("=" * 60)
print("    TRANSFORMATION BASED TAGGING")
print("=" * 60)

print()

for word in sentence:
    if word.lower() in ["is", "am", "are", "was", "were"]:
        tag = "VB"
    elif word.endswith("ing"):
        tag = "VBG"
    elif word[0].isupper():

        tag = "NNP"
    else:
        tag = "NN"

    print("{:<15}{}".format(word, tag))

print("\nTransformation Based Tagging Completed Successfully.")
print("=" * 60)