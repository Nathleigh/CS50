from pyfiglet import Figlet
import random
import sys

figlet = Figlet()
# print(figlet.getFonts())
fonts_list = figlet.getFonts()
arguments = sys.argv
user_arguments = arguments[1:]

if len(user_arguments) == 0:
    user_font = random.choice(fonts_list)
else:
    if user_arguments[0] == '--font' or user_arguments[0] =='-f':
        user_font = user_arguments[1]
    else:
        print("Invalid usage")
        sys.exit(1)

figlet.setFont(font=user_font)
msg = input("Input: ")
print(figlet.renderText(msg))
