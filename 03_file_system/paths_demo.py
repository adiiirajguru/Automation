from pathlib import Path

def main():
    print("Current working directory:")
    print(Path.cwd())

    print("\nScript location:")
    print(Path(__file__).resolve())

    print("\nScript directory:")
    print(Path(__file__).resolve().parent)

if __name__ == "__main__":
    main()
