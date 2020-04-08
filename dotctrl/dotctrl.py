"""CLI Dotctrl"""
import snakypy
from dotctrl import ROOT, HOME
from dotctrl.utils import arguments
from dotctrl.utils.decorators import assign_cli
from dotctrl.actions.init import InitCommand
from dotctrl.actions.pull import PullCommand
from dotctrl.actions.link import LinkCommand
from dotctrl.actions.unlink import UnlinkCommand
from dotctrl.actions.config import ConfigCommand
from dotctrl.actions.check import CheckCommand
from dotctrl.actions.remove import RemoveCommand
from dotctrl.actions.restore import RestoreCommand
from dotctrl.actions.list import ListCommand
from dotctrl.actions.credits import CreditsCommand


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


@snakypy.decorators.only_for_linux
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
