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


def test_cli_dispatches_files_command(tmp_path, capsys, monkeypatch):
    """The main CLI should dispatch the files command to file operations."""
    (tmp_path / "demo.txt").write_text("demo")
    monkeypatch.setattr(sys, "argv", ["lernerpy", "files", "--list", str(tmp_path)])

    cli_main()

    output = capsys.readouterr().out.splitlines()
    assert "demo.txt" in output


def test_cli_reports_unknown_command(capsys, monkeypatch):
    """Unknown commands should print a clear message."""
    monkeypatch.setattr(sys, "argv", ["lernerpy", "not-a-command"])

    cli_main()

    output = capsys.readouterr().out
    assert "Unknown command: not-a-command" in output
