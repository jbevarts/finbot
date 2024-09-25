# finbot
financial advice chatbot


## Project Overview
Includes following development tools:
* `ruff`: identifies many errors and style issues (`flake8`, `isort`, `pyupgrade`)
* `black`: auto-formats code

Those checks are run as pre-commit hooks using the `pre-commit` library.

Includes `pytest` for testing plus the `pytest-cov` plugin to measure coverage.

The checks and tests are all run using Github actions on every pull request and merge to main.

This repository is setup for Python 3.12. To change the version:
1. Change the `image` argument in `.devcontainer/devcontainer.json` (see [https://github.com/devcontainers/images/tree/main/src/python](https://github.com/devcontainers/images/tree/main/src/python#configuration) for a list of pre-built Docker images)
1. Change the config options in `.precommit-config.yaml`
1. Change the version number in `.github/workflows/python.yaml`

## Development instructions

## With devcontainer

This repository comes with a devcontainer (a Dockerized Python environment). If you open it in Codespaces, it should automatically initialize the devcontainer.

Locally, you can open it in VS Code with the Dev Containers extension installed.

## Without devcontainer

If you can't or don't want to use the devcontainer, then you should first create a virtual environment:

```
python3 -m venv .venv
source .venv/bin/activate
```

Then install the dev tools and pre-commit hooks:

```
python3 -m pip install -r requirements-dev.txt
pre-commit install
```

## Testing

When you're ready to run tests, run:

```
python3 -m pytest
```

# File breakdown
* `.devcontainer`: Folder containing files used for setting up a devcontainer
  * `devcontainer.json`: File configuring the devcontainer, includes VS Code settings
* `.github`: Folder for Github-specific files and folders
  * `workflows`: Folder containing Github actions config files
    * `python.yaml`: File configuring Github action that runs tools and tests
* `tests`: Folder containing Python tests
  * `main_test.py`: File with pytest-style tests of main.py
* `.gitignore`: File describing what file patterns Git should never track
* `.pre-commit-config.yaml`: File listing all the pre-commit hooks and args
* `main.py`: The main (and currently only) Python file for the program
* `pyproject.toml`: File configuring most of the Python dev tools
* `README.md`: You're reading it!
* `requirements-dev.txt`: File listing all PyPi packages required for development
* `requirements.txt`: File listing all PyPi packages required for production
