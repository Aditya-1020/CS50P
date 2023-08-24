grocery_list = {}

try:
    while True:
        item = input()
        lowercase_item = item.lower()
        grocery_list[lowercase_item] = grocery_list.get(lowercase_item, 0) + 1
except EOFError:
    sorted_items = sorted(grocery_list.items())

    for item, count in sorted_items:
        print(f"{count} {item.upper()}")
