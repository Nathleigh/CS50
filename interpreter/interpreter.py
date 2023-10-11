expr = input("Expression: ")
x, y, z = expr.split(" ")  # will assign 1 to x, + to y, and 1 to z.

if y =='+':
    print(float(x) + float(z))
if y =='-':
    print(float(x) - float(z))
if y =='/':
    print(float(x) / float(z))
if y =='*':
    print(float(x) * float(z))
