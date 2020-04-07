import shutil
import snakypy
from os.path import exists, join
from sys import exit
from snakypy import FG, printer
from dotctrl.console import utils
from dotctrl.config import base


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
        utils.rm_objects(dst)
        shutil.move(src, dst)
        snakypy.os.rmdir_blank(repo)
    elif exists(src) and not exists(dst):
        shutil.move(src, dst)
        snakypy.os.rmdir_blank(repo)
    else:
        printer(
            f'Restore failed. Element "{src}" not found in repository.',
            foreground=FG.ERROR,
        )
        exit(1)


class Command(base.Base):
    def __init__(self, root, home):
        base.Base.__init__(self, root, home)

    def main(self, arguments):
        """Method to restore dotfiles from the repository to their
        original location."""

        utils.check_init(self.ROOT)

        utils.rm_garbage_config(
            self.HOME, self.repo_path, self.config_path, only_repo=True
        )

        if arguments["--element"]:
            file_home = join(self.HOME, arguments["--element"])
            file_repo = join(self.repo_path, arguments["--element"])
            if "/" in arguments["--element"]:
                utils.path_creation(self.HOME, arguments["--element"])
            restore_args(self.repo_path, file_repo, file_home, arguments)
        else:
            objects = [
                *utils.listing_files(self.repo_path, only_rc_files=True),
                *self.data,
            ]
            for item in objects:
                file_home = join(self.HOME, item)
                file_repo = join(self.repo_path, item)
                if "/" in item:
                    utils.path_creation(self.HOME, item)
                restore_args(self.repo_path, file_repo, file_home, arguments)
            if len(objects) == 0:
                printer("Empty repository. Nothing to restore.", foreground=FG.WARNING)
