def main():
    x = float(input("What's x? "))
    y = float(input("What's y? "))
    z = input("Enter operator (+, -, *, %, /): ")
    
    if z == "+":
        result = x + y
    elif z == "-":
        result = x - y
    elif z == "*":
        result = x * y
    elif z == "/":
        result = x / y
    else:
        print("Invalid operator!")
        result = None
    
    print("Result:", result)

main()
