# import os
from os import walk
from os.path import join

from docopt import docopt
from snakypy.helpers import FG
from snakypy.helpers.ansi import NONE

from snakypy.dotctrl import __info__
from snakypy.dotctrl.config import menu


def arguments(argv=None) -> dict:
    """Function to return the option menu arguments."""
    formatted_version = (
        f"{__info__['name']} version: " f"{FG().CYAN}{__info__['version']}{NONE}"
    )
    data = docopt(menu.options, argv=argv, version=formatted_version)
    return data


def listing_files(directory) -> list:
    """Lists files from a specific directory."""
    objects = list()
    for root, _, files in walk(directory):
        for file in files:
            elem = join(root, file)
            elem = elem.replace(f"{directory}/", "")
            objects.append(elem)
    return objects
