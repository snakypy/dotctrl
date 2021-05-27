# import os
from glob import glob
from os import walk
from os.path import isfile, islink, join

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


def listing_files(directory, only_rc_files=False) -> list:
    """Lists files from a specific directory."""
    objects = list()
    if only_rc_files:
        for file in glob(join(directory, ".*rc"), recursive=False):
            if isfile(file) and not islink(file):
                objects.append(file.split("/")[-1])
        return objects
    for r, d, f in walk(directory):
        for file in f:
            elem = join(r, file)
            elem = elem.replace(f"{directory}/", "")
            objects.append(elem)
    return objects
