"""Modulate to store records and data."""
from contextlib import suppress
from genericpath import exists
from os.path import join

from snakypy.helpers import printer
from snakypy.helpers.files import read_json

from snakypy.dotctrl import __info__

from snakypy.dotctrl.utils import get_key

from snakypy.dotctrl.utils.messages import Messages


class Base(Messages):
    """Class to retrieve data"""

    def __init__(self, root, home):
        self.root = root
        self.home = home
        self.data: list = list()
        self.config_path = join(self.root, __info__["config"])
        self.repo_path = join(self.root, "dotctrl")
        self.gitignore_path = join(self.root, ".gitignore")
        self.readme = join(self.root, "README.txt")
        Messages.__init__(self, self.config_path)

        with suppress(FileNotFoundError):
            self.parsed = read_json(self.config_path)
            self.elements = list(get_key(self.parsed, "dotctrl", "elements"))
            self.data: list = self.elements

    def checking_init(self):
        if not exists(join(self.root, __info__["config"])):

            printer(self.cod["cod:28"], foreground=self.WARNING)

            return False

        return True


class Options:
    def __init__(self):
        self.opts = {
            "element": ["--element", "--e"],
            "force": ["--force", "--f"],
        }

    def element(self, arguments: dict):
        if arguments[self.opts["element"][0]]:
            return arguments[self.opts["element"][0]]
        return arguments[self.opts["element"][1]]

    def force(self, arguments: dict):
        if arguments[self.opts["force"][0]]:
            return arguments[self.opts["force"][0]]
        return arguments[self.opts["force"][1]]
