from os.path import exists, isdir, join
from typing import Any

from snakypy.helpers import FG, printer
from snakypy.helpers.ansi import NONE

from snakypy.dotctrl.config.base import Base
from snakypy.dotctrl.utils import check_init, listing_files


class ListCommand(Base):
    def __init__(self, root, home):
        Base.__init__(self, root, home)

    @property
    def listing_data(self) -> Any:
        for item in {*listing_files(self.repo_path, only_rc_files=True), *self.data}:
            if exists(join(self.repo_path, item)):
                yield item

    def main(self) -> bool:
        """Method that lists the dotfiles in the repository."""
        check_init(self.ROOT)

        if len(list(self.listing_data)) == 0:
            printer("Repository is empty. No elements.", foreground=FG().WARNING)
            return False
        printer(
            "\nElements(s):",
            foreground=FG().CYAN,
        )
        for item in self.listing_data:
            if isdir(join(self.repo_path, item)):
                print(f"{FG().CYAN}➜{FG().MAGENTA} Directory: {NONE}{item}")
            else:
                print(f"{FG().CYAN}➜{FG().MAGENTA} File: {NONE}{item}")
        return True
