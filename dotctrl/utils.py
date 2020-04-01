"""This module will store useful functions for Dotctrl."""
import os
import shutil
import contextlib
import subprocess
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


def git_init():
    if shutil.which("git") and not isdir(".git"):
        subprocess.call(["git", "init"], stdout=subprocess.PIPE)


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


def to_move(src, dst, arguments):
    """Moves the dot files from the drive to the repository
    src = local source
    dst = repository
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
            with contextlib.suppress(Exception):
                shutil.move(src, dst)
            return True
    return


def create_symlink(src, dst, arguments):
    """Creates symbolic links. In this case, the "src" is the
    repository for dotctrl.
    src = repository
    dst = local source
    """
    if exists(src):
        if islink(dst) and not arguments:
            printer(
                "Some symbolic links have already been created.\n"
                "Use the --element option to create unique links "
                "or use --force.",
                foreground=FG.WARNING,
            )
            exit(0)
        else:
            with contextlib.suppress(Exception):
                os.remove(dst)
            os.symlink(src, dst)


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


def listing_files(directory, only_rc=False):
    data = []
    if only_rc:
        for file in glob(join(directory, ".*rc"), recursive=False):
            if isfile(file) and not islink(file):
                data.append(file.split("/")[-1])
        return data
    for r, d, f in os.walk(directory):
        for file in f:
            elem = os.path.join(r, file)
            elem = elem.replace(f"{directory}/", "")
            data.append(elem)
    return data


def clear_config_garbage(repo, home, config):
    parsed = snakypy.json.read(config)
    elements = parsed["dotctrl"]["elements"]
    new_elements = []
    for item in elements:
        if exists(join(repo, item)) or exists(join(home, item)):
            new_elements.append(item)
    parsed["dotctrl"]["elements"] = new_elements
    snakypy.json.create(parsed, config, force=True)


def add_element_config(src, element, config):
    parsed = snakypy.json.read(config)
    if element not in parsed["dotctrl"]["elements"]:
        if element[-2:] == "rc" and "/" not in element:
            pass
        else:
            if exists(src):
                lst = list(parsed["dotctrl"]["elements"])
                lst.append(element)
                parsed["dotctrl"]["elements"] = lst
                snakypy.json.create(parsed, config, force=True)
