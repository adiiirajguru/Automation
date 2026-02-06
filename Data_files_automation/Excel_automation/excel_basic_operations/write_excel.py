from openpyxl import load_workbook
from pathlib import Path


def main():
    base_dir = Path(__file__).resolve().parent
    excel_file = base_dir / "employees.xlsx"

    wb = load_workbook(excel_file)
    sheet = wb["Employees"]

    sheet.append(["Name", "Age", "City"])
    sheet.append(["Aditya", 23, "Indore"])
    sheet.append(["Priya", 25, "Bangalore"])

    wb.save(excel_file)

    print("Data written to Excel_CSV_file_cleaner!")


if __name__ == "__main__":
    main()
