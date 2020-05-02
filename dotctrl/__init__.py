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


# Version
__version__ = "1.1.5"
# Path current
ROOT = os.getcwd()
# HOME user
HOME = str(Path.home())
