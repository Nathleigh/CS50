def main():
    valid_input = False
    percent = None
    while valid_input == False:
        frac = input("Fraction: ")
        try:
            percent = convert(frac)
        except:
            pass
        if type(percent) == int:
            valid_input = True
    # print(valid_input)
    # print(num_denom)
    print(gauge(percent))


def convert(fraction):
    num_denom = fraction.split("/")
    if len(num_denom) == 2:
        if not num_denom[0].isdecimal() or not num_denom[1].isdecimal():
            raise ValueError
        elif num_denom[1] == "0":
            raise ZeroDivisionError
        elif int(num_denom[0]) > int(num_denom[1]):
            raise ValueError
        else:
            percent = round(int(num_denom[0]) / int(num_denom[1]) * 100)
            return percent


def gauge(percentage):
    if percentage >= 99:
        return("F")
    elif percentage <= 1:
        return("E")
    else:
        return(f"{percentage}%")


if __name__ == "__main__":
    main()