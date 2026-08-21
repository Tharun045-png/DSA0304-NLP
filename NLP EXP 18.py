import re

expression = input("Enter logical expression: ")

pattern = r"^([A-Za-z][A-Za-z0-9_]*)\(([^()]*)\)$"
match = re.match(pattern, expression.strip())

print("=" * 55)
print("              FOPC PARSER")
print("=" * 55)

if match:
    predicate = match.group(1)
    arguments = [x.strip() for x in match.group(2).split(",")]

    if all(arguments):
        print("\nPredicate :", predicate)
        print("Arguments :", arguments)
        print("Result    : VALID FOPC EXPRESSION")
    else:
        print("\nResult    : INVALID FOPC EXPRESSION")
else:
    print("\nResult    : INVALID FOPC EXPRESSION")

print("=" * 55)