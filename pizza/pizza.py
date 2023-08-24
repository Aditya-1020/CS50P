import sys
import csv
from tabulate import tabulate

if len(sys.argv) != 2 or not sys.argv[1].endswith(".csv"):
    sys.exit("Too few command-line arguments")

data = []
try:
    with open(sys.argv[1], "r") as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
except FileNotFoundError:
    sys.exit("file does not exist")
headers = data[0]
table = data[1:]
print(tabulate(table, headers, tablefmt="grid"))