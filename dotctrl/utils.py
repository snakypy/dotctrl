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
    """Function to start a Git repository in the Dotctrl repository."""
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
            with contextlib.suppress(Exception):
                shutil.move(src, dst)
            return True
    return


def create_symlink(src, dst, arguments):
    """Creates symbolic links. In this case, the "src" is the
        repository for dotctrl.
    :param src: Dotctrl repository location
    :param dst: Element source location
    :param arguments: Receive a Docopt dictionary
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
            try:
                os.symlink(src, dst)
                return True
            except PermissionError as p:
                printer(
                    "User without permission to create the symbolic link.",
                    p,
                    foreground=FG.ERROR,
                )
    return


def rm_objects(obj):
    """Removes objects according to the type of folder,
    file or symbolic link.
    :param obj: Object to be removed (files or folders).
    """
    if isfile(obj) or islink(obj):
        with contextlib.suppress(Exception):
            os.remove(obj)
    else:
        with contextlib.suppress(Exception):
            shutil.rmtree(obj)


def listing_files(directory, only_rc=False):
    """Lists files from a specific directory."""
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


def update_config(repo, home, config, only_repo=False):
    """Deletes elements in the configuration file that is
    neither in the Dotctrl repository nor in the source location."""
    parsed = snakypy.json.read(config)
    elements = parsed["dotctrl"]["elements"]
    new_elements = []
    for item in elements:
        if only_repo:
            if exists(join(repo, item)):
                new_elements.append(item)
        else:
            if exists(join(repo, item)) or exists(join(home, item)):
                new_elements.append(item)
    parsed["dotctrl"]["elements"] = new_elements
    snakypy.json.create(parsed, config, force=True)


def path_creation(root, item):
    """Create repository for file with a path"""
    path_split = item.split("/")[:-1]
    path_str = "/".join(path_split)
    path = join(root, path_str)
    snakypy.path.create(path)
    return str(path)


def add_element_config(src, element, config):
    """Function that adds element to the configuration file
    when using the "pull --element=<object>" option."""
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
                return True
            return


def exists_levels(src, dst, arguments):
    """A function that returns level by checking source, destination
    and forced argument files."""
    if exists(src) and exists(dst) and not arguments()["--force"]:
        return 0
    elif exists(src) and exists(dst) and arguments()["--force"]:
        return 1
    elif exists(src) and not exists(dst):
        return 2
    return


def restore_args(repo, src, dst, arguments):
    """Function presents the possibilities of options for restored
    the elements."""
    if exists_levels(src, dst, arguments) is None:
        printer(
            f'Restore failed. Element "{src}" not found in repository.',
            foreground=FG.ERROR,
        )
        exit(1)
    if exists_levels(src, dst, arguments) == 0:
        printer(
            "The files match the repository and the drive. User --force.",
            foreground=FG.WARNING,
        )
        exit(0)
    if exists_levels(src, dst, arguments) == 1:
        rm_objects(dst)
        shutil.move(src, dst)
        snakypy.os.rmdir_blank(repo)
    if exists_levels(src, dst, arguments) == 2:
        shutil.move(src, dst)
        snakypy.os.rmdir_blank(repo)


def remove_opts(root, repo, data, arguments):
    """Function presents the possibilities of options for removing
    the elements."""
    cheking_init(root)
    objects = [*listing_files(repo, only_rc=True), *data]
    if len(objects) <= 0:
        printer("Nothing to remove.", foreground=FG.WARNING)
        exit(0)
    else:
        if arguments["--all"] and arguments["--noconfirm"]:
            return "all", objects
        printer(
            "ATTENTION! This choice is permanent, there will be no going back.",
            foreground=FG.WARNING,
        )
        if arguments["--all"] and not arguments["--noconfirm"]:
            reply = snakypy.pick(
                "Do you really want to destroy ALL elements of the repository?",
                ["Yes", "No"],
                colorful=True,
                lowercase=True,
            )
            if reply == "yes":
                return "all", objects
            return

        reply = snakypy.pick(
            "Choose the element you want to remove from the repository:",
            objects,
            colorful=True,
            ctrl_c_message=True,
        )
        exit(0) if reply is None else None
        if not arguments["--noconfirm"]:
            confirm = snakypy.pick(
                f'Really want to destroy the "{reply}"?', ["yes", "no"], colorful=True,
            )
            exit(0) if confirm is None else None
            if confirm == "yes":
                return reply, objects
            return
        return reply, objects


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
