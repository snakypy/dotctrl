"""CLI Dotctrl"""
import snakypy
from dotctrl import ROOT, HOME, decorators
from dotctrl.dotctrl import Dotctrl


# Creating instance Dotctrl class
dotctrl_inst = Dotctrl(ROOT, HOME)

# Get arguments CLI
arguments = dotctrl_inst.arguments()


@decorators.assign_cli(arguments, "init")
def init():
    dotctrl_inst.init_command(arguments)


@decorators.assign_cli(arguments, "pull")
def pull():
    dotctrl_inst.pull_command(arguments)


@decorators.assign_cli(arguments, "link")
def link():
    dotctrl_inst.link_command(arguments)


@decorators.assign_cli(arguments, "unlink")
def unlink():
    dotctrl_inst.unlink_command(arguments)


@decorators.assign_cli(arguments, "config")
def config():
    dotctrl_inst.config_command(arguments)


@decorators.assign_cli(arguments, "check")
def check():
    dotctrl_inst.check_command()


@decorators.assign_cli(arguments, "list")
def list_():
    dotctrl_inst.list_command()


@decorators.assign_cli(arguments, "restore")
def restore():
    dotctrl_inst.restore_command(arguments)


@decorators.assign_cli(arguments, "remove")
def remove():
    dotctrl_inst.remove_command(arguments)


@decorators.assign_cli(arguments, "--credits")
def credence():
    dotctrl_inst.credence()


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
