from sys import exit
from os.path import join, exists
from snakypy import printer, FG
from dotctrl.config import package


def check_init(root):
    """Function that ends commands that depend on the created repository, but
    the repository was not created."""
    if not exists(join(root, package.info["config"])):
        printer(
            f"The repository was not created. "
            f"Use \"{package.info['pkg_name']} init\". Aborted",
            foreground=FG.WARNING,
        )
        exit(1)
