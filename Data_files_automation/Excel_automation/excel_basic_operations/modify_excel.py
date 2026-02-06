from openpyxl import load_workbook
from pathlib import Path


def main():
    base_dir = Path(__file__).resolve().parent
    excel_file = base_dir / "employees.xlsx"

    wb = load_workbook(excel_file)
    sheet = wb["Employees"]

    sheet["B2"] = 24  # modify age

    wb.save(excel_file)

    print(" Excel_CSV_file_cleaner updated!")


if __name__ == "__main__":
    main()
