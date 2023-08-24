import inflect

p = inflect.engine()

names = []
while True:
    try:
        name = input("Name (or press Enter to finish): ")
        if name:
            names.append(name)
        else:
            break
    except EOFError:
        print()
        break

if names:
    output = p.join(names)
    print("Adieu, adieu, to " + output)
else:
    print("No names entered.")