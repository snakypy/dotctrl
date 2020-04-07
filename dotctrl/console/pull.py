from os.path import exists, islink, join
from snakypy import FG, printer
from dotctrl.console import utils
from dotctrl.config import base


class Command(base.Base):
    def __init__(self, root, home):
        base.Base.__init__(self, root, home)

    def main(self, arguments):
        """Method responsible for pulling the elements from the
        place of origin to the repository."""

        utils.check_init(self.ROOT)

        utils.rm_garbage_config(self.HOME, self.repo_path, self.config_path)

        if arguments["--element"]:
            file_home = utils.join_two(self.HOME, arguments["--element"])
            file_repo = utils.join_two(self.repo_path, arguments["--element"])
            if "/" in arguments["--element"]:
                utils.path_creation(self.repo_path, arguments["--element"])
            status = utils.add_element_config(
                file_home, arguments["--element"], self.config_path
            )
            if status:
                return utils.to_move(file_home, file_repo, arguments["--force"])
            return printer(
                "Nothing was pulled. Nonexistent element.", foreground=FG.ERROR
            )
        else:
            for item in self.data:
                file_home = join(self.HOME, item)
                file_repo = join(self.repo_path, item)
                if "/" in item:
                    if not islink(file_home) and exists(file_home):
                        utils.path_creation(self.repo_path, item)
                utils.to_move(file_home, file_repo, arguments["--force"])
            if len(self.data) == 0:
                printer(
                    "Nothing to pull, in droves. Empty list of elements.",
                    foreground=FG.WARNING,
                )
