from contextlib import suppress
from os import remove
from os.path import exists, islink, join

from snakypy.helpers import printer

from snakypy.dotctrl.config.base import Base, Options
from snakypy.dotctrl.utils import is_repo_symbolic_link, join_two


def unlinks_to_do(data: list, repo_dir: str, home_dir: str):
    objects: list = list()

    for item in {*data}:
        elem_repo: str = join(repo_dir, item)
        elem_home: str = join(home_dir, item)

        if islink(elem_home) and exists(elem_repo):
            objects.append(elem_repo.replace(f"{repo_dir}/", ""))

    return objects


class UnlinkCommand(Base, Options):
    def __init__(self, root: str, home: str) -> None:
        Base.__init__(self, root, home)
        Options.__init__(self)

    def main(self, arguments: dict) -> dict:
        """Method to unlink point files from the repository
        with their place of origin."""

        if not self.checking_init():
            return {"status": False, "code": "28"}

        element = self.element(arguments)
        force = self.force(arguments)

        # Use option --element (--e)
        if element:
            element_repo: str = join(self.repo_path, element)
            element_home: str = join(self.home, element)

            if (
                islink(element_home)
                and is_repo_symbolic_link(element_home, element_repo) is False
                and not force
            ):
                out: dict = self.error_symlink(element_home)
                return out

            element_home_: str = join_two(self.home, element)

            if islink(element_home_):
                with suppress(Exception):
                    remove(element_home_)

                    # Element unlinked successfully!
                    printer(self.text["msg:12"], foreground=self.FINISH)

                    return {"status": True, "code": "12"}

            # Element not found.
            printer(
                self.text["msg:29"],
                f"({self.text['word:12']}: {element_home_}).",
                foreground=self.ERROR,
            )

            return {"status": False, "code": "29"}

        # Not use option --element (--e)
        if len(unlinks_to_do(self.data, self.repo_path, self.home)) == 0:

            # Nothing for bulk unlinked.
            printer(self.text["msg:30"], foreground=self.WARNING)

            return {"status": False, "code": "30"}

        else:
            for item in unlinks_to_do(self.data, self.repo_path, self.home):
                element_home = join(self.home, item)

                if islink(element_home):
                    with suppress(Exception):
                        remove(element_home)

            # Massively unlinked links successfully!
            printer(self.text["msg:31"], foreground=self.FINISH)

            return {"status": True, "code": "31"}
