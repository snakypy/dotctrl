from os.path import join, exists

from snakypy.helpers import FG, printer
from snakypy.dotctrl import __info__

from snakypy.dotctrl.config.base import Base, ElementForce
from snakypy.dotctrl.utils import (
    check_init,
    create_symlink,
    path_creation,
    rm_garbage_config,
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

        rm_garbage_config(self.HOME, self.repo_path, self.config_path)

        check_init(self.ROOT)

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
                printer(
                    "Link(s) was found, but maybe it can be linked from another location, but it's not "
                    f"from the {__info__['name']} repository. \n"
                    f"If you want to link to the {__info__['name']} repository, use the --force (--f) option."
                    " option to recreate.",
                    foreground=FG().WARNING,
                )
                return False

            status = create_symlink(file_repo, file_home, force)

            if not status:
                printer(
                    f'Element "{file_repo}" not linked. Review the same in the repository.',
                    foreground=FG().ERROR,
                )

            return True

        # If you don't use the --element flag (--e)
        if len(self.links_to_do(self.data, self.repo_path, self.HOME)) == 0:
            printer("Nothing to linked, en masse.", foreground=FG().WARNING)
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
                    printer(
                        "Link(s) was found, but maybe it can be linked from another location, but it's not "
                        f"from the {__info__['name']} repository. \n"
                        f"If you want to link to the {__info__['name']} repository, use the --force (--f) option."
                        " option to recreate.",
                        foreground=FG(warning_icon="[!] ").WARNING,
                    )
                    return False

                create_symlink(file_repo, file_home, force)

            printer("Element(s) linked successfully!", foreground=FG().FINISH)
