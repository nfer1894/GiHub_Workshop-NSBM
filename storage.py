import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    """Load tasks from the JSON file. Returns an empty list if file doesn't exist."""
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    """Save the current list of tasks to the JSON file."""
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=2)