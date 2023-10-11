from datetime import date
import sys
import inflect

def get_dob(dob):
    try:
        y, m, d = list(map(int, dob.split("-")))
        # print("dob =", date(y, m, d))
        return y, m, d
    except:
        return None

def main():
    dob = input("Date of Birth: ")
    dob_ymd = get_dob(dob)
    if dob_ymd == None:
        sys.exit("Invalid date")

    delta = date.today() - date(*dob_ymd)
    if delta.days < 0:
        sys.exit("Invalid date")
    # print("Days old =", delta.days, type(delta.days))
    minutes = delta.days * 24 * 60
    # print("Minutes =", minutes)
    p = inflect.engine()
    words = p.number_to_words(minutes, andword="")
    print(words.capitalize(), "minutes")


if __name__ == "__main__":
    main()