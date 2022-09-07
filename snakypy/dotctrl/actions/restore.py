from genericpath import isdir, isfile
from os.path import exists, join, islink
from shutil import move
from sys import exit


from snakypy.helpers.os import rmdir_blank
from snakypy.helpers import printer

from snakypy.dotctrl.config.base import Base, Options
from snakypy.dotctrl.utils import (
    listing_files,
    path_creation,
    remove_objects,
    is_repo_symbolic_link,
)
from snakypy.dotctrl.utils import pick


class RestoreCommand(Base, Options):
    def __init__(self, root, home):
        Base.__init__(self, root, home)
        Options.__init__(self)

    def not_errors(self, element_origin: str, element_repo: str, force: bool) -> bool:

        if not exists(element_repo):

            # Operation aborted!
            printer(self.cod["cod:45"], foreground=self.ERROR)

            # Element not found in repository to restore.
            printer(self.cod["cod:38"], foreground=self.WARNING)

            return False

        if (
            islink(element_origin)
            and not is_repo_symbolic_link(element_origin, element_repo)
            and not force
        ):

            self.error_symlink(element_origin)
            return False

        if (
            exists(element_repo)
            and not islink(element_origin)
            and (isfile(element_origin) or isdir(element_origin))
            and not force
        ):
            # Operation aborted!
            printer(self.cod["cod:45"], foreground=self.ERROR)

            # TODO: [Adicionar o texto do print AQUI]
            printer(self.cod["cod:44"], element_origin, foreground=self.WARNING)
            return False

        return True

    def mass_verification(self, objects: list, force: bool) -> bool:

        for item in objects:
            element_origin = join(self.home, item)
            element_repo = join(self.repo_path, item)
            if not self.not_errors(element_origin, element_repo, force):
                return False

        return True

    def restore(self, element_origin: str, element_repo: str):

        if exists(element_repo):
            remove_objects(element_origin)
            move(element_repo, element_origin)
            rmdir_blank(self.repo_path)

    def main(self, arguments: dict) -> None:
        """Method to restore dotfiles from the repository to their
        original location."""

        self.checking_init()

        element = self.element(arguments)
        force = self.force(arguments)

        if element:
            element_origin = join(self.home, element)
            element_repo = join(self.repo_path, element)
            if "/" in element:
                path_creation(self.home, element)

            if self.not_errors(element_origin, element_repo, force):
                self.restore(element_origin, element_repo)

                # Complete restoration!
                printer(self.cod["cod:46"], foreground=self.FINISH)

        # Not use option --element (--e) [bulk]
        else:
            title_ = self.cod["cod:41"]
            options_ = [self.cod["cod:w08"], self.cod["cod:w09"]]

            reply = pick(
                title_,
                options_,
                index=True,
                cancel_msg=self.cod["cod:42"],
                opt_msg=self.cod["cod:43"],
            )

            if reply is not None and reply[0] == 1:

                # Canceled by user.
                printer(self.cod["cod:42"], foreground=self.WARNING)

                exit(0)

            elif reply is not None and reply[0] == 0:

                objects = [*listing_files(self.repo_path), *self.data]

                # Empty repository. Nothing to restore.
                if len(objects) == 0:

                    # Empty repository. Nothing to restore.
                    printer(self.cod["cod:40"], foreground=self.WARNING)

                    exit(0)

                if self.mass_verification(objects, force):
                    for item in objects:
                        element_origin = join(self.home, item)
                        element_repo = join(self.repo_path, item)

                        if "/" in item:
                            path_creation(self.home, item)

                        self.restore(element_origin, element_repo)

                    # Complete restoration!
                    printer(self.cod["cod:46"], foreground=self.FINISH)
