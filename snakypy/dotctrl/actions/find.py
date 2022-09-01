from os import walk
from os.path import join
from pydoc import pager
from snakypy.dotctrl import __info__

from snakypy.helpers import FG, NONE, printer

from snakypy.dotctrl.config.base import Base


def listing_objects(directory) -> list:
    objects = list()

    for root, directories, files in walk(directory):
        for file in files:
            filepath = join(root, file).replace(f"{directory}/", "")
            objects.append(filepath)

        for dir_ in directories:
            dirpath = join(root, dir_).replace(f"{directory}/", "")
            objects.append(dirpath)

    return objects


class FindCommand(Base):
    def __init__(self, root, home):
        Base.__init__(self, root, home)

    def main(self, arguments: dict):
        if len(list(listing_objects(self.repo_path))) == 0:
            printer("Repository is empty. No elements.", foreground=FG().WARNING)
            return False

        elements = [
            f"{FG().YELLOW}[!] The elements below are found in the "
            f'"{FG().MAGENTA}{self.repo_path}{FG().YELLOW}" directory of {__info__["name"]}:',
            f'\n{FG().CYAN}[ Search: ] (Type "q" to exit) {NONE}',
        ]

        for item in listing_objects(self.repo_path):
            if arguments["--name"] == item.split("/")[-1]:
                elements.append(f"{FG().CYAN}➜{FG().MAGENTA} Element: {NONE}{item}")

        pager("\n".join(elements))
        return True
