import shutil
import subprocess
from os.path import isdir


def git_init_command():
    """Function to start a Git repository in the Dotctrl repository."""
    if shutil.which("git") and not isdir(".git"):
        subprocess.call(["git", "init"], stdout=subprocess.PIPE)
