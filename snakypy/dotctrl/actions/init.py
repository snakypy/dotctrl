from os.path import exists, join

from snakypy.helpers import FG, printer
from snakypy.helpers.checking import whoami
from snakypy.helpers.files import create_file, create_json
from snakypy.helpers.path import create as create_path

from snakypy.dotctrl import AUTO_PATH, __info__
from snakypy.dotctrl.config import config, readme
from snakypy.dotctrl.config.base import Base
from snakypy.dotctrl.utils import git_init_command
from snakypy.dotctrl.utils.process import super_command


class InitCommand(Base):
    def __init__(self, root: str, home: str) -> None:
        Base.__init__(self, root, home)

    def creator(self, path: str) -> dict:
        create_path(join(path, "dotctrl"))
        create_json(config.content, join(path, __info__["config"]), force=True)
        create_file(readme.content, self.readme, force=True)

        return {"status": True, "code": "10"}

    def git_repo(self, path: str) -> None:
        git_init = git_init_command(path)

        if not git_init["status"]:
            # Dotctrl created the repository but did not find Git installed
            # to create a Git repository.
            printer(self.text["msg:50"], foreground=self.WARNING)

    def automatic(self, path: str) -> dict:

        if exists(join(path, __info__["config"])):
            directory = f"{FG().BLUE}{path}{FG().YELLOW}"

            # Dotctrl is already configured in this directory:
            printer(self.text["msg:07"], directory, foreground=self.WARNING)

            return {"status": False, "code": "07"}

        # You must have SUDO permission on your machine to proceed with this step and create
        # an automatic repository with Dotctrl. You can approach the operation by
        # pressing Ctrl + C.
        # NOTE: The Dotctrl directory will be created in:
        printer(self.text["msg:08"], f"{path}\n", foreground=self.WARNING)

        # [ Enter password for sudo ]
        printer(self.text["msg:09"], foreground=self.QUESTION)

        commands: list[str] = [
            f"mkdir -p {join(AUTO_PATH, '.dotfiles')}",
            f"chown -R {whoami()} {join(AUTO_PATH, '.dotfiles')}",
            f"chmod -R 700 {join(AUTO_PATH, '.dotfiles')}",
        ]

        cmd: dict = super_command(commands)

        if cmd["str"] == "err":
            printer(self.text["msg:49"], foreground=self.ERROR)
            return {"status": False, "code": "49"}

        if cmd["str"] == "interrupt":
            printer(self.text["msg:42"], foreground=self.WARNING)
            return {"status": False, "code": "42"}

        self.creator(path)

        return {"status": True, "code": "10"}

    def main(self, arguments: dict) -> dict:
        """Base repository method."""

        root: str = self.root
        out: dict = dict()

        if arguments["--auto"] and arguments["--git"]:
            root = join(AUTO_PATH, ".dotfiles")
            out = self.automatic(root)

            if out["status"]:
                self.git_repo(root)

        elif arguments["--auto"] and not arguments["--git"]:
            root = join(AUTO_PATH, ".dotfiles")
            out = self.automatic(root)

        elif not arguments["--auto"] and arguments["--git"]:
            out = self.creator(root)
            self.git_repo(root)

        elif not arguments["--auto"] and not arguments["--git"]:
            out = self.creator(root)

        # Initialized Dotctrl repository in: path/to/root
        printer(self.text["msg:10"], root, foreground=self.FINISH)
        return out
