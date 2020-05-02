from os import listdir
from os.path import exists, join, islink
from snakypy import FG, printer
from snakypy.ansi import NONE
from dotctrl.config.base import Base
from dotctrl.utils import check_init, listing_files


class CheckCommand(Base):
    # TODO: Unify "check" and "list" command
    def __init__(self, root, home):
        Base.__init__(self, root, home)

    def main(self):
        """Method to check if the repository's dotfiles are linked
             with their place of origin. If there is no list and information,
             the message Not linked"""
        check_init(self.ROOT)

        listing_data = list()
        objects = set([*listing_files(self.repo_path, only_rc_files=True), *self.data])
        for item in objects:
            if exists(join(self.repo_path, item)) and not islink(join(self.HOME, item)):
                listing_data.append(item)

        if len(listdir(self.repo_path)) == 0 or len(list(listing_data)) == 0:
            return printer("Nothing to check.", foreground=FG.FINISH)
        printer(
            f"\nElement(s):", foreground=FG.CYAN,
        )
        for item in listing_data:
            status = f"{FG.YELLOW}[Not linked]{NONE}"
            print(f"{FG.CYAN}➜{NONE} {item} {status}")
