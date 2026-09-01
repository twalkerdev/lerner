"""Tests for the CLI module and file command behavior."""

import sys

from lernerpy.cli import main as cli_main
from lernerpy.commands.files import main as files_main


def test_files_list_command_lists_directory_contents(tmp_path, capsys):
    """Listing a directory should print each file name."""
    (tmp_path / "alpha.txt").write_text("alpha")
    (tmp_path / "beta.txt").write_text("beta")

    files_main(["--list", str(tmp_path)])

    output = capsys.readouterr().out.splitlines()
    assert "alpha.txt" in output
    assert "beta.txt" in output


def test_files_make_dir_creates_directory(tmp_path):
    """The mkdir option should create a directory."""
    target = tmp_path / "new_folder"

    files_main(["--mkdir", str(target)])

    assert target.exists()
    assert target.is_dir()


def test_files_touch_creates_empty_file(tmp_path):
    """The touch option should create an empty file."""
    target = tmp_path / "new_file.txt"

    files_main(["--touch", str(target)])

    assert target.exists()
    assert target.read_text() == ""


def test_cli_dispatches_files_command(tmp_path, capsys, monkeypatch):
    """The main CLI should dispatch the files command to file operations."""
    (tmp_path / "demo.txt").write_text("demo")
    monkeypatch.setattr(sys, "argv", ["lern", "files", "--list", str(tmp_path)])

    result = cli_main()

    assert result == 0
    output = capsys.readouterr().out.splitlines()
    assert "demo.txt" in output


def test_cli_reports_unknown_command(capsys, monkeypatch):
    """Unknown commands should print a clear message."""
    monkeypatch.setattr(sys, "argv", ["lern", "not-a-command"])

    result = cli_main()

    assert result == 1
    output = capsys.readouterr().out
    assert "Unknown command: not-a-command" in output
