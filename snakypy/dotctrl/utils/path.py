from os.path import join
from pathlib import Path
from typing import Union

from snakypy.helpers.path import create as create_path


def shorten_path(file_path: str, length: int) -> Path:
    return Path(*Path(file_path).parts[-length:])


def path_creation(root: str, item: str) -> str:
    """Create repository for file with a path"""
    path_split = item.split("/")[:-1]
    path_str = "/".join(path_split)
    path = join(root, path_str)
    create_path(path)

    return str(path)


def join_two(elem1: str, elem2: str) -> Union[bytes, str]:
    """Formats the element entry with the pull --element command. By default,
    when you type a forward slash (/) in the second parameter of the join command,
    the union is not made. This function has the responsibility of making the join
    even if it finds a slash (/)"""
    if elem2[0] == "/":
        elem2 = elem2[1:]

    return join(elem1, elem2)
