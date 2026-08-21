singular = ["he", "she", "the boy", "the girl"]
plural = ["they", "we", "the boys", "the girls"]

singular_verbs = ["is", "runs", "plays", "eats"]
plural_verbs = ["are", "run", "play", "eat"]

sentence = input("Enter sentence: ").lower()

words = sentence.split()

if len(words) >= 2:
    subject = " ".join(words[:-1])
    verb = words[-1]

    if subject in singular and verb in singular_verbs:
        result = "Agreement Correct"
    elif subject in plural and verb in plural_verbs:
        result = "Agreement Correct"
    else:
        result = "Agreement Incorrect"
else:
    result = "Invalid Sentence"

print("=" * 50)
print("        SUBJECT-VERB AGREEMENT")
print("=" * 50)
print("\nSentence :", sentence)
print("Result   :", result)
print("=" * 50)