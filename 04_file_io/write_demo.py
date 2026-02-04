from pathlib import Path

def main():
    base_dir = Path(__file__).resolve().parent
    output_file = base_dir / "output.txt"

    with open(output_file, "a") as file:
        file.write("Second Automation started\n")
        file.write("Writing Second output\n")

    print("Data written successfully")

if __name__ == "__main__":
    main()
