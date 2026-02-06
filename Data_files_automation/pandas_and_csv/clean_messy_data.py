import pandas as pd
from pathlib import Path


def main():
    base_dir = Path(__file__).resolve().parent
    input_file = base_dir / "messy_data.xlsx"
    output_file = base_dir / "clean_data.xlsx"

    df = pd.read_excel(input_file)

    print("Original data:\n", df)

    # ---------- CLEANING ----------

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Strip extra spaces in text columns
    df["Name"] = df["Name"].str.strip()
    df["City"] = df["City"].str.strip()

    # Convert age to numeric
    df["Age"] = pd.to_numeric(df["Age"], errors="coerce")

    # Remove invalid ages
    df = df[df["Age"] > 0]

    # Handle missing values
    df = df.dropna()

    # Rename columns (optional formatting)
    df.columns = df.columns.str.lower()

    print("\nCleaned data:\n", df)

    # ---------- EXPORT ----------
    df.to_excel(output_file, index=False)

    print("\n Clean Excel saved!")


if __name__ == "__main__":
    main()
