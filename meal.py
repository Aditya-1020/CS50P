def convert(time):
    hours, minutes = map(int, time.split(":"))
    return hours + minutes / 60

def main():
    time = input("Enter the current time in 24-hour format (e.g., 7:30): ")
    converted_time = convert(time)

    if 7.0 <= converted_time <= 8.0:
        print("It's breakfast time!")
    elif 12.0 <= converted_time <= 13.0:
        print("It's lunch time!")
    elif 18.0 <= converted_time <= 19.0:
        print("It's dinner time!")

if __name__ == "__main__":
    main()