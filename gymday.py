monday_push = [
    "Chest excercise: ",
    "Barbell bench press",
    "Dumbbell incline press",
    "Push-ups",
    "Chest press machine",
    
    "Shoulder exercises:",
    "Overhead press (barbell or dumbbell)",
    "Arnold press",
    "Lateral raises",
    "Front raises",
    "Shoulder press machine",
    
    "Triceps exercises:",
    "Triceps dips",
    "Close-grip bench press",
    "Triceps pushdowns",
    "Skull crushers"]

wednesday_pull = [
    "Back exercises:",
    "Pull-ups or lat pulldowns",
    "Barbell rows",
    "Dumbbell rows",
    "T-bar rows",
    "Cable rows",
    
    "Biceps exercises: ",
    "Barbell curls",
    "Dumbbell curls",
    "Hammer curls",
    "Preacher curls",
    "Cable curls",
    
    "Rear deltoid exercises: ",
    "Face pulls",
    "Reverse pec deck flyes",
    "Bent-over lateral raises"]

friday_legs = [
    "Squat variations:",

    "Barbell squats (back squats or front squats)",
    "Goblet squats",
    "Bulgarian split squats",
    "Box squats",
    
    "Deadlift variations:",

    "Conventional deadlifts",
    "Sumo deadlifts",
    "Romanian deadlifts",
    "Single-leg deadlifts",
    
    "Hamstring exercises:",

    "Hamstring curls (machine or stability ball)",
    "Glute-ham raises",
    "Romanian deadlifts",
    
    "Quadriceps exercises:",

    "Lunges (walking lunges or stationary lunges)",
    "Leg press",
    "Leg extensions",
    "Hack squats"]


def get_day():
    try:
        exercise_day = input("What day is it today? ").lower()
        if exercise_day == "monday":
            print("Monday Push Exercises: ")
            for exercise in monday_push:
                print(exercise)
        elif exercise_day == "wednesday":
            print("Wednesday Pull Exercises: ")
            for exercise in wednesday_pull:
                print(exercise)
        elif exercise_day == "friday":
            print("Friday Legs Exercises: ")
            for exercise in friday_legs:
                print(exercise)
        elif exercise_day not in ["sunday", "tuesday", "thursday", "saturday"]: # used comma instead of or statements 
            print("INVALID INPUT. PLEASE TRY AGAIN.")
        else:
            print("TODAY IS REST DAY!!")
    except ValueError:
        print("INVALID FORMAT")

get_day()



# formatted code compare later
monday_push = [
    "Chest excercise: ",
    "Barbell bench press",
    "Dumbbell incline press",
    "Push-ups",
    "Chest press machine",
    "Shoulder exercises:",
    "Overhead press (barbell or dumbbell)",
    "Arnold press",
    "Lateral raises",
    "Front raises",
    "Shoulder press machine",
    "Triceps exercises:",
    "Triceps dips",
    "Close-grip bench press",
    "Triceps pushdowns",
    "Skull crushers",
]

wednesday_pull = [
    "Back exercises:",
    "Pull-ups or lat pulldowns",
    "Barbell rows",
    "Dumbbell rows",
    "T-bar rows",
    "Cable rows",
    "Biceps exercises: ",
    "Barbell curls",
    "Dumbbell curls",
    "Hammer curls",
    "Preacher curls",
    "Cable curls",
    "Rear deltoid exercises: ",
    "Face pulls",
    "Reverse pec deck flyes",
    "Bent-over lateral raises",
]

friday_legs = [
    "Squat variations:",
    "Barbell squats (back squats or front squats)",
    "Goblet squats",
    "Bulgarian split squats",
    "Box squats",
    "Deadlift variations:",
    "Conventional deadlifts",
    "Sumo deadlifts",
    "Romanian deadlifts",
    "Single-leg deadlifts",
    "Hamstring exercises:",
    "Hamstring curls (machine or stability ball)",
    "Glute-ham raises",
    "Romanian deadlifts",
    "Quadriceps exercises:",
    "Lunges (walking lunges or stationary lunges)",
    "Leg press",
    "Leg extensions",
    "Hack squats",
]


def get_day():
    try:
        exercise_day = input("What day is it today? ").lower()
        if exercise_day == "monday":
            print("Monday Push Exercises: ")
            for exercise in monday_push:
                print(exercise)
        elif exercise_day == "wednesday":
            print("Wednesday Pull Exercises: ")
            for exercise in wednesday_pull:
                print(exercise)
        elif exercise_day == "friday":
            print("Friday Legs Exercises: ")
            for exercise in friday_legs:
                print(exercise)
        elif exercise_day not in [
            "sunday",
            "tuesday",
            "thursday",
            "saturday",
        ]:  # used comma instead of or statements
            print("INVALID INPUT. PLEASE TRY AGAIN.")
        else:
            print("TODAY IS REST DAY!!")
    except ValueError:
        print("INVALID FORMAT")


get_day()
