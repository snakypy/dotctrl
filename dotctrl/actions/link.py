from sys import exit
from os.path import join, islink
from snakypy import FG, printer
from dotctrl.config.base import Base
from dotctrl.utils import (
    check_init,
    rm_garbage_config,
    path_creation,
    create_symlink,
    listing_files,
)


class LinkCommand(Base):
    def __init__(self, root, home):
        Base.__init__(self, root, home)

    def main(self, arguments):
        """Method responsible for creating symbolic links from the
        repository to the place of origin of the elements."""

        rm_garbage_config(self.HOME, self.repo_path, self.config_path)

        check_init(self.ROOT)

        if arguments["--element"]:
            file_home = join(self.HOME, arguments["--element"])
            file_repo = join(self.repo_path, arguments["--element"])
            if "/" in arguments["--element"]:
                path_creation(self.HOME, arguments["--element"])
            if islink(file_home) and not arguments["--force"]:
                printer(
                    "This symbolic link already exists. Use the --force"
                    " option to recreate.",
                    foreground=FG.WARNING,
                )
                exit(0)
            status = create_symlink(file_repo, file_home, arguments["--force"])
            if not status:
                printer(
                    f'Element "{file_repo}" not linked. Review the same in the repository.',
                    foreground=FG.ERROR,
                )
        else:
            data_ = (
                *listing_files(self.repo_path, only_rc_files=True),
                *self.data,
            )
            for item in data_:
                if "/" in item:
                    path_creation(self.HOME, item)
                file_home = join(self.HOME, item)
                file_repo = join(self.repo_path, item)
                create_symlink(file_repo, file_home, arguments["--force"])
            if len(data_) == 0:
                printer(
                    "Nothing to linked, en masse. Empty repository.",
                    foreground=FG.WARNING,
                )
