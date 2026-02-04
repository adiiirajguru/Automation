from pathlib import Path

def main():
    sandbox_dir = Path(__file__).resolve().parent / "sandbox"

    # Renaming images with prefix IMG_
    image_folder = sandbox_dir / "Images"
    for i, file in enumerate(image_folder.iterdir(), start=1):
        if file.is_file() and file.suffix in [".jpg", ".png"]:
            new_name = f"IMG_{i:03}{file.suffix}"  # IMG_001.jpg
            new_path = image_folder / new_name
            if not new_path.exists():
                file.rename(new_path)

    # Renaming documents with prefix DOC_
    doc_folder = sandbox_dir / "Documents"
    for file in doc_folder.iterdir():
        if file.is_file():
            new_name = f"DOC_{file.name}"
            new_path = doc_folder / new_name
            if not new_path.exists():
                file.rename(new_path)

if __name__ == "__main__":
    main()
