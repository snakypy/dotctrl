from os.path import exists
from sys import exit
from snakypy import FG, printer
from snakypy.path import create as create_path
from snakypy.json import create as create_json
from snakypy.file import create as create_file
from dotctrl.config import gitignore, package, readme, config
from dotctrl.config.base import Base
from dotctrl.utils import git_init_command


class InitCommand(Base):
    def __init__(self, root, home):
        Base.__init__(self, root, home)

    def main(self, arguments):
        """Base repository method."""
        if exists(self.config_path):
            printer("Repository is already defined.", foreground=FG.FINISH)
            exit(0)
        create_path(self.repo_path)
        create_json(config.content, self.config_path, force=True)
        create_file(readme.content, self.readme, force=True)
        if arguments["--git"]:
            git_init_command()
            create_file(gitignore.content, self.gitignore_path, force=True)
        printer(
            f"Initialized {package.info['name']} repository in {self.repo_path}",
            foreground=FG.FINISH,
        )
