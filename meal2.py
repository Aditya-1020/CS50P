    def convert(time):
        hours, minutes = map(int, time.split(":"))
        return hours + minutes / 60

    def main():
        time = input("What's the time? ")
        converted_time = convert(time)
        
        if 7.0 <= converted_time <= 8.0:
            print("breakfast time!")
        elif 12.0 <= converted_time <= 13.0:
            print("lunch time!")
        elif 18.0 <= converted_time <= 19.0:
            print("dinner time!")


    if __name__ == "__main__":
        main()