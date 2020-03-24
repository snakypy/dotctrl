"""
Dotctrl
~~~~~~~~

Dotctrl is a package for managing your dot files on Linux.
Dotctrl works on top of a configuration file that
contains the absolute paths of the place of origin of
dotfiles.

For more information, access: 'https://github.com/snakypy/dotctrl'

:copyright: Copyright 2020-2020 by Snakypy team, see AUTHORS.
:license: MIT license, see LICENSE for details.
"""

import os
from pathlib import Path
from dotctrl import __name__


# Version
__version__ = "0.1.0"
# Path current
ROOT = os.getcwd()
# HOME user
HOME = str(Path.home())
# A dictionary that loads some global package settings.
__pkginfo__ = {
    "name": "Dotctrl",
    "description": "Dotctrl is a package for managing your dotfiles on Linux.",
    "pkg_name": __name__,
    "executable": __name__,
    "config": "dotctrl.toml",
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
