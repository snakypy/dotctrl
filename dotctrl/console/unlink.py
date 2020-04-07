from os import remove
from contextlib import suppress
from os.path import islink, join
from snakypy import FG, printer
from dotctrl.config.base import Base
from dotctrl.console.utils import (
    check_init,
    rm_garbage_config,
    listing_files,
    join_two,
)


class UnlinkCommand(Base):
    def __init__(self, root, home):
        Base.__init__(self, root, home)

    def main(self, arguments):
        """Method to unlink point files from the repository
        with their place of origin."""
        check_init(self.ROOT)

        rm_garbage_config(self.HOME, self.repo_path, self.config_path)

        if arguments["--element"]:
            file_home = join_two(self.HOME, arguments["--element"])
            if islink(file_home):
                with suppress(Exception):
                    remove(file_home)
                    return True
            return printer(
                f'Element "{file_home}" not unlinked. Element not found.',
                foreground=FG.ERROR,
            )
        else:
            objects = [
                *listing_files(self.repo_path, only_rc_files=True),
                *self.data,
            ]
            for item in objects:
                file_home = join(self.HOME, item)
                with suppress(Exception):
                    remove(file_home)
            if len(objects) == 0:
                printer(
                    "Nothing to unlinked, en masse. Empty list of elements.",
                    foreground=FG.WARNING,
                )
