import csv
from pathlib import Path


def main():
    base_dir = Path(__file__).resolve().parent

    input_file = base_dir / "sample_data.csv"
    output_file = base_dir / "filtered_data.csv"

    filtered_rows = []

    # Read CSV
    with open(input_file, mode="r") as file:
        reader = csv.reader(file)

        header = next(reader)
        filtered_rows.append(header)

        for row in reader:
            age = int(row[1])

            if age >= 23:  # filter condition
                filtered_rows.append(row)

    # Write filtered CSV
    with open(output_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(filtered_rows)

    print("Filtered CSV created!")


if __name__ == "__main__":
    main()
