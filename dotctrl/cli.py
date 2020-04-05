"""CLI Dotctrl"""
import snakypy
from dotctrl import ROOT, HOME, decorators
from dotctrl.dotctrl import Dotctrl


# Creating instance Dotctrl class
dotctrl_ = Dotctrl(ROOT, HOME)

# Get arguments CLI
arguments = dotctrl_.arguments()


@decorators.assign_cli(arguments, "init")
def init():
    dotctrl_.init_command(arguments)


@decorators.assign_cli(arguments, "pull")
def pull():
    dotctrl_.pull_command(arguments)


@decorators.assign_cli(arguments, "link")
def link():
    dotctrl_.link_command(arguments)


@decorators.assign_cli(arguments, "unlink")
def unlink():
    dotctrl_.unlink_command(arguments)


@decorators.assign_cli(arguments, "config")
def config():
    dotctrl_.config_command(arguments)


@decorators.assign_cli(arguments, "check")
def check():
    dotctrl_.check_command()


@decorators.assign_cli(arguments, "list")
def list_():
    dotctrl_.list_command()


@decorators.assign_cli(arguments, "restore")
def restore():
    dotctrl_.restore_command(arguments)


@decorators.assign_cli(arguments, "remove")
def remove():
    dotctrl_.remove_command(arguments)


@decorators.assign_cli(arguments, "--credits")
def credence():
    dotctrl_.credence()


@snakypy.decorators.only_for_linux
def main():
    init()
    pull()
    link()
    unlink()
    check()
    list_()
    config()
    restore()
    remove()
    credence()
