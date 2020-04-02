"""Dotctrl main module, where everything happens."""
# Quick and Dirty, then refinery. :)
import os
import pydoc
import shutil
import subprocess
import snakypy
from sys import exit
from os.path import join, exists, islink
from docopt import docopt
from contextlib import suppress
from snakypy import printer, FG
from snakypy.ansi import NONE
from dotctrl import __version__, __pkginfo__
from dotctrl import utils, config


# # Debug
# from pdb import set_trace


class Data:
    """Class to store data"""

    def __init__(self, root, home):
        self.ROOT = root
        self.HOME = home
        self.repo = join(self.ROOT, "dotctrl")
        self.config = join(self.ROOT, __pkginfo__["config"])
        self.gitignore = join(self.ROOT, ".gitignore")
        self.readme = join(self.ROOT, "README.md")
        self.text_editors = [
            ".config/Code/User/settings.json",
            ".config/Code/User/locale.json",
            ".atom/config.cson",
            ".atom/github.cson",
            ".atom/snippets.cson",
            ".config/sublime-text-3/Packages/User/" "Preferences.sublime-settings",
            ".config/sublime-text-3/Packages/User/" "Package Control.sublime-settings",
            ".config/sublime-text-3/Packages/User/" "Distraction Free.sublime-settings",
        ]

        if exists(self.config):
            try:
                self.parsed = snakypy.json.read(self.config)
                self.elements = [*self.parsed["dotctrl"]["elements"]]
                self.rc_status = self.parsed["dotctrl"]["smart"]["rc"]["enable"]
                self.text_editors_status = self.parsed["dotctrl"]["smart"][
                    "text_editors"
                ]["enable"]
            except Exception as err:
                printer(
                    "An error occurred while reading the configuration file.",
                    err,
                    foreground=FG.ERROR,
                )
                exit(1)

            rc = utils.listing_files(self.HOME, only_rc=True)
            if self.rc_status and self.text_editors_status:
                self.data = rc + self.text_editors + self.elements
            elif self.rc_status and not self.text_editors_status:
                self.data = rc + self.elements
            elif not self.rc_status and self.text_editors_status:
                self.data = self.text_editors + self.elements
            else:
                self.data = self.elements


class Utils(Data):
    def __init__(self, root, home):
        Data.__init__(self, root, home)

    @staticmethod
    def path_creation(root, item):
        """Create repository for file with a path"""
        # A condição é para não criar pastas vazias.
        # if not islink(join(self.HOME, item)) and exists(join(self.HOME, item)):
        path_split = item.split("/")[:-1]
        path_str = "/".join(path_split)
        path = join(root, path_str)
        snakypy.path.create(path)
        return str(path)
        # return

    def listing_repo(self, check_islink=False):
        """Method lists the dotfiles in the repository and checks whether
        they are linked."""
        listing_data = list()
        data = (*utils.listing_files(self.repo, only_rc=True), *self.data)
        # data = self.data
        for item in data:
            if check_islink:
                if exists(join(self.repo, item)) and not islink(join(self.HOME, item)):
                    listing_data.append(item)
            else:
                if exists(join(self.repo, item)):
                    listing_data.append(item)
        return listing_data

    def restore_conditions(self, src, dst, arguments):
        if utils.exists_levels(src, dst, arguments) == 0:
            printer(
                "The files match the repository and the drive. " "User --force.",
                foreground=FG.WARNING,
            )
            exit(0)
        if utils.exists_levels(src, dst, arguments) == 1:
            utils.rm_objects(src)
            shutil.move(dst, src)
            snakypy.os.rmdir_blank(self.repo)
        if utils.exists_levels(src, dst, arguments) == 2:
            shutil.move(dst, src)
            snakypy.os.rmdir_blank(self.repo)


