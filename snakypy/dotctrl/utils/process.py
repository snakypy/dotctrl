from getpass import getpass
from os.path import isdir
from shutil import which
from subprocess import PIPE, Popen, call, run

from snakypy.helpers.ansi import FG
from snakypy.helpers.console import printer


def git_init_command() -> None:
    """Function to start a Git repository in the Dotctrl repository."""
    if which("git") and not isdir(".git"):
        call(["git", "init"], stdout=PIPE)


def super_command(commands: list) -> bool:
    """Command super user"""
    try:
        run(["sudo", "-k"])
        get_pass = getpass()
        for command in commands:
            p = Popen(
                "echo {} | sudo -S {};".format(get_pass, command),
                stdin=PIPE,
                stderr=PIPE,
                stdout=PIPE,
                universal_newlines=True,
                shell=True,
            )
            out, err = p.communicate(get_pass + "\n")
            if p.returncode != 0:
                printer("Error in password authentication.", foreground=FG().ERROR)
                return False
        return True
    except KeyboardInterrupt:
        printer("Aborted by user.", foreground=FG().WARNING)
        return False
    finally:
        if which("faillock"):
            run(["faillock", "--reset"])
