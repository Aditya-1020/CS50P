def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Removing the dollar sign ('$') from the input string
    amount = d[1:]
    return float(amount)

def percent_to_float(p):
    # Removing the percentage sign ('%') from the input string
    percentage = p[:-1]
    return float(percentage) / 100

main()