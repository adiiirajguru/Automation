# smart_file_organizer.py
from pathlib import Path
import shutil

def main():
    # Set the folder to organize
    sandbox_dir = Path(__file__).resolve().parent / "sandbox"
    sandbox_dir.mkdir(exist_ok=True)  # create sandbox if not exists

    # Create subfolders for organization
    folders = ["Images", "Documents", "Others"]
    for folder in folders:
        (sandbox_dir / folder).mkdir(exist_ok=True)

    # Scan and organize files
    for file in sandbox_dir.iterdir():
        if file.is_file():
            # Decide destination folder by file type
            if file.suffix.lower() in [".jpg", ".png", ".jpeg", ".gif"]:
                dest = sandbox_dir / "Images" / file.name
            elif file.suffix.lower() in [".pdf", ".docx", ".txt"]:
                dest = sandbox_dir / "Documents" / file.name
            else:
                dest = sandbox_dir / "Others" / file.name

            # Handle duplicates
            counter = 1
            original_dest = dest
            while dest.exists():
                dest = original_dest.with_name(f"{original_dest.stem}_{counter}{original_dest.suffix}")
                counter += 1

            # Move the file
            shutil.move(str(file), str(dest))
            print(f"Moved: {file.name} -> {dest.name}")

    print("\n Folder organization complete!")

#  Standard Python main guard
if __name__ == "__main__":
    main()
