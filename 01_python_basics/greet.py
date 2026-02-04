import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python greet.py <name>")
        return

    name = sys.argv[1]
    print(f"Hello, {name}!")

if __name__ == "__main__":
    main()
