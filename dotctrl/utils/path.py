from snakypy.path import create as create_path
from os.path import join
from pathlib import Path


def shorten_path(file_path, length):
    return Path(*Path(file_path).parts[-length:])


def path_creation(root, item):
    """Create repository for file with a path"""
    path_split = item.split("/")[:-1]
    path_str = "/".join(path_split)
    path = join(root, path_str)
    create_path(path)
    return str(path)


def join_two(obj1, obj2):
    """Formats the element entry with the pull --element command. By default,
    when you type a forward slash (/) in the second parameter of the join command,
    the union is not made. This function has the responsibility of making the join
    even if it finds a slash (/)"""
    new_obj2 = obj2
    if new_obj2[0] == "/":
        new_obj2 = new_obj2[1:]
    result = join(obj1, new_obj2)
    return result
