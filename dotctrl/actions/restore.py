from shutil import move
from snakypy.utils.os import rmdir_blank
from os.path import exists, join
from sys import exit
from snakypy import FG, printer
from dotctrl.config.base import Base
from dotctrl.console.utils import (
    check_init,
    path_creation,
    rm_garbage_config,
    listing_files,
    rm_objects,
)


def restore_args(repo, src, dst, arguments):
    """Function presents the possibilities of options for restored
    the elements."""
    if exists(src) and exists(dst) and not arguments["--force"]:
        printer(
            "The files match the repository and the drive. User --force.",
            foreground=FG.WARNING,
        )
        exit(0)
    elif exists(src) and exists(dst) and arguments["--force"]:
        rm_objects(dst)
        move(src, dst)
        rmdir_blank(repo)
    elif exists(src) and not exists(dst):
        move(src, dst)
        rmdir_blank(repo)
    else:
        printer(
            f'The element "{src}" not found in repository to be restored.'
            f" Review the configuration file, or use other option.",
            foreground=FG.WARNING,
        )


class RestoreCommand(Base):
    def __init__(self, root, home):
        Base.__init__(self, root, home)

    def main(self, arguments):
        """Method to restore dotfiles from the repository to their
        original location."""

        check_init(self.ROOT)

        # Uncomment to remove the element from the registry.
        # rm_garbage_config(self.HOME, self.repo_path, self.config_path, only_repo=True)

        if arguments["--element"]:
            file_home = join(self.HOME, arguments["--element"])
            file_repo = join(self.repo_path, arguments["--element"])
            if "/" in arguments["--element"]:
                path_creation(self.HOME, arguments["--element"])
            restore_args(self.repo_path, file_repo, file_home, arguments)
        else:
            objects = [
                *listing_files(self.repo_path, only_rc_files=True),
                *self.data,
            ]
            for item in objects:
                file_home = join(self.HOME, item)
                file_repo = join(self.repo_path, item)
                if "/" in item:
                    path_creation(self.HOME, item)
                restore_args(self.repo_path, file_repo, file_home, arguments)
            if len(objects) == 0:
                printer("Empty repository. Nothing to restore.", foreground=FG.WARNING)