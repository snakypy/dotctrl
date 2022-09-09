from os import walk
from os.path import join, isdir
from pydoc import pager

from snakypy.helpers import printer

from snakypy.dotctrl.config.base import Base


def listing_objects(directory: str) -> list:
    objects: list = list()

    for root, directories, files in walk(directory):
        for file in files:
            filepath = join(root, file).replace(f"{directory}/", "")
            objects.append(filepath)

        for dir_ in directories:
            dirpath = join(root, dir_).replace(f"{directory}/", "")
            objects.append(dirpath)

    return objects


class FindCommand(Base):
    def __init__(self, root: str, home: str) -> None:
        Base.__init__(self, root, home)

    def main(self, arguments: dict) -> dict:

        if not self.checking_init():
            return {"status": False, "code": "28"}

        if len(list(listing_objects(self.repo_path))) == 0:

            # Repository is empty. No elements.
            printer(self.text["msg:02"], foreground=self.WARNING)

            return {"status": False, "code": "02"}

        # The elements below are found in the Dotctrl directory. (Type "q" to exit)
        # [ Result: ]
        elements: list = [
            self.yellow(self.text["msg:03"]),
            f"{self.cyan(self.text['word:15'])}:\n",
        ]

        for item in listing_objects(self.repo_path):
            if arguments["--name"] == item.split("/")[-1]:

                # Element:
                if isdir(join(self.repo_path, item)):
                    elements.append(f"> {self.magenta(self.text['word:14'])}: {item}")
                else:
                    elements.append(f"> {self.magenta(self.text['word:10'])}: {item}")
            else:
                printer(self.text["msg:04"], foreground=self.WARNING)

                return {"status": False, "code": "04"}

        pager("\n".join(elements))

        return {"status": True, "code": "03"}
