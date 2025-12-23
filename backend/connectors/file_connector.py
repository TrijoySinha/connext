from pathlib import Path
import os

BASE_SEARCH_DIRS = [
    Path.home() / "Downloads",
    Path.home() / "Documents",
    Path.home() / "Desktop",
]

def search_file(user_input: str):
    keywords = user_input.lower().split()
    matches = []

    for base_dir in BASE_SEARCH_DIRS:
        if not base_dir.exists():
            continue

        for root, _, files in os.walk(base_dir):
            for file in files:
                filename = file.lower()
                if any(word in filename for word in keywords):
                    matches.append(os.path.join(root, file))

            if len(matches) >= 5:
                return matches

    return "No matching files found."

def latest_file():
    latest = None
    latest_time = 0

    for base_dir in BASE_SEARCH_DIRS:
        if not base_dir.exists():
            continue

        for root, _, files in os.walk(base_dir):
            for file in files:
                path = os.path.join(root, file)
                try:
                    mtime = os.path.getmtime(path)
                    if mtime > latest_time:
                        latest_time = mtime
                        latest = path
                except:
                    continue

    return latest or "No files found."