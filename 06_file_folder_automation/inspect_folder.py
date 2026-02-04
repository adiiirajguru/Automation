from pathlib import Path

def main():
    base_dir = Path(__file__).resolve().parent
    sandbox_dir = base_dir / "sandbox"

    print("Inspecting folder:", sandbox_dir)
    print("\nContents:\n")

    for item in sandbox_dir.iterdir():
        if item.is_file():
            print(f"FILE  -> {item.name}")
        elif item.is_dir():
            print(f"FOLDER-> {item.name}")

if __name__ == "__main__":
    main()
