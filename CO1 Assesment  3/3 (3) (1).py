import re

# ----------- Input Text -----------
print("Enter the text (Type END on a new line to finish):")

lines = []
while True:
    line = input()
    if line.upper() == "END":
        break
    lines.append(line)

text = "\n".join(lines)

# ----------- Menu -----------
while True:
    print("\n------ Pattern Matching Menu ------")
    print("1. Search Date")
    print("2. Search Phone Number")
    print("3. Search Hashtag")
    print("4. Search Mention")
    print("5. Search Prefix")
    print("6. Search Suffix")
    print("7. Search Word")
    print("8. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number between 1 and 8.")
        continue

    if choice == 1:
        # Date Search (DD/MM/YYYY)
        dates = re.findall(r'\b\d{2}/\d{2}/\d{4}\b', text)

        if dates:
            print("Dates Found:", dates)
        else:
            print("No Date Found")

    elif choice == 2:
        # Phone Number Search
        phones = re.findall(r'\b[6-9]\d{9}\b', text)

        if phones:
            print("Phone Numbers Found:", phones)
        else:
            print("No Phone Number Found")

    elif choice == 3:
        # Hashtag Search
        hashtags = re.findall(r'#\w+', text)

        if hashtags:
            print("Hashtags Found:", hashtags)
        else:
            print("No Hashtag Found")

    elif choice == 4:
        # Mention Search
        mentions = re.findall(r'@\w+', text)

        if mentions:
            print("Mentions Found:", mentions)
        else:
            print("No Mention Found")

    elif choice == 5:
        # Prefix Search
        prefix = input("Enter Prefix: ")

        words = re.findall(r'\b' + re.escape(prefix) + r'\w*\b', text, re.IGNORECASE)

        if words:
            print("Matching Words:", words)
        else:
            print("No Matching Words Found")

    elif choice == 6:
        # Suffix Search
        suffix = input("Enter Suffix: ")

        words = re.findall(r'\b\w*' + re.escape(suffix) + r'\b', text, re.IGNORECASE)

        if words:
            print("Matching Words:", words)
        else:
            print("No Matching Words Found")

    elif choice == 7:
        # Word Search
        word = input("Enter Word: ")

        words = re.findall(r'\b' + re.escape(word) + r'\b', text, re.IGNORECASE)

        if words:
            print("Word Found:", words)
        else:
            print("Word Not Found")

    elif choice == 8:
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice! Please enter a number between 1 and 8.")