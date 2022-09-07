from genericpath import isfile
from os.path import join, exists, islink

from snakypy.helpers import printer

from snakypy.dotctrl.config.base import Base, Options
from snakypy.dotctrl.utils import (
    create_symlink,
    path_creation,
    is_repo_symbolic_link,
)


class LinkCommand(Base, Options):
    def __init__(self, root, home):
        Base.__init__(self, root, home)
        Options.__init__(self)

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

        self.checking_init()

        element = self.element(arguments)
        force = self.force(arguments)

        # If you use the --element flag (--e)
        if element:
            element_home = join(self.home, element)
            element_repo = join(self.repo_path, element)

            if "/" in element:
                path_creation(self.home, element)

            if (
                islink(element_home)
                and is_repo_symbolic_link(element_home, element_repo) is False
                and not force
            ):
                cod = self.error_symlink(element_home)

                return {"bool": False, "cod": cod["cod"]}

            if not exists(element_repo):

                printer(self.cod["cod:11"], foreground=self.WARNING)

                return {"bool": False, "cod": "cod:11"}

            if isfile(element_home) and not force:
                # TODO: [Adicionar o texto do print AQUI]
                printer(self.cod["cod:27"], foreground=self.WARNING)

                return {"bool": False, "cod": "cod:27"}

            status = create_symlink(element_repo, element_home, force)

            if not status:

                # TODO: [Adicionar o texto do print AQUI]
                printer(self.cod["cod:05"], element_repo, foreground=self.WARNING)

                return {"bool": False, "cod": "cod:05"}

            # TODO: [Adicionar o texto do print AQUI]
            printer(self.cod["cod:15"], foreground=self.FINISH)

            return {"bool": True, "cod": "cod:15"}

        # If you don't use the --element flag (--e)
        if len(self.links_to_do(self.data, self.repo_path, self.home)) == 0:

            # TODO: [Adicionar o texto do print AQUI]
            printer(self.cod["cod:14"], foreground=self.FINISH)

            return {"bool": False, "cod": "cod:14"}

        else:
            for item in self.links_to_do(self.data, self.repo_path, self.home):
                if "/" in item:
                    path_creation(self.home, item)

                element_home = join(self.home, item)
                element_repo = join(self.repo_path, item)

                if (
                    islink(element_home)
                    and is_repo_symbolic_link(element_home, element_repo) is False
                    and not force
                ):
                    cod = self.error_symlink(element_home)

                    return {"bool": False, "cod": cod["cod"]}

                if isfile(element_home) and not force:
                    # TODO: [Adicionar o texto do print AQUI]
                    printer(self.cod["cod:27"], foreground=self.WARNING)

                    return {"bool": False, "cod": "cod:27"}

                create_symlink(element_repo, element_home, force)

            # TODO: [Adicionar o texto do print AQUI]
            printer(self.cod["cod:15"], foreground=self.FINISH)
            return {"bool": True, "cod": "cod:15"}
