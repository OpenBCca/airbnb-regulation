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