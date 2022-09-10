"""Module menu"""

from snakypy.helpers import FG
from snakypy.helpers.ansi import NONE

from snakypy.dotctrl import __info__

from snakypy.dotctrl.config.base import Base
from snakypy.dotctrl.utils import get_key
from os.path import exists
from docopt import docopt
from typing import Any


EN_US: str = f"""
{__info__['name']} version: {FG().CYAN}{__info__['version']}{NONE}

{__info__['name']} - Managing your dotfiles in $HOME on Linux or macOS.

USAGE:
    {__info__['executable']} init [--auto] [--git]
    {__info__['executable']} pull [--e=<object> | --element=<object>] [--f | --force]
    {__info__['executable']} link [--e=<object> | --element=<object>] [--f | --force]
    {__info__['executable']} unlink [--e=<object> | --element=<object>] [--f | --force]
    {__info__['executable']} restore [--e=<object> | --element=<object>] [--f | --force]
    {__info__['executable']} repo (--check | --ls | --info)
    {__info__['executable']} find (--name=<object>)
    {__info__['executable']} config (--open | --view | --lang | --autoclean)
    {__info__['executable']} --help
    {__info__['executable']} --version
    {__info__['executable']} --credits

ARGUMENTS:
    {FG().CYAN}init{NONE} ----------- Creates the dotfiles repository.
    {FG().CYAN}find{NONE} ----------- Find some object in the Dotctrl repository.
    {FG().CYAN}pull{NONE} ----------- Pulls the dotfiles from the source location on the
                    machine to the repository.
    {FG().CYAN}link{NONE} ----------- Links the repository's dotfiles to the source location
                    on the machine.
    {FG().CYAN}repo{NONE} ----------- Show {__info__["name"]} repository information.
    {FG().CYAN}unlink{NONE} --------- Unlink the dotfiles from the repository with the original location
                    on the machine.
    {FG().CYAN}config{NONE} --------- Handles the configuration file.
    {FG().CYAN}restore{NONE} -------- Moves all dotfiles from the repository to the default source location.

OPTIONS:
    {FG().BLUE}--check{NONE} --------------------- Checks whether the dotfiles in the repository are linked to
                                the place of origin or not.
    {FG().BLUE}--e | --element <object>{NONE} ---- Receives an object without its absolute path, just the relative one.
    {FG().BLUE}--open{NONE} ---------------------- Open a file in edit mode.
    {FG().BLUE}--view{NONE} ---------------------- View the contents of a file in the terminal.
    {FG().BLUE}--git{NONE} ----------------------- Create a Git repository.
    {FG().BLUE}--auto{NONE} ---------------------- Creates the {__info__["name"]} repository automatically in the users
                                directory. On Linux it will create in "/home", on macOS in "/Users".
                                You must have super user permission.
    {FG().BLUE}--info{NONE} ---------------------- Shows detailed information for the Do Ctrl repository.
    {FG().BLUE}--ls{NONE} ------------------------ List all files and folders in the {__info__["name"]} repository.
    {FG().BLUE}--lang{NONE} ---------------------- Change the language of {__info__["name"]}.
    {FG().BLUE}--name <object>{NONE} ------------- Receives the name of an object, it can be a folder or a file.
    {FG().BLUE}--f | --force{NONE} --------------- Complete the command regardless of whether or not files exist.
                                ATTENTION! Using this option will replace existing files.
    {FG().BLUE}--autoclean{NONE} ----------------- Clear the {__info__["name"]} registry, if there is no element in the
                                repository.
    {FG().BLUE}--version{NONE} ------------------- Show version.
    {FG().BLUE}--credits{NONE} ------------------- Show credits.
    {FG().BLUE}--help{NONE} ---------------------- Show this screen.

{FG().CYAN}Documentation:{NONE} {__info__["home_page"]}
"""

