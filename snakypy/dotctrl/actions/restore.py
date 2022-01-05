from concurrent.futures import ThreadPoolExecutor
from os.path import exists, join
from shutil import move
from sys import exit

from snakypy.helpers import FG, printer
from snakypy.helpers.os import rmdir_blank

from snakypy.dotctrl.config.base import Base
from snakypy.dotctrl.utils import (  # rm_garbage_config
    check_init,
    listing_files,
    path_creation,
    remove_objects,
    shorten_path,
)


def restore_action(repo_path: str, src: str, dst: str, arguments: dict) -> None:
    """Function presents the possibilities of options for restored
    # the elements."""
    if not exists(src) and not arguments["--force"]:
        printer(
            f'The element "{str(shorten_path(src, 1))}" not found in '
            f"repository to be restored. Review the configuration file, "
            f"or use other option.",
            foreground=FG().WARNING,
        )
        exit(0)

    if exists(src) and exists(dst) and not arguments["--force"]:
        printer(
            "Elements correspond to the repository and the place of origin. "
            "User --force.",
            foreground=FG().WARNING,
        )
        exit(0)

    if exists(src) and exists(dst) and arguments["--force"]:
        remove_objects(dst)
        move(src, dst)
        rmdir_blank(repo_path)
    elif exists(src) and not exists(dst):
        move(src, dst)
        rmdir_blank(repo_path)


class RestoreCommand(Base):
    def __init__(self, root, home):
        Base.__init__(self, root, home)

    def main(self, arguments: dict) -> None:
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
            with ThreadPoolExecutor() as e:
                e.submit(restore_action, self.repo_path, file_repo, file_home, arguments)
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
                with ThreadPoolExecutor() as e:
                    e.submit(restore_action, self.repo_path, file_repo, file_home, arguments)
            if len(objects) == 0:
                printer(
                    "Empty repository. Nothing to restore.", foreground=FG().WARNING
                )
