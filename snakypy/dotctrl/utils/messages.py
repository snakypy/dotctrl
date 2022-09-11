from contextlib import suppress
from os.path import realpath

from snakypy.helpers import printer
from snakypy.helpers.files import read_json

from snakypy.dotctrl.config.lang import LANG
from snakypy.dotctrl.utils import get_key
from snakypy.dotctrl.utils.colors import Colors


class Messages(Colors):
    def __init__(self, config_path: str) -> None:
        self.lang: str = "en_US"
        self.config_path: str = config_path
        Colors.__init__(self)

    @property
    def text(self) -> dict:

        with suppress(FileNotFoundError):
            parsed: dict = read_json(self.config_path)
            self.lang = get_key(parsed, "dotctrl", "config", "language")

        if not self.lang or self.lang not in LANG:
            return LANG["en_US"]
        return LANG[self.lang]

    def error_symlink(self, element_home: str) -> dict:
        # Operation aborted!
        printer(self.text["msg:45"], foreground=self.WARNING, end="\n" * 2)

        # Dotctrl encountered a symbolic link to an element that is not
        # linked with the Dotctrl repository.
        # If you want to proceed and replace this symbolic link (and others) found
        # by the Dotctrl repository element, use the --force (--f) option.
        # Note: If you use the --force (--f) option, this symlink
        # found will be removed.
        # We recommend that you verify this symbolic link before proceeding with the option --force (--f)
        #
        # Symbolic link found:
        printer(self.text["msg:39"], foreground=self.YELLOW, end="")

        print(f"{self.cyan(element_home)} -> {realpath(element_home)}")

        return {"status": False, "code": "39"}
