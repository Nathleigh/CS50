# CS50 Python week 6 - file IO
# use a .png file to create a t-shirt design
# need to run from terminal: python ex_shirt.py pic1 pic2
import csv
import sys
import os
from PIL import Image, ImageOps


arguments = sys.argv
if len(arguments) < 3:
    sys.exit("Too few command-line arguments")
elif len(arguments) > 3:
    sys.exit("Too many command-line arguments")
elif os.path.splitext(arguments[1])[1] != os.path.splitext(arguments[2])[1]:
    sys.exit("Input and output have different extensions")
else:
    if not arguments[1].endswith(".png") and not arguments[2].endswith(".png") \
            and not arguments[1].endswith(".jpeg") and not arguments[2].endswith(".jpeg") \
            and not arguments[1].endswith(".jpg") and not arguments[2].endswith(".jpg"):
        sys.exit("Invalid input")
    elif not os.path.exists(arguments[1]):
        sys.exit("Input does not exist")
    else:
        shirt = Image.open("shirt.png")
        size = shirt.size  # returns a height, width tuple
        # print("shirt overlay =", size)
        arg1 = Image.open(arguments[1])
        # print("input pic size =", arg1.size)
        arg1sized = ImageOps.fit(arg1, size)
        # print("Resized", arg1sized.size)
        arg1sized.paste(shirt, shirt)
        arg1sized.save(arguments[2])