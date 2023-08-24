def convert(fraction):
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
        if x < 0 or y <= 0 or x > y:
            return None

        percentage = x / y * 100

        if percentage <= 1:
            return "E"
        elif percentage >= 99:
            return "F"
        else:
            return round(percentage)

    except (ValueError, ZeroDivisionError):
        return None


def gauge(percentage):
    if percentage is not None:
        if isinstance(percentage, int):
            return f"{percentage}%"
        else:
            return percentage
    else:
        return "Invalid"


def main():
    while True:
        fraction = input("Fraction: ")
        percentage = convert(fraction)
        result = gauge(percentage)
        print(result)
        if result != "Invalid":
            break


if __name__ == "__main__":
    main()