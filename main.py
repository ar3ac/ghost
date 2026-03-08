import sys
import urllib.request
import json


def fetch_github_events(username):
    url = f"https://api.github.com/users/{username}/events"
    try:
        with urllib.request.urlopen(url) as response:
            return response.read().decode("utf-8")
    # except 404 with a custom message
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"User {username} not found.")
            sys.exit(1)
        elif e.code == 403 or e.code == 429:
            print(f"Rate limit exceeded. Please try again later.")
            sys.exit(1)
        else:
            print(f"Error fetching GitHub events for user {username}: {e}")
            sys.exit(1)
    # generic lan error handling
    except urllib.error.URLError as e:
        print(f"Error connecting to GitHub API: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <username>")
        sys.exit(1)

    username = sys.argv[1]
    print(f"Searching activities for user: {username}")

    events_str = fetch_github_events(username)
    events_list = json.loads(events_str)
    for event in events_list:
        event_type = event["type"]
        repo_name = event["repo"]["name"]

        if event_type == "PushEvent":
            commits = event["payload"].get("commits")
            if commits:
                print(f"Pushed {len(commits)} commits to {repo_name}")
            else:
                print(f"Pushed to {repo_name}")
        elif event_type == "WatchEvent":
            print(f"Starred {repo_name}")
        elif event_type == "IssuesEvent" and event["payload"]["action"] == "opened":
            print(f"Opened a new issue in {repo_name}")
        elif event_type == "CreateEvent":
            ref_type = event["payload"].get("ref_type", "item")
            if ref_type == "repository":
                print(f"Created {repo_name}")
            else:
                print(f"Created {ref_type} in {repo_name}")


if __name__ == "__main__":
    main()
