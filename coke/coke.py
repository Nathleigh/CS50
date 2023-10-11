total = 0
owing = 50
while owing > 0:
    print("Amount Due:", owing)
    coin = int(input("Insert coin value: "))
    if coin not in [25, 10, 5]:
        continue
    owing -= coin
print("Change Owed:", 0 - owing)
