# CS50P week 6 pizza menu csv file
import tabulate
import csv
import sys
import os


arguments = sys.argv
if len(arguments) == 1:
    sys.exit("Too few command-line arguments")
elif len(arguments) > 2:
    sys.exit("Too many command-line arguments")
elif len(arguments) == 2:
    if not arguments[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    elif not os.path.exists(arguments[1]):
        sys.exit("File does not exist")
    else:
        with open(arguments[1]) as f:
            menu = list(csv.reader(f))
            print(tabulate.tabulate(menu, headers='firstrow', tablefmt='grid'))