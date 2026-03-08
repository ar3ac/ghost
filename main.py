import sys
import urllib.request


def fetch_github_events(username):
    url = f"https://api.github.com/users/{username}/events"
    with urllib.request.urlopen(url) as response:
        return response.read().decode("utf-8")


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <username>")
        sys.exit(1)

    username = sys.argv[1]
    print(f"Searching activities for user: {username}")

    events = fetch_github_events(username)
    print(f"Events for {username}:\n{events}")


if __name__ == "__main__":
    main()
