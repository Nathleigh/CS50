var = input("camelCase variable name: ")
for letter in var:
    if letter.isupper():
        letter = "_" + letter.lower()
    print(letter, end="")
print()