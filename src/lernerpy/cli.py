#!/usr/bin/env python3
"""Simple command-line script that accepts input and executes it as a command."""

from lernerpy.commands.files import main as files
import sys

def main():
    """Main function to exectute the command passed as arguments."""
    if len(sys.argv) < 2:
        print("Usage: lern <command>")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "files":
        files(sys.argv[2:])
    else:
        print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()
