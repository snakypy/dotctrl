from getpass import getpass
from os.path import isdir
from shutil import which
from subprocess import PIPE, Popen, call, run
from textwrap import dedent

from snakypy.helpers.ansi import FG
from snakypy.helpers.console import printer


def git_init_command() -> None:
    """Function to start a Git repository in the Dotctrl repository."""
    if which("git") and not isdir(".git"):
        call(["git", "init"], stdout=PIPE)


def super_command(command):
    """Command super user"""
    try:
        run(["sudo", "-k"])
        get_pass = getpass()
        # command = dedent(command).replace("\n", " ").strip()
        command = " ".join(dedent(command).split())
        cmd = "echo {} | sudo -S {};".format(get_pass, command)
        p = Popen(
            cmd,
            stdin=PIPE,
            stderr=PIPE,
            stdout=PIPE,
            universal_newlines=True,
            shell=True,
        )
        out, err = p.communicate(get_pass + "\n")
        run(["sudo", "-k"])
        return p.returncode
    except KeyboardInterrupt:
        printer("Aborted by user.", foreground=FG().WARNING)
        return False
