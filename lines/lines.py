# Harvard CS50 Python week 6 - file IO
# Count the number of non blank, non comment lines in a program
import sys
import os

arguments = sys.argv
if len(arguments) == 1:
    sys.exit("Too few command-line arguments")
elif len(arguments) > 2:
    sys.exit("Too many command-line arguments")
elif len(arguments) == 2:
    if not arguments[1].endswith(".py"):
        sys.exit("Not a Python file")
    elif not os.path.exists(arguments[1]):
        sys.exit("File does not exist")
    else:
        non_blank_count = 0
        with open(arguments[1]) as f:
            for line in f:
                if not line.isspace() and not line.strip().startswith("#"):
                    non_blank_count += 1
        print(non_blank_count)