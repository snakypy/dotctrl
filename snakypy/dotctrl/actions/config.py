import pydoc
from os import environ
from os.path import exists, join
from shutil import which
from subprocess import call
from sys import exit
from typing import Any, Union

from snakypy.helpers import printer
from snakypy.helpers.files import create_json, read_file, read_json

from snakypy.dotctrl.config.base import Base
from snakypy.dotctrl.utils import pick


def editor_run(editor, config):
    if which(editor):
        get_editor = environ.get("EDITOR", editor)
        with open(config) as f:
            call([get_editor, f.name])
            exit(0)
    return


class ConfigCommand(Base):
    def __init__(self, root: str, home: str) -> None:
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

    def autoclean(self) -> dict:
        parsed: dict = read_json(self.config_path)
        elements: list = parsed["dotctrl"]["elements"]
        applied_cleaning: bool = False

        if len(elements) != 0:
            for elem in elements[:]:
                elem_repo: str = join(self.repo_path, elem)
                if not exists(elem_repo):
                    applied_cleaning = True
                    elements.remove(elem)

        parsed["dotctrl"]["elements"] = elements
        create_json(parsed, self.config_path, force=True)

        if applied_cleaning:
            # Cleaning completed!
            printer(self.text["msg:35"], foreground=self.FINISH)
            return {"status": True, "code": "35"}

        # Nothing to clean!
        printer(self.text["msg:36"], foreground=self.WARNING)
        return {"status": False, "code": "36"}

    def main(self, arguments: dict) -> Union[dict, None]:
        """Method for opening or viewing the configuration file."""

        if not self.checking_init():
            return {"status": False, "code": "28"}

        # --autoclean
        if arguments[self.opts[0]]:
            out = self.autoclean()
            return out

        # --open
        elif arguments[self.opts[1]]:
            editor_conf: str = self.parsed["dotctrl"]["config"]["editor"]
            if editor_conf:
                editor_run(editor_conf, self.config_path)
            else:
                editors: list[str] = ["vim", "nano", "emacs", "micro"]
                for edt in editors:
                    editor_run(edt, self.config_path)

            return {"status": True}

        # --view
        elif arguments[self.opts[2]]:
            read_config: str = read_file(self.config_path)
            pydoc.pager(read_config)

            return {"status": True}

        # --lang
        elif arguments[self.opts[3]]:
            title_: str = self.text["msg:47"]
            reply = pick(
                title_,
                self.languages,
                index=True,
                cancel_msg=self.text["msg:42"],
                invalid_msg=self.text["msg:43"],
            )

            if reply is None:
                return {"status": False, "code": "42"}

            language: Any = self.choice_language[reply[0]]
            self.change_language(language)

            printer(
                self.text["msg:48"], f"{self.cyan(reply[1])}", foreground=self.FINISH
            )

            return {"status": True, "code": "48"}

        return None
