def main():
    expression = input("enter an expression: ")

    x, y, z = expression.split()

    x = float(x)
    z = float(z)

    if y == "+":
        result = x + z
    elif y == "-":
        result = x - z
    elif y == "*":
        result = x * z
    elif y == "/":
        result = x / z

    if result is not None:
        result = round(result, 1)
        print(result)

    else:
        print("INVALID")

    main()