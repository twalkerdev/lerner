import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

DATA_DIR = Path(".lernerpy")
DATA_FILE = DATA_DIR / "tasks.json"


def ensure_data_dir():
    """Ensure the data directory exists."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)


def load_tasks():
    """Load tasks from the JSON file."""
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks):
    """Save tasks to the JSON file."""
    ensure_data_dir()
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4)


def add_task(title, description="", priority="medium", due_date=None):
    """Add a new task to the task list."""
    # Placeholder for adding a task to a data store
    tasks = load_tasks()
    task = {
        "title": title,
        "description": description,
        "priority": priority,
        "due_date": due_date,
        "status": "open",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "completed_at": None,
    }

    tasks.append(task)
    save_tasks(tasks)
    print(f"Task: '{title}' added with added")


"""
# list tasks
lern tasks list
# mark task done
lern tasks done 1
# delete task
lern tasks delete 1
# filter by status or priority
lern tasks list --status open
lern tasks list --priority high
# save/load tasks from disk 
"""


def main(argv=None):
    """Parse and execute task management commands."""
    parser = argparse.ArgumentParser(
        prog="lern tasks",
        description="Manage tasks: add, list, mark done, delete.",
        epilog="Use lern tasks list --help",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a task")
    add_parser.add_argument("--title", required=True, help="Title of the task")
    add_parser.add_argument(
        "--description", default="", help="Optional task description"
    )
    add_parser.add_argument(
        "--priority",
        choices=["low", "medium", "high"],
        default="medium",
        help="Task priority",
    )
    add_parser.add_argument("--due-date", dest="due_date", help="Optional due date")

    args = parser.parse_args(argv)

    if args.command == "add":
        add_task(args.title, args.description, args.priority, args.due_date)
        return 0

    parser.error(f"Unknown command: {args.command}")
    return 1


"""
optional features:
- priority filtering
- due date filtering
- search by title or description
- show "open tasks only" by default
"""

if __name__ == "__main__":
    raise SystemExit(main())
