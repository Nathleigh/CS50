# Harvard CS50 Python week 7 - Regex.  Convert from 12 to 24hr time format.
# Expect input strings like "9:00 AM to 5:00 PM" or "9 AM to 5 PM"
# Raise a ValueError instead if the input to convert is not in either of those
# formats or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.).
# But do not assume that someone’s hours will start ante meridiem and end
# post meridiem; someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).
import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    isCorrectFormat = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) (AM|PM) to (([0-9][0-2]*):*([0-5][0-9])*) (AM|PM)$", s)
    # print(isCorrectFormat)
    if isCorrectFormat:
        # print("OK")
        pieces = isCorrectFormat.groups()
        # print(pieces)  # pieces = ['4', '4', None, "AM", '9', '9', None, "PM"]
        hour1 = int(pieces[1])
        hour2 = int(pieces[5])
        # print(hour1, hour2)
        # check hours
        if hour1 == 12 and pieces[3] == "AM":
            hour1 = 0
        if hour2 == 12 and pieces[7] == "AM":
            hour2 = 0
        if pieces[3] == "PM" and hour1 != 12:
            hour1 += 12
        if pieces[7] == "PM" and hour2 != 12:
            hour2 += 12
        # check minutes
        if pieces[2] == None:
            mins1 = "00"
        else:
            mins1 = pieces[2]
        if pieces[6] == None:
            mins2 = "00"
        else:
            mins2 = pieces[6]
        # print(hour1, ":", mins1, "to", hour2, ":", mins2)
        ...
    else:
        raise ValueError

    timestring = f"{hour1:02d}:{mins1} to {hour2:02d}:{mins2}"
    return timestring


if __name__ == "__main__":
    main()