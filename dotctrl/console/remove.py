import os
import snakypy
from contextlib import suppress
from os.path import exists, islink, join
from sys import exit
from snakypy import FG, printer
from dotctrl.console import utils
from dotctrl.config import base


def remove_opts(root, repo, objects, arguments):
    """Function presents the possibilities of options for removing
    the elements."""
    utils.check_init(root)
    get_objects = [*utils.listing_files(repo, only_rc_files=True), *objects]
    if len(get_objects) <= 0:
        printer("Nothing to remove.", foreground=FG.WARNING)
        exit(0)
    else:
        if arguments["--all"] and arguments["--noconfirm"]:
            return "all", get_objects
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
                return "all", get_objects
            return

        reply = snakypy.pick(
            "Choose the element you want to remove from the repository:",
            get_objects,
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
                return reply, get_objects
            return
        return reply, get_objects


def rm_elements(home, repo, item):
    if exists(join(repo, item)):
        if islink(join(home, item)):
            with suppress(Exception):
                os.remove(join(home, item))
        with suppress(Exception):
            os.remove(join(repo, item))


class Command(base.Base):
    def __init__(self, root, home):
        base.Base.__init__(self, root, home)

    def main(self, arguments):
        """Method of removing elements from the repository and
        symbolic links linked to them. Calls other methods and functions
        that also perform other actions."""

        utils.rm_garbage_config(self.HOME, self.repo_path, self.config_path)

        option = remove_opts(self.ROOT, self.repo_path, self.data, arguments)

        if option is None:
            printer("Aborted by user.", foreground=FG.WARNING)
        elif option and option[0] != "all":
            rm_elements(self.HOME, self.repo_path, option[0])
        elif option and option[0] == "all":
            for i in option[1]:
                rm_elements(self.HOME, self.repo_path, i)
            snakypy.os.rmdir_blank(self.repo_path)

        utils.rm_garbage_config(self.HOME, self.repo_path, self.config_path)
