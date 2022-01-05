"""
Dotctrl
~~~~~~~~

Dotctrl is a package for managing your "dotfiles" on Linux.
Dotctrl works on top of a configuration file that
contains the absolute paths of the place of origin of
dotfiles.

For more information, access: 'https://github.com/snakypy/dotctrl'

:copyright: Copyright 2020-2021 by Snakypy team, see AUTHORS.
:license: MIT license, see LICENSE for details.
"""
import os
from os.path import abspath, dirname, join
from pathlib import Path

from snakypy.helpers.files import eqversion

__info__ = {
    "name": "Dotctrl",
    "version": "1.3.1",
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
            "my_name": "William C. Canin",
            "email": "william.costa.canin@gmail.com",
            "website": "https://williamcanin.github.io",
            "locale": "Brazil - SP",
        }
    ],
}


def choose_root(env):
    """
    Function to return the ROOT path. If the DOTFILES environment variable
    exists then this path will be returned, otherwise it will return
    the current path.
    """
    if os.environ.get(env):
        return os.environ.get(env)
    return os.getcwd()


# Path current
ROOT = choose_root(__info__["env"])
# HOME user
HOME = str(Path.home())

# Keep the versions the same on pyproject.toml and __init__.py
pyproject = join(dirname(abspath(__file__)), "../..", "pyproject.toml")
eqversion(pyproject, __info__["version"])
