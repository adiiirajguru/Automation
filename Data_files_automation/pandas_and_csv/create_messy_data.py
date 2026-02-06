import pandas as pd
from pathlib import Path


def main():
    base_dir = Path(__file__).resolve().parent
    file_path = base_dir / "messy_data.xlsx"

    data = {
        "Name": [" Aditya ", "Priya", "Rahul", "Priya", None],
        "Age": [23, "25", -5, "25", None],
        "City": ["Indore", " Bangalore ", "Pune", " Bangalore ", ""]
    }

    df = pd.DataFrame(data)
    df.to_excel(file_path, index=False)

    print("Messy Excel_CSV_file_cleaner created!")


if __name__ == "__main__":
    main()
