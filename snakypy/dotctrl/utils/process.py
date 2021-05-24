from os.path import isdir
from shutil import which
from subprocess import PIPE, call


def git_init_command() -> None:
    """Function to start a Git repository in the Dotctrl repository."""
    if which("git") and not isdir(".git"):
        call(["git", "init"], stdout=PIPE)
