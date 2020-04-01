"""CLI Dotctrl"""
import snakypy
from snakypy import FG
from dotctrl import ROOT, HOME, __version__, __pkginfo__, decorators
from dotctrl.dotctrl import Dotctrl
from dotctrl import utils


# Creating instance Dotctrl class
dotctrl_inst = Dotctrl(ROOT, HOME)


@decorators.assign_cli(dotctrl_inst.arguments(), "init")
def init():
    dotctrl_inst.init_command()


@decorators.assign_cli(dotctrl_inst.arguments(), "pull")
def pull():
    # dotctrl_inst.pull_link_command(use_move=True, force=True)
    dotctrl_inst.pull_command(force=True)


@decorators.assign_cli(dotctrl_inst.arguments(), "link")
def link():
    # dotctrl_inst.pull_link_command(use_link=True, force=True)
    dotctrl_inst.link_command(force=True)


@decorators.assign_cli(dotctrl_inst.arguments(), "unlink")
def unlink():
    dotctrl_inst.unlink_command()


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
    dotctrl_inst.restore_command()


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
