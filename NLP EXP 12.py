grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": [["the"]],
    "N": [["cat"], ["dog"]],
    "V": [["sees"], ["likes"]]
}

sentence = input("Enter sentence: ").lower().split()

chart = [[] for _ in range(len(sentence) + 1)]
chart[0].append(("S", ["NP", "VP"], 0, 0))

for i in range(len(chart)):
    changed = True

    while changed:
        changed = False

        for lhs, rhs, dot, start in chart[i]:
            if dot < len(rhs):
                symbol = rhs[dot]

                if symbol in grammar:
                    for rule in grammar[symbol]:
                        state = (symbol, rule, 0, i)
                        if state not in chart[i]:
                            chart[i].append(state)
                            changed = True

                elif i < len(sentence) and symbol == sentence[i]:
                    state = (lhs, rhs, dot + 1, start)
                    if state not in chart[i + 1]:
                        chart[i + 1].append(state)

            else:
                for plhs, prhs, pdot, pstart in chart[start]:
                    if pdot < len(prhs) and prhs[pdot] == lhs:
                        state = (plhs, prhs, pdot + 1, pstart)
                        if state not in chart[i]:
                            chart[i].append(state)
                            changed = True

accepted = ("S", ["NP", "VP"], 2, 0) in chart[len(sentence)]

print("=" * 50)
print("           EARLEY PARSER")
print("=" * 50)

if accepted:
    print("\nResult : ACCEPTED")
else:
    print("\nResult : REJECTED")

print("=" * 50)