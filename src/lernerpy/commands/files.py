"""File-management commands for lernerpy."""

import argparse
import shutil
from pathlib import Path


def list_dir(path):
    """List the contents of a directory."""
    target = Path(path)
    if not target.exists():
        raise FileNotFoundError(f"Path does not exist: {path}")
    for entry in sorted(target.iterdir(), key=lambda p: p.name):
        print(entry.name)


def make_dir(path):
    """Create a directory and any missing parent folders."""
    target = Path(path)
    target.mkdir(parents=True, exist_ok=True)
    print(f"Created directory: {target}")


def touch_file(path):
    """Create an empty file if it does not already exist."""
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.touch(exist_ok=True)
    print(f"Created file: {target}")


def remove_path(path):
    """Remove a file or directory."""
    target = Path(path)
    if not target.exists():
        raise FileNotFoundError(f"Path does not exist: {path}")

    if target.is_dir():
        shutil.rmtree(target)
        print(f"Removed directory: {target}")
    else:
        target.unlink()
        print(f"Removed file: {target}")


def main(argv=None):
    """Parse and execute file-management commands."""
    parser = argparse.ArgumentParser(
        prog="lernerpy files",
        description="List, create, and remove files.",
    )
    parser.add_argument("path", nargs="?", default=".", help="Path to operate on")
    parser.add_argument("--list", action="store_true", help="List files in the directory")
    parser.add_argument("--mkdir", metavar="DIR", help="Create a new directory")
    parser.add_argument("--touch", metavar="FILE", help="Create an empty file")
    parser.add_argument("--remove", metavar="PATH", help="Remove a file or directory")

    args = parser.parse_args(argv)

    if args.mkdir:
        make_dir(args.mkdir)
        return 0

    if args.touch:
        touch_file(args.touch)
        return 0

    if args.remove:
        remove_path(args.remove)
        return 0

    if args.list or not any([args.mkdir, args.touch, args.remove]):
        list_dir(args.path)
        return 0

    return 0


if __name__ == "__main__":
    raise SystemExit(main())