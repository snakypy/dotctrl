from contextlib import suppress
from os import remove
from os.path import islink, join, exists

from snakypy.helpers import FG, printer

from snakypy.dotctrl.config.base import Base, ElementForce
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


class UnlinkCommand(Base, ElementForce):
    def __init__(self, root, home):
        Base.__init__(self, root, home)
        ElementForce.__init__(self)

    def main(self, arguments: dict) -> bool:
        """Method to unlink point files from the repository
        with their place of origin."""

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
                # TODO: [Adicionar o texto do print AQUI]
                printer(
                    f"{self.msg['str:27']}", foreground=FG(warning_icon="[!]").WARNING
                )
                return False

            file_home = join_two(self.HOME, element)
            if islink(file_home):
                with suppress(Exception):
                    remove(file_home)
                    return True

            # TODO: Add message print UNLINKED

            # Element not found.
            printer(
                f'{self.msg["words"][3]} "{file_home}" {self.msg["str:28"]}. {self.msg["str:29"]}',
                foreground=FG(error_icon="[x] ").ERROR,
            )
            return False

        # Not use option --element (--e)
        if len(unlinks_to_do(self.data, self.repo_path, self.HOME)) == 0:
            # TODO: [Adicionar o texto do print AQUI]
            printer(f'{self.msg["str:30"]}', foreground=FG().WARNING)
            return False
        else:
            for item in unlinks_to_do(self.data, self.repo_path, self.HOME):
                file_home = join(self.HOME, item)

                if islink(file_home):
                    with suppress(Exception):
                        remove(file_home)

            # TODO: [Adicionar o texto do print AQUI]
            printer(f'{self.msg["str:31"]}', foreground=FG().FINISH)
        return True
