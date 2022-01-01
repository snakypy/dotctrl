"""CLI Dotctrl"""
from snakypy.helpers.decorators import denying_os

from snakypy.dotctrl import HOME, ROOT
from snakypy.dotctrl.actions.check import CheckCommand
from snakypy.dotctrl.actions.config import ConfigCommand
from snakypy.dotctrl.actions.credits import CreditsCommand
from snakypy.dotctrl.actions.init import InitCommand
from snakypy.dotctrl.actions.link import LinkCommand
from snakypy.dotctrl.actions.list import ListCommand
from snakypy.dotctrl.actions.pull import PullCommand
from snakypy.dotctrl.actions.remove import RemoveCommand
from snakypy.dotctrl.actions.restore import RestoreCommand
from snakypy.dotctrl.actions.unlink import UnlinkCommand
from snakypy.dotctrl.utils import arguments
from snakypy.dotctrl.utils.decorators import assign_cli

# Get arguments Docopt
args = arguments()


@assign_cli(args, "init")
def run_init():
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


@assign_cli(args, "config")
def run_config():
    ConfigCommand(ROOT, HOME).main(args)


@assign_cli(args, "check")
def run_check():
    CheckCommand(ROOT, HOME).main()


@assign_cli(args, "list")
def run_list():
    ListCommand(ROOT, HOME).main()


@assign_cli(args, "restore")
def run_restore():
    RestoreCommand(ROOT, HOME).main(args)


@assign_cli(args, "remove")
def run_remove():
    RemoveCommand(ROOT, HOME).main(args)


@assign_cli(args, "--credits")
def run_credits():
    CreditsCommand().main()


@denying_os("Windows")
def main():
    run_init()
    run_pull()
    run_link()
    run_unlink()
    run_check()
    run_list()
    run_config()
    run_restore()
    run_remove()
    run_credits()
