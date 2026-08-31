"""Method to list, mkdir, touch, and remove files"""

import argparse
from pathlib import Path

def list_dir(path):
    """List the contents of a directory."""
    for entry in Path(path).iterdir():
        print(entry.name)

def main(argv=None):
    parser = argparse.ArgumentParser(prog="lernerpy files", description="List, create, and remove files.")
    parser.add_argument("--list", action="store_true", help="List files in the directory")
    parser.add_argument("--mkdir", metavar="DIR", help="Create a new directory" )
    parser.add_argument("path", nargs="?", default=".", help="Path to the directory (default: current directory)")

    args = parser.parse_args(argv)

    if args.list:
        list_dir(args.path)

if __name__ == "__main__":
    main()