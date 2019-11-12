"""Use this file to install {{ cookiecutter.project_slug }} as a module"""

from distutils.core import setup
from typing import List


def prod_dependencies() -> List[str]:
    """
    Pull the dependencies from the requirements dir
    :return: Each of the newlines, strings of the dependencies
    """
    with open("./requirements/prod.txt", "r") as file:
        return file.read().splitlines()


setup(
    name="{{ cookiecutter.project_slug }}",
    version="{{ cookiecutter.version }}",
    description="{{ cookiecutter.project_short_description }}",
    author="{{ cookiecutter.full_name }}",
    author_email="{{ cookiecutter.email }}",
    package_dir={"{{ cookiecutter.project_slug }}": "./src"},
    packages=["{{ cookiecutter.project_slug }}"],
    install_requires=prod_dependencies(),
)
