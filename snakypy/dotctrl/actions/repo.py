from os import environ, listdir
from os.path import exists, isdir, islink, join
from pydoc import pager
from textwrap import dedent
from typing import Any

from snakypy.helpers import FG, SGR, printer
from snakypy.helpers.ansi import NONE

from snakypy.dotctrl import __info__
from snakypy.dotctrl.config.base import Base
from snakypy.dotctrl.utils import check_init, listing_files
from snakypy.dotctrl.utils.catch import count_objects


class RepoCommand(Base):
    def __init__(self, root, home):
        Base.__init__(self, root, home)

    def listing_data(self, arguments) -> Any:
        for item in {*listing_files(self.repo_path, only_rc_files=True), *self.data}:
            if arguments["--imported"]:
                if exists(join(self.repo_path, item)):
                    yield item
            elif arguments["--check"]:
                if exists(join(self.repo_path, item)) and not islink(
                    join(self.HOME, item)
                ):
                    yield item

    # @property
    # def listing_data_imported(self) -> Any:
    #     for item in {*listing_files(self.repo_path, only_rc_files=True), *self.data}:
    #         if exists(join(self.repo_path, item)):
    #             yield item
    #
    # @property
    # def listing_data_check(self) -> Any:
    #     for item in {*listing_files(self.repo_path, only_rc_files=True), *self.data}:
    #         if exists(join(self.repo_path, item)) and not islink(join(self.HOME, item)):
    #             yield item

    def main(self, arguments: dict) -> bool:
        check_init(self.ROOT)
        if arguments["--check"]:
            count_repo = len(listdir(self.repo_path)) == 0
            count_repo_opt = len(list(self.listing_data(arguments))) == 0
            if count_repo or count_repo_opt:
                # printer("Nothing to check.", foreground=FG().FINISH)
                return True
            printer(
                "\nElement(s):",
                foreground=FG().CYAN,
            )
            for item in self.listing_data(arguments):
                status = f"{FG().YELLOW}[Not linked]{NONE}"
                if isdir(join(self.repo_path, item)):
                    print(
                        f"{FG().CYAN}➜{FG().MAGENTA} Directory: {NONE}{item} {status}"
                    )
                else:
                    print(f"{FG().CYAN}➜{FG().MAGENTA} File: {NONE}{item} {status}")

            return False
        elif arguments["--info"]:
            dotctrl_path = "active" if environ.get("DOTCTRL_PATH") else "disabled"
            counts = count_objects(join(self.ROOT, __info__["pkg_name"]))
            info = dedent(
                f"""
            {SGR().BOLD}Repository info{NONE}
            {FG().BLUE}Path: {FG().GREEN}{self.ROOT}
            {FG().BLUE}Files: {FG().GREEN} {counts[0]}
            {FG().BLUE}Directories: {FG().GREEN} {counts[1]}
            {FG().BLUE}Total: {FG().GREEN} {counts[2]}
            {FG().BLUE}DOTCTRL_PATH: {FG().GREEN}{dotctrl_path}"""
            )
            print(info)
            return True
        elif arguments["--imported"]:
            if len(list(self.listing_data(arguments))) == 0:
                printer("Repository is empty. No elements.", foreground=FG().WARNING)
                return False
            elements = [f'{FG().CYAN}[ Imported elements ] (Type "q" to exit) {NONE}']
            for item in self.listing_data(arguments):
                if isdir(join(self.repo_path, item)):
                    elements.append(
                        f"{FG().CYAN}➜{FG().MAGENTA} Directory: {NONE}{item}"
                    )
                else:
                    elements.append(f"{FG().CYAN}➜{FG().MAGENTA} File: {NONE}{item}")
            pager("\n".join(elements))
            return True
        return False
