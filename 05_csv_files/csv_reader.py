'''import csv
from pathlib import Path

def main():
    base_dir = Path(__file__).resolve().parent
    csv_path = base_dir / "data.csv"

    with open(csv_path, newline="", mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

if __name__ == "__main__":
    main()
'''
#to read as dictionary
import csv
from pathlib import Path

def main():
    base_dir = Path(__file__).resolve().parent
    csv_path = base_dir / "data.csv"

    with open(csv_path, newline="", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:

            print(row["name"], row["city"])

if __name__ == "__main__":
    main()
