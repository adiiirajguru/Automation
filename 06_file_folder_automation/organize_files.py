from pathlib import Path
import shutil

def main():
    base_dir = Path(__file__).resolve().parent
    sandbox_dir = base_dir / "sandbox"

    for item in sandbox_dir.iterdir():
        if item.is_file():
            if item.suffix in [".jpg", ".png"]:
                shutil.move(str(item), str(sandbox_dir / "Images" / item.name))

            elif item.suffix in [".pdf", ".docx", ".txt"]:
                shutil.move(str(item), str(sandbox_dir / "Documents" / item.name))

            else:
                shutil.move(str(item), str(sandbox_dir / "Others" / item.name))

if __name__ == "__main__":
    main()
