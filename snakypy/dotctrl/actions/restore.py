from os.path import exists, islink, join
from shutil import move

from snakypy.helpers import printer
from snakypy.helpers.os import rmdir_blank

from snakypy.dotctrl.config.base import Base, Options
from snakypy.dotctrl.utils import (
    is_repo_symbolic_link,
    path_creation,
    pick,
    remove_objects,
)


class RestoreCommand(Base, Options):
    def __init__(self, root: str, home: str) -> None:
        Base.__init__(self, root, home)
        Options.__init__(self)

    def not_errors(self, element_origin: str, element_repo: str, force: bool) -> dict:

        if not exists(element_repo):

            # Operation aborted!
            printer(self.text["msg:45"], foreground=self.ERROR)

            # Element not found in repository to restore.
            printer(self.text["msg:38"], foreground=self.WARNING)

            return {"status": False, "code": "38"}

        if (
            islink(element_origin)
            and not is_repo_symbolic_link(element_origin, element_repo)
            and not force
        ):

            out: dict = self.error_symlink(element_origin)
            return out

        if (
            exists(element_repo)
            and exists(element_origin)
            and islink(element_origin) is False
            and not force
        ):

            # Operation aborted!
            printer(self.text["msg:45"], foreground=self.ERROR)

            # Dotctrl FOUND an element at source location with
            # same name as the repository as Dotctrl, and this prevented it from proceeding with the restore.
            # If you want to replace it with the repository element Dotctrl,
            # run this command again with the --force (--f) option.
            # Note: If you use the --force (--f) option, this element
            # found (and more) will be removed.
            # We recommend that you verify this (and other) element(s) before proceeding with the --force (--f) option.
            #
            # Element found:
            printer(self.text["msg:44"], element_origin, foreground=self.WARNING)

            return {"status": False, "code": "44"}

        return {"status": True, "str": "success"}

    def mass_verification(self, objects: list, force: bool) -> dict:

        for item in objects:
            element_origin: str = join(self.home, item)
            element_repo: str = join(self.repo_path, item)

            checking: dict = self.not_errors(element_origin, element_repo, force)

            if not checking["status"]:
                break

        return checking

    def restore(self, element_origin: str, element_repo: str) -> None:

        if exists(element_repo):
            remove_objects(element_origin)
            move(element_repo, element_origin)

        return None

    def main(self, arguments: dict) -> dict:
        """Method to restore dotfiles from the repository to their
        original location."""

        if not self.checking_init():
            return {"status": False, "code": "28"}

        element = self.element(arguments)
        force = self.force(arguments)

        if element:
            element_origin = join(self.home, element)
            element_repo = join(self.repo_path, element)
            if "/" in element:
                path_creation(self.home, element)

            checking: dict = self.not_errors(element_origin, element_repo, force)

            if checking["status"]:
                self.restore(element_origin, element_repo)
                rmdir_blank(self.repo_path)

                # Complete restoration!
                printer(self.text["msg:46"], foreground=self.FINISH)

                return {"status": True, "code": "46"}

            return checking

        # Not use option --element (--e) [bulk]
        else:
            # objects: list = [*listing_files(self.repo_path), *self.data]
            objects: list = self.data

            # Empty repository. Nothing to restore.
            if len(objects) == 0:

                # Empty repository. Nothing to restore.
                printer(self.text["msg:40"], foreground=self.WARNING)

                return {"status": False, "code": "40"}

            title_: str = self.text["msg:41"]
            options_: list[str] = [self.text["word:08"], self.text["word:09"]]

            reply = pick(
                title_,
                options_,
                index=True,
                cancel_msg=self.text["msg:42"],
                invalid_msg=self.text["msg:43"],
            )

            if reply is not None and reply[0] == 1:

                # Canceled by user.
                printer(self.text["msg:42"], foreground=self.WARNING)

                return {"status": False, "code": "42"}

            elif reply is not None and reply[0] == 0:

                checking = self.mass_verification(objects, force)

                if checking["status"]:
                    for item in objects:
                        element_origin = join(self.home, item)
                        element_repo = join(self.repo_path, item)

                        if "/" in item:
                            path_creation(self.home, item)

                        self.restore(element_origin, element_repo)

                    rmdir_blank(self.repo_path)

                    # Complete restoration!
                    printer(self.text["msg:46"], foreground=self.FINISH)

                    return {"status": True, "code": "46"}

                return checking

        return {"status": None}
