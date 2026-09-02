"""Command-line entry point for lern."""

import sys

from lernerpy.commands.files import main as files_main
from lernerpy.commands.tasks import main as tasks_main


def main(argv=None):
    """Dispatch to the appropriate subcommand."""
    args = sys.argv[1:] if argv is None else argv

    if not args:
        print("Usage: lern <command> [options]")
        return 1

    command = args[0]

    if command == "files":
        return files_main(args[1:])

    if command == "tasks":
        return tasks_main(args[1:])

    print(f"Unknown command: {command}")
    print("Available commands: files, tasks")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
