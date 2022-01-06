from os import walk
from os.path import isdir, join
from pydoc import pager

from snakypy.helpers import FG, NONE, printer

from snakypy.dotctrl.config.base import Base


def listing_objects(directory) -> list:
    objects = list()
    for root, directories, files in walk(directory):
        for file in files:
            objects.append(join(root, file))
        for dir_ in directories:
            objects.append(join(root, dir_))
    return objects


class FindCommand(Base):
    def __init__(self, root, home):
        Base.__init__(self, root, home)

    def main(self, arguments: dict):
        if len(list(listing_objects(self.repo_path))) == 0:
            printer("Repository is empty. No elements.", foreground=FG().WARNING)
            return False
        elements = [f'{FG().CYAN}[ Search: ] (Type "q" to exit) {NONE}']
        for item in listing_objects(self.repo_path):
            if arguments["--name"] == item.split("/")[-1]:
                if isdir(item):
                    elements.append(
                        f"{FG().CYAN}➜{FG().MAGENTA} Directory: {NONE}{item}"
                    )
                else:
                    elements.append(f"{FG().CYAN}➜{FG().MAGENTA} File: {NONE}{item}")
        pager("\n".join(elements))
        return True
