# Contributing to Malbench
Thank you for considering contributing to Malbench! This document provides guidelines and suggestions for how to contribute to Malbench.

## Code of Conduct
This project and everyone participating in it is governed by the Malbench Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to on of the Project maintainers.

## Reporting Bugs
If you encounter a bug while using Malbench, please open an issue on the [GitHub repository](https://github.com/youkergav/Malbench/issues) to let us know. Please include a clear and detailed description of the issue, as well as any relevant code or output.

## Submitting Changes
If you would like to contribute to Malbench by submitting changes, please follow these guidelines.

### Forking and Creating a Pull Request
When you create a pull request, GitHub Actions will automatically run the following checks:

1. Fork the Malbench repository on GitHub.
2. Create a new branch for your changes.
3. Ensure your code follows the guidelines and best practices outline in this document.
4. Make your changes and commit them with a clear commit messages.
5. Push your changes to your fork.
6. Open a pull request on the GitHub repository with a clear title and description of your changes.

### Guidelines for a Pull Request
When you create a pull request, the following checks will be ran:
- **Linting and Formatting**: This ensures that code changes conform to our coding style and best practices, including formatting, linting, and type checking. If formatting changes are made to the code, a commit will automatically be created.
- **Unit Testing**: This action runs tests to ensure that the changes you've made do not break existing functionality. Additionally, a coverage report will run after to ensure the project is at or above 80% code coverage.
- **Documenting**: This generates documentation for the code changes you've made and ensures that documentation is up-to-date. If changes are made to documentation, a commit will automatically be created.
- **Vulnerability Checking**: This will check for known security vulnerabilities in our dependencies.
- **Manual Review**: A manual review from a code maintainer will be done.

*For more detailed information on guidelines, see the [Developer Workflow](#developer-workflow) section.*

## Installation
If you are a developer who wants to contribute to Malbench or modify the source code, you will need to follow these installation steps:

1.  Ensure the following is installed on your system: [Python 3.8.1+](https://www.python.org/downloads/), [PIP](https://pypi.org/project/pip/) (included with most Python installations), [Git](https://git-scm.com/downloads), [Poetry](https://python-poetry.org/docs/), and an IDE of your choice ([VSCode](https://code.visualstudio.com/download) recommended).
2.  Clone (or fork) the Malbench repository using Git:
    ```bash
    git clone https://github.com/youkergav/Malbench.git
    ```
3.  Navigate to the project directory:
    ```bash
    cd malbench
    ```
4.  Install the required dependencies using Poetry:
    ```bash
    poetry install
    ```
    *Note: Please ensure the your PATH is configured for poetry*
5. Launch the virtual environment using one of the following methods:
    - For general use, the virtual environment can be opened with:
      ```
      poetry shell
      ```
    - Alternatively, the virtual environment can be opened in VSCode. First ensure the [Python extension for VSCode](https://marketplace.visualstudio.com/items?itemName=ms-python.python) is installed. Then, open the `Malbench` folder in VSCode and ensure the Python interpreter is set to use the local poetry `.venv` (you may need to reload VSCode after this).

## Developer Operations
### General Coding Practices
We follow the Pythonic coding style, which emphasizes readability and simplicity of code. This includes using whitespace for indentation, using descriptive variable names, and following the PEP 8 style guide.

We also use class-based programming, which allows for encapsulation and reusability of code. Our code is organized into modules, which are files containing related functionality that can be imported into other files. This helps keep the codebase organized and makes it easier to maintain and extend the functionality.

### File Structure
The file structure can be seen as the following:
```yaml
Malbench/                    # Root of the project
├── .git/                    # Git version control data
├── .github/                 # GitHub workflows
├── .venv/                   # Project's virtual environment
├── .vscode/                 # VSCode config settings
├── dist/                    # Location of distributable package.
├── docs/                    # Documentations for `malbench` module
├── malbench/                # Malbench module source code
│   ├── data/                # Static data for project
│   ├── __main__.py          # Malbench entry point
├── tests/                   # Testing for functions in `malbench/`
├── .env                     # File holding environment variables
├── .gitignore               # Config for ignoring files from git
├── LICENSE.md               # File describing licensing for Malbench
├── poetry.lock              # Poetry lock file
├── poetry.toml              # Poetry config file
├── pyproject.toml           # Project config file
├── README.md                # General project documentation
├── CONTRIBUTING.md          # Documentation for developers
└── setup.cfg                # Setup config
```

### Tasks
Malbench utilizes [PoeThePoet](https://github.com/nat-n/poethepoet) for managing developer tasks. These tasks can be accessed through the virtual environment CLI, or there VSCode.

| Name        | Description                  | Command                                      |
| ----------- | ---------------------------- | -------------------------------------------- |
| `format`    | Performs type checking       | `autopep8 --in-place --recursive malbench`   |
| `lint`      | Lints code                   | `flake8 malbench`                            |
| `typecheck` | Formats code                 | `mypy malbench`                              |
| `test`      | Runs all unit tests          | `coverage run -m unittest discover -s tests` |
| `coverage`  | Generates coverage report    | `coverage report --fail-under=80`            |
| `docs`      | Generates code documentation | `pdoc -o docs malbench`                      |
| `vulncheck` | Runs a vulnerability check   | `poetry check`                               |

### Formatting
The Malbench project follows the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide for Python code. We use the `autopep8` tool to automatically format code to follow these conventions.

The configuration is as follows:
```
[pycodestyle]
exclude = tests/, scripts/, .venv, .git, init.py, docs/source/conf.py, dist, pycache
max-line-length = 130
```

Formatting can be run with the following command:
```bash
poe format
```

### Linting
The Malbench project uses `flake8` for linting Python code.

The configuration is as follows:
```
[flake8]
exclude = tests/*, scripts/*, .venv, .git, __init__.py, docs/source/conf.py, dist, __pycache__
max_line_length = 130
extend-ignore = D100, D202, D401
docstring-convention = pep257
```

Formatting can be run with the following command:
```bash
poe lint
```

### Unit Testing and Coverage
The Malbench project uses `unittest` for unit testing and `coverage` for generating test coverage reports. All public functions under `./malbench` should be backed up by a unit test. The test should hit a minimum of 80% coverage.

Unit tests can be run with the following command:
```bash
poe test
```

After running the unit tests, coverage reports can be generated with the following command:
```bash
poe coverage
```

### Documentation
We use `pdoc` for generating Python code documentation.

For public methods and classes, it's recommended to use docstrings that follow the PEP 257 style guide. For private methods, it's generally not necessary to include docstrings that follow the PEP 257 style guide. However, it can be useful to include a one-line summary that describes the method's purpose

Documentation can be generated with the following command:
```bash
poe docs
```
