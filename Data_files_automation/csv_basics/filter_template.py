import csv
from pathlib import Path


def row_filter(row):
    """
    PLACE YOUR FILTER LOGIC HERE

    Return True  -> keep the row
    Return False -> discard the row

    Example ideas:
    - age check
    return int(row[1]) >= 25

    - name match
    return row[0].startswith("A")

    - salary threshold
    return float(row[2]) > 50000

    """

    # TODO: Write your filter condition
    return True   # currently keeps all rows


def main():
    base_dir = Path(__file__).resolve().parent

    input_file = base_dir / "sample_data.csv"
    output_file = base_dir / "filtered_output.csv"

    filtered_rows = []

    # Read CSV
    with open(input_file, mode="r") as file:
        reader = csv.reader(file)

        header = next(reader)
        filtered_rows.append(header)

        for row in reader:
            if row_filter(row):
                filtered_rows.append(row)

    # Write CSV
    with open(output_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(filtered_rows)

    print("CSV processing complete!")


if __name__ == "__main__":
    main()
