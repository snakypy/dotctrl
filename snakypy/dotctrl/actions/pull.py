from os.path import exists, islink, join

from snakypy.helpers import FG, printer

from snakypy.dotctrl.config.base import Base
from snakypy.dotctrl.utils import (
    add_element_config,
    check_init,
    join_two,
    path_creation,
    rm_garbage_config,
    to_move,
)


class PullCommand(Base):
    def __init__(self, root, home):
        Base.__init__(self, root, home)

    @staticmethod
    def force(arguments: dict) -> dict:
        if arguments["--force"]:
            return arguments["--force"]
        return arguments["--f"]

    @staticmethod
    def element(arguments: dict) -> dict:
        if arguments["--element"]:
            return arguments["--element"]
        return arguments["--e"]

    def main(self, arguments: dict) -> bool:
        """Method responsible for pulling the elements from the
        place of origin to the repository."""

        check_init(self.ROOT)

        rm_garbage_config(self.HOME, self.repo_path, self.config_path)

        element = self.element(arguments)
        force = self.force(arguments)

        if element:
            file_home = join_two(self.HOME, element)
            file_repo = join_two(self.repo_path, element)
            if "/" in element:
                path_creation(self.repo_path, element)
            add_element_config(file_home, element, self.config_path)
            if not exists(file_home) or islink(file_home):
                printer(
                    "Nothing was pulled. Nonexistent element.", foreground=FG().ERROR
                )
                return False
            to_move(file_home, file_repo, force)
            return True
        else:
            if len(self.data) == 0:
                printer(
                    "Nothing to pull, in droves. Empty list of elements.",
                    foreground=FG().WARNING,
                )
                return False
            for item in self.data:
                file_home = join(self.HOME, item)
                file_repo = join(self.repo_path, item)
                if "/" in item:
                    if not islink(file_home) and exists(file_home):
                        path_creation(self.repo_path, item)
                to_move(file_home, file_repo, force)
            return True
