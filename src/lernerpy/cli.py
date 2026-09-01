#!/usr/bin/env python3
"""Command-line entry point for lernerpy."""

import sys

from lernerpy.commands.files import main as files_main

def main(argv=None):
    """Dispatch to the appropriate subcommand."""
    args = sys.argv[1:] if argv is None else argv

    if not args:
        print("Usage: lerner <command> [options]")
        return 1

    command = args[0]

    if command == "files":
        return files_main(args[1:])

    print(f"Unknown command: {command}")
    print("Available commands: files")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
