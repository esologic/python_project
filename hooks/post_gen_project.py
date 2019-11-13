"""
Will run after the project has been generated
"""

import os
import subprocess
from typing import Optional
import sys
from time import sleep


PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def run_command(command: str) -> None:
    """
    Wrapper about a command run
    :param command:
    :return: None
    """

    def fail_build(error: Optional[str] = None) -> None:
        """
        Print the error, and then exit.
        :param error: Info about the error that occurred
        :return: None
        """
        err_note = "Cookiecutter project build failed."
        if error is None:
            print(err_note)
        else:
            print(err_note + f"Error: [{error}]")

        # The project generation will stop and the generated directory will be cleaned up.
        sys.exit(1)

    output = subprocess.run(command, shell=True)
    if output.returncode != 0:
        fail_build()

def remove_cookiecutter_file(file_name: str) -> None:
    """
    Wrapper for removing a file from the project directory
    :param file_name: the name of the file in the project data to delete
    :return: None
    """
    os.remove(os.path.join(PROJECT_DIRECTORY, file_name))


if __name__ == '__main__':

    if '{{ cookiecutter.create_author_file }}' != 'y':
        remove_cookiecutter_file('AUTHORS.md')

    if '{{ cookiecutter.create_venv_install_reqs }}' == 'y':
        run_command("./bin/create_venv.sh")

    if '{{ cookiecutter.enable_pre_commit_hooks }}' != 'y':
        remove_cookiecutter_file('.pre-commit-config.yaml')
    else:
        # we can't wait on the files to get written to disk, so we sleep to make sure they're there
        sleep(5)
        run_command("git init")
        run_command("pre-commit install")
        run_command("pre-commit install --hook-type pre-push")
        run_command("git add .")
        run_command('git commit -m "init"')

    if '{{ cookiecutter.create_setup_py }}' != 'y':
        remove_cookiecutter_file("setup.py")
