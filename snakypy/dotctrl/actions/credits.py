from snakypy.helpers import FG, printer
from snakypy.helpers.console import billboard, credence

from snakypy.dotctrl import __info__


class CreditsCommand:
    @staticmethod
    def main():
        print("\n")
        printer("Offered by:".center(50), foreground=FG().GREEN)
        billboard(
            __info__["organization_name"], justify="center", foreground=FG().YELLOW
        )
        printer("copyright (c) since 2020\n".center(100), foreground=FG().GREEN)
        credence(
            __info__["name"],
            __info__["version"],
            __info__["home_page"],
            __info__,
            foreground=FG().CYAN,
        )
