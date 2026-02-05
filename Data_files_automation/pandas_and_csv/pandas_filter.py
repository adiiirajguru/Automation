import pandas as pd
from pathlib import Path


def main():
    base_dir = Path(__file__).resolve().parent

    input_file = base_dir.parent / "csv_basics" / "sample_data.csv"
    output_file = base_dir / "pandas_filtered.csv"

    # Load CSV
    df = pd.read_csv(input_file)

    print("Original Data:")
    print(df)

    # Filter data
    filtered_df = df[df["Age"] >= 23]

    # Add new column (automation transformation)
    filtered_df["age_group"] = "Adult"

    # Save result
    filtered_df.to_csv(output_file, index=False)

    print("\n Pandas filtering complete!")


if __name__ == "__main__":
    main()
