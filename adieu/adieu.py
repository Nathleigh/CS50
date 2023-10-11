# CS50’s Introduction to Programming with Python - problem set 4 - adieu
names_list = []
while True:
    try:
        name = input("Name: ")
    except EOFError:
        print()
        break
    names_list.append(name)
    print(names_list)
lyric = "Adieu, adieu, to "
if len(names_list) > 2:
    for i in range(len(names_list) - 1):
        lyric += names_list[i] + ', '
    lyric += 'and ' + names_list[-1]
elif len(names_list) == 2:
    lyric += names_list[0] + ' and ' + names_list[-1]
elif len(names_list) == 1:
    lyric += names_list[0]
else:
    lyric += 'nobody'
print(lyric)