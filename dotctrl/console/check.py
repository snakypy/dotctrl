import os
from os.path import exists, join, islink
from snakypy import FG, printer
from snakypy.ansi import NONE
from dotctrl.config import base
from dotctrl.console import utils


class Command(base.Base):
    def __init__(self, root, home):
        base.Base.__init__(self, root, home)

    def main(self):
        """Method to check if the repository's dotfiles are linked
             with their place of origin. If there is no list and information,
             the message Not linked"""
        utils.check_init(self.ROOT)

        listing_data = list()
        objects = [*utils.listing_files(self.repo_path, only_rc_files=True), *self.data]
        for item in objects:
            if exists(join(self.repo_path, item)) and not islink(join(self.HOME, item)):
                listing_data.append(item)

        if len(os.listdir(self.repo_path)) == 0 or len(list(listing_data)) == 0:
            return printer("Nothing to check.", foreground=FG.FINISH)
        printer(
            f"\nElement(s):", foreground=FG.CYAN,
        )
        for item in listing_data:
            status = f"{FG.YELLOW}[Not linked]{NONE}"
            print(f"{FG.CYAN}➜{NONE} {item} {status}")
