from getpass import getpass
from os.path import isdir, join
from shutil import which
from subprocess import PIPE, Popen, call, run


def git_init_command(directory: str) -> dict:
    """Function to start a Git repository in the Dotctrl repository."""

    if which("git") and not isdir(join(directory, ".git")):

        call(["git", "init", directory], stdout=PIPE)
        return {"status": True, "str": "success"}

    return {"status": False, "code": "50"}


def super_command(commands: list) -> dict:
    """Command super user"""
    try:
        run(["sudo", "-k"])
        get_pass: str = getpass()

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
                return {"status": False, "str": "error"}

        return {"status": True, "str": "success"}

    except KeyboardInterrupt:
        return {"status": False, "str": "interrupt"}

    finally:
        if which("faillock"):
            run(["faillock", "--reset"])
