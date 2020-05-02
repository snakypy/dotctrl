from os.path import exists, join
from snakypy import FG, printer
from snakypy.ansi import NONE
from dotctrl.config.base import Base
from dotctrl.utils import check_init, listing_files


class ListCommand(Base):
    def __init__(self, root, home):
        Base.__init__(self, root, home)

    def main(self):
        """Method that lists the dotfiles in the repository."""
        check_init(self.ROOT)

        listing_data = list()
        objects = set([*listing_files(self.repo_path, only_rc_files=True), *self.data])
        for item in objects:
            if exists(join(self.repo_path, item)):
                listing_data.append(item)

        # listing_data = utils.listing_repo(self.repo, self.HOME, self.data)
        if len(list(listing_data)) == 0:
            return printer("Repository is empty. No elements.", foreground=FG.WARNING)
        printer(
            f"\nElements(s):", foreground=FG.CYAN,
        )
        for item in listing_data:
            print(f"{FG.CYAN}➜{NONE} {item}")
