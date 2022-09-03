"""Modulate to store records and data."""
from os.path import join
from sys import exit

from snakypy.helpers import FG, printer
from snakypy.helpers.files import read_json

from snakypy.dotctrl import __info__
from snakypy.dotctrl.utils import lang_sys
from snakypy.dotctrl.config.lang import LANG


class Base:
    """Class to retrieve data"""

    def __init__(self, root, home):
        self.ROOT = root
        self.HOME = home
        self.repo_path = join(self.ROOT, "dotctrl")
        self.config_path = join(self.ROOT, __info__["config"])
        self.gitignore_path = join(self.ROOT, ".gitignore_path")
        self.readme = join(self.ROOT, "README.txt")

        try:
            self.parsed = read_json(self.config_path)
            self.elements = list(self.parsed["dotctrl"]["elements"])
            self.data = self.elements

        except FileNotFoundError:

            # TODO: [Adicionar o texto do print AQUI]
            printer(
                f"{self.msg['str:32']} ({self.config_path}).",
                foreground=FG(error_icon="[x] ").ERROR,
            )
            # TODO: [Adicionar o texto do print AQUI]
            printer(f"{self.msg['str:34']}", foreground=FG(warning_icon="[!] ").WARNING)
            exit(1)

        except Exception as err:
            # TODO: [Adicionar o texto do print AQUI]
            printer(f"{self.msg['str:33']}", str(err), foreground=FG().ERROR)
            exit(1)

    @property
    def msg(self):
        return LANG[lang_sys(LANG)]


class ElementForce:
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
