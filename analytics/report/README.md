# README about reporting module

## Getting Started

Make sure you have [Python 3.10](https://www.python.org/downloads/release/python-3100/) installed on your system.

This project uses [Poetry](https://python-poetry.org/) for virtual environment creation and dependency management.

## Installation

[Install Poetry](https://python-poetry.org/docs/#installing-with-pipx) globally on your system.

```bash
# Clone the repository
git clone https://github.com/OpenBCca/airbnb-regulation.git

# Navigate to the project directory
cd analytics\report

# Install dependencies using Poetry
poetry install

```

## Usage

Start the virtual environment with the following command:

```bash
poetry shell
```

To exit the virtual environment, use this command:

```bash
exit
```

## Dependencies

Dependencies are defined in `pyproject.toml` and specific versions are locked into `poetry.lock`. This allows for exact reproducible environments across all machines that use the project, both during development and in production.

```bash
# Upgrade all dependencies to their latest versions
poetry update

# Add a dependency
poetry add <dependency_name>

# Add a development dependency
poetry add -D <dependency_name>
```

## Project Structure

All the source code is located in the src/ directory.

Test files are located in the project root in the tests folder.

## Unit Testing

Unit testing is performed with [pytest](https://pytest.org/).

pytest will automatically discover and run tests by recursively searching for folders and `.py`
files prefixed with `test` for any functions prefixed by `test`.

The `tests` folder is created as a Python package (i.e. there is an `__init__.py` file within it)
because this helps `pytest` uniquely namespace the test files. Without this, two test files cannot
be named the same, even if they are in different subdirectories.

## Code Coverage

Code coverage is performed with [coverage](https://coverage.readthedocs.io/), which measures test coverage of Python programs.

## Code Style Checking

[PEP 8](https://peps.python.org/pep-0008/) is the universally accepted style guide for Python
code. PEP 8 code compliance is verified using [Ruff][Ruff].

Ruff is configured in the
`[tool.ruff]` section of [`pyproject.toml`](./pyproject.toml).

[Ruff]: https://github.com/astral-sh/ruff

## Automated Code Formatting

[Ruff][Ruff] is used to automatically format code and group and sort imports.

## Type checking

[Type annotations](https://docs.python.org/3/library/typing.html) allows developers to include
optional static typing information to Python source code. [mypy](http://mypy-lang.org/) is used as static analyzer.

mypy is configured in the
`[tool.mypy]` section of [`pyproject.toml`](./pyproject.toml).
