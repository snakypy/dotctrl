"""Dotctrl main module, where everything happens."""
import os
import pydoc
import shutil
import subprocess
import snakypy
import tomlkit
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
                self.config_rc = snakypy.file.read(self.config)
                self.parsed = tomlkit.parse(self.config_rc)
                self.elements = [*self.parsed["dotctrl"]["elements"]]
                self.rc_status = self.parsed["dotctrl"]["smart"]["rc"]["enable"]
                self.text_editors_status = self.parsed["dotctrl"]["smart"][
                    "text_editors"
                ]["enable"]
            except Exception as err:
                printer(
                    "An error occurred while reading the configuration" "file.",
                    err,
                    foreground=FG.ERROR,
                )
                exit(1)

            rc = utils.listing_rc(self.HOME)
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

    def path_creation(self, item):
        """Create repository for file with a path"""
        if not islink(join(self.HOME, item)) and exists(join(self.HOME, item)):
            path_split = item.split("/")[:-1]
            path_str = "/".join(path_split)
            path = join(self.repo, path_str)
            snakypy.path.create(path)
            return path
        return

    def pull_link_action(
        self,
        data,
        *,
        use_move=False,
        use_link=False,
        use_path_creation=False,
        force=False,
    ):
        """Method with action of moving dotfiles to the repository
        and linking with links to them"""
        for item in data:
            if use_move and use_path_creation:
                # if path := self.path_creation(item):
                if self.path_creation(item) is not None:
                    utils.to_move(
                        join(self.HOME, item),
                        join(self.repo, self.path_creation(item)),
                        force=force,
                    )
            elif use_move and not use_path_creation:
                utils.to_move(join(self.HOME, item), join(self.repo, item), force=force)
            if use_link:
                utils.create_symlink(
                    join(self.repo, item), join(self.HOME, item), force=force
                )

    def listing_repo(self, check_islink=False):
        """Method lists the dotfiles in the repository and checks whether
        they are linked."""
        listing_data = list()
        data = (*utils.listing_rc(self.repo), *self.data)
        for item in data:
            if check_islink:
                if exists(join(self.repo, item)) and not islink(join(self.HOME, item)):
                    listing_data.append(item)
            else:
                if exists(join(self.repo, item)):
                    listing_data.append(item)
        return listing_data


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
    {__pkginfo__['executable']} pull
    {__pkginfo__['executable']} link
    {__pkginfo__['executable']} unlink
    {__pkginfo__['executable']} config (--open | --view)
    {__pkginfo__['executable']} restore [--force]
    {__pkginfo__['executable']} --help
    {__pkginfo__['executable']} --version
    {__pkginfo__['executable']} --credits

