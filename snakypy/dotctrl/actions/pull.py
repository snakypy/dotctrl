from os.path import exists, islink, join

from snakypy.helpers import FG, printer

from snakypy.dotctrl.config.base import Base, ElementForce
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


class PullCommand(Base, ElementForce):
    def __init__(self, root, home):
        Base.__init__(self, root, home)
        ElementForce.__init__(self)

    def main(self, arguments: dict) -> bool:
        """Method responsible for pulling the elements from the
        place of origin to the repository."""

        element = self.element(arguments)
        force = self.force(arguments)

        # If you use the --element flag (--e)
        if element:
            file_home = join_two(self.HOME, element)
            file_repo = join_two(self.repo_path, element)

            if "/" in element:
                path_creation(self.repo_path, element)

            add_element_config(file_home, element, self.config_path)

            if not exists(file_home) or islink(file_home):

                # TODO: [Adicionar o texto do print AQUI]
                printer(f"{self.msg['str:16']}", foreground=FG().ERROR)
                return False

            to_move(file_home, file_repo, self.msg["str:37"], force)
            return True

        # If you don't use the --element flag (--e)
        if len(pulled_to_do(self.data, self.HOME)) == 0:
            # TODO: [Adicionar o texto do print AQUI]
            printer(f"{self.msg['str:17']}", foreground=FG().WARNING)
            return False

        for item in self.data:
            file_home = join(self.HOME, item)
            file_repo = join(self.repo_path, item)
            if "/" in item:
                if not islink(file_home) and exists(file_home):
                    path_creation(self.repo_path, item)
            to_move(file_home, file_repo, self.msg["str:37"], force)

        # TODO: [Adicionar o texto do print AQUI]
        printer(f"{self.msg['str:18']}", foreground=FG().FINISH)
        return True
