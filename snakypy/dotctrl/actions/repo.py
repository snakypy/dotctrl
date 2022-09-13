from os import environ, listdir, walk
from os.path import exists, isdir, join
from pydoc import pager
from textwrap import dedent
from typing import Any

from snakypy.helpers import FG, SGR, printer
from snakypy.helpers.ansi import NONE
from snakypy.helpers.checking import whoami

from snakypy.dotctrl import __info__
from snakypy.dotctrl.config.base import Base
from snakypy.dotctrl.utils import is_repo_symbolic_link


class RepoCommand(Base):
    def __init__(self, root: str, home: str) -> None:
        Base.__init__(self, root, home)
        self.opts: tuple = ("--ls", "--check", "--info")

    @staticmethod
    def count_elements(path: str) -> tuple:
        d, f = [], []
        for _, directories, files in walk(path):
            for dir_ in directories:
                d.append(dir_)
            for file in files:
                f.append(file)

        total = d + f

        return len(f), len(d), len(total)

    @staticmethod
    def repl(string: str, sub: list) -> str:
        for i in sub:
            if i in string:
                return string.replace(f"{i}{whoami()}", "~")

        return string

    def simlink_path(self, linkpath: str, repopath: str) -> str:
        if is_repo_symbolic_link(linkpath, repopath):
            return self.none(linkpath)

        # Not linked!
        return self.red(self.text["msg:20"])

    def listing_data(self, arguments: dict) -> Any:

        # --ls choice
        if arguments[self.opts[0]]:

            # Lists all folders and files contained in the Dotctrl repository
            # for item in {*listing_files(self.repo_path), *self.data}:
            for item in {*self.data}:
                if exists(join(self.repo_path, item)):
                    yield item

        # --check choice
        elif arguments[self.opts[1]]:

            #
            for item in {*self.data}:
                src: str = join(self.repo_path, item)
                dest: str = join(self.home, item)
                if exists(src) and is_repo_symbolic_link(dest, src) is False:
                    yield item

    def main(self, arguments: dict) -> dict:

        if not self.checking_init():
            return {"status": False, "code": "28"}

        # --check
        if arguments[self.opts[1]]:
            count_repo: bool = len(listdir(self.repo_path)) == 0
            count_unlinked: bool = len(list(self.listing_data(arguments))) == 0

            if count_repo:
                # Empty repository. Nothing to link.
                printer(self.text["msg:19"], foreground=self.FINISH)

                return {"status": False, "code": "19"}

            if count_unlinked:
                # Congratulations! All elements are linked.
                printer(self.text["msg:21"], foreground=self.FINISH)

                return {"status": True, "code": "21"}

            # The elements below are NOT linked! Use "dotctrl link" to link them.
            printer(self.text["msg:22"], foreground=self.WARNING, end="\n" * 2)

            # Element(s)
            printer(self.text["msg:13"], foreground=self.CYAN, end="\n" * 2)

            for item in self.listing_data(arguments):
                if isdir(join(self.repo_path, item)):

                    # Directory
                    print(f"{self.magenta(self.text['word:11'])}: {item}")

                else:

                    # File
                    print(f"{self.magenta(self.text['word:10'])}: {item}")

            return {"status": False, "code": "22"}

        # --info
        elif arguments[self.opts[2]]:
            counts: tuple = self.count_elements(join(self.root, __info__["pkg_name"]))
            n_files: str = self.cyan(counts[0])
            n_dir: str = self.cyan(counts[1])
            n_total: str = self.cyan(counts[2])
            dotctrl_path_title: str = f"{FG().MAGENTA}DOTCTRL_PATH{NONE}"
            dotctrl_path: str = (
                self.green(self.text["word:06"])
                if environ.get("DOTCTRL_PATH")
                else self.green(self.text["word:07"])
            )

            out: str = f"""
            {SGR().BOLD}{self.cyan(self.text["msg:23"])}{NONE}\n
            {self.magenta(self.text["word:11"])}: {self.root}
            {self.magenta(self.text["word:01"])}: {n_files} {self.text["word:05"]}
            {self.magenta(self.text["word:04"])}: {n_dir} {self.text["word:05"]}
            {self.magenta(self.text["word:13"])}: {n_total} {self.text["word:03"]}
            {dotctrl_path_title}: {dotctrl_path}
            """

            print(dedent(out))

            return {"status": True}

        # --ls
        elif arguments[self.opts[0]]:
            if len(list(self.listing_data(arguments))) == 0:

                # The repository is empty of registration. No elements.
                printer(self.text["msg:24"], foreground=self.WARNING)

                return {"status": False, "code": "24"}

            repo: str = self.repl(self.repo_path, ["/home/", "/Users/"])
            arrow_invert: str = self.cyan(" <- ")

            elements: list = [
                f"{self.cyan(self.text['msg:25'])}",
                f"\nREPO={self.yellow(repo)}\n",
                f"{self.cyan(self.text['msg:26'])}",
            ]

            for item in self.listing_data(arguments):
                elem_repo: str = f"{self.none('$REPO')}{self.green(f'/{item}')}"
                is_link: str = self.simlink_path(
                    join(self.home, item), join(self.repo_path, item)
                )

                ll: str = self.green(f"{elem_repo}{arrow_invert}{is_link}")

                if isdir(join(self.repo_path, item)):
                    elements.append(f"{self.magenta(self.text['word:11'])}: {ll}")
                else:
                    elements.append(f"{self.magenta(self.text['word:10'])}: {ll}")
            pager("\n".join(elements))

            return {"status": True, "str": "success"}

        return {"status": False, "str": "invalid"}
