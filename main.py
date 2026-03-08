import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <username>")
        sys.exit(1)

    username = sys.argv[1]
    print(f"Searching activities for user: {username}")


if __name__ == "__main__":
    main()