ARGUMENTS:
    {FG.CYAN}init{NONE} ----------- Creates the dotfiles repository.
    {FG.CYAN}check{NONE} ---------- Checks whether the dotfiles in the
                     repository are linked to the place of origin or not.
    {FG.CYAN}list{NONE} ----------- Lists all dot files in the repository.
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
    {FG.BLUE}--help{NONE} --------- Show this screen.
    {FG.BLUE}--open{NONE} --------- Open the configuration file in edit mode and
                     perform the automatic update when you exit.
    {FG.BLUE}--view{NONE} --------- View the configuration file on the terminal.
    {FG.BLUE}--version{NONE} ------ Show version.
    {FG.BLUE}--credits{NONE} ------ Show credits.
        """
        return opts

    def arguments(self, argv=None):
        """Function to return the option menu arguments."""
        formatted_version = (
            f"{__pkginfo__['name']} version: " f"{FG.CYAN}{__version__}{NONE}"
        )
        data = docopt(self.menu_opts(), argv=argv, version=formatted_version)
        return data

    def init_command(self):
        """Base repository method."""
        if exists(self.config):
            printer("Repository is already defined.", foreground=FG.FINISH)
            exit(0)
        snakypy.path.create(self.repo)
        utils.create_file(config.config_rc_content, self.config, config_toml=True)
        utils.create_file(config.gitignore_content, self.gitignore)
        utils.create_file(config.readme_content, self.readme)
        printer(
            f"Initialized {__pkginfo__['name']} repository in {self.repo}",
            foreground=FG.FINISH,
        )

    def config_command(self):
        """Method for opening or viewing the configuration file."""

        utils.cheking_init(self.ROOT)

        if self.arguments()["--open"]:
            editors = ["vim", "nano", "emacs"]
            for editor in editors:
                if shutil.which(editor):
                    get_editor = os.environ.get("EDITOR", editor)
                    with open(self.config) as f:
                        subprocess.call([get_editor, f.name])
                        printer("Done!", foreground=FG.FINISH)
                    return True
            return

        if self.arguments()["--view"]:
            read_config = snakypy.file.read(self.config)
            pydoc.pager(read_config)

    def list_command(self):
        """Method that lists the dotfiles in the repository."""
        utils.cheking_init(self.ROOT)

        listing_data = self.listing_repo()
        if len(list(listing_data)) == 0:
            return printer("Repository is empty. No dotfiles.", foreground=FG.YELLOW)
        printer(
            f"\nListing in: ./{self.repo.split('/')[-1]}\n\nElements:",
            foreground=FG.CYAN,
        )
        for item in listing_data:
            print(f"{FG.CYAN}➜{NONE} {item}")

    def check_command(self):
        """Method to check if the repository's dotfiles are linked
        with their place of origin. If there is no list and information, the message
        "Not linked"""
        utils.cheking_init(self.ROOT)

        if len(os.listdir(self.repo)) == 0:
            return printer("Nothing to do.", foreground=FG.FINISH)
        listing_data = self.listing_repo(check_islink=True)
        if len(list(listing_data)) == 0:
            return printer("Everything is OK.", foreground=FG.FINISH)
        printer(
            f"\nListing in: ./{self.repo.split('/')[-1]}\n\nElements:",
            foreground=FG.CYAN,
        )
        for item in listing_data:
            status = f"{FG.YELLOW}[Not linked]{NONE}"
            print(f"{FG.CYAN}➜{NONE} {item} {status}")

    def unlink_command(self):
        """Method to unlink point files from the repository
        with their place of origin."""
        utils.cheking_init(self.ROOT)

        check = set()
        data = (*utils.listing_rc(self.repo), *self.data)
        for item in data:
            file_home = join(self.HOME, item)
            file_repo = join(self.repo, item)
            if islink(file_home) and exists(file_repo):
                check.add(True)
                with suppress(Exception):
                    os.remove(file_home)
        status = len(list(check))
        if status:
            return printer("Done! Unlinked repository files.", foreground=FG.FINISH)
        printer("Nothing to do.", foreground=FG.FINISH)

    def pull_link_command(self, *, use_link=False, use_move=False, force=False):
        """Method that pulls the files from the source to the repository and also
        links the files from the repository with the source location."""
        utils.cheking_init(self.ROOT)

        only_element = []
        only_folder = []
        elements_subdir = []
        directory_subdir = []
        data = [*utils.listing_rc(self.repo), *self.data]
        for item in data:
            if "/" in item:
                utils.append_dir_file(
                    join(self.HOME, item), item, directory_subdir, elements_subdir
                )
            else:
                utils.append_dir_file(
                    join(self.HOME, item), item, only_folder, only_element
                )
        self.pull_link_action(
            only_element, use_move=use_move, use_link=use_link, force=force
        )
        self.pull_link_action(
            only_folder, use_move=use_move, use_link=use_link, force=force
        )
        self.pull_link_action(
            elements_subdir,
            use_move=use_move,
            use_link=use_link,
            force=force,
            use_path_creation=True,
        )
        self.pull_link_action(
            directory_subdir,
            use_move=use_move,
            use_link=use_link,
            force=force,
            use_path_creation=True,
        )
        if len(os.listdir(self.repo)) == 0:
            return printer("Nothing to do.", foreground=FG.FINISH)
        printer("Done!", foreground=FG.FINISH)

    def restore_command(self):
        """Method to restore dotfiles from the repository to their
        original location."""
        utils.cheking_init(self.ROOT)

        check = set()
        data = (*utils.listing_rc(self.repo), *self.data)
        for item in data:
            file_home = join(self.HOME, item)
            file_repo = join(self.repo, item)

            if utils.exists_levels(file_home, file_repo, self.arguments) == 0:
                printer(
                    "The files match the repository and the drive. " "User --force.",
                    foreground=FG.WARNING,
                )
                exit(0)

            if utils.exists_levels(file_home, file_repo, self.arguments) == 1:
                check.add(True)
                utils.rm_objects(file_home)
                shutil.move(file_repo, file_home)
                snakypy.os.rmdir_blank(self.repo)

            if utils.exists_levels(file_home, file_repo, self.arguments) == 2:
                check.add(True)
                shutil.move(file_repo, file_home)
                snakypy.os.rmdir_blank(self.repo)

        status = len(list(check))
        if status:
            return printer("Done! Everything was reset.", foreground=FG.FINISH)
        printer("Nothing to do.", foreground=FG.FINISH)
