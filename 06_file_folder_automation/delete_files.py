from pathlib import Path

def main():
    sandbox_dir = Path(__file__).resolve().parent / "sandbox"
    doc_folder = sandbox_dir / "Documents"

    # Delete all .txt files
    for file in doc_folder.glob("*.txt"):
        if file.is_file():
            print(f"Deleting: {file.name}")
            file.unlink()  # safely deletes file

if __name__ == "__main__":
    main()
