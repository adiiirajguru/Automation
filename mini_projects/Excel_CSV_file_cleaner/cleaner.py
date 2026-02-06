import pandas as pd
from pathlib import Path

#Function to scan the file for file type
def scan_file_type(input_dir):
    #scan input file to get the correct file type
    # CSV or Excel_CSV_file_cleaner
    for file in input_dir.iterdir():
        if file.suffix.lower() ==".csv":
            print(f"CSV file founded: {file.name}")
            df = pd.read_csv(file)
            return df, file.name
        elif file.suffix.lower() == ".xlsx":
            print(f"Excel_CSV_file_cleaner file founded: {file.name}")
            df = pd.read_excel(file)
            return df, file.name
        return None, None

#Function to clean the file.
#Removes duplicate values, strip whitespace, numeric conversion, remove missing values row
def clean_data(df):

    print("\n Cleaning data...")

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Strip whitespace from text columns
    for col in df.select_dtypes(include=["object", "string"]):
        df[col] = df[col].astype(str).str.strip()

        # Try numeric conversion safely
        converted = pd.to_numeric(df[col], errors="coerce")

        # Only replace column if conversion makes sense
        if converted.notna().sum() > 0:
            df[col] = converted

    # Remove rows with missing values
    df = df.dropna()

    print("Cleaning complete!")

    return df

#Saves the cleaned file
def save_clean_file(df, filename, output_dir):

    output_name = f"cleaned_{filename}"
    output_path = output_dir / output_name

    if filename.lower().endswith(".csv"):
        df.to_csv(output_path, index=False)

    elif filename.lower().endswith(".xlsx"):
        df.to_excel(output_path, index=False)

    print(f"\n Clean file saved to: {output_path.name}")




def main():
    base_dir = Path(__file__).resolve().parent
    input_dir = base_dir / "input"
    output_dir = base_dir / "output"

    print("Scaning input file....")

    #Load file
    df, filename = scan_file_type(input_dir) #using function we made

    if df is None:
        print("No Excel_CSV_file_cleaner or CSV file found in input folder")
        return
    print(f"Loaded file: {filename}")
    print(f"Rows loaded: {len(df)}")

    print("\nPreview:")
    print(df.head())

    df = clean_data(df)
    print(f"\n CLean rows remaining: {len(df)}")
    print(df.head())

    save_clean_file(df, filename, output_dir)

if __name__ == "__main__":
    main()


