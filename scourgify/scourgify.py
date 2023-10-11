# CS50 Python week 6 - file IO
# Reformat a csv file to separate a "lastname, firstname" field into 2 cols
import csv
import sys
import os


arguments = sys.argv
if len(arguments) < 3:
    sys.exit("Too few command-line arguments")
elif len(arguments) > 3:
    sys.exit("Too many command-line arguments")
else:
    if not arguments[1].endswith(".csv") or not arguments[2].endswith(".csv"):
        sys.exit("Not a CSV file")
    elif not os.path.exists(arguments[1]):
        sys.exit("File does not exist")
    else:
        with open(arguments[1]) as f:
            data = list(csv.reader(f))
        # print(len(data))
        fixed = [["first", "last", "house"]]
        for i in range(1,len(data)):
        # print(data[0], data[1], data[1][0], data[1][0].split(","))
            last = data[i][0].split(",")[0]
            first = data[i][0].split(",")[1].strip()
            house = data[i][1]
            student = [first, last, house]
            fixed.append(student)
        # print(fixed)
        with open(arguments[2], 'w') as f2:
            write_obj = csv.writer(f2)
            write_obj.writerows(fixed)
            # data = list(csv.reader(f2))
