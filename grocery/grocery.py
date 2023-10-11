items = []
while True:
    try:
        item = input().title()  # get new grocery item
    except EOFError:
        # print()
        break
    items.append(item)
items.sort()
item_counts = {item: items.count(item) for item in items}
# print(item_counts)
for k, v in item_counts.items():
    print(v, k.upper())