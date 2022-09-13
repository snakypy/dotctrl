"""
Dotctrl
~~~~~~~~

Dotctrl is a package for managing your "dotfiles" on Linux.
Dotctrl works on top of a configuration file that
contains the absolute paths of the place of origin of
dotfiles.

For more information, access: 'https://github.com/snakypy/dotctrl'

:copyright: Copyright 2020-present by Snakypy team, see AUTHORS.
:license: MIT license, see LICENSE for details.
"""
import os
from os.path import abspath, dirname, join
from pathlib import Path

from snakypy.helpers.files import eqversion

__info__: dict = {
    "name": "Dotctrl",
    "version": "2.0.0",
    "description": "Dotctrl is a package for managing your dotfiles on Linux.",
    "pkg_name": "dotctrl",
    "executable": "dotctrl",
    "config": "dotctrl.json",
    "home_page": "https://github.com/snakypy/dotctrl",
    "organization_name": "Snakypy",
    "env": "DOTCTRL_PATH",
    "author": {
        "name": "William C. Canin",
        "email": "william.costa.canin@gmail.com",
        "website": "https://williamcanin.github.io",
        "github": "https://github.com/williamcanin",
    },
    "credence": [
        {
            "name": "William C. Canin",
            "email": "william.costa.canin@gmail.com",
            "website": "https://williamcanin.github.io",
            "locale": "Brazil - SP",
        }
    ],
}


def choose_root(env: str):
    """
    Function to return the ROOT path. If the DOTFILES environment variable
    exists then this path will be returned, otherwise it will return
    the current path.
    """
    if os.environ.get(env):
        return os.environ.get(env)

    return os.getcwd()


# Path current
ROOT: str = choose_root(__info__["env"])

# HOME user
HOME: str = str(Path.home())

# It only takes the HOME, not the user's.
# Linux: /home and macOS: /Users
AUTO_PATH = join("/", list(filter(None, HOME.split("/")))[0])

# Keep the versions the same on pyproject.toml and __init__.py
pyproject: str = join(dirname(abspath(__file__)), "../..", "pyproject.toml")

eqversion(pyproject, __info__["version"])
