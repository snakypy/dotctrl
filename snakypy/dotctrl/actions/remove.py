from concurrent.futures import ThreadPoolExecutor
from contextlib import suppress
from os import remove
from os.path import exists, islink, join
from sys import exit
from typing import Any, Tuple, Union

from snakypy.helpers import FG, pick, printer
from snakypy.helpers.os import rmdir_blank

from snakypy.dotctrl.config.base import Base
from snakypy.dotctrl.utils import check_init, listing_files, rm_garbage_config


def remove_opts(repo, objects, arguments: dict) -> Union[tuple]:
    """Function presents the possibilities of options for removing
    the elements."""
    objects_repo = []
    for item in [*listing_files(repo, only_rc_files=True), *objects]:
        if exists(join(repo, item)):
            objects_repo.append(item)

    if len(objects_repo) <= 0:
        printer("Nothing to remove.", foreground=FG().WARNING)
        exit(0)
    else:
        if arguments["--all"] and arguments["--noconfirm"]:
            return "all", objects_repo
        printer(
            "ATTENTION! This choice is permanent, there will be no going back.",
            foreground=FG().WARNING,
        )
        if arguments["--all"] and not arguments["--noconfirm"]:
            reply: Union[tuple[int, Any], bool, None] = pick(
                "Do you really want to destroy ALL elements of the repository?",
                ["Yes", "No"],
                colorful=True,
                lowercase=True,
            )
            if reply == "yes":
                return "all", objects_repo

        reply = pick(
            "Choose the element you want to remove from the repository:",
            objects_repo,
            colorful=True,
            ctrl_c_message=True,
        )
        exit(0) if reply is None else None
        if not arguments["--noconfirm"]:
            confirm = pick(
                f'Really want to destroy the "{reply}"?',
                ["yes", "no"],
                colorful=True,
            )
            exit(0) if confirm is None else None
            if confirm == "yes":
                return reply, objects_repo
        return reply, objects_repo


def rm_elements(home, repo, item):
    if exists(join(repo, item)):
        if islink(join(home, item)):
            with suppress(Exception):
                remove(join(home, item))
        with suppress(Exception):
            remove(join(repo, item))


class RemoveCommand(Base):
    def __init__(self, root, home):
        Base.__init__(self, root, home)

    def main(self, arguments: dict) -> None:
        """Method of removing elements from the repository and
        symbolic links linked to them. Calls other methods and functions
        that also perform other actions."""
        check_init(self.ROOT)

        rm_garbage_config(self.HOME, self.repo_path, self.config_path)

        option: tuple = remove_opts(self.repo_path, self.data, arguments)

        if option is None:
            printer("Aborted by user.", foreground=FG().WARNING)
        elif option and option[0] != "all":
            with ThreadPoolExecutor() as e:
                e.submit(rm_elements, self.HOME, self.repo_path, option[0])
        elif option and option[0] == "all":
            for i in option[1]:
                with ThreadPoolExecutor() as e:
                    e.submit(rm_elements, self.HOME, self.repo_path, i)
            with ThreadPoolExecutor() as e:
                e.submit(rmdir_blank, self.repo_path)

        rm_garbage_config(self.HOME, self.repo_path, self.config_path)
