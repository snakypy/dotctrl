from os.path import exists
from sys import exit

from snakypy.helpers import FG, printer
from snakypy.helpers.files import create_file, create_json
from snakypy.helpers.path import create as create_path

from snakypy.dotctrl import __info__
from snakypy.dotctrl.config import config, gitignore, readme
from snakypy.dotctrl.config.base import Base
from snakypy.dotctrl.utils import git_init_command


class InitCommand(Base):
    def __init__(self, root, home):
        Base.__init__(self, root, home)

    def main(self, arguments: dict) -> None:
        """Base repository method."""
        if exists(self.config_path):
            printer("Repository is already defined.", foreground=FG().FINISH)
            exit(0)
        create_path(self.repo_path)
        create_json(config.content, self.config_path, force=True)
        create_file(readme.content, self.readme, force=True)
        if arguments["--git"]:
            git_init_command()
            create_file(gitignore.content, self.gitignore_path, force=True)
        printer(
            f"Initialized {__info__['name']} repository in {self.repo_path}",
            foreground=FG().FINISH,
        )
