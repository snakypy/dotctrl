from contextlib import suppress
from os import remove
from os.path import islink, join
from sys import exit

from snakypy.helpers import FG, printer

from snakypy.dotctrl.config.base import Base
from snakypy.dotctrl.utils import check_init, join_two, listing_files, rm_garbage_config


class UnlinkCommand(Base):
    def __init__(self, root, home):
        Base.__init__(self, root, home)

    def main(self, arguments: dict) -> bool:
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
            printer(
                f'Element "{file_home}" not unlinked. Element not found.',
                foreground=FG().ERROR,
            )
            return False
        else:
            objects = [
                *listing_files(self.repo_path, only_rc_files=True),
                *self.data,
            ]
            for item in objects:
                file_home = join(self.HOME, item)
                if not islink(file_home) and not arguments["--force"]:
                    printer(
                        "Unlinked elements were found. Use the --element option "
                        "to unlink unique links or use --force.",
                        foreground=FG().WARNING,
                    )
                    exit(0)
                if islink(file_home):
                    with suppress(Exception):
                        remove(file_home)
            if len(objects) == 0:
                printer(
                    "Nothing to unlinked, en masse. Empty list of elements.",
                    foreground=FG().WARNING,
                )
                return False
            return True
