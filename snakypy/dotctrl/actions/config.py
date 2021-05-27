import pydoc
from os import environ
from shutil import which
from subprocess import call
from sys import exit

from snakypy.helpers.files import read_file

from snakypy.dotctrl.config.base import Base
from snakypy.dotctrl.utils import check_init


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

    def main(self, arguments) -> None:
        """Method for opening or viewing the configuration file."""
        check_init(self.ROOT)

        if arguments["--open"]:
            editor_conf = self.parsed["dotctrl"]["config"]["editor"]
            if editor_conf:
                editor_run(editor_conf, self.config_path)
            else:
                editors = ["vim", "nano", "emacs", "micro"]
                for edt in editors:
                    editor_run(edt, self.config_path)

        if arguments["--view"]:
            read_config = read_file(self.config_path)
            pydoc.pager(read_config)
