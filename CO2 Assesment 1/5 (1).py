words = ["relational", "relation", "relate"]

print("{:<15}{:<25}{:<20}{:<12}".format(
    "Word", "Applied Rule", "Intermediate", "Final Stem"))

for word in words:
    if word == "relational":
        rule = "ational -> ate"
        intermediate = "relate"
        stem = "relat"

    elif word == "relation":
        rule = "remove ion"
        intermediate = "relat"
        stem = "relat"

    elif word == "relate":
        rule = "remove e"
        intermediate = "relat"
        stem = "relat"

    print("{:<15}{:<25}{:<20}{:<12}".format(
        word, rule, intermediate, stem))