class Dotctrl(Utils):
    """Main class Dotctrl"""

    def __init__(self, root, home):
        Utils.__init__(self, root, home)

    @staticmethod
    def menu_opts():
        """Option menu assembly function"""
        opts = f"""
{__pkginfo__['name']} version: {FG.CYAN}{__version__}{NONE}

{__pkginfo__['name']} - Managing your dotfiles on Linux.

USAGE:
    {__pkginfo__['executable']} init
    {__pkginfo__['executable']} check
    {__pkginfo__['executable']} list
    {__pkginfo__['executable']} pull [--element=<object>] [--force]
    {__pkginfo__['executable']} link [--element=<object>] [--force]
    {__pkginfo__['executable']} unlink [--element=<object>]
    {__pkginfo__['executable']} config (--open | --view)
    {__pkginfo__['executable']} restore [--element=<object>] [--force]
    {__pkginfo__['executable']} --help
    {__pkginfo__['executable']} --version
    {__pkginfo__['executable']} --credits

ARGUMENTS:
    {FG.CYAN}init{NONE} ----------- Creates the dotfiles repository.
    {FG.CYAN}check{NONE} ---------- Checks whether the dotfiles in the
                     repository are linked to the place of origin or not.
    {FG.CYAN}list{NONE} ----------- Lists all files present in the repository
                     and in the configuration.
    {FG.CYAN}pull{NONE} ----------- Pulls the dotfiles from the source location
                     on the machine to the repository.
    {FG.CYAN}link{NONE} ----------- Links the repository's dotfiles to the source
                     location on the machine.
    {FG.CYAN}unlink{NONE} --------- Unlink the dotfiles from the repository with
                     the original location on the machine.
    {FG.CYAN}config{NONE} --------- Open or view settings.
    {FG.CYAN}restore{NONE} -------- Moves all dotfiles from the repository to the
                     default source location.

OPTIONS:
    {FG.BLUE}--help{NONE} ---------------- Show this screen.
    {FG.BLUE}--element=<object>{NONE} ---- Receive an object where, have the absolute
                            path to a file or folder, always from the HOME directory.
    {FG.BLUE}--open{NONE} ---------------- Open the configuration file in edit mode and
                            perform the automatic update when you exit.
    {FG.BLUE}--view{NONE} ---------------- View the configuration file on the terminal.
    {FG.BLUE}--version{NONE} ------------- Show version.
    {FG.BLUE}--credits{NONE} ------------- Show credits.
        """
        return opts

    def arguments(self, argv=None):
        """Function to return the option menu arguments."""
        formatted_version = (
            f"{__pkginfo__['name']} version: " f"{FG.CYAN}{__version__}{NONE}"
        )
        data = docopt(self.menu_opts(), argv=argv, version=formatted_version)
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

    def init_command(self):
        """Base repository method."""
        if exists(self.config):
            printer("Repository is already defined.", foreground=FG.FINISH)
            exit(0)
        snakypy.path.create(self.repo)
        snakypy.json.create(config.config_rc_content, self.config, force=True)
        snakypy.file.create(config.readme_content, self.readme, force=True)
        snakypy.file.create(config.gitignore_content, self.gitignore, force=True)
        utils.git_init()
        printer(
            f"Initialized {__pkginfo__['name']} repository in {self.repo}",
            foreground=FG.FINISH,
        )

    def config_command(self):
        """Method for opening or viewing the configuration file."""

        utils.cheking_init(self.ROOT)

        def action(editor_terminal):
            if shutil.which(editor_terminal):
                get_editor = os.environ.get("EDITOR", editor_terminal)
                with open(self.config) as f:
                    subprocess.call([get_editor, f.name])
                    exit(0)
            return

        if self.arguments()["--open"]:
            editor = self.parsed["dotctrl"]["config"]["editor"]
            if editor:
                action(editor)
            else:
                editors = ["vim", "nano", "emacs", "micro"]
                for editor in editors:
                    action(editor)

        if self.arguments()["--view"]:
            read_config = snakypy.file.read(self.config)
            pydoc.pager(read_config)

    def list_command(self):
        """Method that lists the dotfiles in the repository."""
        utils.cheking_init(self.ROOT)

        listing_data = self.listing_repo()
        if len(list(listing_data)) == 0:
            return printer("Repository is empty. No elements.", foreground=FG.YELLOW)
        printer(
            f"\nListing in: ./{self.repo.split('/')[-1]}\n\nObjects:",
            foreground=FG.CYAN,
        )
        for item in listing_data:
            print(f"{FG.CYAN}➜{NONE} {item}")

    def check_command(self):
        """Method to check if the repository's dotfiles are linked
            with their place of origin. If there is no list and information,
            the message Not linked"""
        utils.cheking_init(self.ROOT)
        if len(os.listdir(self.repo)) == 0:
            return printer("Nothing to do.", foreground=FG.FINISH)
        listing_data = self.listing_repo(check_islink=True)
        if len(list(listing_data)) == 0:
            return printer("Nothing to link.", foreground=FG.FINISH)
        printer(
            f"\nObjects in: ./{self.repo.split('/')[-1]}", foreground=FG.CYAN,
        )
        for item in listing_data:
            status = f"{FG.YELLOW}[Not linked]{NONE}"
            print(f"{FG.CYAN}➜{NONE} {item} {status}")

    def unlink_command(self, arguments=None):
        """Method to unlink point files from the repository
        with their place of origin."""
        utils.cheking_init(self.ROOT)
        if arguments["--element"]:
            file_home = join(self.HOME, arguments["--element"])
            with suppress(Exception):
                os.remove(file_home)
        else:
            data = (*utils.listing_files(self.repo, only_rc=True), *self.data)
            for item in data:
                file_home = join(self.HOME, item)
                with suppress(Exception):
                    os.remove(file_home)

    def pull_command(self, arguments=None):
        utils.cheking_init(self.ROOT)
        utils.clear_config_garbage(self.HOME, self.repo, self.config)
        if arguments["--element"]:
            file_home = join(self.HOME, arguments["--element"])
            file_repo = join(self.repo, arguments["--element"])
            if "/" in arguments["--element"]:
                self.path_creation(self.repo, arguments["--element"])
            utils.add_element_config(file_home, arguments["--element"], self.config)
            utils.to_move(file_home, file_repo, arguments["--force"])
        else:
            for item in self.data:
                file_home = join(self.HOME, item)
                file_repo = join(self.repo, item)
                if "/" in item:
                    if not islink(file_home) and exists(file_home):
                        self.path_creation(self.repo, item)
                utils.to_move(file_home, file_repo, arguments["--force"])

    def link_command(self, arguments=None):
        utils.cheking_init(self.ROOT)
        if arguments["--element"]:
            file_home = join(self.HOME, arguments["--element"])
            file_repo = join(self.repo, arguments["--element"])
            if "/" in arguments["--element"]:
                self.path_creation(self.HOME, arguments["--element"])
            utils.create_symlink(file_repo, file_home, arguments["--force"])
        else:
            data = (*utils.listing_files(self.repo, only_rc=True), *self.data)
            for item in data:
                if "/" in item:
                    self.path_creation(self.HOME, item)
                file_home = join(self.HOME, item)
                file_repo = join(self.repo, item)
                utils.create_symlink(file_repo, file_home, arguments["--force"])

    def restore_command(self, arguments=None):
        """Method to restore dotfiles from the repository to their
        original location."""
        utils.cheking_init(self.ROOT)
        if arguments["--element"]:
            file_home = join(self.HOME, arguments["--element"])
            file_repo = join(self.repo, arguments["--element"])
            if "/" in arguments["--element"]:
                self.path_creation(self.HOME, arguments["--element"])
            self.restore_conditions(file_home, file_repo, self.arguments)
        else:
            data = (*utils.listing_files(self.repo, only_rc=True), *self.data)
            for item in data:
                file_home = join(self.HOME, item)
                file_repo = join(self.repo, item)
                if "/" in item:
                    self.path_creation(self.HOME, item)
                self.restore_conditions(file_home, file_repo, self.arguments)
        utils.clear_config_garbage(self.HOME, self.repo, self.config)
