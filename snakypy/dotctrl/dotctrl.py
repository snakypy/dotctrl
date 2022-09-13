"""CLI Dotctrl"""
from os.path import join

from snakypy.helpers.decorators import denying_os

from snakypy.dotctrl import AUTO_PATH, HOME, ROOT
from snakypy.dotctrl.actions.config import ConfigCommand
from snakypy.dotctrl.actions.credits import CreditsCommand
from snakypy.dotctrl.actions.find import FindCommand
from snakypy.dotctrl.actions.init import InitCommand
from snakypy.dotctrl.actions.link import LinkCommand
from snakypy.dotctrl.actions.pull import PullCommand
from snakypy.dotctrl.actions.repo import RepoCommand
from snakypy.dotctrl.actions.restore import RestoreCommand
from snakypy.dotctrl.actions.unlink import UnlinkCommand
from snakypy.dotctrl.config.menu import Menu
from snakypy.dotctrl.utils.decorators import assign_cli

# Get arguments Docopt
args: dict = Menu(ROOT, HOME).args()


@assign_cli(args, "init")
def run_init():
    if args["--auto"] is True:
        ROOT_ = join(AUTO_PATH, ".dotfiles")
        InitCommand(ROOT_, HOME).main(args)
    else:
        InitCommand(ROOT, HOME).main(args)


@assign_cli(args, "pull")
def run_pull():
    PullCommand(ROOT, HOME).main(args)


@assign_cli(args, "link")
def run_link():
    LinkCommand(ROOT, HOME).main(args)


@assign_cli(args, "unlink")
def run_unlink():
    UnlinkCommand(ROOT, HOME).main(args)


@assign_cli(args, "find")
def run_find():
    FindCommand(ROOT, HOME).main(args)


@assign_cli(args, "config")
def run_config():
    ConfigCommand(ROOT, HOME).main(args)


@assign_cli(args, "repo")
def run_repo():
    RepoCommand(ROOT, HOME).main(args)


@assign_cli(args, "restore")
def run_restore():
    RestoreCommand(ROOT, HOME).main(args)


@assign_cli(args, "--credits")
def run_credits():
    CreditsCommand(ROOT, HOME).main()


@denying_os("Windows")
def main():
    run_init()
    run_pull()
    run_link()
    run_unlink()
    run_repo()
    run_find()
    run_config()
    run_restore()
    run_credits()
