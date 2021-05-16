from shutil import which
from subprocess import call, PIPE
from os.path import isdir


def git_init_command():
    """Function to start a Git repository in the Dotctrl repository."""
    if which("git") and not isdir(".git"):
        call(["git", "init"], stdout=PIPE)
