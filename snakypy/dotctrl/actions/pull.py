from genericpath import isfile
from os.path import exists, islink, join
from snakypy.helpers import printer
from snakypy.dotctrl.config.base import Base, Options
from snakypy.dotctrl.utils import (
    add_element_config,
    join_two,
    path_creation,
    to_move,
)


def pulled_to_do(data, home_path):
    objects = list()

    for item in {*data}:
        elem_home = join(home_path, item)
        if exists(elem_home) and not islink(elem_home):
            objects.append(elem_home.replace(f"{home_path}/", ""))
    return objects


class PullCommand(Base, Options):
    def __init__(self, root, home):
        Base.__init__(self, root, home)
        Options.__init__(self)

    def main(self, arguments: dict):
        """Method responsible for pulling the elements from the
        place of origin to the repository."""

        self.checking_init()

        element = self.element(arguments)
        force = self.force(arguments)

        # If you use the --element flag (--e)
        if element:
            file_home = join_two(self.home, element)
            file_repo = join_two(self.repo_path, element)

            if "/" in element:
                path_creation(self.repo_path, element)

            add_element_config(file_home, element, self.config_path)

            if not exists(file_home) or islink(file_home):

                # Nothing was pulled. Nonexistent element.
                printer(self.cod["cod:16"], foreground=self.ERROR)

                return {"bool": False, "cod": "cod:16"}

            if isfile(file_home) and isfile(file_repo) and not force:

                # TODO: [Adicionar o texto do print AQUI]
                printer(self.cod["cod:37"], foreground=self.WARNING)

                return {"bool": False, "cod": "cod:37"}

            to_move(file_home, file_repo)

            # Element(s) pulled successfully!
            printer(self.cod["cod:18"], foreground=self.FINISH)

            return {"bool": True, "cod": "cod:18"}

        # If you don't use the --element flag (--e)
        if len(pulled_to_do(self.data, self.home)) == 0:

            # Nothing to pull, in droves.
            printer(self.cod["cod:17"], foreground=self.WARNING)

            return {"bool": False, "cod": "cod:17"}

        for item in self.data:
            file_home = join(self.home, item)
            file_repo = join(self.repo_path, item)

            if "/" in item:
                if not islink(file_home) and exists(file_home):
                    path_creation(self.repo_path, item)

            if isfile(file_home) and isfile(file_repo) and not force:

                # TODO: [Adicionar o texto do print AQUI]
                printer(self.cod["cod:37"], foreground=self.WARNING)

                return {"bool": False, "cod": "cod:37"}

            to_move(file_home, file_repo)

        # Element(s) pulled successfully!
        printer(self.cod["cod:18"], foreground=self.FINISH)

        return {"bool": True, "cod": "cod:18"}
