import pydoc
from os import environ
from os.path import join, exists
from shutil import which
from subprocess import call
from sys import exit

from snakypy.helpers import printer
from snakypy.helpers.files import read_file, create_json, read_json
from snakypy.dotctrl.utils import pick

from snakypy.dotctrl.config.base import Base


def editor_run(editor, config):
    if which(editor):
        get_editor = environ.get("EDITOR", editor)
        with open(config) as f:
            call([get_editor, f.name])
            exit(0)
    return


class ConfigCommand(Base):
    def __init__(self, root, home):
        Base.__init__(self, root, home)
        self.opts: tuple = ("--autoclean", "--open", "--view", "--lang")
        self.languages: list = [
            "English (USA)",
            "Português (Brasil)",
        ]
        self.choice_language: dict = {
            0: "en_US",
            1: "pt_BR",
        }

    def change_language(self, lang: str):
        parsed: dict = read_json(self.config_path)
        parsed["dotctrl"]["config"]["language"] = lang
        create_json(parsed, self.config_path, force=True)

    def autoclean(self) -> bool:
        parsed: dict = read_json(self.config_path)
        elements: list = parsed["dotctrl"]["elements"]
        applied_cleaning = False

        if len(elements) != 0:
            for elem in elements[:]:
                elem_repo = join(self.repo_path, elem)
                if not exists(elem_repo):
                    applied_cleaning = True
                    elements.remove(elem)

        parsed["dotctrl"]["elements"] = elements
        create_json(parsed, self.config_path, force=True)

        if applied_cleaning:
            # TODO: [Adicionar o texto do print AQUI]
            printer(self.cod["cod:35"], foreground=self.FINISH)
            return True

        # TODO: [Adicionar o texto do print AQUI]
        printer(self.cod["cod:36"], foreground=self.WARNING)
        return False

    def main(self, arguments) -> None:
        """Method for opening or viewing the configuration file."""

        self.checking_init()

        # --autoclean
        if arguments[self.opts[0]]:
            self.autoclean()

        # --open
        elif arguments[self.opts[1]]:
            editor_conf: str = self.parsed["dotctrl"]["config"]["editor"]
            if editor_conf:
                editor_run(editor_conf, self.config_path)
            else:
                editors = ["vim", "nano", "emacs", "micro"]
                for edt in editors:
                    editor_run(edt, self.config_path)

        # --view
        elif arguments[self.opts[2]]:
            read_config = read_file(self.config_path)
            pydoc.pager(read_config)

        # --lang
        elif arguments[self.opts[3]]:
            title_ = self.cod["cod:47"]
            reply = pick(
                title_,
                self.languages,
                index=True,
                cancel_msg=self.cod["cod:42"],
                opt_msg=self.cod["cod:43"],
            )
            language = self.choice_language[reply[0]]
            self.change_language(language)
            printer(self.cod["cod:48"], foreground=self.FINISH)
