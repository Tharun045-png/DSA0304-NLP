queries = {
    "Q1": "ACTIVATE(Roaming, Customer)",
    "Q2": "DEACTIVATE(CallerTune, Customer)",
    "Q3": "QUERY(DataBalance, Customer)",
    "Q4": "ACTIVATE(5GService, Customer)"
}

actual = {
    "Q1": "Activate Roaming",
    "Q2": "Deactivate Caller Tune",
    "Q3": "Check Data Balance",
    "Q4": "Enable 5G Service"
}

predicted = {
    "Q1": "Activate Roaming",
    "Q2": "Activate Caller Tune",
    "Q3": "Check Data Balance",
    "Q4": "Activate 5G Service"
}

print("Semantic Representations:")
for q, representation in queries.items():
    print(q, ":", representation)

print("\nSemantic Errors:")
for q in actual:
    if actual[q] != predicted[q]:
        print("Query:", q)
        print("Actual Intent   :", actual[q])
        print("Predicted Intent:", predicted[q])
        print()