"""CLI Dotctrl"""
import snakypy
from dotctrl import ROOT, HOME, decorators
from dotctrl.dotctrl import Dotctrl


# Creating instance Dotctrl class
dotctrl_inst = Dotctrl(ROOT, HOME)


@decorators.assign_cli(dotctrl_inst.arguments(), "init")
def init():
    dotctrl_inst.init_command()


@decorators.assign_cli(dotctrl_inst.arguments(), "pull")
def pull():
    dotctrl_inst.pull_command(dotctrl_inst.arguments())


@decorators.assign_cli(dotctrl_inst.arguments(), "link")
def link():
    dotctrl_inst.link_command(dotctrl_inst.arguments())


@decorators.assign_cli(dotctrl_inst.arguments(), "unlink")
def unlink():
    dotctrl_inst.unlink_command(dotctrl_inst.arguments())


@decorators.assign_cli(dotctrl_inst.arguments(), "config")
def config():
    dotctrl_inst.config_command()


@decorators.assign_cli(dotctrl_inst.arguments(), "check")
def check():
    dotctrl_inst.check_command()


@decorators.assign_cli(dotctrl_inst.arguments(), "list")
def list_():
    dotctrl_inst.list_command()


@decorators.assign_cli(dotctrl_inst.arguments(), "restore")
def restore():
    dotctrl_inst.restore_command(dotctrl_inst.arguments())


@decorators.assign_cli(dotctrl_inst.arguments(), "--credits")
def credence():
    dotctrl_inst.credence()


@snakypy.decorators.only_for_linux
def main():
    (
        init(),
        pull(),
        link(),
        unlink(),
        check(),
        list_(),
        config(),
        restore(),
        credence(),
    )
