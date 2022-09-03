from contextlib import suppress
from os import remove, symlink
from os.path import exists, isfile, islink
from shutil import move, rmtree
from sys import exit

from snakypy.helpers import FG, printer
from snakypy.helpers.files import create_json, read_json


def create_symlink(src, dst, arguments) -> bool:
    """
    Creates symbolic links. In this case, the "src" is the
    repository for dotctrl.
    """
    if exists(src):
        # if exists(dst) and not arguments:
        #     printer(
        #         "Some symbolic links already exist according to the ones you want to create.\n"
        #         "Use the --element (--e) option to recreate unique links "
        #         "or use --force (--f).",
        #         foreground=FG().WARNING,
        #     )
        # #     exit(0)
        # else:
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
        except FileExistsError:
            remove(dst)
            symlink(src, dst)
    return False


def to_move(src: str, dst: str, message: str, force: bool) -> bool:
    """Moves the dot files from the drive to the repository."""

    if not islink(src):
        if exists(src) and exists(dst) and not force:
            # Files with the same name were found in the Dotctrl repository and source location.
            # To override those in the Dotctrl repository, use the --force (--f) option.
            printer(message, foreground=FG(warning_icon="[!] ").WARNING)
            exit(0)
        else:
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


# # DEPRECATED
# def rm_garbage_config(
#     repo: str, home: str, config: str, only_repo: bool = False
# ) -> None:
#     """Deletes elements in the configuration file that is
#     neither in the Dotctrl repository nor in the source location."""
#     parsed = read_json(config)
#     elements = parsed["dotctrl"]["elements"]
#     new_elements = list()
#     for item in elements:
#         if only_repo:
#             if exists(join(repo, item)):
#                 new_elements.append(item)
#         else:
#             if exists(join(repo, item)) or exists(join(home, item)):
#                 new_elements.append(item)
#     parsed["dotctrl"]["elements"] = new_elements
#     create_json(parsed, config, force=True)


def add_element_config(src: str, element: str, config_path: str) -> bool:
    """Function that adds element to the configuration file
    when using the "pull --element=<object>" option."""
    parsed = read_json(config_path)
    if element not in parsed["dotctrl"]["elements"] and exists(src):
        lst = list(parsed["dotctrl"]["elements"])
        lst.append(element)
        parsed["dotctrl"]["elements"] = lst
        create_json(parsed, config_path, force=True)
        return True
    return False
