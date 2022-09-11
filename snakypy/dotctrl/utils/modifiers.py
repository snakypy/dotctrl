from contextlib import suppress
from os import remove, symlink
from os.path import exists, isfile, islink
from shutil import move, rmtree
from typing import Any

from snakypy.helpers import FG, printer
from snakypy.helpers.files import create_json, read_json


def create_symlink(src: str, dst: str) -> bool:
    """
    Creates symbolic links. In this case, the "src" is the
    repository for dotctrl.
    """
    if exists(src):
        with suppress(Exception):
            if isfile(dst):
                remove(dst)
            else:
                rmtree(dst)

        try:

            symlink(src, dst)
            return True

        except PermissionError as err:
            printer(
                "User without permission to create the symbolic link.",
                str(err),
                foreground=FG().ERROR,
            )
            return False

        except FileExistsError:
            remove(dst)
            symlink(src, dst)
    return False


def to_move(src: str, dst: str) -> bool:
    """Moves the dot files from the drive to the repository."""

    if not islink(src):
        with suppress(Exception):
            move(src, dst)
        return True
    return False


def remove_objects(object_path: str) -> None:
    """Removes objects according to the type of folder,
    file or symbolic link.
    :param obj: Object to be removed (files or folders).
    """
    if isfile(object_path) or islink(object_path):
        with suppress(Exception):
            remove(object_path)
    else:
        with suppress(Exception):
            rmtree(object_path)


def add_element_config(src: str, element: str, config_path: str) -> bool:
    """Function that adds element to the configuration file
    when using the "pull --element=<object>" option."""

    parsed: Any = read_json(config_path)

    if element not in parsed["dotctrl"]["elements"] and exists(src):
        lst: list = list(parsed["dotctrl"]["elements"])
        lst.append(element)
        parsed["dotctrl"]["elements"] = lst
        create_json(parsed, config_path, force=True)
        return True

    return False
