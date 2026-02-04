'''

from pathlib import Path

def main():
    base_dir = Path(__file__).resolve().parent
    file_path = base_dir / "output.txt"

    with open(file_path, "r") as file:
        content = file.read()

    print("Full file content:")
    print(content)

if __name__ == "__main__":
    main()
'''
#to read line by line
'''
from pathlib import Path

def main():
    base_dir = Path(__file__).resolve().parent
    file_path = base_dir / "output.txt"

    with open(file_path, "r") as file:
        for line in file:
            print(line.strip())

if __name__ == "__main__":
    main()
'''
#to read lines into list
from pathlib import Path

def main():
    base_dir = Path(__file__).resolve().parent
    file_path = base_dir / "output.txt"

    with open(file_path, "r") as file:
        lines = file.readlines()

    print(lines)

if __name__ == "__main__":
    main()
