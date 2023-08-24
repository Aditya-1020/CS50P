import random

def main():
    while True:
        level_prompt = input("Level: ")
        try:
            level = int(level_prompt)
            break
        except ValueError:
            print("Invalid, enter a positive integer")

    number = random.randint(1, level)

    while True:
        user_guess = input("Guess: ")
        try:
            guess = int(user_guess)
            if guess < 1:
                print("Enter a positive integer")
            elif guess < number:
                print("Too small!")
            elif guess > number:
                print("Too large!")
            elif guess == number:
                print("Just right!")
                break  # Exit the loop when the correct guess is made
        except ValueError:
            print("Invalid, enter a positive integer")

if __name__ == '__main__':
    main()