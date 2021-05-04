"""
This module is called after project is created.

It does the following:
1. Generates and saves random secret key
2. Prints further instructions

A portion of this code was adopted from Django's standard crypto functions and
utilities, specifically:
https://github.com/django/django/blob/master/django/utils/crypto.py

And from pydanny's cookiecutter-django:
https://github.com/pydanny/cookiecutter-django

"""

import os
import secrets
import shutil
import string

# CHANGEME mark
import cookiecutter.extensions

CHANGEME = '__CHANGEME__'

# Get the root project directory
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
PROJECT_NAME = '{{ cookiecutter.project_name }}'

# Messages
PROJECT_SUCCESS = """
Your project {0} is created.
Now you can start working on it:

    cd {0}
"""


def print_futher_instuctions():
    """Shows user what to do next after project creation."""
    print(PROJECT_SUCCESS.format(PROJECT_NAME))  # noqa: WPS421


def copy_local_configuration():
    """
    Handler to copy local configuration.

    It is copied from ``.template`` files to the actual files.
    """

    # Local config:
    local_template = os.path.join(
        PROJECT_DIRECTORY,
        'server',
        'settings',
        'environments',
        'local.py.template',
    )
    local_config = os.path.join(
        PROJECT_DIRECTORY,
        'server',
        'settings',
        'environments',
        'local.py',
    )
    shutil.copyfile(local_template, local_config)


copy_local_configuration()
print_futher_instuctions()
