from datetime import date
import re
import sys
import inflect

p = inflect.engine()

def main():
    birth_date = input("Enter DOB: ")
    try:
        year, month, day = check_date(birth_date)
    except:
        sys.exit("Invalid date")
    date_of_birth = date(int(year), int(month), int(day))
    todays_date = date.today()
    diff = todays_date - date_of_birth
    total_mins = diff.days * 24 * 60
    output = p.number_to_words(total_mins, andword="")
    print(output.capitalize() + " minutes")

def check_date(birth_date):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birth_date):
        year, month, day = birth_date.split("-")
        return year, month, day
    else:
        raise ValueError("Invalid date")

if __name__ == "__main__":
    main()
