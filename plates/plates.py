def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    s = str(s)
    fulfilled_conditions = 0
    # plates must start with at least two letters
    if s[:2].isalpha():
        fulfilled_conditions +=1
    # plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters
    if 2 <= len(s) <= 6:
        fulfilled_conditions +=1
    # Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
    nums_found = False
    for chr in s:
        if chr.isdecimal():
            if nums_found == False:
                first_num = s.index(chr)
                nums_found = True
                # The first number used cannot be a ‘0’.
                if s[first_num] != '0':
                    fulfilled_conditions +=1
                if s[first_num:].isdecimal():
                    fulfilled_conditions +=1
    if nums_found == False:
        fulfilled_conditions +=2
    # No periods, spaces, or punctuation marks are allowed
    if s.isalnum():
        fulfilled_conditions +=1
    # print(fulfilled_conditions, "conditions met")
    if fulfilled_conditions == 5:
        return True
    else:
        return False


main()