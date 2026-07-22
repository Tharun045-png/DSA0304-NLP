def ends_with_ab(string):
    state = 0

    for ch in string:
        if state == 0:
            if ch == 'a':
                state = 1
            else:
                state = 0

        elif state == 1:
            if ch == 'b':
                state = 2
            elif ch == 'a':
                state = 1
            else:
                state = 0

        elif state == 2:
            if ch == 'a':
                state = 1
            else:
                state = 0

    return state == 2

print("=" * 50)
print("        FINITE STATE AUTOMATON")
print("=" * 50)

word = input("\nEnter Input String : ")

print("\nChecking whether the string ends with 'ab'...\n")

if ends_with_ab(word):
    print("Result : ACCEPTED")
    print("The input string belongs to the language.")
else:
    print("Result : REJECTED")
    print("The input string does not belong to the language.")

print("=" * 50)