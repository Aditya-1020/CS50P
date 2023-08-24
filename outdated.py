months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

year = month = day = None

while True:
    date = input("Date: ")
    try:
        month, day, year = date.split("/")
        if (1 <= int(month) <= 12) and (1 <= int(day) <= 31):
            break
    except ValueError:
        pass

    try:
        old_month, old_day, old_year = date.split(" ")
        for i, month_name in enumerate(months, start=1):
            if old_month == month_name:
                day = old_day.replace(",", "")
                if 1 <= int(day) <= 31:
                    month = str(i)
                    year = old_year
                    break
    except ValueError:
        pass

    if month and day and year:
        break
    else:
        print("Invalid date format. Please try again.")

print(f"{int(year)}-{int(month):02}-{int(day):02}")
