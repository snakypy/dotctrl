from os import environ, listdir
from os.path import exists, isdir, join
from pydoc import pager
from textwrap import dedent
from typing import Any, Union
from os import walk

from snakypy.helpers import FG, SGR, printer
from snakypy.helpers.ansi import NONE

from snakypy.dotctrl import __info__
from snakypy.dotctrl.config.base import Base
from snakypy.dotctrl.utils import listing_files, is_repo_symbolic_link
from snakypy.helpers.checking import whoami


class RepoCommand(Base):
    def __init__(self, root, home):
        Base.__init__(self, root, home)
        self.opts = ("--ls", "--check", "--info")

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

    @staticmethod
    def repl(string: str, sub: list) -> str:
        for i in sub:
            if i in string:
                return string.replace(f"{i}{whoami()}", "~")
        return string

    def simlink_path(self, linkpath: str, repopath: str) -> str:
        if is_repo_symbolic_link(linkpath, repopath):
            return self.none(linkpath)
        # TODO: [Adicionar o texto do print AQUI]
        return self.red(self.cod["cod:20"])

    def listing_data(self, arguments) -> Any:

        # --ls choice
        if arguments[self.opts[0]]:

            # Lists all folders and files contained in the Dotctrl repository
            for item in {*listing_files(self.repo_path), *self.data}:
                if exists(join(self.repo_path, item)):
                    yield item

        # --check choice
        elif arguments[self.opts[1]]:

            #
            for item in {*self.data}:
                src = join(self.repo_path, item)
                dest = join(self.home, item)
                if exists(src) and is_repo_symbolic_link(dest, src) is False:
                    yield item

    def main(self, arguments: dict) -> Union[None, bool]:

        self.checking_init()

        # --check
        if arguments[self.opts[1]]:
            count_repo = len(listdir(self.repo_path)) == 0
            count_unlinked = len(list(self.listing_data(arguments))) == 0

            if count_repo:
                # Empty repository. Nothing to link.
                printer(self.cod["cod:19"], foreground=self.FINISH)
                return None

            if count_unlinked:
                # Congratulations! All elements are linked.
                printer(self.cod["cod:21"], foreground=self.FINISH)
                return True

            # TODO: [Adicionar o texto do print AQUI]
            printer(self.cod["cod:22"], foreground=self.WARNING, end="\n" * 2)

            # Element(s)
            printer(self.cod["cod:13"], foreground=self.CYAN, end="\n" * 2)

            for item in self.listing_data(arguments):
                if isdir(join(self.repo_path, item)):
                    # TODO: [Adicionar o texto do print AQUI]
                    print(f"{self.magenta(self.cod['cod:w11'])}: {item}")
                else:
                    # TODO: [Adicionar o texto do print AQUI]
                    print(f"{self.magenta(self.cod['cod:w10'])}: {item}")

            return False

        # --info
        elif arguments[self.opts[2]]:
            counts = self.count_elements(join(self.root, __info__["pkg_name"]))
            n_files = self.cyan(counts[0])
            n_dir = self.cyan(counts[1])
            n_total = self.cyan(counts[2])
            dotctrl_path_title = f"{FG().MAGENTA}DOTCTRL_PATH{NONE}"
            dotctrl_path = (
                self.green(self.cod["cod:w06"])
                if environ.get("DOTCTRL_PATH")
                else self.green(self.cod["cod:w07"])
            )

            out = f"""
            {SGR().BOLD}{self.cyan(self.cod["cod:23"])}{NONE}\n
            {self.magenta(self.cod["cod:w11"])}: {self.root}
            {self.magenta(self.cod["cod:w01"])}: {n_files} {self.cod["cod:w03"]}
            {self.magenta(self.cod["cod:w04"])}: {n_dir} {self.cod["cod:w03"]}
            {self.magenta(self.cod["cod:w13"])}: {n_total} {self.cod["cod:w03"]}
            {dotctrl_path_title}: {dotctrl_path}
            """

            print(dedent(out))
            return True

        # --ls
        elif arguments[self.opts[0]]:
            if len(list(self.listing_data(arguments))) == 0:

                # TODO: [Adicionar o texto do print AQUI]
                printer(self.cod["cod:24"], foreground=self.WARNING)
                return False

            repo = self.repl(self.repo_path, ["/home/", "/Users/"])
            arrow_invert = self.cyan(" <- ")

            elements = [
                f"{self.cyan(self.cod['cod:25'])}",
                f"\nREPO={self.yellow(repo)}\n",
                f"{self.cyan(self.cod['cod:26'])}",
            ]

            for item in self.listing_data(arguments):
                elem_repo = f"{self.none('$REPO')}{self.green(f'/{item}')}"
                is_link = self.simlink_path(
                    join(self.home, item), join(self.repo_path, item)
                )

                ll = self.green(f"{elem_repo}{arrow_invert}{is_link}")

                if isdir(join(self.repo_path, item)):
                    elements.append(f"{self.magenta(self.cod['cod:w11'])}: {ll}")
                else:
                    elements.append(f"{self.magenta(self.cod['cod:w10'])}: {ll}")
            pager("\n".join(elements))

            return True

        return False
