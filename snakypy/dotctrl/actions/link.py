from os.path import islink, join
from sys import exit
from typing import Union

from snakypy.helpers import FG, printer

from snakypy.dotctrl.config.base import Base
from snakypy.dotctrl.utils import (
    check_init,
    create_symlink,
    listing_files,
    path_creation,
    rm_garbage_config,
)


class LinkCommand(Base):
    def __init__(self, root, home):
        Base.__init__(self, root, home)

    @staticmethod
    def force(arguments: dict) -> Union[None, bool]:
        if arguments["--force"]:
            return arguments["--force"]
        return arguments["--f"]

    @staticmethod
    def element(arguments: dict) -> str:
        if arguments["--element"]:
            return arguments["--element"]
        return arguments["--e"]

    def main(self, arguments: dict) -> None:
        """Method responsible for creating symbolic links from the
        repository to the place of origin of the elements."""

        rm_garbage_config(self.HOME, self.repo_path, self.config_path)

        check_init(self.ROOT)

        element = self.element(arguments)
        force = self.force(arguments)

        if element:
            file_home = join(self.HOME, element)
            file_repo = join(self.repo_path, element)
            if "/" in element:
                path_creation(self.HOME, element)
            if islink(file_home) and not force:
                printer(
                    "This symbolic link already exists. Use the --force or --f"
                    " option to recreate.",
                    foreground=FG().WARNING,
                )
                exit(0)
            status = create_symlink(file_repo, file_home, force)
            if not status:
                printer(
                    f'Element "{file_repo}" not linked. Review the same in the repository.',
                    foreground=FG().ERROR,
                )
        else:
            data_ = (
                *listing_files(self.repo_path, only_rc_files=True),
                *self.data,
            )
            for item in data_:
                if "/" in item:
                    path_creation(self.HOME, item)
                file_home = join(self.HOME, item)
                file_repo = join(self.repo_path, item)
                create_symlink(file_repo, file_home, force)
            if len(data_) == 0:
                printer(
                    "Nothing to linked, en masse. Empty repository.",
                    foreground=FG().WARNING,
                )
