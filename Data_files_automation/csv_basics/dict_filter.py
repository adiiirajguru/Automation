import csv
from pathlib import Path


def row_filter(row):
    """
    Write any rule using column names.
    Return True to keep the row.
    """

    # Example filter
    return int(row["Age"]) >= 23


def main():
    base_dir = Path(__file__).resolve().parent

    input_file = base_dir / "sample_data.csv"
    output_file = base_dir / "dict_filtered_output.csv"

    filtered_rows = []

    with open(input_file, mode="r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row_filter(row):
                filtered_rows.append(row)

    # Write CSV
    with open(output_file, mode="w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=filtered_rows[0].keys()
        )
        writer.writeheader()
        writer.writerows(filtered_rows)

    print(" Dict-based CSV filtering done!")


if __name__ == "__main__":
    main()
