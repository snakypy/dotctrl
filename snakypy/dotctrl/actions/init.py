import os
from os.path import exists, join
from sys import exit, platform
from textwrap import dedent

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
            printer("Repository is already defined.", foreground=FG().FINISH)
            exit(0)

        if not arguments["--auto"]:
            create_path(self.repo_path)
            create_json(config.content, self.config_path, force=True)
            create_file(readme.content, self.readme, force=True)

        if arguments["--git"]:
            git_init_command()
            create_file(gitignore.content, self.gitignore_path, force=True)
        elif arguments["--auto"]:
            path_current = join(AUTO_PATH[0], ".dotfiles", AUTO_PATH[1])
            if exists(join(path_current, __info__["config"])):
                dir_ = f"{FG().BLUE}{path_current}{FG().YELLOW}"
                printer(
                    f'{__info__["name"]} is already configured in this directory "{dir_}"',
                    foreground=FG().WARNING,
                )
                exit(0)
            message_initial = dedent(
                f"""
            [ATTENTION!]
            You must have SUDO permission on your machine to proceed with this step and create
            an automatic repository with {__info__["name"]}. You can approach the operation by
            pressing Ctrl + C.

            NOTE: The {__info__['name']} directory will be created in: "{FG().BLUE}{path_current}{FG().YELLOW}".
            """
            )
            printer(message_initial, foreground=FG().YELLOW)
            printer("[ Enter password for sudo ]", foreground=FG().QUESTION)
            user_current = whoami()
            commands = [
                f"mkdir -p {join(AUTO_PATH[0], '.dotfiles', AUTO_PATH[1])}",
                f"chown -R {user_current} {join(AUTO_PATH[0], '.dotfiles')}",
                f"chmod -R 700 {join(AUTO_PATH[0], '.dotfiles')}",
            ]

            sp = super_command(commands)
            if not sp:
                exit(1)

            create_path(self.repo_path)
            create_json(config.content, self.config_path, force=True)
            create_file(readme.content, self.readme, force=True)

            printer(
                f"Initialized {__info__['name']} repository in {join(AUTO_PATH[0], '.dotfiles', AUTO_PATH[1])}",
                foreground=FG().FINISH,
            )
            init_auto = True

        if not init_auto:
            printer(
                f"Initialized {__info__['name']} repository in {self.repo_path}",
                foreground=FG().FINISH,
            )
