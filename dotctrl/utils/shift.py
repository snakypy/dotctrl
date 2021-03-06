from snakypy.json import read as json_read
from snakypy.json import create as json_create
from shutil import move, rmtree
from os import remove, symlink
from contextlib import suppress
from sys import exit
from os.path import exists, islink, isfile, join
from snakypy import printer, FG


def create_symlink(src, dst, arguments):
    """Creates symbolic links. In this case, the "src" is the
        repository for dotctrl.
    :param src: Dotctrl repository location
    :param dst: Element source location
    :param arguments: Receive a Docopt dictionary
    """
    if exists(src):
        if exists(dst) and not arguments:
            printer(
                "Some symbolic links have already been created.\n"
                "Use the --element option to create unique links "
                "or use --force.",
                foreground=FG.WARNING,
            )
            exit(0)
        else:
            with suppress(Exception):
                if isfile(dst):
                    remove(dst)
                else:
                    rmtree(dst)
            try:
                symlink(src, dst)
                return True
            except PermissionError as p:
                printer(
                    "User without permission to create the symbolic link.",
                    p,
                    foreground=FG.ERROR,
                )
    return


def to_move(src, dst, arguments):
    """Moves the dot files from the drive to the repository.
    :param arguments: Receive "Docopt" argument output
    :param src: Element source location
    :param dst: Dotctrl repository location
    """
    if not islink(src):
        if exists(src) and exists(dst) and not arguments:
            printer(
                "The same files were found in the dotctrl repository"
                " and in the source location. Use --force",
                foreground=FG.WARNING,
            )
            exit(0)
        else:
            with suppress(Exception):
                move(src, dst)
            return True
    return


def rm_objects(obj):
    """Removes objects according to the type of folder,
    file or symbolic link.
    :param obj: Object to be removed (files or folders).
    """
    if isfile(obj) or islink(obj):
        with suppress(Exception):
            remove(obj)
    else:
        with suppress(Exception):
            rmtree(obj)


def rm_garbage_config(repo, home, config, only_repo=False):
    """Deletes elements in the configuration file that is
    neither in the Dotctrl repository nor in the source location."""
    parsed = json_read(config)
    elements = parsed["dotctrl"]["elements"]
    new_elements = list()
    for item in elements:
        if only_repo:
            if exists(join(repo, item)):
                new_elements.append(item)
        else:
            if exists(join(repo, item)) or exists(join(home, item)):
                new_elements.append(item)
    parsed["dotctrl"]["elements"] = new_elements
    json_create(parsed, config, force=True)


def add_element_config(src, element, config):
    """Function that adds element to the configuration file
    when using the "pull --element=<object>" option."""
    parsed = json_read(config)
    if element not in parsed["dotctrl"]["elements"]:
        if element[-2:] == "rc" and "/" not in element:
            pass
        else:
            if exists(src):
                lst = list(parsed["dotctrl"]["elements"])
                lst.append(element)
                parsed["dotctrl"]["elements"] = lst
                json_create(parsed, config, force=True)
                return True
            return
