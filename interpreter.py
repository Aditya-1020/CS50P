def main():
    expression = input("enter an expression: ")

    x, y, z = expression.split()

    x = float(x)
    y = float(y)

    if y == "+":
        result = x + z
    elif y == "-":
        result = x - z
    elif y == "*":
        result = x * z
    elif y == "/":
        result = x / z

    result = round(result, 1)

    print(result)

    main()
