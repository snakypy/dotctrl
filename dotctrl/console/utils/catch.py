# import os
from glob import glob
from docopt import docopt
from snakypy import FG
from snakypy.ansi import NONE
from os import walk
from os.path import join, islink, isfile
from dotctrl import __version__
from dotctrl.config import menu, package


def arguments(argv=None):
    """Function to return the option menu arguments."""
    formatted_version = (
        f"{package.info['name']} version: " f"{FG.CYAN}{__version__}{NONE}"
    )
    data = docopt(menu.options, argv=argv, version=formatted_version)
    return data


def listing_files(directory, only_rc_files=False):
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
