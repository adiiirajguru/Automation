# Smart File Organizer

## 📌 Project Description
The **Smart File Organizer** is a Python-based automation script that scans a directory and automatically organizes files into folders based on their type.  
It handles duplicates safely and can be reused to clean up any messy folder, such as your **Downloads** or **Project directories**.  

This mini project demonstrates mastery of **file system automation** and Python scripting using **pathlib** and **shutil**.

---

## 💡 Features
- Scans a directory (`sandbox/`) and identifies all files
- Automatically organizes files into:
  - `Images` → `.jpg`, `.png`, `.jpeg`, `.gif`
  - `Documents` → `.pdf`, `.docx`, `.txt`
  - `Others` → all other file types
- Handles duplicate files by adding a number suffix (`_1`, `_2`, etc.)
- Safe: only operates inside the `sandbox` folder
- Provides clear feedback for each file moved

---

## 🛠 Technologies Used
- Python 3.x
- Libraries:
  - `pathlib` → for safe, cross-platform path and folder handling
  - `shutil` → for moving files safely
- Concepts used:
  - Loops and conditionals for bulk operations
  - Safe file handling and idempotent operations
  - Duplicate file handling
  - Pattern-based organization

---

## 📁 Folder Structure
mini_projects/
└── smart_file_organizer/
├── sandbox/ # Test folder, place your messy files here
├──file_organizer.py # Main Python script
└── README.md # Project documentation


---

## 🚀 How to Use
1. **Prepare your sandbox folder**  
   - Place all files you want to organize inside the `sandbox/` folder  
   - Example: `Downloads/photo.jpg`, `Downloads/resume.docx`, `Downloads/misc.xyz`

2. **Run the script**  
   - Open `smart_file_organizer.py` in PyCharm or any Python IDE  
   - Run the script (`Shift+F10` in PyCharm or `python smart_file_organizer.py` in terminal)

3. **Check organized folders**  
   - After running, `sandbox/` will contain subfolders:
     - `Images` → all image files
     - `Documents` → all document files
     - `Others` → all other files
   - Duplicate files will be automatically renamed with `_1`, `_2`, etc.

4. **Add more files**  
   - You can keep adding files to the sandbox folder and rerun the script  
   - The script is **idempotent** – it won’t overwrite existing files

---