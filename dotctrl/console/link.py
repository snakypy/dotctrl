from os.path import join
from snakypy import FG, printer
from dotctrl.config import base
from dotctrl.console import utils


class Command(base.Base):
    def __init__(self, root, home):
        base.Base.__init__(self, root, home)

    def main(self, arguments):
        """Method responsible for creating symbolic links from the
        repository to the place of origin of the elements."""

        utils.rm_garbage_config(self.HOME, self.repo_path, self.config_path)

        utils.check_init(self.ROOT)

        if arguments["--element"]:
            file_home = join(self.HOME, arguments["--element"])
            file_repo = join(self.repo_path, arguments["--element"])
            if "/" in arguments["--element"]:
                utils.path_creation(self.HOME, arguments["--element"])
            status = utils.create_symlink(file_repo, file_home, arguments["--force"])
            if not status:
                printer(
                    f'Element "{file_repo}" not linked. Review the same in the repository.',
                    foreground=FG.ERROR,
                )
        else:
            data_ = (
                *utils.listing_files(self.repo_path, only_rc_files=True),
                *self.data,
            )
            for item in data_:
                if "/" in item:
                    utils.path_creation(self.HOME, item)
                file_home = join(self.HOME, item)
                file_repo = join(self.repo_path, item)
                utils.create_symlink(file_repo, file_home, arguments["--force"])
            if len(data_) == 0:
                printer(
                    "Nothing to linked, en masse. Empty repository.",
                    foreground=FG.WARNING,
                )
