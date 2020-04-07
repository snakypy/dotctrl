import snakypy
from os.path import exists
from sys import exit
from snakypy import FG, printer
from dotctrl.config import base, gitignore, package, readme, config
from dotctrl.console import utils


class Command(base.Base):
    def __init__(self, root, home):
        base.Base.__init__(self, root, home)

    def main(self, arguments):
        """Base repository method."""
        if exists(self.config_path):
            printer("Repository is already defined.", foreground=FG.FINISH)
            exit(0)
        snakypy.path.create(self.repo_path)
        snakypy.json.create(config.content, self.config_path, force=True)
        snakypy.file.create(readme.content, self.readme, force=True)
        if arguments["--git"]:
            utils.git_init_command()
            snakypy.file.create(gitignore.content, self.gitignore_path, force=True)
        printer(
            f"Initialized {package.info['name']} repository in {self.repo_path}",
            foreground=FG.FINISH,
        )
