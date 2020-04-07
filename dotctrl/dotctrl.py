"""CLI Dotctrl"""
import snakypy
from dotctrl import ROOT, HOME
from dotctrl.console import utils
from dotctrl.console import init
from dotctrl.console import pull
from dotctrl.console import link
from dotctrl.console import unlink
from dotctrl.console import config
from dotctrl.console import check
from dotctrl.console import remove
from dotctrl.console import restore
from dotctrl.console import list
from dotctrl.console import credits


# Get arguments Docopt
args = utils.arguments()


@utils.decorators.assign_cli(args, "init")
def run_init():
    init.Command(ROOT, HOME).main(args)


@utils.decorators.assign_cli(args, "pull")
def run_pull():
    pull.Command(ROOT, HOME).main(args)


@utils.decorators.assign_cli(args, "link")
def run_link():
    link.Command(ROOT, HOME).main(args)


@utils.decorators.assign_cli(args, "unlink")
def run_unlink():
    unlink.Command(ROOT, HOME).main(args)


@utils.decorators.assign_cli(args, "config")
def run_config():
    config.Command(ROOT, HOME).main(args)


@utils.decorators.assign_cli(args, "check")
def run_check():
    check.Command(ROOT, HOME).main()


@utils.decorators.assign_cli(args, "list")
def run_list():
    list.Command(ROOT, HOME).main()


@utils.decorators.assign_cli(args, "restore")
def run_restore():
    restore.Command(ROOT, HOME).main(args)


@utils.decorators.assign_cli(args, "remove")
def run_remove():
    remove.Command(ROOT, HOME).main(args)


@utils.decorators.assign_cli(args, "--credits")
def run_credits():
    credits.Command().main()


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
