"""This module will store useful functions for Dotctrl."""
import os
import shutil
import contextlib
import tomlkit
import snakypy
from sys import exit
from glob import glob
from os.path import join, exists, islink, isfile, isdir
from snakypy import printer, FG
from dotctrl import __pkginfo__


def show_billboard():
    """Function to create a billboard."""
    print("\n")
    printer("Offered by:".center(50), foreground=FG.GREEN)
    snakypy.console.billboard(
        __pkginfo__["organization_name"], justify="center", foreground=FG.YELLOW
    )
    printer(f"copyright (c) since 2020\n".center(100), foreground=FG.GREEN)


def cheking_init(root):
    """Function that ends commands that depend on the created repository, but
    the repository was not created."""
    if not exists(join(root, __pkginfo__["config"])):
        printer(
            f"The repository was not created. "
            f"Use \"{__pkginfo__['pkg_name']} init\". Aborted",
            foreground=FG.WARNING,
        )
        exit(1)


def create_file(content, file_path, config_toml=False, force=False):
    """Function to create configuration file and common."""
    if not exists(file_path) or force:
        if config_toml:
            parsed_toml = tomlkit.parse(content)
            content = tomlkit.dumps(parsed_toml)
        snakypy.file.create(content, file_path, force=force)
        return True
    return


def to_move(src, dst, *, force=False):
    """Moves the dot files from the drive to the repository
    src = local source
    dst = repository
    """
    if not islink(src):
        if exists(src) and exists(dst) and not force:
            printer(
                'The same files were found in the repository and "dotctrl" '
                "on the machine. Use --force",
                foreground=FG.WARNING,
            )
            exit(0)
        else:
            with contextlib.suppress(Exception):
                shutil.move(src, dst)
            return True
    return


def create_symlink(src, dst, *, force=False):
    """Creates symbolic links. In this case, the "src" is the
    repository for dotctrl.
    src = repository
    dst = local source
    """
    if exists(src):
        if islink(dst) and not force:
            printer(
                "Symbolic links have already been found. Use --force",
                foreground=FG.WARNING,
            )
            exit(0)
        else:
            with contextlib.suppress(Exception):
                os.remove(dst)
            os.symlink(src, dst)


def listing_rc(path):
    """Intelligently lists all rc files."""
    resources_file = []
    for file in glob(join(path, ".*rc"), recursive=False):
        if isfile(file) and not islink(file):
            resources_file.append(file.split("/")[-1])
    return resources_file


def append_dir_file(path, item, lst1: list, lst2: list):
    """Function to check if a path is a directory and add it
    to a list, if not, add it to another list."""
    if isdir(path):
        lst1.append(item)
    else:
        lst2.append(item)


def rm_objects(obj):
    """Removes objects according to the type of folder,
    file or symbolic link."""
    if isfile(obj) or islink(obj):
        with contextlib.suppress(Exception):
            os.remove(obj)
    else:
        with contextlib.suppress(Exception):
            shutil.rmtree(obj)


def exists_levels(src, dst, arguments):
    """A function that returns level by checking source, destination
    and forced argument files."""
    if exists(src) and exists(dst) and not arguments()["--force"]:
        return 0
    elif exists(src) and exists(dst) and arguments()["--force"]:
        return 1
    elif not exists(src) and exists(dst):
        return 2
