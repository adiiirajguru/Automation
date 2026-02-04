from pathlib import Path

def main():
    base_dir = Path(__file__).resolve().parent
    sandbox_dir = base_dir / "sandbox"

    # Create folders
    folders = ["Images", "Documents", "Others"]

    for folder in folders:
        folder_path = sandbox_dir / folder
        folder_path.mkdir(exist_ok=True)

    # Create files
    files = [
        "photo1.jpg",
        "photo2.png",
        "resume.docx",
        "notes.txt",
        "report.pdf"
    ]

    for file_name in files:
        file_path = sandbox_dir / file_name
        if not file_path.exists():
            file_path.touch()

if __name__ == "__main__":
    main()
