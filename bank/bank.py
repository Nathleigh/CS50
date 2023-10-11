gtg = input("Greeting: ")
gtg = gtg.strip().lower()
if gtg[0:5] == 'hello':
    print("$0")
elif gtg[0] == 'h':
    print("$20")
else:
    print("$100")
