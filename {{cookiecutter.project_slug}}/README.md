# {{cookiecutter.project_name}} - {{cookiecutter.project_slug}} 

Description: {{cookiecutter.project_short_description}}


## Usage


####  Environment variables

TODO: add if needed

#### Correct usage

With the virtual env activated, run: 

```
python {{ cookiecutter.project_slug }}.py
```

#### Incorrect usage

TODO: add if needed

## Getting Started


### Python Dependencies

See the `requirements` directory for required Python modules for building, testing, developing etc.
They can all be installed in a [virtual environment](https://docs.python.org/3/library/venv.html) 
using the follow commands:

```
python3 -m venv venv
. venv/bin/activate
pip install -r ./requirements/dev.txt -r ./requirements/prod.txt -r ./requirements/test.txt
```

There's also a bin script to do this:

```
./bin/create_venv.sh
```

## Testing

This project uses pytest to manage and run unit tests. Unit tests located in the `test` directory 
are automatically run during the CI build. You can run them manually with:

```
./bin/run_tests.sh
```


### Local Linting

There are a few linters/code checks included with this project to speed up the development process:

* Black - An automatic code formatter, never think about python style again.
* Isort - Automatically organizes imports in your modules.
* Pylint - Check your code against many of the python style guide rules.
* Mypy - Check your code to make sure it is properly typed.
* Vulture - Looks for dead code.

You can run these tools automatically in check mode, meaning you will get an error if any of them
would not pass with:

```
./bin/run_checks.sh
```

Or actually automatically apply the fixes with:

```
./bin/apply_linters.sh
```

There are also scritps in `./bin/` that include run/check for each individual tool.

{% if cookiecutter.enable_pre_commit_hooks == 'y' %}
### Using pre-commit

First you need to init the repo as a git repo with:

```
git init
```

Then you can set up the git hook scripts with:

```
pre-commit install
```

By default:

* black
* pylint
* isort
* mypy
* vulture

Are all run in apply-mode and must pass in order to actually make the commit.

Also by default, pytest needs to pass before you can push.

If you'd like skip these checks you can commit with:

```
git commit --no-verify
```

If you'd like to quickly run these pre-commit checks on all files (not just the staged ones) you
can run:

```
pre-commit run --all-files
```
{% endif %}
