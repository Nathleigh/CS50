# CS50’s Introduction to Programming with Python - problem set 4 - bitcoin
import requests
import sys

arguments = sys.argv
user_arguments = arguments[1:]

if len(user_arguments) == 0:
    print("Missing command-line argument")
else:
    try:
        qty = float(user_arguments[0])
    except:
        print("Command-line argument is not a number")
        sys.exit(1)

try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    bit_dict = r.json()
    bit_value = float(bit_dict["bpi"]["USD"]['rate'].replace(",", ""))
    amount = bit_value * qty
    print(f"${amount:>25,.4f}")  # prints $ with 4 dec places
except requests.RequestException:
    print("uh oh, request failed.")

