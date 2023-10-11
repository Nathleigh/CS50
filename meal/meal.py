# Structure your program per the below, wherein convert is a function (that can be called by main) that converts time,
# a str in 24-hour format, to the corresponding number of hours as a float. For instance, given a time like "7:30"
# (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).

def main():
    user_time = input("What time is it? ")
    dec_time = convert(user_time)
    if 7 <= dec_time <= 8:
        print("Breakfast time")
    elif 12 <= dec_time <= 13:
        print("Lunch time")
    elif 18 <= dec_time <= 19:
        print("Dinner time")


def convert(time):
    hr, min = time.split(":")
    decimal = int(hr) + int(min) / 60
    return decimal


if __name__ == "__main__":
    main()