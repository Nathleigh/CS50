# Harvard CS50P week 7 - Regex
import re

# check for valid IP address: 255 max, 4 numbers, 3 dots

def main():
    address = input("IPv4 address:")
    print(validate(address))


def validate(address):
    if not re.search(r"^\d+\.\d+\.\d+\.\d+$", address):
        validity = False
        return validity
    else:
        nums = list(map(int, address.split(".")))
        validity = True
        for n in nums:
            if n > 255:
                validity = False
        return validity


if __name__ == "__main__":
    main()