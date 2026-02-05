import csv
from pathlib import Path


def main():
    # Locate CSV file
    base_dir = Path(__file__).resolve().parent
    csv_file = base_dir / "sample_data.csv"

    # Read CSV
    print("Reading CSV file:\n")

    with open(csv_file, mode="r") as file:
        reader = csv.reader(file)

        for row in reader:
            print(row)


if __name__ == "__main__":
    main()
