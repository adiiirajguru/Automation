import csv
from pathlib import Path


def main():
    # Locate folder
    base_dir = Path(__file__).resolve().parent
    csv_file = base_dir / "sample_data.csv"

    # Data to write
    data = [
        ["Name", "Age", "City"],
        ["Aditya", 22, "Indore"],
        ["Ravi", 25, "Delhi"],
        ["Sneha", 23, "Mumbai"]
    ]

    # Write CSV
    with open(csv_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print("✅ CSV file written successfully!")


if __name__ == "__main__":
    main()
