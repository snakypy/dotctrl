from os.path import exists, islink, join

from genericpath import isfile
from snakypy.helpers import printer

from snakypy.dotctrl.config.base import Base, Options
from snakypy.dotctrl.utils import (
    add_element_config,
    is_repo_symbolic_link,
    join_two,
    path_creation,
    to_move,
)


def pulled_to_do(data: list, home_path: str) -> list:
    objects: list = list()

    for item in {*data}:
        elem_home: str = join(home_path, item)

        if exists(elem_home) and not islink(elem_home):
            objects.append(elem_home.replace(f"{home_path}/", ""))

    return objects


class PullCommand(Base, Options):
    def __init__(self, root: str, home: str) -> None:
        Base.__init__(self, root, home)
        Options.__init__(self)

    def main(self, arguments: dict) -> dict:
        """Method responsible for pulling the elements from the
        place of origin to the repository."""

        if not self.checking_init():
            return {"status": False, "code": "28"}

        element: dict = self.element(arguments)
        force: dict = self.force(arguments)

        # If you use the --element flag (--e)
        if element:
            file_home: str = join_two(self.home, element)
            file_repo: str = join_two(self.repo_path, element)

            if "/" in element:
                path_creation(self.repo_path, element)

            add_element_config(file_home, element, self.config_path)

            if not exists(file_home) or islink(file_home):

                # Nothing was pulled. Nonexistent element.
                printer(self.text["msg:16"], foreground=self.ERROR)

                return {"status": False, "code": "16"}

            if isfile(file_home) and isfile(file_repo) and not force:

                # Elements with the same name were found in the repository
                # Dotctrl and in the source location. These elements are not linked to the repository of the
                # Dotctrl.
                # To replace those in the Dotctrl repository, use the --force (--f) option.
                printer(self.text["msg:37"], foreground=self.WARNING)

                return {"status": False, "code": "37"}

            to_move(file_home, file_repo)

            # Element(s) pulled successfully!
            printer(self.text["msg:18"], foreground=self.FINISH)

            return {"status": True, "code": "18"}

        # If you don't use the --element flag (--e)
        if len(pulled_to_do(self.data, self.home)) == 0:

            # Nothing to pull, in droves.
            printer(self.text["msg:17"], foreground=self.WARNING)

            return {"status": False, "code": "17"}

        for item in self.data:
            file_home = join(self.home, item)
            file_repo = join(self.repo_path, item)

            if "/" in item:
                if not islink(file_home) and exists(file_home):
                    path_creation(self.repo_path, item)

            if (
                not is_repo_symbolic_link(file_home, file_repo)
                and isfile(file_home)
                and isfile(file_repo)
                and not force
            ):

                # Elements with the same name were found in the repository
                # Dotctrl and in the source location. These elements are not linked to the repository of the
                # Dotctrl.
                # To replace those in the Dotctrl repository, use the --force (--f) option.
                printer(self.text["msg:37"], foreground=self.WARNING)

                return {"status": False, "code": "37"}

            to_move(file_home, file_repo)

        # Element(s) pulled successfully!
        printer(self.text["msg:18"], foreground=self.FINISH)

        return {"status": True, "code": "18"}
