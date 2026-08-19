queries = {
    "Apple accessories": {
        "clicked_result": "iPhone Charger",
        "sense": "Technology Brand"
    },
    "Mouse wireless": {
        "clicked_result": "Bluetooth Mouse",
        "sense": "Computer Device"
    },
    "Java tutorial": {
        "clicked_result": "Coding Lessons",
        "sense": "Programming Language"
    },
    "Python course": {
        "clicked_result": "Software Development Training",
        "sense": "Programming Language"
    }
}

for query, data in queries.items():
    print("Query:", query)
    print("Clicked Result:", data["clicked_result"])
    print("Correct Sense:", data["sense"])
    print()