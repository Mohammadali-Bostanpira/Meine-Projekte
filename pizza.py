import sys
import csv
from tabulate import tabulate

def main():

    if len(sys.argv) < 2:
        sys.exit("too few")

    if len(sys.argv) > 2:
        sys.exit("too many")

    filename = sys.argv[1]

    if not filename.lower().endswith(".csv"):
        sys.exit("not csv")

    try:
        with open(filename) as file:
            reader = csv.reader(file)
            table = list(reader)
    except FileNotFoundError:
        sys.exit("not exist")

    print(tabulate(table[1:], headers=table[0], tablefmt="grid"))

if __name__ == "__main__":
    main()
