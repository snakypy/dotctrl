from concurrent.futures import ThreadPoolExecutor
from os.path import exists, join
from shutil import move
from sys import exit
from typing import Union

from snakypy.helpers import FG, printer
from snakypy.helpers.files import create_json, read_json
from snakypy.helpers.os import rmdir_blank

from snakypy.dotctrl.config.base import Base
from snakypy.dotctrl.utils import (
    check_init,
    listing_files,
    path_creation,
    remove_objects,
    shorten_path,
)

# --keep-record


def restore_action(
    repo_path: str, src: str, dst: str, force: Union[None, bool]
) -> None:
    """Function presents the possibilities of options for restored
    # the elements."""
    if not exists(src) and not force:
        printer(
            f'The element "{str(shorten_path(src, 1))}" not found in '
            f"repository to be restored. Review the configuration file, "
            f"or use other option.",
            foreground=FG().WARNING,
        )
        exit(0)

    if exists(src) and exists(dst) and not force:
        printer(
            "Elements correspond to the repository and the place of origin. "
            "User --force or --f.",
            foreground=FG().WARNING,
        )
        exit(0)

    if exists(src) and exists(dst) and force:
        remove_objects(dst)
        move(src, dst)
        rmdir_blank(repo_path)
    elif exists(src) and not exists(dst):
        move(src, dst)
        rmdir_blank(repo_path)


def keep_record(arguments: dict, config: str, obj: str) -> None:
    if not arguments["--keep-record"]:
        parsed = read_json(config)
        elements = parsed["dotctrl"]["elements"]
        if obj in elements:
            elements.remove(obj)
            parsed["dotctrl"]["elements"] = elements
            create_json(parsed, config, force=True)


class RestoreCommand(Base):
    def __init__(self, root, home):
        Base.__init__(self, root, home)

    @staticmethod
    def element(arguments: dict) -> str:
        if arguments["--element"]:
            return arguments["--element"]
        return arguments["--e"]

    @staticmethod
    def force(arguments: dict) -> Union[None, bool]:
        if arguments["--force"]:
            return arguments["--force"]
        return arguments["--f"]

    def main(self, arguments: dict) -> None:
        """Method to restore dotfiles from the repository to their
        original location."""

        check_init(self.ROOT)

        # Uncomment to remove the element from the registry.
        # rm_garbage_config(self.HOME, self.repo_path, self.config_path, only_repo=True)

        element = self.element(arguments)
        force = self.force(arguments)

        if element:
            file_home = join(self.HOME, element)
            file_repo = join(self.repo_path, element)
            if "/" in element:
                path_creation(self.HOME, element)
            with ThreadPoolExecutor() as e:
                e.submit(restore_action, self.repo_path, file_repo, file_home, force)
                e.submit(keep_record, arguments, self.config_path, element)
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
                    e.submit(
                        restore_action, self.repo_path, file_repo, file_home, force
                    )
                    e.submit(keep_record, arguments, self.config_path, item)
            if len(objects) == 0:
                printer(
                    "Empty repository. Nothing to restore.", foreground=FG().WARNING
                )
