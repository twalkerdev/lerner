# LernerPy

A lightweight Python CLI application that accepts user input and executes it as shell commands.

## Installation

### Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install the package in development mode:
```bash
pip install -e ".[dev]"
```

## Usage

Run the CLI:
```bash
lern
```

Or directly with Python:
```bash
python -m lernerpy.cli
```

Then type commands at the prompt:
```
$ ls
$ echo "hello"
$ date
$ exit  # or quit
```

## Development

### Run tests:
```bash
pip install pytest
pytest
```

### Project Structure
```
lernerpy/
├── src/lernerpy/        # Main package
│   ├── cli.py           # Entry point
│   └── utils/           # Utility modules
├── tests/               # Test files
├── pyproject.toml       # Project configuration
├── README.md            # Project docs
└── LEARNING_PROJECTS.md # Optional learning notes
```

## Requirements

- Python 3.8+
