from os.path import exists, islink, join
from snakypy import FG, printer
from dotctrl.config.base import Base
from dotctrl.utils import (
    check_init,
    path_creation,
    join_two,
    rm_garbage_config,
    add_element_config,
    to_move,
)


class PullCommand(Base):
    def __init__(self, root, home):
        Base.__init__(self, root, home)

    def main(self, arguments):
        """Method responsible for pulling the elements from the
        place of origin to the repository."""

        check_init(self.ROOT)

        rm_garbage_config(self.HOME, self.repo_path, self.config_path)

        if arguments["--element"]:
            file_home = join_two(self.HOME, arguments["--element"])
            file_repo = join_two(self.repo_path, arguments["--element"])
            if "/" in arguments["--element"]:
                path_creation(self.repo_path, arguments["--element"])
            add_element_config(file_home, arguments["--element"], self.config_path)
            if not exists(file_home) or islink(file_home):
                return printer(
                    "Nothing was pulled. Nonexistent element.", foreground=FG.ERROR
                )
            to_move(file_home, file_repo, arguments["--force"])
        else:
            if len(self.data) == 0:
                return printer(
                    "Nothing to pull, in droves. Empty list of elements.",
                    foreground=FG.WARNING,
                )
            for item in self.data:
                file_home = join(self.HOME, item)
                file_repo = join(self.repo_path, item)
                if "/" in item:
                    if not islink(file_home) and exists(file_home):
                        path_creation(self.repo_path, item)
                to_move(file_home, file_repo, arguments["--force"])