PT_BR = f"""
{__info__['name']} version: {FG().CYAN}{__info__['version']}{NONE}

{__info__['name']} - Gerenciando seus dotfiles do HOME no Linux ou macOS.

USAGE:
    {__info__['executable']} init [--auto] [--git]
    {__info__['executable']} pull [--e=<object> | --element=<object>] [--f | --force]
    {__info__['executable']} link [--e=<object> | --element=<object>] [--f | --force]
    {__info__['executable']} unlink [--e=<object> | --element=<object>] [--f | --force]
    {__info__['executable']} restore [--e=<object> | --element=<object>] [--f | --force]
    {__info__['executable']} repo (--check | --ls | --info)
    {__info__['executable']} find (--name=<object>)
    {__info__['executable']} config (--open | --view | --lang | --autoclean)
    {__info__['executable']} --help
    {__info__['executable']} --version
    {__info__['executable']} --credits

ARGUMENTS:
    {FG().CYAN}init{NONE} ----------- Creates the dotfiles repository.
    {FG().CYAN}find{NONE} ----------- Find some object in the Dotctrl repository.
    {FG().CYAN}pull{NONE} ----------- Pulls the dotfiles from the source location on the
                    machine to the repository.
    {FG().CYAN}link{NONE} ----------- Links the repository's dotfiles to the source location
                    on the machine.
    {FG().CYAN}repo{NONE} ----------- Show {__info__["name"]} repository information.
    {FG().CYAN}unlink{NONE} --------- Unlink the dotfiles from the repository with the original location
                    on the machine.
    {FG().CYAN}config{NONE} --------- Handles the configuration file.
    {FG().CYAN}restore{NONE} -------- Moves all dotfiles from the repository to the default source location.

OPTIONS:
    {FG().BLUE}--check{NONE} --------------------- Checks whether the dotfiles in the repository are linked to
                                the place of origin or not.
    {FG().BLUE}--e | --element <object>{NONE} ---- Receives an object without its absolute path, just the relative one.
    {FG().BLUE}--open{NONE} ---------------------- Open a file in edit mode.
    {FG().BLUE}--view{NONE} ---------------------- View the contents of a file in the terminal.
    {FG().BLUE}--git{NONE} ----------------------- Create a Git repository.
    {FG().BLUE}--auto{NONE} ---------------------- Creates the {__info__["name"]} repository automatically in the users
                                directory. On Linux it will create in "/home", on macOS in "/Users".
                                You must have super user permission.
    {FG().BLUE}--info{NONE} ---------------------- Shows detailed information for the Do Ctrl repository.
    {FG().BLUE}--ls{NONE} ------------------------ List all files and folders in the {__info__["name"]} repository.
    {FG().BLUE}--lang{NONE} ---------------------- Change the language of {__info__["name"]}.
    {FG().BLUE}--name <object>{NONE} ------------- Receives the name of an object, it can be a folder or a file.
    {FG().BLUE}--f | --force{NONE} --------------- Complete the command regardless of whether or not files exist.
                                ATTENTION! Using this option will replace existing files.
    {FG().BLUE}--autoclean{NONE} ----------------- Clear the {__info__["name"]} registry, if there is no element in the
                                repository.
    {FG().BLUE}--version{NONE} ------------------- Show version.
    {FG().BLUE}--credits{NONE} ------------------- Show credits.
    {FG().BLUE}--help{NONE} ---------------------- Show this screen.

{FG().CYAN}Documentation:{NONE} {__info__["home_page"]}
"""


class Menu(Base):
    def __init__(self, root: str, home: str) -> None:
        Base.__init__(self, root, home)

    @staticmethod
    def languages() -> dict:
        return {"pt_BR": PT_BR, "en_US": EN_US}

    # TODO: Error tests
    @property
    def menu(self) -> str:

        if exists(self.config_path):
            lang_current: str = get_key(self.parsed, "dotctrl", "config", "language")

            if not lang_current or lang_current not in self.languages().keys():
                return self.languages()["en_US"]
            return self.languages()[lang_current]
        else:
            return self.languages()["en_US"]

        # return self.languages()["en_US"]

    def args(self, argv: Any = None) -> dict:
        """Function to return the option menu arguments."""

        formatted_version: str = (
            f"{__info__['name']} version: " f"{FG().CYAN}{__info__['version']}{NONE}"
        )

        data: dict = docopt(self.menu, argv=argv, version=formatted_version)

        return data
