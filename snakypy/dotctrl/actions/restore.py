from concurrent.futures import ThreadPoolExecutor
from os.path import exists, join, isdir, islink
from shutil import move
from sys import exit
from typing import Union
from os import remove, rmdir

from snakypy.helpers import FG, printer
from snakypy.helpers.files import create_json, read_json
from snakypy.helpers.os import rmdir_blank

from snakypy.dotctrl.config.base import Base, ElementForce
from snakypy.dotctrl.utils import (
    listing_files,
    path_creation,
    remove_objects,
    shorten_path,
    is_repo_symbolic_link,
)
from snakypy.dotctrl.utils import pick

# def restore_action(
#     repo_path: str, src: str, dst: str, force: Union[None, bool]
# ) -> None:
#     """Function presents the possibilities of options for restored
#     # the elements."""
#     if not exists(src) and not force:
#         printer(
#             f'The element "{str(shorten_path(src, 1))}" not found in '
#             f"repository to be restored. Review the configuration file, "
#             f"or use other option.",
#             foreground=FG().WARNING,
#         )
#         exit(0)

#     if exists(src) and exists(dst) and not force:
#         printer(
#             "Elements correspond to the repository and the place of origin. "
#             "User --force (--f).",
#             foreground=FG().WARNING,
#         )
#         exit(0)

#     if exists(src) and exists(dst) and force:
#         remove_objects(dst)
#         move(src, dst)
#         rmdir_blank(repo_path)
#     elif exists(src) and not exists(dst):
#         move(src, dst)
#         rmdir_blank(repo_path)


class RestoreCommand(Base, ElementForce):
    def __init__(self, root, home):
        Base.__init__(self, root, home)
        ElementForce.__init__(self)

    def restore_action(self, obj_origin: str, obj_repo: str):
        remove_objects(obj_origin)
        move(obj_repo, obj_origin)
        rmdir_blank(self.repo_path)

    def restore(self, obj_origin: str, obj_repo: str):
        # TODO: Criar lógica

        if not exists(obj_repo):
            printer("Use dotctrl config --autoclean")
            exit(0)

        if exists(obj_repo):
            if not exists(obj_origin):
                self.restore_action(obj_origin, obj_repo)
            elif islink(obj_origin):
                if not is_repo_symbolic_link(obj_origin, obj_repo):
                    # TODO: [Adicionar o texto do print AQUI]
                    print(
                        "Existe link mas não é vinculado com o repositorio do Dotctrl"
                        "Faça a manutenção manualmente"
                    )
                    return False
                else:
                    self.restore_action(obj_origin, obj_repo)

    def main(self, arguments: dict) -> None:
        """Method to restore dotfiles from the repository to their
        original location."""

        element = self.element(arguments)
        # force = self.force(arguments)

        if element:
            file_home = join(self.HOME, element)
            file_repo = join(self.repo_path, element)
            if "/" in element:
                path_creation(self.HOME, element)

            self.restore(file_home, file_repo)

        else:
            title_ = (
                "Está opção ira fazer a restauração em massa de todos elementos "
                "do repositório do Dotctrl para o local de original. Deseja continuar?"
            )
            options_ = ["Yes", "No"]

            reply = pick(title_, options_, index=True)
            if reply is not None and reply[0] == 1:
                # TODO: [Adicionar o texto do print AQUI]
                printer("Cancelado")
                return False
            elif reply is not None and reply[0] == 0:

                objects = [*listing_files(self.repo_path), *self.data]

                # Empty repository. Nothing to restore.
                if len(objects) == 0:

                    # TODO: [Adicionar o texto do print AQUI]
                    printer(
                        "Empty repository. Nothing to restore.",
                        foreground=FG(warning_icon="[!] ").WARNING,
                    )

                for item in objects:
                    file_home = join(self.HOME, item)
                    file_repo = join(self.repo_path, item)
                    if "/" in item:
                        path_creation(self.HOME, item)

                    self.restore(file_home, file_repo)
