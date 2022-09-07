from snakypy.helpers import printer
from snakypy.dotctrl.config.lang import LANG
from snakypy.helpers.files import read_json
from subprocess import check_output
from snakypy.dotctrl.utils import get_key
from snakypy.dotctrl.utils.colors import Colors
from contextlib import suppress


class Messages(Colors):
    def __init__(self, config_path: str):
        self.config_path = config_path
        Colors.__init__(self)

    @property
    def cod(self):
        self.lang: str = "en_US"

        with suppress(FileNotFoundError):
            parsed: dict = read_json(self.config_path)
            self.lang: str = get_key(parsed, "dotctrl", "config", "language")

        if not self.lang or self.lang not in LANG:
            return LANG["en_US"]
        return LANG[self.lang]

    def error_symlink(self, element_home: str) -> None:
        # Operation aborted!
        printer(self.cod["cod:45"], foreground=self.WARNING, end="\n" * 2)

        # TODO: [Adicionar o texto do print AQUI]
        printer(self.cod["cod:39"], foreground=self.YELLOW, end="")

        symlink = check_output(
            ["ls", "-l", element_home], universal_newlines=True
        ).split()

        print(symlink[-3], symlink[-2], symlink[-1])

        return {"bool": False, "cod": "cod:39"}
