from os import listdir
from os.path import exists, isdir, islink, join
from typing import Any

from snakypy.helpers import FG, printer
from snakypy.helpers.ansi import NONE

from snakypy.dotctrl.config.base import Base
from snakypy.dotctrl.utils import check_init, listing_files


class CheckCommand(Base):
    def __init__(self, root, home):
        Base.__init__(self, root, home)

    @property
    def listing_data(self) -> Any:
        for item in {*listing_files(self.repo_path, only_rc_files=True), *self.data}:
            if exists(join(self.repo_path, item)) and not islink(join(self.HOME, item)):
                yield item

    def main(self) -> bool:
        """Method to check if the repository's dotfiles are linked
        with their place of origin. If there is no list and information,
        the message Not linked"""
        check_init(self.ROOT)

        if len(listdir(self.repo_path)) == 0 or len(list(self.listing_data)) == 0:
            printer("Nothing to check.", foreground=FG().FINISH)
            return True
        printer(
            "\nElement(s):",
            foreground=FG().CYAN,
        )
        for item in self.listing_data:
            status = f"{FG().YELLOW}[Not linked]{NONE}"
            if isdir(join(self.repo_path, item)):
                print(f"{FG().CYAN}➜{FG().MAGENTA} Directory: {NONE}{item} {status}")
            else:
                print(f"{FG().CYAN}➜{FG().MAGENTA} File: {NONE}{item} {status}")

        return False
