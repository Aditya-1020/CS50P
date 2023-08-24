def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    s = s.lower()
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[:2].isalpha():
        return False
    if not s.isalnum():
        return False
    if s[-1].isdigit() and not s[:-1].isdigit() and s[0] != "0":
        return True
    return False


if __name__ == "__main__":
    main()
