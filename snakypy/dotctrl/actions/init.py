from os.path import exists, join
from sys import exit

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

    def main(self, arguments: dict) -> None:
        """Base repository method."""
        init_auto = False

        if exists(self.config_path):

            # Repository is already defined in: /path/to/repo
            printer(self.cod["cod:06"], f'"{self.repo_path}"', foreground=self.WARNING)

            exit(0)

        if not arguments["--auto"]:
            create_path(self.repo_path)
            create_json(config.content, self.config_path, force=True)
            create_file(readme.content, self.readme, force=True)

        if arguments["--git"]:
            git_init_command(self.root)
            create_file(gitignore.content, self.gitignore_path, force=True)
        elif arguments["--auto"]:

            path_current = join(AUTO_PATH[0], ".dotfiles", AUTO_PATH[1])

            if exists(join(path_current, __info__["config"])):
                directory = f"{FG().BLUE}{path_current}{FG().YELLOW}"

                # Dotctrl is already configured in this directory:
                printer(self.cod["cod:07"], directory, foreground=self.WARNING)

                exit(0)

            # You must have SUDO permission on your machine to proceed with this step and create
            # an automatic repository with Dotctrl. You can approach the operation by
            # pressing Ctrl + C.
            # NOTE: The Dotctrl directory will be created in:
            printer(self.cod["cod:08"], path_current, foreground=self.WARNING)

            # [ Enter password for sudo ]
            printer(self.cod["cod:09"], foreground=self.QUESTION)

            user_current = whoami()

            commands = [
                f"mkdir -p {join(AUTO_PATH[0], '.dotfiles', AUTO_PATH[1])}",
                f"chown -R {user_current} {join(AUTO_PATH[0], '.dotfiles')}",
                f"chmod -R 700 {join(AUTO_PATH[0], '.dotfiles')}",
            ]

            if not super_command(commands, self.cod["cod:49"], self.cod["cod:42"]):
                exit(1)

            create_path(self.repo_path)
            create_json(config.content, self.config_path, force=True)
            create_file(readme.content, self.readme, force=True)

            # Initialized Dotctrl repository in
            path = f"{join(AUTO_PATH[0], '.dotfiles', AUTO_PATH[1])}"
            printer(self.cod["cod:10"], path, foreground=self.FINISH)

            init_auto = True

        if not init_auto:
            # # Initialized Dotctrl repository in
            printer(self.cod["cod:10"], self.repo_path, foreground=self.FINISH)
