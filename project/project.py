import time
import random
import string

def main():
    print()
    print("╔═══════════════════════════════════════════╗")
    print("║            WELCOME TO PASS BOT            ║")
    print("╚═══════════════════════════════════════════╝")
    
    while True:
        display_menu()
        user_input = get_user_input()

        if user_input == "A":
            generate_password()
        elif user_input == "B":
            validate_password()
        elif user_input == "C":
            print("Exiting...")
            time.sleep(1)
            return


def display_menu():
    print()
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("%  [A] = Generate a password   %")
    print("%  [B] = Validate a password   %")
    print("%  [C] = Exit                  %")
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print()


def get_user_input():
    menu_options = ["A", "B", "C"]
    while True:
        user_input = input("Enter an option: ").upper()

        if user_input in menu_options:
            return user_input
        else:
            print("INVALID!! PICK FROM THE MENU")


def generate_password():
    while True:
        length = int(input("Enter password length (minimum 6): "))
        if length >= 6:
            break
        else:
            print("Password length must be 6 or more")
    print()
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
    print()
    include_lowercase = input("Include lowercase letters? (y/n): ").lower() == "y"
    print()
    include_digits = input("Include digits? (y/n): ").lower() == "y"
    print()
    include_special_chars = input("Include special characters? (y/n): ").lower() == "y"
    print()

    characters = ''
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    if not characters:
        print("You must select at least one character type")
        return
    password = ''.join(random.choice(characters) for _ in range(length))
    print("GENERATED PASSWORD ->", password)


def validate_password():
    while True:
        password = input("Enter the password to validate: ")

        if len(password) < 6 or len(password) > 20:
            print("Password length should be between 6 and 20 characters.")
            continue

        has_upper = False
        has_lower = False
        has_digit = False
        has_special = False

        for char in password:
            if char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
            elif char.isdigit():
                has_digit = True
            elif char in string.punctuation:
                has_special = True

        if not (has_upper and has_lower and has_digit and has_special):
            print("Password must have at least one uppercase, one lowercase, one digit, and one special character.")
            continue

        print("Password is valid!")


if __name__ == "__main__":
    main()
