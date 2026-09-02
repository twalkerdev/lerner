"""Tests for the CLI module and tasks command behavior."""

import sys

from lernerpy.cli import main as cli_main
from lernerpy.commands.tasks import main as tasks_main


def test_tasks_add_command_creates_task(capsys):
    """The add command should create a new task."""
    task_name = "Test Task"
    tasks_main(["add", task_name])

    output = capsys.readouterr().out
    assert f"Task: '{task_name}' added" in output
