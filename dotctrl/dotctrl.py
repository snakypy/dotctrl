"""Dotctrl main module, where everything happens."""
# Quick and Dirty, then refinery. :)
# TODO: Use SOLID Metodology
import os
import pydoc
import shutil
import subprocess
import snakypy
from contextlib import suppress
from os.path import exists, islink, join
from sys import exit
from docopt import docopt
from snakypy import FG, printer
from snakypy.ansi import NONE
from dotctrl import __pkginfo__, __version__, config, utils
from dotctrl.ransom import Ransom
from dotctrl.menu import menu_opts


class Dotctrl(Ransom):
    """Main class Dotctrl"""

    def __init__(self, root, home):
        Ransom.__init__(self, root, home)

    @staticmethod
    def arguments(argv=None):
        """Function to return the option menu arguments."""
        formatted_version = (
            f"{__pkginfo__['name']} version: " f"{FG.CYAN}{__version__}{NONE}"
        )
        data = docopt(menu_opts, argv=argv, version=formatted_version)
        return data

    @staticmethod
    def credence():
        utils.show_billboard()
        snakypy.console.credence(
            __pkginfo__["name"],
            __version__,
            __pkginfo__["home_page"],
            __pkginfo__,
            foreground=FG.CYAN,
        )

    def init_command(self, arguments):
        """Base repository method."""
        if exists(self.config):
            printer("Repository is already defined.", foreground=FG.FINISH)
            exit(0)
        snakypy.path.create(self.repo)
        snakypy.json.create(config.config_content, self.config, force=True)
        snakypy.file.create(config.readme_content, self.readme, force=True)
        if arguments["--git"]:
            utils.git_init()
            snakypy.file.create(config.gitignore_content, self.gitignore, force=True)
        printer(
            f"Initialized {__pkginfo__['name']} repository in {self.repo}",
            foreground=FG.FINISH,
        )

    def config_command(self, arguments):
        """Method for opening or viewing the configuration file."""
        utils.cheking_init(self.ROOT)

        def action(editor):
            if shutil.which(editor):
                get_editor = os.environ.get("EDITOR", editor)
                with open(self.config) as f:
                    subprocess.call([get_editor, f.name])
                    exit(0)
            return

        if arguments["--open"]:
            editor_conf = self.parsed["dotctrl"]["config"]["editor"]
            if editor_conf:
                action(editor_conf)
            else:
                editors = ["vim", "nano", "emacs", "micro"]
                for edt in editors:
                    action(edt)

        if arguments["--view"]:
            read_config = snakypy.file.read(self.config)
            pydoc.pager(read_config)

    def listing_repo(self, check_linked=False):
        """Method lists the dotfiles in the repository and checks whether
        they are linked."""
        listing_data = list()
        data = [*utils.listing_files(self.repo, only_rc=True), *self.data]
        for item in data:
            if check_linked:
                if exists(join(self.repo, item)) and not islink(join(self.HOME, item)):
                    listing_data.append(item)
            else:
                if exists(join(self.repo, item)):
                    listing_data.append(item)
        return listing_data

    def list_command(self):
        """Method that lists the dotfiles in the repository."""
        utils.cheking_init(self.ROOT)

        listing_data = self.listing_repo()
        if len(list(listing_data)) == 0:
            return printer("Repository is empty. No elements.", foreground=FG.WARNING)
        printer(
            f"\nElements(s):", foreground=FG.CYAN,
        )
        for item in listing_data:
            print(f"{FG.CYAN}➜{NONE} {item}")

    def check_command(self):
        """Method to check if the repository's dotfiles are linked
            with their place of origin. If there is no list and information,
            the message Not linked"""
        utils.cheking_init(self.ROOT)
        listing_data = self.listing_repo(check_linked=True)
        if len(os.listdir(self.repo)) == 0 or len(list(listing_data)) == 0:
            return printer("Nothing to check.", foreground=FG.FINISH)
        printer(
            f"\nElement(s):", foreground=FG.CYAN,
        )
        for item in listing_data:
            status = f"{FG.YELLOW}[Not linked]{NONE}"
            print(f"{FG.CYAN}➜{NONE} {item} {status}")

    def unlink_command(self, arguments):
        """Method to unlink point files from the repository
        with their place of origin."""
        utils.cheking_init(self.ROOT)
        if arguments["--element"]:
            file_home = utils.join_two(self.HOME, arguments["--element"])
            if islink(file_home):
                with suppress(Exception):
                    os.remove(file_home)
                    return True
            return printer(
                f'Element "{file_home}" not unlinked. Element not found.',
                foreground=FG.ERROR,
            )
        else:
            data = [*utils.listing_files(self.repo, only_rc=True), *self.data]
            for item in data:
                file_home = join(self.HOME, item)
                with suppress(Exception):
                    os.remove(file_home)
            if len(data) == 0:
                printer(
                    "Nothing to unlinked, en masse. Empty list of elements.",
                    foreground=FG.WARNING,
                )

    def pull_command(self, arguments):
        """Method responsible for pulling the elements from the
        place of origin to the repository."""

        utils.cheking_init(self.ROOT)

        if arguments["--element"]:
            file_home = utils.join_two(self.HOME, arguments["--element"])
            file_repo = utils.join_two(self.repo, arguments["--element"])
            if "/" in arguments["--element"]:
                utils.path_creation(self.repo, arguments["--element"])
            status = utils.add_element_config(
                file_home, arguments["--element"], self.config
            )
            if status:
                return utils.to_move(file_home, file_repo, arguments["--force"])
            return printer(
                "Nothing was pulled. Nonexistent element.", foreground=FG.ERROR
            )
        else:
            for item in self.data:
                file_home = join(self.HOME, item)
                file_repo = join(self.repo, item)
                if "/" in item:
                    if not islink(file_home) and exists(file_home):
                        utils.path_creation(self.repo, item)
                utils.to_move(file_home, file_repo, arguments["--force"])
            if len(self.data) == 0:
                printer(
                    "Nothing to pull, in droves. Empty list of elements.",
                    foreground=FG.WARNING,
                )

    def link_command(self, arguments):
        """Method responsible for creating symbolic links from the
        repository to the place of origin of the elements."""
        utils.cheking_init(self.ROOT)
        if arguments["--element"]:
            file_home = join(self.HOME, arguments["--element"])
            file_repo = join(self.repo, arguments["--element"])
            if "/" in arguments["--element"]:
                utils.path_creation(self.HOME, arguments["--element"])
            status = utils.create_symlink(file_repo, file_home, arguments["--force"])
            if not status:
                printer(
                    f'Element "{file_repo}" not linked. Review the same in the repository.',
                    foreground=FG.ERROR,
                )
        else:
            data = (*utils.listing_files(self.repo, only_rc=True), *self.data)
            for item in data:
                if "/" in item:
                    utils.path_creation(self.HOME, item)
                file_home = join(self.HOME, item)
                file_repo = join(self.repo, item)
                utils.create_symlink(file_repo, file_home, arguments["--force"])
            if len(data) == 0:
                printer(
                    "Nothing to linked, en masse. Empty repository.",
                    foreground=FG.WARNING,
                )

    def restore_command(self, arguments):
        """Method to restore dotfiles from the repository to their
        original location."""

        utils.cheking_init(self.ROOT)

        utils.update_config(self.HOME, self.repo, self.config, only_repo=True)

        if arguments["--element"]:
            file_home = join(self.HOME, arguments["--element"])
            file_repo = join(self.repo, arguments["--element"])
            if "/" in arguments["--element"]:
                utils.path_creation(self.HOME, arguments["--element"])
            utils.restore_args(self.repo, file_repo, file_home, self.arguments)
        else:
            data = [*utils.listing_files(self.repo, only_rc=True), *self.data]
            for item in data:
                file_home = join(self.HOME, item)
                file_repo = join(self.repo, item)
                if "/" in item:
                    utils.path_creation(self.HOME, item)
                utils.restore_args(self.repo, file_repo, file_home, self.arguments)
            if len(data) == 0:
                printer("Empty repository. Nothing to restore.", foreground=FG.WARNING)

    def remove_command(self, arguments):
        """Method of removing elements from the repository and
        symbolic links linked to them. Calls other methods and functions
        that also perform other actions."""

        def rm_elements(home, repo, item):
            if exists(join(repo, item)):
                if islink(join(home, item)):
                    with suppress(Exception):
                        os.remove(join(home, item))
                with suppress(Exception):
                    os.remove(join(repo, item))

        option = utils.remove_opts(self.ROOT, self.repo, self.data, arguments)
        if option is None:
            printer("Aborted by user.", foreground=FG.WARNING)
        elif option and option[0] != "all":
            rm_elements(self.HOME, self.repo, option[0])
        elif option and option[0] == "all":
            for i in option[1]:
                rm_elements(self.HOME, self.repo, i)
            snakypy.os.rmdir_blank(self.repo)

        utils.update_config(self.HOME, self.repo, self.config)
