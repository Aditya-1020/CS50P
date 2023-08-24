import random

def main():
    level = get_level()
    problems = generate_integer(level)
    score = 0
    for problem in problems:
        attempts = 0
        while attempts < 3:
            try:
                answer = int(input(problem + " = "))
                x, y = problem.split("+")
                x = int(x.strip())
                y = int(y.strip())
                if answer == x + y:
                    print("Correct!")
                    score += 1
                    break
                else:
                    attempts += 1
                    print("EEE")
            except ValueError:
                attempts += 1
                print("EEE")
        else:
            x, y = problem.split("+")
            x = x.strip()
            y = y.strip()
            print(f"The correct answer is {int(x) + int(y)}.")

    print(f"COMPLETED!! YOUR SCORE IS {score} out of {len(problems)}.")

def get_level():
    while True:
        try:
            level_prompt = input("Level: ")
            if level_prompt in ["1", "2", "3"]:
                return int(level_prompt)
        except ValueError:
            print("Invalid")

def generate_integer(level):
    problems = []
    if level == 1:
        for _ in range(10):
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            problem = f"{x} + {y} "
            problems.append(problem)
    elif level == 2:
        for _ in range(10):
            x = random.randint(10, 99)
            y = random.randint(10, 99)
            problem = f"{x} + {y} "
            problems.append(problem)
    elif level == 3:
        for _ in range(10):
            x = random.randint(100, 999)
            y = random.randint(100, 999)
            problem = f"{x} + {y} "
            problems.append(problem)
    return problems

if __name__ == "__main__":
    main()