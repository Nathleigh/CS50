valid_input = False
while valid_input == False:
    frac = input("Fraction: ")
    num_denom = frac.split("/")
    if num_denom[0].isdecimal() and num_denom[1].isdecimal():
        if len(num_denom) == 2:
            if int(num_denom[0]) <= int(num_denom[1]):
                if num_denom[1] != 0:
                    valid_input = True
# print(valid_input)
# print(num_denom)
gauge = round(int(num_denom[0]) / int(num_denom[1]) * 100)
# print(type(gauge))
if gauge >= 99:
    print("F")
elif gauge <= 1:
    print("E")
else:
    print(f"{gauge}%")