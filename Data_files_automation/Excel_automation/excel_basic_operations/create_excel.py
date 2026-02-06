from openpyxl import Workbook
from pathlib import Path


def main():
    base_dir = Path(__file__).resolve().parent
    excel_file = base_dir / "employees.xlsx"

    wb = Workbook()
    sheet = wb.active
    sheet.title = "Employees"

    wb.save(excel_file)

    print("Excel_CSV_file_cleaner file created!")


if __name__ == "__main__":
    main()
