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
from contextlib import suppress
from os.path import abspath, dirname, join
from pathlib import Path

from snakypy.helpers.files import create_file, read_file
from tomlkit import dumps, parse

# Path current
ROOT = os.getcwd()
# HOME user
HOME = str(Path.home())


__info__ = {
    "name": "Dotctrl",
    "version": "1.1.9",
    "description": "Dotctrl is a package for managing your dotfiles on Linux.",
    "pkg_name": "dotctrl",
    "executable": "dotctrl",
    "config": "dotctrl.json",
    "home_page": "https://github.com/snakypy/dotctrl",
    "organization_name": "Snakypy",
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
            "website": "http://williamcanin.me",
            "locale": "Brazil - SP",
        }
    ],
}

# Updates the version of the pyproject.toml file according to the package version.
with suppress(FileNotFoundError):
    pyproject_file = join(dirname(abspath(__file__)), "../../pyproject.toml")
    parsed = parse(read_file(pyproject_file))
    if parsed["tool"]["poetry"]["version"] != __info__["version"]:
        parsed["tool"]["poetry"]["version"] = __info__["version"]
        create_file(dumps(parsed), pyproject_file, force=True)
