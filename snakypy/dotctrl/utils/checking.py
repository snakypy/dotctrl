from os.path import exists, join
from sys import exit

from snakypy.helpers import FG, printer

from snakypy.dotctrl import __info__


def check_init(root) -> None:
    """Function that ends commands that depend on the created repository, but
    the repository was not created."""
    if not exists(join(root, __info__["config"])):
        printer(
            f"The repository was not created. "
            f"Use \"{__info__['pkg_name']} init\". Aborted",
            foreground=FG().WARNING,
        )
        exit(1)
