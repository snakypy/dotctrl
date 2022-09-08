from os.path import exists, join

from snakypy.helpers import FG, printer
from snakypy.helpers.checking import whoami
from snakypy.helpers.files import create_file, create_json
from snakypy.helpers.path import create as create_path

from snakypy.dotctrl import AUTO_PATH, __info__
from snakypy.dotctrl.config import config, gitignore, readme
from snakypy.dotctrl.config.base import Base
from snakypy.dotctrl.utils import git_init_command
from snakypy.dotctrl.utils.process import super_command


class InitCommand(Base):
    def __init__(self, root, home):
        Base.__init__(self, root, home)

    def creator(self, path: str):
        create_path(join(path, "dotctrl"))
        create_json(config.content, join(path, __info__["config"]), force=True)
        create_file(readme.content, self.readme, force=True)
        return {"bool": True, "cod": "cod:10"}

    def git_repo(self, path: str):
        git_init_command(path)
        create_file(gitignore.content, join(path, ".gitignore"), force=True)

    def automatic(self, path: str):

        if exists(join(path, __info__["config"])):
            directory = f"{FG().BLUE}{path}{FG().YELLOW}"

            # Dotctrl is already configured in this directory:
            printer(self.cod["cod:07"], directory, foreground=self.WARNING)

            return {"bool": False, "cod": "cod:07"}

        # You must have SUDO permission on your machine to proceed with this step and create
        # an automatic repository with Dotctrl. You can approach the operation by
        # pressing Ctrl + C.
        # NOTE: The Dotctrl directory will be created in:
        printer(self.cod["cod:08"], path, foreground=self.WARNING)

        # [ Enter password for sudo ]
        printer(self.cod["cod:09"], foreground=self.QUESTION)

        commands = [
            f"mkdir -p {join(AUTO_PATH[0], '.dotfiles', AUTO_PATH[1])}",
            f"chown -R {whoami()} {join(AUTO_PATH[0], '.dotfiles')}",
            f"chmod -R 700 {join(AUTO_PATH[0], '.dotfiles')}",
        ]

        cmd = super_command(commands)

        if cmd["str"] == "err":
            printer(self.cod["cod:49"], foreground=self.ERROR)
            return {"bool": False, "cod": "cod:49"}

        if cmd["str"] == "interrupt":
            printer(self.cod["cod:42"], foreground=self.WARNING)
            return {"bool": False, "cod": "cod:42"}

        self.creator(path)

        return {"bool": True, "cod": "cod:10"}

    def main(self, arguments: dict):
        """Base repository method."""

        if arguments["--auto"] and arguments["--git"]:
            root = join(AUTO_PATH[0], ".dotfiles", AUTO_PATH[1])
            out = self.automatic(root)
            if out["bool"]:
                self.git_repo(root)
        elif arguments["--auto"] and not arguments["--git"]:
            root = join(AUTO_PATH[0], ".dotfiles", AUTO_PATH[1])
            out = self.automatic(root)
        elif not arguments["--auto"] and arguments["--git"]:
            root = self.root
            out = self.creator(root)
            self.git_repo(root)
        elif not arguments["--auto"] and not arguments["--git"]:
            root = self.root
            out = self.creator(root)

        # Initialized Dotctrl repository in: path/to/root
        printer(self.cod["cod:10"], root, foreground=self.FINISH)
        return out
