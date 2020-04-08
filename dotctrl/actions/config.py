import pydoc
from shutil import which
from subprocess import call
from os import environ
from sys import exit
from snakypy.file import read as read_file
from dotctrl.utils import check_init
from dotctrl.config.base import Base


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

    def main(self, arguments):
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
