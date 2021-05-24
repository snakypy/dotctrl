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
from pathlib import Path

# Path current
ROOT = os.getcwd()
# HOME user
HOME = str(Path.home())

__info__ = {
    "name": "Dotctrl",
    "version": "1.1.8",
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
