grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": [["the"]],
    "N": [["cat"], ["dog"]],
    "V": [["sees"], ["likes"]]
}

sentence = input("Enter sentence: ").lower().split()

def parse(symbol, index):
    if symbol not in grammar:
        if index < len(sentence) and sentence[index] == symbol:
            return index + 1
        return None

    for rule in grammar[symbol]:
        current = index
        success = True

        for item in rule:
            current = parse(item, current)

            if current is None:
                success = False
                break

        if success:
            return current

    return None

result = parse("S", 0)

if result == len(sentence):
    print("Sentence Accepted")
else:
    print("Sentence Rejected")