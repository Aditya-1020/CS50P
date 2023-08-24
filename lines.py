import sys

if len(sys.argv) != 2:
    sys.exit("Too many or too few command-line arguments")


def count_lines(file_path):
    if not file_path.endswith(".py"):
        sys.exit("Not a Python File")
    try:
        with open(file_path, "r") as file:
            code_lines = 0
            for line in file:
                line = line.strip()
                if line.startswith("#") or not line: 
                    continue
                code_lines += 1
            return code_lines
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    file_path = sys.argv[1].strip()
    num_lines = count_lines(file_path)
    print(num_lines)
