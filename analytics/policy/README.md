# Policy Evaluation Module

## Description

To determine illegal rental listings on Airbnb, it is important to make sure business registry for each listing is validated. A system composed of policies and rules needs to be set up to effectively handle a large number of listings. 

## Package Management

This package uses [Poetry](https://python-poetry.org/) to manage dependencies and
isolated [Python virtual environments](https://docs.python.org/3/library/venv.html).

To proceed,
[install Poetry globally](https://python-poetry.org/docs/#installation)
onto your system.

### Dependencies

Dependencies are defined in [`pyproject.toml`](./pyproject.toml) and specific versions are locked
into [`poetry.lock`](./poetry.lock). This allows for exact reproducible environments across
all machines that use the project, both during development and in production.

To install all dependencies into an isolated virtual environment:

> Append `--sync` to uninstall dependencies that are no longer in use from the virtual environment.

```bash
$ poetry install
```

To [activate](https://python-poetry.org/docs/basic-usage#activating-the-virtual-environment) the
virtual environment that is automatically created by Poetry:

```bash
$ poetry shell
```

To deactivate the environment:

```bash
$ exit
```

To upgrade all dependencies to their latest versions:

```bash
$ poetry update
```

To add dependency:

```bash
$ poetry add <dependency_name>
```

To add development dependency:
```bash
$ poetry add -G dev <dependency_name>
```

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

## Project Structure

This module will be structured based on
https://www.cosmicpython.com/book/appendix_project_structure.html
