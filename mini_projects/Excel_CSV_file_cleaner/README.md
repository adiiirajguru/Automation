# 📊 Excel Data Cleaner — Python Automation Tool

## 🚀 Overview

Excel Data Cleaner is a Python automation tool that processes messy CSV or Excel files and outputs a clean, structured dataset.

It automatically removes duplicates, fixes formatting issues, handles missing values, and standardizes data — simulating real-world business data cleaning workflows.

This project demonstrates how Python and pandas can automate repetitive spreadsheet cleanup tasks commonly required in analytics, reporting, and data preprocessing.

---

## 🎯 What This Tool Does

The cleaner performs automated data processing:

✅ Detects CSV or Excel input files
✅ Removes duplicate rows
✅ Trims extra whitespace in text
✅ Converts numeric fields
✅ Removes invalid or incomplete records
✅ Outputs a clean file automatically

---

## 📂 Project Structure

```
excel_data_cleaner/
│
├── input/        → Place messy CSV/Excel files here
├── output/       → Cleaned files are saved here
├── cleaner.py    → Automation script
└── README.md
```

---

## ⚙️ How It Works

Workflow pipeline:

```
Raw file → Detection → Cleaning → Export clean file
```

1. Script scans the `input` folder
2. Detects CSV or Excel file
3. Loads data using pandas
4. Cleans the dataset automatically
5. Saves cleaned file to `output`

---

## ▶ How to Use

### Step 1 — Install dependencies

```
pip install pandas openpyxl
```

---

### Step 2 — Add a messy file

Place any CSV or Excel file inside:

```
input/
```

Example:

```
input/employees.xlsx
```

---

### Step 3 — Run the cleaner

```
python cleaner.py
```

---

### Step 4 — Get cleaned output

Cleaned file will appear in:

```
output/
```

Example:

```
output/cleaned_employees.xlsx
```

---

## 🧠 Example Use Cases

* Cleaning HR spreadsheets
* Preparing datasets for analysis
* Removing duplicate business records
* Preprocessing data for ML pipelines
* Automating report cleanup

---

## 🛠 Technologies Used

* Python 3
* pandas (data processing)
* openpyxl (Excel handling)
* pathlib (file management)

---

## 💡 Key Concepts Demonstrated

* Automated file detection
* Data cleaning pipelines
* CSV & Excel automation
* Reusable script architecture
