"""Modulate to store records and data."""
from contextlib import suppress
from os.path import join

from genericpath import exists
from snakypy.helpers import printer
from snakypy.helpers.files import read_json

from snakypy.dotctrl import __info__
from snakypy.dotctrl.utils import get_key
from snakypy.dotctrl.utils.messages import Messages


class Base(Messages):
    """Class to retrieve data"""

    def __init__(self, root: str, home: str) -> None:
        self.root: str = root
        self.home: str = home
        self.data: list = list()
        self.elements: list = list()
        self.parsed: dict = dict()
        self.config_path: str = join(self.root, __info__["config"])
        self.repo_path: str = join(self.root, "dotctrl")
        self.gitignore_path: str = join(self.root, ".gitignore")
        self.readme: str = join(self.root, "README.txt")
        Messages.__init__(self, self.config_path)

        with suppress(FileNotFoundError):
            self.parsed = read_json(self.config_path)
            self.elements = list(get_key(self.parsed, "dotctrl", "elements"))
            self.data = self.elements

    def checking_init(self) -> bool:
        if not exists(join(self.root, __info__["config"])):

            printer(self.text["msg:28"], foreground=self.WARNING)

            return False

        return True


class Options:
    def __init__(self) -> None:
        self.opts: dict = {
            "element": ["--element", "--e"],
            "force": ["--force", "--f"],
        }

    def element(self, arguments: dict) -> dict:
        if arguments[self.opts["element"][0]]:
            return arguments[self.opts["element"][0]]
        return arguments[self.opts["element"][1]]

    def force(self, arguments: dict) -> dict:
        if arguments[self.opts["force"][0]]:
            return arguments[self.opts["force"][0]]
        return arguments[self.opts["force"][1]]
