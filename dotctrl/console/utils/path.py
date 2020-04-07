import os
import snakypy


def path_creation(root, item):
    """Create repository for file with a path"""
    path_split = item.split("/")[:-1]
    path_str = "/".join(path_split)
    path = os.path.join(root, path_str)
    snakypy.path.create(path)
    return str(path)


def join_two(obj1, obj2):
    """Formats the element entry with the pull --element command. By default,
    when you type a forward slash (/) in the second parameter of the join command,
    the union is not made. This function has the responsibility of making the join
    even if it finds a slash (/)"""
    new_obj2 = obj2
    if new_obj2[0] == "/":
        new_obj2 = new_obj2[1:]
    result = os.path.join(obj1, new_obj2)
    return result
