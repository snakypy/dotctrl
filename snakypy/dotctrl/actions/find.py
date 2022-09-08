from os import walk
from os.path import join, isdir
from pydoc import pager

from snakypy.helpers import printer

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

        self.checking_init()

        if len(list(listing_objects(self.repo_path))) == 0:

            # Repository is empty. No elements.
            printer(self.cod["cod:02"], foreground=self.WARNING)

            return {"bool": False, "cod": "cod:02"}

        # The elements below are found in the Dotctrl directory. (Type "q" to exit)
        # [ Result: ]
        elements = [
            self.yellow(self.cod["cod:03"]),
            f"{self.cyan(self.cod['cod:w15'])}:\n",
        ]

        for item in listing_objects(self.repo_path):
            if arguments["--name"] == item.split("/")[-1]:

                # Element:
                if isdir(join(self.repo_path, item)):
                    elements.append(f"> {self.magenta(self.cod['cod:w14'])}: {item}")
                else:
                    elements.append(f"> {self.magenta(self.cod['cod:w10'])}: {item}")
            else:
                printer(self.cod["cod:04"], foreground=self.WARNING)

                return {"bool": False, "cod": "cod:04"}

        pager("\n".join(elements))

        return {"bool": True, "cod": "cod:03"}
