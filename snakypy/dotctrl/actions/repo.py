from os import environ, listdir
from os.path import exists, isdir, join, realpath
from pydoc import pager
from textwrap import dedent
from typing import Any
from os import walk

from snakypy.helpers import FG, SGR, printer
from snakypy.helpers.ansi import NONE

from snakypy.dotctrl import __info__
from snakypy.dotctrl.config.base import Base
from snakypy.dotctrl.utils import check_init, listing_files, is_repo_symbolic_link


class RepoCommand(Base):
    # TODO: Verifica se o link existente é o mesmo do repo do Dotctrl.
    def __init__(self, root, home):
        Base.__init__(self, root, home)
        self.opts = ("--reg", "--check", "--info")

    @staticmethod
    def count_elements(path: str) -> tuple:
        directories, files = [], []
        for _, dirs_, files_ in walk(path):
            for file in files_:
                files.append(file)
            for d in dirs_:
                directories.append(d)
        total = files + directories
        return len(files), len(directories), len(total)

    def listing_data(self, arguments) -> Any:
        if arguments[self.opts[0]]:

            # Lists all folders and files contained in the Dotctrl repository
            for item in {*listing_files(self.repo_path), *self.data}:
                if exists(join(self.repo_path, item)):
                    yield item

        elif arguments[self.opts[1]]:

            #
            for item in {*self.data}:
                src = join(self.repo_path, item)
                dest = join(self.HOME, item)
                if exists(src) and is_repo_symbolic_link(dest, src) is False:
                    yield item

    def main(self, arguments: dict) -> bool:
        check_init(self.ROOT)

        # --check
        if arguments[self.opts[1]]:
            count_repo = len(listdir(self.repo_path)) == 0
            count_unlinked = len(list(self.listing_data(arguments))) == 0

            if count_repo:
                printer("Empty repository. Nothing to link.", foreground=FG().FINISH)
                return True

            if count_unlinked:
                printer(
                    f"{FG().MAGENTA}Congratulations! {FG().GREEN}All elements are linked.",
                    foreground=FG().FINISH,
                )
                return True

            printer(
                f"The elements below are {FG().RED}NOT{FG().YELLOW} linked! ",
                foreground=FG(warning_icon="\n[!] ").WARNING,
            )
            printer(
                "\nElement(s):",
                foreground=FG().CYAN,
            )

            for item in self.listing_data(arguments):
                if isdir(join(self.repo_path, item)):
                    print(f"{FG().CYAN}➜{FG().MAGENTA} Directory: {NONE}{item}")
                else:
                    print(f"{FG().CYAN}➜{FG().MAGENTA} File: {NONE}{item}")

            return False

        # --info
        elif arguments[self.opts[2]]:
            dotctrl_path = "active" if environ.get("DOTCTRL_PATH") else "disabled"
            counts = self.count_elements(join(self.ROOT, __info__["pkg_name"]))
            info = dedent(
                f"""
            {SGR().BOLD}Repository info{NONE}
            {FG().BLUE}Path: {FG().GREEN}{self.ROOT}
            {FG().BLUE}Files: {FG().YELLOW} {SGR().BOLD} {counts[0]} {NONE} {FG().GREEN} unit(s)
            {FG().BLUE}Directories: {FG().YELLOW} {SGR().BOLD} {counts[1]} {NONE} {FG().GREEN} unit(s)
            {FG().BLUE}Total: {FG().YELLOW} {SGR().BOLD} {counts[2]} {NONE} {FG().GREEN} element(s)
            {FG().BLUE}DOTCTRL_PATH: {FG().GREEN}{dotctrl_path}"""
            )
            print(info)
            return True

        # --reg
        elif arguments[self.opts[0]]:
            if len(list(self.listing_data(arguments))) == 0:
                printer(
                    "The repository is empty of registration. No elements.",
                    foreground=FG(warning_icon="[!] ").WARNING,
                )
                return False

            elements = [
                f"{FG().YELLOW}Dotctrl repository element registration.{NONE}\n",
                f'{FG().CYAN}[ Element(s) ] (Type "q" to exit) {NONE}',
            ]
            for item in self.listing_data(arguments):
                # elem_home = join(self.HOME, item)
                if isdir(join(self.repo_path, item)):
                    elements.append(
                        f"{FG().CYAN}➜{FG().MAGENTA} Directory: {NONE}{item}"
                    )
                else:
                    elements.append(f"{FG().CYAN}➜{FG().MAGENTA} File: {NONE}{item}")
            pager("\n".join(elements))
            return True
        return False
