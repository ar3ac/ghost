import sys
import urllib.request
import json


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

    events_str = fetch_github_events(username)
    events_list = json.loads(events_str)
    for event in events_list:
        print(f"Event Type: {event['type']}, Repo: {event['repo']['name']}")


if __name__ == "__main__":
    main()
