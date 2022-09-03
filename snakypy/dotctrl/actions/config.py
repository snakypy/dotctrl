import pydoc
from os import environ
from os.path import join, exists
from shutil import which
from subprocess import call
from sys import exit

from snakypy.helpers.files import read_file, create_json, read_json
from snakypy.helpers import printer, FG

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
        self.opts = ("--autoclean", "--open", "--view")

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
            printer(f"{self.msg['str:35']}", foreground=FG(finish_icon="[ok] ").FINISH)
            return True

        # TODO: [Adicionar o texto do print AQUI]
        printer(f"{self.msg['str:36']}", foreground=FG(warning_icon="[!] ").WARNING)
        return False

    def main(self, arguments) -> None:
        """Method for opening or viewing the configuration file."""

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
