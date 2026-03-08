# Ghost: GitHub Observer of Silly Things

A simple command-line interface (CLI) tool to fetch and display the recent activity of a GitHub user, also known as the "GitHub User Activity CLI".

This project was built following the specifications from roadmap.sh.

## Features

- 🐍 Written entirely in Python.
- 📦 **Zero dependencies**: uses only standard libraries (`urllib`, `json`, `sys`).
- 🛡️ Robust error handling (User not found, Rate Limit, Connection errors).
- 🎨 Formatted output for easy reading.

## Requirements

- Python 3.x installed.

## Usage

Run the script passing the GitHub username as an argument:

```bash
python main.py <username>
```

### Example

```bash
python main.py torvalds
```

Output:

```text
Searching activities for user: torvalds
Pushed 2 commits to torvalds/linux
Starred facebook/react
Opened a new issue in microsoft/vscode
Created repository my-new-project
```
