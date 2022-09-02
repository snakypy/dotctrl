from os import environ, listdir
from os.path import exists, isdir, join
from pydoc import pager
from textwrap import dedent
from typing import Any
from os import walk

from snakypy.helpers import FG, SGR, printer
from snakypy.helpers.ansi import NONE

from snakypy.dotctrl import __info__
from snakypy.dotctrl.config.base import Base
from snakypy.dotctrl.utils import listing_files, is_repo_symbolic_link


class RepoCommand(Base):
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

        # --check
        if arguments[self.opts[1]]:
            count_repo = len(listdir(self.repo_path)) == 0
            count_unlinked = len(list(self.listing_data(arguments))) == 0

            if count_repo:
                printer(f"{self.msg['str:19']}", foreground=FG().FINISH)
                return True

            if count_unlinked:
                printer(
                    f"{FG().MAGENTA}{self.msg['words'][7]} {FG().GREEN}{self.msg['str:21']}",
                    foreground=FG().FINISH,
                )
                return True

            printer(
                f"{self.msg['str:22']}", foreground=FG(warning_icon="\n[!] ").WARNING
            )
            printer(
                f"\n{self.msg['words'][3]}(s):",
                foreground=FG().CYAN,
            )

            for item in self.listing_data(arguments):
                if isdir(join(self.repo_path, item)):
                    print(
                        f"{FG().CYAN}➜{FG().MAGENTA} {self.msg['words'][5]}: {NONE}{item}"
                    )
                else:
                    print(
                        f"{FG().CYAN}➜{FG().MAGENTA} {self.msg['words'][0]}: {NONE}{item}"
                    )

            return False

        # --info
        elif arguments[self.opts[2]]:
            dotctrl_path = (
                self.msg["words"][9]
                if environ.get("DOTCTRL_PATH")
                else self.msg["words"][10]
            )
            counts = self.count_elements(join(self.ROOT, __info__["pkg_name"]))

            path_ = f'{FG().BLUE}{self.msg["words"][2]}'
            files_ = f'{FG().BLUE}{self.msg["words"][1]}'
            unit_ = f"{self.msg['words'][8]}(s)"
            dirs_ = f'{FG().BLUE}{self.msg["words"][6]}'
            elem_ = f"{self.msg['words'][3]}(s)"

            info = f"""
            {SGR().BOLD}{self.msg['str:23']}{NONE}
            {path_}: {FG().GREEN}{self.ROOT}
            {files_}: {FG().YELLOW}{SGR().BOLD}{counts[0]}{NONE}{FG().GREEN} {unit_}
            {dirs_}: {FG().YELLOW} {SGR().BOLD} {counts[1]} {NONE} {FG().GREEN} {unit_}
            {FG().BLUE}Total: {FG().YELLOW} {SGR().BOLD} {counts[2]} {NONE} {FG().GREEN} {elem_}
            {FG().BLUE}DOTCTRL_PATH: {FG().GREEN}{dotctrl_path}"""

            print(dedent(info))
            return True

        # --reg
        elif arguments[self.opts[0]]:
            if len(list(self.listing_data(arguments))) == 0:
                printer(
                    f"{self.msg['str:24']}", foreground=FG(warning_icon="[!] ").WARNING
                )
                return False

            elements = [
                f"{FG().YELLOW}{self.msg['str:25']}{NONE}\n",
                f"{FG().CYAN}{self.msg['str:26']} {NONE}",
            ]
            for item in self.listing_data(arguments):
                # elem_home = join(self.HOME, item)
                if isdir(join(self.repo_path, item)):
                    elements.append(
                        f"{FG().CYAN}➜{FG().MAGENTA} {self.msg['words'][5]}: {NONE}{item}"
                    )
                else:
                    elements.append(
                        f"{FG().CYAN}➜{FG().MAGENTA} {self.msg['words'][0]}: {NONE}{item}"
                    )
            pager("\n".join(elements))
            return True
        return False
