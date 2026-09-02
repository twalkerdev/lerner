import argparse


def add_task(title, description="", priority="medium", due_date=None):
    """Add a new task to the task list."""
    # Placeholder for adding a task to a data store
    print(f"Task: '{title}' added")


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

"""
data model object
id: int
title: str
description: str or empty
status: str (open, done)
priority: str (low, medium, high)
due_date: str or empty
created_at: str (timestamp)
completed_at: str or empty (timestamp)
"""

"""
optional features:
- priority filtering
- due date filtering
- search by title or description
- show "open tasks only" by default
"""

if __name__ == "__main__":
    raise SystemExit(main())
