import os
from contextlib import suppress
from os.path import islink, join
from snakypy import FG, printer
from dotctrl.console import utils
from dotctrl.config import base


class Command(base.Base):
    def __init__(self, root, home):
        base.Base.__init__(self, root, home)

    def main(self, arguments):
        """Method to unlink point files from the repository
        with their place of origin."""
        utils.check_init(self.ROOT)

        utils.rm_garbage_config(self.HOME, self.repo_path, self.config_path)

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
            objects = [
                *utils.listing_files(self.repo_path, only_rc_files=True),
                *self.data,
            ]
            for item in objects:
                file_home = join(self.HOME, item)
                with suppress(Exception):
                    os.remove(file_home)
            if len(objects) == 0:
                printer(
                    "Nothing to unlinked, en masse. Empty list of elements.",
                    foreground=FG.WARNING,
                )
