from os.path import join, exists

from snakypy.helpers import FG, printer

from snakypy.dotctrl.config.base import Base, ElementForce
from snakypy.dotctrl.utils import (
    create_symlink,
    path_creation,
    is_repo_symbolic_link,
)


class LinkCommand(Base, ElementForce):
    def __init__(self, root, home):
        Base.__init__(self, root, home)
        ElementForce.__init__(self)

    @staticmethod
    def links_to_do(data: list, repo_dir: str, home_dir: str) -> list:
        objects = list()
        for item in {*data}:
            elem_repo = join(repo_dir, item)
            elem_home = join(home_dir, item)
            if (
                not exists(elem_home)
                or is_repo_symbolic_link(elem_home, elem_repo) is False
            ):
                objects.append(elem_repo.replace(f"{repo_dir}/", ""))
        return objects

    def main(self, arguments: dict):
        """Method responsible for creating symbolic links from the
        repository to the place of origin of the elements."""

        element = self.element(arguments)
        force = self.force(arguments)

        # If you use the --element flag (--e)
        if element:
            file_home = join(self.HOME, element)
            file_repo = join(self.repo_path, element)

            if "/" in element:
                path_creation(self.HOME, element)

            if (
                exists(file_home)
                and is_repo_symbolic_link(file_home, file_repo) is False
                and not force
            ):
                printer(f"{self.msg['str:11']}", foreground=FG().WARNING)
                return False

            status = create_symlink(file_repo, file_home, force)

            if not status:
                # TODO: [Adicionar o texto do print AQUI]
                printer(
                    f'{self.msg["words"][3]} "{file_repo}" {self.msg["str:12"]} {self.msg["str:13"]}',
                    foreground=FG().ERROR,
                )

            # TODO: [Adicionar o texto do print AQUI]
            printer(f"{self.msg['str:15']}", foreground=FG().FINISH)
            return True

        # If you don't use the --element flag (--e)
        if len(self.links_to_do(self.data, self.repo_path, self.HOME)) == 0:
            # TODO: [Adicionar o texto do print AQUI]
            printer(f"{self.msg['str:14']}", foreground=FG().WARNING)
            return False
        else:
            for item in self.links_to_do(self.data, self.repo_path, self.HOME):
                if "/" in item:
                    path_creation(self.HOME, item)

                file_home = join(self.HOME, item)
                file_repo = join(self.repo_path, item)

                if (
                    exists(file_home)
                    and is_repo_symbolic_link(file_home, file_repo) is False
                    and not force
                ):
                    # TODO: [Adicionar o texto do print AQUI]
                    printer(f"{self.msg['str:11']}", foreground=FG().WARNING)
                    return False

                create_symlink(file_repo, file_home, force)

            # TODO: [Adicionar o texto do print AQUI]
            printer(f"{self.msg['str:15']}", foreground=FG().FINISH)
