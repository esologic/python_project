# Python Project 

A cookiecutter repo for creating blank python projects with common process improvement tools
already intalled. 

By default, you get:

* **Black** - An automatic code formatter, never think about python style again.
* **Isort** - Automatically organizes imports in your modules.
* **Pylint** - Check your code against many of the python style guide rules.
* **Mypy** - Check your code to make sure it is properly typed.
* **Vulture** - Looks for dead code.
* **Pytest** - A modern test suite manager with amazing plugins and utlities.
* **CircleCi** - A working config that runs tests and linters on circle.

## Creating a project

You can install cookiecutter with either pip or apt:

```
pip install --user cookiecutter
```

```
sudo apt-get install cookiecutter
```

Then, run the following command and follow the prompts to create your new project in the current
directory:

```
cookiecutter git@bitbucket.org:devon_tvi/python_project.git
```
