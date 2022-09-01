from contextlib import suppress
from os import remove
from os.path import islink, join, exists

from snakypy.helpers import FG, printer

from snakypy.dotctrl.config.base import Base, ElementForce
from snakypy.dotctrl.utils import (
    check_init,
    join_two,
    rm_garbage_config,
    is_repo_symbolic_link,
)
from snakypy.dotctrl import __info__


def unlinks_to_do(data, repo_dir, home_dir):
    objects = list()
    for item in {*data}:
        elem_repo = join(repo_dir, item)
        elem_home = join(home_dir, item)
        if islink(elem_home) and exists(elem_repo):
            objects.append(elem_repo.replace(f"{repo_dir}/", ""))
    return objects


class UnlinkCommand(Base, ElementForce):
    def __init__(self, root, home):
        Base.__init__(self, root, home)
        ElementForce.__init__(self)

    def main(self, arguments: dict) -> bool:
        """Method to unlink point files from the repository
        with their place of origin."""

        check_init(self.ROOT)

        rm_garbage_config(self.HOME, self.repo_path, self.config_path)

        element = self.element(arguments)
        force = self.force(arguments)

        # Use option --element (--e)
        if element:
            elem_repo = join(self.repo_path, element)
            elem_home = join(self.HOME, element)

            if (
                exists(elem_home)
                and is_repo_symbolic_link(elem_home, elem_repo) is False
                and not force
            ):
                printer(
                    f"{__info__['name']} found links in the source location, but they are not "
                    f"from the {__info__['name']} repository. If you want to turn it off, "
                    "use the --force (--f) option.",
                    foreground=FG().WARNING,
                )
                return False

            file_home = join_two(self.HOME, element)
            if islink(file_home):
                with suppress(Exception):
                    remove(file_home)
                    return True

            printer(
                f'Element "{file_home}" not unlinked. Element not found.',
                foreground=FG().ERROR,
            )
            return False

        # Not use option --element (--e)
        if len(unlinks_to_do(self.data, self.repo_path, self.HOME)) == 0:
            printer("Nothing to unlinked, en masse.", foreground=FG().WARNING)
            return False
        else:
            for item in unlinks_to_do(self.data, self.repo_path, self.HOME):
                file_home = join(self.HOME, item)

                if islink(file_home):
                    with suppress(Exception):
                        remove(file_home)

            printer("Massively unlinked links successfully!", foreground=FG().FINISH)
        return True
