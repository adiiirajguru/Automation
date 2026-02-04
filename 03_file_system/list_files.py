from pathlib import Path

def main():
    base_dir = Path(__file__).resolve().parent
    target_dir = base_dir / "demo_folder"

    print("Only .txt files (using glob):\n")

    for file in target_dir.glob("*.txt"):
        print(file.name)

if __name__ == "__main__":
    main()
