import os
import pydoc
import shutil
import subprocess
import snakypy
from sys import exit
from dotctrl.console import utils
from dotctrl.config import base


def editor_run(editor, config):
    if shutil.which(editor):
        get_editor = os.environ.get("EDITOR", editor)
        with open(config) as f:
            subprocess.call([get_editor, f.name])
            exit(0)
    return


class Command(base.Base):
    def __init__(self, root, home):
        base.Base.__init__(self, root, home)

    def main(self, arguments):
        """Method for opening or viewing the configuration file."""
        utils.check_init(self.ROOT)

        if arguments["--open"]:
            editor_conf = self.parsed["dotctrl"]["config"]["editor"]
            if editor_conf:
                editor_run(editor_conf, self.config_path)
            else:
                editors = ["vim", "nano", "emacs", "micro"]
                for edt in editors:
                    editor_run(edt, self.config_path)

        if arguments["--view"]:
            read_config = snakypy.file.read(self.config_path)
            pydoc.pager(read_config)
