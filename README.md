# LernerPy

A lightweight Python CLI application with file-management and task-management commands.

## Installation

This project uses [uv](https://docs.astral.sh/uv/) to manage its environment and dependencies.

Install uv by following the [official installation instructions](https://docs.astral.sh/uv/getting-started/installation/), then sync the project:

```bash
uv sync
```

This creates the project environment in `.venv` and installs the development dependencies.

## Usage

Run the CLI with uv:
```bash
uv run lern
```

Or directly with Python:
```bash
uv run python -m lernerpy.cli
```

### File commands

List the contents of a directory:

```bash
uv run lern files --list .
```

### Task commands

Add a task:

```bash
uv run lern tasks add --title "Write tests" --priority high
```

Tasks are stored in `.lernerpy/tasks.json`. The `.lernerpy` directory is created automatically when the first task is saved.

## Development

### Run tests

Run the complete test suite:

```bash
uv run pytest
```

Run a specific test file:

```bash
uv run pytest tests/test_tasks.py
```

Run one test function:

```bash
uv run pytest tests/test_tasks.py::test_tasks_add_command_creates_task
```

Watch for changes and rerun tests automatically:

```bash
uv run poe test
```

Stop the watcher with `Ctrl+C`.

### Project Structure
```
lernerpy/
├── src/lernerpy/        # Main package
│   ├── cli.py           # Entry point
│   ├── commands/        # CLI command modules
│   └── data/            # Packaged data files, if needed
├── tests/               # Test files
├── .lernerpy/           # Runtime data, including tasks.json
├── pyproject.toml       # Project configuration
├── README.md            # Project docs
└── LEARNING_PROJECTS.md # Optional learning notes
```

## Requirements

- Python 3.8+
- uv
