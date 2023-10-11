# Harvard CS50 Python week 7 regex
# In a file called response.py,
# implement a program that prompts the user for an email address via input and then prints
# Valid or Invalid, respectively, if the input is a syntatically valid email address.
# You may not use re. And do not validate whether the email address’s domain name actually exists.
# Use either validator-collection or validators from PyPI
import validators


def main():
    e = input("What's your email address? ")
    result = validators.email(e)
    if result == True:
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()