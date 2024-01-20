# Playground

Diogo's playground

## Development Setup

Follow these steps if you are planning to use this library for development.

### Virtual environment

Run the following command to create the virtual environment.

```
make venv
source venv/bin/activate
```

> This will intall the package in development mode.

### Installing dependencies

To install new dependencies run:

```
pipenv install <library_name>
```

To update the current dependencies run

```
pipenv upgrade
```

### Docstrings

If using Visual Studio Code install [this](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring) extention to automatically add docstrings when typing `"""` under the function method.
Go to extension settings and set format to `numpy`.

If using PyCharm, change docstring style to `numpy` in Settings | Tools |
Python Integrated Tools | Docstring format.

### Styling

Run the following command to format the code of the library.

```
make style
```

This command runs the following linters:

```
nbqa black .
nbqa isort .
nbqa flake8 .
black .
flake8
isort .
```

Check [here](https://pycodestyle.pycqa.org/en/latest/intro.html#error-codes) for more details about the errors detected by flake8.

`nbqa` applies styling to notebooks, check [here](https://github.com/nbQA-dev/nbQA) for more details.

### Notebooks

#### Matplotlib Style

Configure matplotlib sword style to apply the sword style to plots.
Follow instructions [here](https://github.com/SWORDHealth/mpl-sword).

#### Code Review

The pre-commit hook automatically converts all the notebooks to a python file with the same name.

Code Reviews should be performed using the python file.

Any change should be performed on the notebook file (and not the corresponding python file).

## CLI

Run the following command to get a list of all the available commands.

```
epl_fantasy --help
```