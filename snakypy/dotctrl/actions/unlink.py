from contextlib import suppress
from os import remove
from os.path import islink, join, exists

from snakypy.dotctrl.config.base import Base, Options
from snakypy.helpers import printer
from snakypy.dotctrl.utils import (
    join_two,
    is_repo_symbolic_link,
)


def unlinks_to_do(data, repo_dir, home_dir):
    objects = list()
    for item in {*data}:
        elem_repo = join(repo_dir, item)
        elem_home = join(home_dir, item)
        if islink(elem_home) and exists(elem_repo):
            objects.append(elem_repo.replace(f"{repo_dir}/", ""))
    return objects


class UnlinkCommand(Base, Options):
    def __init__(self, root, home):
        Base.__init__(self, root, home)
        Options.__init__(self)

    def main(self, arguments: dict) -> bool:
        """Method to unlink point files from the repository
        with their place of origin."""

        self.checking_init()

        element = self.element(arguments)
        force = self.force(arguments)

        # Use option --element (--e)
        if element:
            element_repo = join(self.repo_path, element)
            element_home = join(self.home, element)

            if (
                islink(element_home)
                and is_repo_symbolic_link(element_home, element_repo) is False
                and not force
            ):
                # TODO: [Adicionar o texto do print AQUI]
                self.error_symlink(element_home)
                return False

            element_home_ = join_two(self.home, element)

            if islink(element_home_):
                with suppress(Exception):
                    remove(element_home_)
                    # TODO: [Adicionar o texto do print AQUI]
                    printer(self.cod["cod:12"], foreground=self.FINISH)
                    return True

            # Element not found.
            printer(
                self.cod["cod:29"], f"Object: {element_home_}", foreground=self.ERROR
            )
            return False

        # Not use option --element (--e)
        if len(unlinks_to_do(self.data, self.repo_path, self.home)) == 0:
            # TODO: [Adicionar o texto do print AQUI]
            printer(self.cod["cod:30"], foreground=self.WARNING)
            return False
        else:
            for item in unlinks_to_do(self.data, self.repo_path, self.home):
                element_home = join(self.home, item)

                if islink(element_home):
                    with suppress(Exception):
                        remove(element_home)

            # TODO: [Adicionar o texto do print AQUI]
            printer(self.cod["cod:31"], foreground=self.FINISH)
        return True
