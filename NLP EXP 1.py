import re

print("=" * 50)
print("        REGULAR EXPRESSION MATCHING")
print("=" * 50)

text = "My phone number is 9876543210 and email is test@gmail.com"

print("\nInput Text:")
print(text)

phone = re.search(r"\d{10}", text)
email = re.search(r"\S+@\S+", text)

print("\nSearching for Patterns...\n")

if phone:
    print("Phone Number Found :", phone.group())

if email:
    print("Email Address Found:", email.group())

print("\nPattern Matching Completed Successfully.")
print("=" * 50)