from getpass import getpass
from os.path import isdir, join
from shutil import which
from subprocess import PIPE, Popen, call, run

from snakypy.helpers.ansi import FG
from snakypy.helpers.console import printer


def git_init_command(directory: str) -> None:
    """Function to start a Git repository in the Dotctrl repository."""
    if which("git") and not isdir(join(directory, ".git")):
        call(["git", "init", directory], stdout=PIPE)


def super_command(commands: list, msg_err: str, msg_interrupt: str) -> bool:
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
                # TODO: [Adicionar o texto do print AQUI]
                printer(msg_err, foreground=FG().ERROR)
                return False
        return True
    except KeyboardInterrupt:
        # TODO: [Adicionar o texto do print AQUI]
        printer(msg_interrupt, foreground=FG().WARNING)
        return False
    finally:
        if which("faillock"):
            run(["faillock", "--reset"])
